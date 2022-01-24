import numpy
import math

"""
Indoors is a class which represents the model calculation. A detailed description of
the mathematical model can be found at: Martin Z. Bazant and John W. M. Bush, medRxiv preprint (2020): 
"Beyond Six Feet: A Guideline to Limit Indoor Airborne Transmission of COVID-19"

http://web.mit.edu/bazant/www/COVID-19/

type: 'conditional' 'prevalence' 'personal'

Properties:
Model Parameters
Calculated Variables
merv_dict: MERV values to aerosol filtration efficiency conversion

Methods:
def __init__: Constructor
def calc_vars: Calculates and stores all variables used in the model, based on the model parameters.
def calc_n_max: Calculate maximum people allowed in the room given an exposure time (hours), using the transient
                model.
def calc_n_max_ss: Calculate maximum people allowed in the room given an exposure time (hours), using the steady-state
                   model.
def calc_max_time: Calculate maximum exposure time allowed given a capacity (# people, transient)
def calc_n_max_series: Calculate maximum people allowed in the room across a range of exposure times
def get_six_ft_n: Get the maximum number of people allowed in the room, based on the six-foot rule.
def set_default_params: Sets default parameters.
def merv_to_eff: Converts a MERV rating to an aerosol filtration efficiency. 
def clamp: Clamps a value within a given range.
"""


class Indoors:
    # Model Parameters
    floor_area = 900  # ft2
    mean_ceiling_height = 12  # ft
    air_exchange_rate = 3  # /hr (air changes per hour (ACH))
    primary_outdoor_air_fraction = 0.2  # 1.0 = natural ventilation
    aerosol_filtration_eff = 0  # >0.9997 HEPA, =0.2-0.9 MERVs, =0 no filter
    relative_humidity = 0.6
    breathing_flow_rate = 0.5  # m3/hr
    max_aerosol_radius = 2  # micrometers
    exhaled_air_inf = 30  # infection quanta/m3
    max_viral_deact_rate = 0.6  # /hr
    mask_passage_prob = 0.1  # 1 = no masks, ~0.1 cloth, <0.05 N95
    risk_tolerance = 0.1  # expected transmissions per infector

    prevalence = 0.01
    percentage_sus = 1
    sr_age_factor = 1
    sr_strain_factor = 1
    atm_co2 = 410  # ppm

    # Calculated Variables
    room_vol = 0  # ft3
    fresh_rate = 0  # ft3/min
    recirc_rate = 0  # ft3/min
    air_filt_rate = 0  # /hr
    sett_speed = 0  # m/hr
    conc_relax_rate = 0  # /hr
    airb_trans_rate = 0  # /hr
    viral_deact_rate = 0  # /hr
    eff_aerosol_radius = 0  # um
    relative_sus = 1

    # Source: https://www.ashrae.org/technical-resources/filtration-disinfection
    # Table of MERV values corresponding to aerosol filtration efficiency, by different particle sizes (in microns)
    merv_dict = [
        {'merv': 1, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.01},
        {'merv': 2, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.01},
        {'merv': 3, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.01},
        {'merv': 4, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.01},
        {'merv': 5, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.2},
        {'merv': 6, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.35},
        {'merv': 7, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.50},
        {'merv': 8, '0.3-1': 0.01, '1-3': 0.20, '3-10': 0.70},
        {'merv': 9, '0.3-1': 0.01, '1-3': 0.35, '3-10': 0.75},
        {'merv': 10, '0.3-1': 0.01, '1-3': 0.50, '3-10': 0.80},
        {'merv': 11, '0.3-1': 0.2, '1-3': 0.65, '3-10': 0.85},
        {'merv': 12, '0.3-1': 0.35, '1-3': 0.80, '3-10': 0.90},
        {'merv': 13, '0.3-1': 0.50, '1-3': 0.85, '3-10': 0.90},
        {'merv': 14, '0.3-1': 0.75, '1-3': 0.90, '3-10': 0.95},
        {'merv': 15, '0.3-1': 0.85, '1-3': 0.90, '3-10': 0.95},
        {'merv': 16, '0.3-1': 0.95, '1-3': 0.95, '3-10': 0.95},
        {'merv': 17, '0.3-1': 0.9997, '1-3': 0.9997, '3-10': 0.9997},
        {'merv': 18, '0.3-1': 0.99997, '1-3': 0.99997, '3-10': 0.99997},
        {'merv': 19, '0.3-1': 0.999997, '1-3': 0.999997, '3-10': 0.999997},
        {'merv': 20, '0.3-1': 0.9999997, '1-3': 0.9999997, '3-10': 0.9999997},
    ]

    density_droplet = 1100  # kg/m3
    viscosity_air = 1.86 * (10 ** -5)  # Pa s
    acceleration_gravity = 9.8  # m/s2
    co2_breath = 38000  # ppm
    ft3_to_m3 = 0.0283168  # m3 / ft3
    min_person_dist = 3  # shortest possible distance between people (ft)

    def __init__(self):
        self.calc_vars()

    # Calculate all calculated variables
    def calc_vars(self):
        self.relative_sus = self.sr_age_factor * self.sr_strain_factor
        exhaled_air_inf = self.exhaled_air_inf * self.relative_sus  # infection quanta/m3

        # Calculation
        mean_ceiling_height_m = self.mean_ceiling_height * 0.3048
        self.room_vol = self.floor_area * self.mean_ceiling_height  # ft3
        room_vol_m = 0.0283168 * self.room_vol  # m3

        self.fresh_rate = self.room_vol * self.air_exchange_rate / 60  # ft3/min

        self.recirc_rate = self.fresh_rate * (1 / self.primary_outdoor_air_fraction - 1)  # ft3/min

        self.air_filt_rate = self.aerosol_filtration_eff * self.recirc_rate * 60 / self.room_vol  # /hr

        self.eff_aerosol_radius = ((0.4 / (1 - self.relative_humidity)) ** (1 / 3)) * self.max_aerosol_radius

        self.viral_deact_rate = self.max_viral_deact_rate * self.relative_humidity

        # self.sett_speed = 3 * (self.eff_aerosol_radius / 5) ** 2  # mm/s
        self.sett_speed = (2 / 9) * self.density_droplet * self.acceleration_gravity * (
                self.eff_aerosol_radius ** 2) / (self.viscosity_air * (10 ** 9))
        self.sett_speed = self.sett_speed * 60 * 60 / 1000  # m/hr

        self.conc_relax_rate = self.air_exchange_rate + self.air_filt_rate + self.viral_deact_rate + self.sett_speed / mean_ceiling_height_m  # /hr

        self.airb_trans_rate = ((self.breathing_flow_rate * self.mask_passage_prob) ** 2) * exhaled_air_inf / (
                room_vol_m * self.conc_relax_rate)

    # Calculate maximum exposure time allowed given a capacity (# people), transient
    def calc_max_time(self, n_max, risk_type='conditional', assump='transient'):
        y_ss = self.risk_tolerance / self.airb_trans_rate
        if risk_type == 'conditional':
            exp_time_ss = y_ss / ((n_max - 1) * self.percentage_sus)
        elif risk_type == 'prevalence':
            exp_time_ss = y_ss / (n_max * (n_max - 1) * self.prevalence * self.percentage_sus)
        elif risk_type == 'personal':
            exp_time_ss = y_ss / ((n_max - 1) * self.prevalence)
        else:
            exp_time_ss = y_ss

        exp_time_trans = exp_time_ss * (1 + (1 + 4 / (self.conc_relax_rate * exp_time_ss)) ** 0.5) / 2  # hrs, transient
        if assump == 'transient':
            return exp_time_trans
        else:
            return exp_time_ss

    # Calculate maximum people allowed in the room given an exposure time (hours),
    # risk type, and assumptions (transient or steady state)
    def calc_n_max(self, exp_time, risk_type='conditional', assump='transient'):
        y_t = self.risk_tolerance * (1 + 1 / (self.conc_relax_rate * exp_time)) / self.airb_trans_rate
        y_ss = self.risk_tolerance / self.airb_trans_rate

        if assump == 'transient':
            y = y_t
        else:
            y = y_ss

        if risk_type == 'conditional':
            n_max = 1 + y / (self.percentage_sus * exp_time)
        elif risk_type == 'prevalence':
            n_max = 0.5 * (1 + (1 + (4 * y) / (self.percentage_sus * self.prevalence * exp_time)) ** 0.5)
        elif risk_type == 'personal':
            n_max = 1 + y / (self.prevalence * exp_time)
        else:
            n_max = 0

        return n_max

    # Calculates the steady-state CO2 level in the room given N
    # Output is in parts per million (ppm) of CO2
    # Warning: Do not use transient N values for this method.
    def calc_co2_n(self, n):
        room_vol_m = self.ft3_to_m3 * self.room_vol  # m3
        return (self.co2_breath * self.breathing_flow_rate * n / (self.air_exchange_rate * room_vol_m)) + self.atm_co2  # ppm

    # Calculate safe steady-state CO2 concentration (ppm) for a single exposure time.
    def calc_co2_exp_time(self, exp_time, risk_mode):
        return self.calc_co2_n(self.calc_n_max(exp_time, risk_mode, 'steady-state'))

    # Get the maximum number of people allowed in the room, based on the six-foot rule.
    def get_six_ft_n(self):
        return math.floor(self.floor_area / (6 ** 2))

    # Get the maximum number of people this room can physically have (based on floor area)
    def get_n_max(self):
        return math.floor(self.floor_area / (self.min_person_dist ** 2))

    # Returns a list of all model parameters
    def get_params(self):
        return [
            self.floor_area,
            self.mean_ceiling_height,
            self.air_exchange_rate,
            self.primary_outdoor_air_fraction,
            self.aerosol_filtration_eff,
            self.relative_humidity,
            self.breathing_flow_rate,
            self.max_aerosol_radius,
            self.exhaled_air_inf,
            self.max_viral_deact_rate,
            self.mask_passage_prob,
            self.risk_tolerance,
            self.prevalence,
            self.atm_co2,
            self.percentage_sus,
            self.sr_age_factor,
            self.sr_strain_factor
        ]

    # Returns the upper limit on CO2 (ppm) given the exposure time (hr).
    @staticmethod
    def get_safe_resp_co2_limit(exp_time):
        # Safety threshold curve, interpolated from USDA threshold values
        # f(x) = 2000 + a/(t + b)
        const = 2000  # ppm
        a = 25636.363641827  # ppm-hr
        b = 0.545454545606364  # hr
        return const + a / (exp_time + b)

    # Convert MERV rating to aerosol filtration efficiency
    # merv: if not integer, floor it
    # aerosol_radius: must be <= 10
    @staticmethod
    def merv_to_eff(merv, aerosol_radius):
        if merv == 0:
            return 0
        eff = 0
        merv = numpy.floor(Indoors.clamp(merv, 1, 20))
        merv_dict = Indoors.merv_dict
        for item in merv_dict:
            if item['merv'] == merv:
                if aerosol_radius < 1:
                    eff = item['0.3-1']
                elif aerosol_radius < 3:
                    eff = item['1-3']
                else:
                    eff = item['3-10']

        return eff

    # Clamp value within range
    @staticmethod
    def clamp(n, smallest, largest):
        return max(smallest, min(n, largest))
