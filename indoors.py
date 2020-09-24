import pandas as pd
import numpy
import math

"""
Indoors is a class which represents the model calculation. A detailed description of
the mathematical model can be found at: Martin Z. Bazant and John W. M. Bush, medRxiv preprint (2020): 
"Beyond Six Feet: A Guideline to Limit Indoor Airborne Transmission of COVID-19"

http://web.mit.edu/bazant/www/COVID-19/

Properties:
Model Parameters
merv_dict: MERV values to aerosol filtration efficiency conversion

Methods:
def __init__: Constructor
def calc_n_max: Calculate maximum people allowed in the room given an exposure time (hours)
def calc_max_time: Calculate maximum exposure time allowed given a capacity (# people)
def calc_n_max_series: Calculate maximum people allowed in the room across a range of exposure times
def get_six_ft_n: Get the maximum number of people allowed in the room, based on the six-foot rule.
def set_default_params: Sets default parameters.
def merv_to_eff: Converts a MERV rating to an aerosol filtration efficiency. 
def clamp: Clamps a value within a given range.
"""


class Indoors:
    # Model Parameters
    physical_params = []
    physio_params = []
    disease_params = []
    prec_params = []

    # Source: https://www.lakeair.com/merv-rating-explanation/
    # Table of MERV values corresponding to aerosol filtration efficiency, by different particle sizes (in microns)
    merv_dict = [
        {'merv': 1, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.01},
        {'merv': 2, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.01},
        {'merv': 3, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.01},
        {'merv': 4, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.01},
        {'merv': 5, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.2},
        {'merv': 6, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.35},
        {'merv': 7, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.50},
        {'merv': 8, '0.3-1': 0.01, '1-3': 0.01, '3-10': 0.70},
        {'merv': 9, '0.3-1': 0.01, '1-3': 0.20, '3-10': 0.85},
        {'merv': 10, '0.3-1': 0.01, '1-3': 0.50, '3-10': 0.85},
        {'merv': 11, '0.3-1': 0.01, '1-3': 0.65, '3-10': 0.85},
        {'merv': 12, '0.3-1': 0.01, '1-3': 0.80, '3-10': 0.90},
        {'merv': 13, '0.3-1': 0.50, '1-3': 0.90, '3-10': 0.90},
        {'merv': 14, '0.3-1': 0.75, '1-3': 0.90, '3-10': 0.90},
        {'merv': 15, '0.3-1': 0.85, '1-3': 0.95, '3-10': 0.90},
        {'merv': 16, '0.3-1': 0.95, '1-3': 0.95, '3-10': 0.90},
        {'merv': 17, '0.3-1': 0.9997, '1-3': 0.9997, '3-10': 0.9997},
        {'merv': 18, '0.3-1': 0.99997, '1-3': 0.99997, '3-10': 0.99997},
        {'merv': 19, '0.3-1': 0.999997, '1-3': 0.999997, '3-10': 0.999997},
        {'merv': 20, '0.3-1': 0.9999997, '1-3': 0.9999997, '3-10': 0.9999997},
    ]

    def __init__(self):
        self.set_default_params()

    # Calculate maximum people allowed in the room given an exposure time (hours)
    def calc_n_max(self, exp_time):
        # Physical Parameters
        floor_area = self.physical_params[0]  # ft2
        mean_ceiling_height = self.physical_params[1]  # ft
        air_exch_rate = self.physical_params[2]  # /hr
        primary_outdoor_air_fraction = self.physical_params[3]  # no units
        aerosol_filtration_eff = self.physical_params[4]  # no units

        # Physiological Parameters
        breathing_flow_rate = self.physio_params[0]  # m3 / hr
        aerosol_radius = self.physio_params[1]

        # Disease Parameters
        exhaled_air_inf = self.disease_params[0]  # infection quanta/m3
        viral_deact_rate = self.disease_params[1]  # /hr

        # Precautionary Parameters
        mask_passage_prob = self.prec_params[0]  # no units
        risk_tolerance = self.prec_params[1]  # no units

        # Calculation
        mean_ceiling_height_m = mean_ceiling_height * 0.3048
        room_vol = floor_area * mean_ceiling_height  # ft3
        room_vol_m = 0.0283168 * room_vol  # m3

        fresh_rate = room_vol * air_exch_rate / 60  # ft3/min

        recirc_rate = fresh_rate * (1/primary_outdoor_air_fraction - 1)  # ft3/min

        air_filt_rate = aerosol_filtration_eff * recirc_rate * 60 / room_vol  # /hr

        sett_speed = 3 * (aerosol_radius / 5) ** 2  # mm/s
        sett_speed = sett_speed * 60 * 60 / 1000  # m/hr

        conc_relax_rate = air_exch_rate + air_filt_rate + viral_deact_rate + sett_speed / mean_ceiling_height_m  # /hr

        airb_trans_rate = ((breathing_flow_rate * mask_passage_prob) ** 2) * exhaled_air_inf / (room_vol_m * conc_relax_rate)

        n_max = 1 + (risk_tolerance * (1 + 1/(conc_relax_rate * exp_time)) / (airb_trans_rate * exp_time))
        return n_max

    # Calculate maximum exposure time allowed given a capacity (# people)
    def calc_max_time(self, n_max):
        # Physical Parameters
        floor_area = self.physical_params[0]  # ft2
        mean_ceiling_height = self.physical_params[1]  # ft
        air_exch_rate = self.physical_params[2]  # /hr
        primary_outdoor_air_fraction = self.physical_params[3]  # no units
        aerosol_filtration_eff = self.physical_params[4]  # no units

        # Physiological Parameters
        breathing_flow_rate = self.physio_params[0]  # m3 / hr
        aerosol_radius = self.physio_params[1]

        # Disease Parameters
        exhaled_air_inf = self.disease_params[0]  # infection quanta/m3
        viral_deact_rate = self.disease_params[1]  # /hr

        # Precautionary Parameters
        mask_passage_prob = self.prec_params[0]  # no units
        risk_tolerance = self.prec_params[1]  # no units

        # Calculation
        mean_ceiling_height_m = mean_ceiling_height * 0.3048
        room_vol = floor_area * mean_ceiling_height  # ft3
        room_vol_m = 0.0283168 * room_vol  # m3

        fresh_rate = room_vol * air_exch_rate / 60  # ft3/min

        recirc_rate = fresh_rate * (1/primary_outdoor_air_fraction - 1)  # ft3/min

        air_filt_rate = aerosol_filtration_eff * recirc_rate * 60 / room_vol  # /hr

        sett_speed = 3 * (aerosol_radius / 5) ** 2  # mm/s
        sett_speed = sett_speed * 60 * 60 / 1000  # m/hr

        conc_relax_rate = air_exch_rate + air_filt_rate + viral_deact_rate + sett_speed / mean_ceiling_height_m  # /hr

        airb_trans_rate = ((breathing_flow_rate * mask_passage_prob) ** 2) * exhaled_air_inf / (room_vol_m * conc_relax_rate)  # /hr

        exp_time_ss = risk_tolerance / ((n_max - 1) * airb_trans_rate)  # hrs, steady-state
        exp_time_trans = exp_time_ss * (1 + (1 + 4 / (conc_relax_rate * exp_time_ss)) ** 0.5) / 2  # hrs, transient
        return exp_time_trans

    # Calculate maximum people allowed in the room across a range of exposure times
    def calc_n_max_series(self, t_min, t_max, t_step):
        df = pd.DataFrame(columns=['Maximum Exposure Time (hours)', 'Maximum Occupancy'])
        for exp_time in numpy.arange(t_min, t_max, t_step):
            n_max = self.calc_n_max(exp_time)
            df = df.append(pd.DataFrame({'Maximum Exposure Time (hours)': [exp_time], 'Maximum Occupancy': [n_max]}))

        return df

    # Get the maximum number of people allowed in the room, based on the six-foot rule.
    def get_six_ft_n(self):
        floor_area = self.physical_params[0]  # ft2
        return math.floor(floor_area / 36)

    # Sets default parameters.
    def set_default_params(self):
        # Physical Parameters
        floor_area = 900  # ft2
        mean_ceiling_height = 12  # ft
        air_exchange_rate = 3  # /hr (air changes per hour (ACH))
        primary_outdoor_air_fraction = 0.2  # 1.0 = natural ventilation
        aerosol_filtration_eff = 0  # >0.9997 HEPA, =0.2-0.9 MERVs, =0 no filter
        self.physical_params = [floor_area, mean_ceiling_height, air_exchange_rate, primary_outdoor_air_fraction,
                                aerosol_filtration_eff]

        # Physiological Parameters
        breathing_flow_rate = 0.5  # m3/hr
        aerosol_radius = 2  # micrometers
        self.physio_params = [breathing_flow_rate, aerosol_radius]

        # Disease Parameters
        exhaled_air_inf = 30  # infection quanta/m3
        viral_deact_rate = 0.3  # /hr
        self.disease_params = [exhaled_air_inf, viral_deact_rate]

        # Precautionary Parameters
        mask_passage_prob = 0.1  # 1 = no masks, ~0.1 cloth, <0.05 N95
        risk_tolerance = 0.1  # expected transmissions per infector
        self.prec_params = [mask_passage_prob, risk_tolerance]

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






