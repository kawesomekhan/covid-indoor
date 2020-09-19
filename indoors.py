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

Methods:
def __init__: Constructor
def calc_n_max: Calculate maximum people allowed in the room given an exposure time (hours)
def calc_max_time: Calculate maximum exposure time allowed given a capacity (# people)
def calc_n_max_series: Calculate maximum people allowed in the room across a range of exposure times
def get_six_ft_n: Get the maximum number of people allowed in the room, based on the six-foot rule.
def set_default_params: Sets default parameters.
"""

class Indoors:
    # Model Parameters
    physical_params = []
    physio_params = []
    disease_params = []
    prec_params = []

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






