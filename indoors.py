import pandas as pd
import numpy
import math
import io
import base64

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
    # TODO: Can refactor these into dictionaries
    physical_params = []
    physio_params = []
    disease_params = []
    prec_params = []
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
        self.set_default_params()
        self.calc_vars()

    # Calculate all calculated variables
    def calc_vars(self):
        # Physical Parameters
        floor_area = self.physical_params[0]  # ft2
        mean_ceiling_height = self.physical_params[1]  # ft
        air_exch_rate = self.physical_params[2]  # /hr
        primary_outdoor_air_fraction = self.physical_params[3]  # no units
        aerosol_filtration_eff = self.physical_params[4]  # no units
        relative_humidity = self.physical_params[5]  # no units

        # Physiological Parameters
        breathing_flow_rate = self.physio_params[0]  # m3 / hr
        max_aerosol_radius = self.physio_params[1]

        # Disease Parameters
        self.relative_sus = self.sr_age_factor * self.sr_strain_factor
        exhaled_air_inf = self.disease_params[0] * self.relative_sus  # infection quanta/m3
        max_viral_deact_rate = self.disease_params[1]  # /hr

        # Precautionary Parameters
        mask_passage_prob = self.prec_params[0]  # no units

        # Calculation
        mean_ceiling_height_m = mean_ceiling_height * 0.3048
        self.room_vol = floor_area * mean_ceiling_height  # ft3
        room_vol_m = 0.0283168 * self.room_vol  # m3

        self.fresh_rate = self.room_vol * air_exch_rate / 60  # ft3/min

        self.recirc_rate = self.fresh_rate * (1 / primary_outdoor_air_fraction - 1)  # ft3/min

        self.air_filt_rate = aerosol_filtration_eff * self.recirc_rate * 60 / self.room_vol  # /hr

        self.eff_aerosol_radius = ((0.4 / (1 - relative_humidity)) ** (1 / 3)) * max_aerosol_radius

        self.viral_deact_rate = max_viral_deact_rate * relative_humidity

        # self.sett_speed = 3 * (self.eff_aerosol_radius / 5) ** 2  # mm/s
        self.sett_speed = (2 / 9) * self.density_droplet * self.acceleration_gravity * (
                self.eff_aerosol_radius ** 2) / (self.viscosity_air * (10 ** 9))
        self.sett_speed = self.sett_speed * 60 * 60 / 1000  # m/hr

        self.conc_relax_rate = air_exch_rate + self.air_filt_rate + self.viral_deact_rate + self.sett_speed / mean_ceiling_height_m  # /hr

        self.airb_trans_rate = ((breathing_flow_rate * mask_passage_prob) ** 2) * exhaled_air_inf / (
                room_vol_m * self.conc_relax_rate)

    # Calculate maximum exposure time allowed given a capacity (# people), transient
    def calc_max_time(self, n_max, risk_type='conditional', assump='transient'):
        risk_tolerance = self.prec_params[1]  # no units
        y_ss = risk_tolerance / self.airb_trans_rate
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
        risk_tolerance = self.prec_params[1]  # no units
        y_t = risk_tolerance * (1 + 1 / (self.conc_relax_rate * exp_time)) / self.airb_trans_rate
        y_ss = risk_tolerance / self.airb_trans_rate

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
        breathing_flow_rate = self.physio_params[0]  # m3 / hr
        outdoor_exchange_rate = self.physical_params[2]  # /hr
        room_vol_m = self.ft3_to_m3 * self.room_vol  # m3
        return (self.co2_breath * breathing_flow_rate * n / (outdoor_exchange_rate * room_vol_m)) + self.atm_co2  # ppm

    # Calculate safe steady-state CO2 concentration (ppm) for a single exposure time.
    def calc_co2_exp_time(self, exp_time, risk_mode):
        return self.calc_co2_n(self.calc_n_max(exp_time, risk_mode, 'steady-state'))

    # Get the maximum number of people allowed in the room, based on the six-foot rule.
    def get_six_ft_n(self):
        floor_area = self.physical_params[0]  # ft2
        return math.floor(floor_area / (6 ** 2))

    # Get the maximum number of people this room can physically have (based on floor area)
    def get_n_max(self):
        floor_area = self.physical_params[0]  # ft2
        return math.floor(floor_area / self.min_person_dist ** 2)

    # Returns an Excel file of the current model inputs & outputs
    # desc_file: Descriptions file used to pull text / labels from
    # risk_mode: Selected risk mode at time of export
    # model_inputs_combined: list of relevant user inputs required to replicate results
    # TODO: Update descriptions files for other languages
    # TODO: Move this to essentials.py
    def get_excel(self, desc_file, risk_mode, model_inputs_combined):
        xlsx_io = io.BytesIO()
        writer = pd.ExcelWriter(xlsx_io, engine='xlsxwriter')
        # Tab 0: Text
        header_text = "COVID-19 Indoor Safety Guideline Data Export (from indoor-covid-safety.herokuapp.com)"
        model_inputs_desc = "Model Inputs: Contains all user-defined inputs in the app."
        model_params_desc = "Model Parameters: Contains parameters used during the calculation of the safety guideline."
        outputs_occ_desc = "Outputs (Safe Occupancy): Maximum exposure time vs. room capacity. The risk mode used " \
                           "here is the same risk mode that was selected in the app at the time of export."
        outputs_co2_desc = "Outputs (CO2): Recommended CO2 Limit vs. room capacity. The risk mode used " \
                           "here is the same risk mode that was selected in the app at the time of export."
        import_desc = "This file can also function as a way to save analyses. Upload this file in Advanced Mode (see" \
                      "the button labeled 'Import from Excel') to pick up where you left off. If you'd like to change" \
                      "any inputs manually, please do so in the 'Model Inputs' tab."

        text_df = pd.DataFrame([model_inputs_desc, model_params_desc, outputs_occ_desc,
                                outputs_co2_desc, import_desc], columns=[header_text])
        text_df.to_excel(writer, sheet_name="Info", index=False)

        # Tab 1: Inputs
        input_df = pd.DataFrame(model_inputs_combined, columns=["Parameter", "Value"])
        input_df.to_excel(writer, sheet_name="Model Inputs", index=False)

        # Tab 2: Model Parameters
        physical_labels = [desc_file.floor_area_text, desc_file.ceiling_height_text,
                           desc_file.ventilation_text_exp, desc_file.outdoor_air_frac_label_exp,
                           desc_file.aerosol_eff_label_exp, desc_file.humidity_text]
        physical_df = pd.DataFrame(list(zip(physical_labels, self.physical_params)), columns=["Parameter", "Value"])

        physio_labels = [desc_file.breathing_rate_label_exp, desc_file.aerosol_radius_text]
        physio_df = pd.DataFrame(list(zip(physio_labels, self.physio_params)), columns=["Parameter", "Value"])

        disease_labels = [desc_file.cq_label_exp, desc_file.viral_deact_text_exp]
        disease_df = pd.DataFrame(list(zip(disease_labels, self.disease_params)), columns=["Parameter", "Value"])

        prec_labels = [desc_file.mask_pass_prob_label_exp, desc_file.curr_risk_header]
        prec_df = pd.DataFrame(list(zip(prec_labels, self.prec_params)), columns=["Parameter", "Value"])

        other_labels = ["Prevalence", "Background CO2 (ppm)", "Percentage susceptible ps", "Age Factor",
                        "Viral Strain Factor"]
        other_params = [self.prevalence, self.atm_co2, self.percentage_sus, self.sr_age_factor, self.sr_strain_factor]
        other_df = pd.DataFrame(list(zip(other_labels, other_params)), columns=["Parameter", "Value"])

        params_df = physical_df.append(physio_df).append(disease_df).append(prec_df).append(other_df)
        params_df.to_excel(writer, sheet_name="Model Parameters", index=False)

        # Tab 3: Outputs (safe occupancy)
        occ_df = self.get_max_time_series(2, self.get_n_max(), 1, risk_mode)
        occ_df = occ_df.rename(columns={'capacity': "Capacity",
                                        'exp-time': "[Risk Mode: " + risk_mode + "] Maximum Exposure Time (hr)"})
        occ_df.to_excel(writer, sheet_name="Outputs (Safe Occupancy)", index=False)

        # Tab 4: Outputs (safe CO2)
        co2_df = self.calc_co2_series(0.1, 1000, 1000, risk_mode)
        co2_df = co2_df.rename(columns={'exposure_time': "Exposure Time (hr)",
                                        'co2_trans': "[Risk Mode: " + risk_mode + "] Safe CO2 Concentration (ppm)",
                                        'co2_resp': "USDA Safety CO2 Threshold (ppm)",
                                        'co2_rec': "Recommended CO2 Limit (ppm)"})
        co2_df.to_excel(writer, sheet_name="Outputs (CO2)", index=False)

        # Autofit column widths
        dfs = {"Info": text_df, "Model Inputs": input_df, "Model Parameters": params_df,
               "Outputs (Safe Occupancy)": occ_df, "Outputs (CO2)": co2_df}
        for sheetname, df in dfs.items():
            worksheet = writer.sheets[sheetname]
            for idx, col in enumerate(df):
                series = df[col]
                max_len = max((
                    series.astype(str).map(len).max(),  # len of largest item
                    len(str(series.name))  # len of column name/header
                )) + 1  # adding a little extra space
                worksheet.set_column(idx, idx, max_len)  # set column width

        # Save file and return data
        writer.save()
        xlsx_io.seek(0)
        # https://en.wikipedia.org/wiki/Data_URI_scheme
        media_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        data = base64.b64encode(xlsx_io.read()).decode("utf-8")
        href_data_downloadable = f'data:{media_type};base64,{data}'
        return href_data_downloadable

    # Sets default parameters.
    def set_default_params(self):
        # Physical Parameters
        floor_area = 900  # ft2
        mean_ceiling_height = 12  # ft
        air_exchange_rate = 3  # /hr (air changes per hour (ACH))
        primary_outdoor_air_fraction = 0.2  # 1.0 = natural ventilation
        aerosol_filtration_eff = 0  # >0.9997 HEPA, =0.2-0.9 MERVs, =0 no filter
        relative_humidity = 0.6
        self.physical_params = [floor_area, mean_ceiling_height, air_exchange_rate, primary_outdoor_air_fraction,
                                aerosol_filtration_eff, relative_humidity]

        # Physiological Parameters
        breathing_flow_rate = 0.5  # m3/hr
        max_aerosol_radius = 2  # micrometers
        self.physio_params = [breathing_flow_rate, max_aerosol_radius]

        # Disease Parameters
        exhaled_air_inf = 30  # infection quanta/m3
        max_viral_deact_rate = 0.3  # /hr
        self.disease_params = [exhaled_air_inf, max_viral_deact_rate]

        # Precautionary Parameters
        mask_passage_prob = 0.1  # 1 = no masks, ~0.1 cloth, <0.05 N95
        risk_tolerance = 0.1  # expected transmissions per infector
        self.prec_params = [mask_passage_prob, risk_tolerance]

        # Prevalence
        self.prevalence = 0.01

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
