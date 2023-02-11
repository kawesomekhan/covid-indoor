import plotly.graph_objects as go
from dash import html

import descriptions as desc
import descriptions_cs as desc_cs
import descriptions_da as desc_da
import descriptions_de as desc_de
import descriptions_el as desc_el
import descriptions_es as desc_es
import descriptions_eu as desc_eu
import descriptions_fr as desc_fr
import descriptions_zh as desc_zh
import descriptions_zh_tw as desc_zh_tw
import descriptions_hi as desc_hi
import descriptions_hu as desc_hu
import descriptions_id as desc_id
import descriptions_it as desc_it
import descriptions_ko as desc_ko
import descriptions_nl as desc_nl
import descriptions_pt_br as desc_pt_br
import descriptions_ru as desc_ru
import descriptions_sv as desc_sv

import pandas as pd
import numpy
import math
from scipy.optimize import fsolve

import io
import base64

"""
essentials.py contains functionality shared by both Basic Mode and Advanced Mode.

"""

# Languages where the time comes before the occupancy in the big red output (SOV order)
sov_languages = ["hi"]

normal_credits = '''William H. Green, Matthew Haefner, 
                 David Keating, Ann Kinzig, Caeli MacLennan, Michelle Quien, Marc Rosenbaum, 
                 David Stark'''
translation_credits = '''Khoiruddin Ad-Damaki, Shashank Agarwal, Juncal Arbelaiz, Antonio Bertei, Henrik Bruus, John Bush, 
                        Rafael Suarez Camacho, Laura Champion, Supratim Das, Inga Dorner, Surya Effendy, Arantza Etxeburua 
                        Anders Flodmarke, Valeri Frumkin, Sung Jae Kim, Vaclav Klika, Ulrike Krewer, Bonho Koo, John Ochsendorf, 
                        Michal Pavelka, Juan Puyo, László Sándor, Myungjin Seo, Lucas Tambasco, 
                        Huanhuan Tian, Ettore Virga, Chenyu Wen, Gede Wenten, Hongbo Zhao, Juner Zhu, Ryan Wu'''

m_to_ft = 3.28084
month_to_hour = 730.001
month_to_day = 30.4167

# CSS Styles for Tabs (currently known issue in Dash with overriding default css)
tabs_card_style = {'margin': '1em', 'padding': '0', 'border': 'none'}

main_panel_tab_style = {'margin-top': '0'}

tab_style = {
    'padding-left': '1em',
    'padding-right': '1em',
    'border-color': '#DDDDDD',
    'font-size': '13px'
}

tab_style_selected = {
    'padding-left': '1em',
    'padding-right': '1em',
    'border-color': '#DDDDDD',
    'border-top-color': '#de1616',
    'font-size': '13px'
}

room_preset_settings = {
    'house': {
        'floor-area': 2000,
        'ceiling-height': 12,
        'floor-area-metric': 2000 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 12 / m_to_ft,
        'ventilation': 3,
        'filtration': 6,
        'recirc-rate': 1,
        'rh': 0.6
    },
    'living-room': {
        'floor-area': 400,
        'ceiling-height': 9,
        'floor-area-metric': 400 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 9 / m_to_ft,
        'ventilation': 3,
        'filtration': 6,
        'recirc-rate': 1,
        'rh': 0.6
    },
    'classroom': {
        'floor-area': 910,
        'ceiling-height': 12,
        'floor-area-metric': 910 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 12 / m_to_ft,
        'ventilation': 3,
        'filtration': 6,
        'recirc-rate': 1,
        'rh': 0.6
    },
    'restaurant': {
        'floor-area': 1000,
        'ceiling-height': 12,
        'floor-area-metric': 1000 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 12 / m_to_ft,
        'ventilation': 9,
        'filtration': 6,
        'recirc-rate': 1,
        'rh': 0.6
    },
    'office': {
        'floor-area': 10000,
        'ceiling-height': 12,
        'floor-area-metric': 10000 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 12 / m_to_ft,
        'ventilation': 8,
        'filtration': 10,
        'recirc-rate': 1,
        'rh': 0.6
    },
    'subway': {
        'floor-area': 580,
        'ceiling-height': 10,
        'floor-area-metric': 580 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 10 / m_to_ft,
        'ventilation': 18,
        'filtration': 6,
        'recirc-rate': 54,
        'rh': 0.6
    },
    'bus': {
        'floor-area': 380,
        'ceiling-height': 10,
        'floor-area-metric': 380 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 10 / m_to_ft,
        'ventilation': 8,
        'filtration': 6,
        'recirc-rate': 1,
        'rh': 0.6
    },
    'airplane': {
        'floor-area': 1440,
        'ceiling-height': 6.7,
        'floor-area-metric': 1440 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 6.7 / m_to_ft,
        'ventilation': 24,
        'filtration': 17,
        'recirc-rate': 24,
        'rh': 0.2
    },
    'church': {
        'floor-area': 1900,
        'ceiling-height': 30,
        'floor-area-metric': 1900 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 30 / m_to_ft,
        'ventilation': 2,
        'filtration': 6,
        'recirc-rate': 1,
        'rh': 0.6
    },
}

human_preset_settings = {
    'masks-1': {
        'exertion': 0.49,
        'expiratory': 4.2,
        'masks': 0.9,
        'mask-fit': 0.95
    },
    'masks-2': {
        'exertion': 0.49,
        'expiratory': 72,
        'masks': 0.9,
        'mask-fit': 0.95
    },
    'masks-3': {
        'exertion': 2.35,
        'expiratory': 8.8,
        'masks': 0.9,
        'mask-fit': 0.95
    },
    'no-masks-1': {
        'exertion': 0.49,
        'expiratory': 4.2,
        'masks': 0,
        'mask-fit': 0.95
    },
    'no-masks-2': {
        'exertion': 0.49,
        'expiratory': 72,
        'masks': 0,
        'mask-fit': 0.95
    },
    'no-masks-3': {
        'exertion': 2.35,
        'expiratory': 8.8,
        'masks': 0,
        'mask-fit': 0.95
    },
    'singing-1': {
        'exertion': 1,
        'expiratory': 970,
        'masks': 0,
        'mask-fit': 0.95
    }
}

ventilation_default = room_preset_settings['classroom']['ventilation']
filter_default = room_preset_settings['classroom']['filtration']
recirc_default = room_preset_settings['classroom']['recirc-rate']

# Nmax values for main red text output
model_output_n_vals = [2, 5, 10, 25, 100]
model_output_n_vals_big = [25, 100, 250, 500, 1000]

# Max time reported in the big red text output
covid_recovery_time = 14  # Days

# CO2 max allowed output for graphs and other front end panels
co2_max_output = 2000  # ppm

viral_strains = {
    1: 'SARS-CoV-2 Wuhan',
    1.2: 'B.1.427/429',
    1.5: 'B.1.1.7 UK, B.1.351 South Africa',
    2.001: 'P.1 Brazil',
    2.5: 'B.1.617.2 India',
    4.0: 'BA.1 South Africa',
    5.2: 'BA.2'
}


# Determines what error message we should use, if any
def get_err_msg(floor_area, ceiling_height, air_exchange_rate, merv, recirc_rate, max_aerosol_radius,
                max_viral_deact_rate, language, n_max_input=2, exp_time_input=1, exp_time_co2=1, prevalence=1,
                atm_co2=410, co2_input=700):
    error_msg = ""

    desc_file = get_desc_file(language)
    # Make sure none of our values are none
    if floor_area is None:
        error_msg = desc_file.error_list["floor_area"]
    elif ceiling_height is None:
        error_msg = desc_file.error_list["ceiling_height"]
    elif recirc_rate is None:
        error_msg = desc_file.error_list["recirc_rate"]
    elif max_aerosol_radius is None:
        error_msg = desc_file.error_list["aerosol_radius"]
    elif max_viral_deact_rate is None:
        error_msg = desc_file.error_list["viral_deact_rate"]
    elif n_max_input is None or n_max_input < 2:
        error_msg = desc_file.error_list["n_max_input"]
    elif exp_time_input == 0 or exp_time_input is None or exp_time_co2 == 0 or exp_time_co2 is None:
        error_msg = desc_file.error_list["exp_time_input"]
    elif air_exchange_rate == 0 or air_exchange_rate is None:
        error_msg = desc_file.error_list["air_exchange_rate"]
    elif merv is None:
        error_msg = desc_file.error_list["merv"]
    elif prevalence is None or prevalence <= 0 or prevalence >= 100000:
        error_msg = desc_file.error_list["prevalence"]
    elif atm_co2 is None or atm_co2 < 0:
        if "atm_co2" in desc_file.error_list:
            error_msg = desc_file.error_list["atm_co2"]
        else:
            error_msg = desc.error_list["atm_co2"]
    elif co2_input is None:
        if "co2_input" in desc_file.error_list:
            error_msg = desc_file.error_list["co2_input"]
        else:
            error_msg = desc.error_list["co2_input"]

    return error_msg


# Returns unit selection based on URL search
def get_units(search):
    params = search_to_params(search)
    my_units = "british"
    if "units" in params:
        my_units = params["units"]

    return my_units


# Returns language based on URL search
def get_lang(search):
    params = search_to_params(search)
    if "lang" in params:
        return params["lang"]
    else:
        return "en"


# Gets the preset dropdown value based on given values. If no preset is found, return 'custom'
def get_room_preset_dd_value(floor_area, ceiling_height, air_exchange_rate, recirc_rate, merv, relative_humidity,
                             units):
    preset_dd_value = 'custom'
    for setting_key in room_preset_settings:
        setting = room_preset_settings[setting_key]

        is_right_volume = False
        if units == "british":
            is_right_volume = setting['floor-area'] == floor_area and \
                              setting['ceiling-height'] == ceiling_height
        elif units == "metric":
            is_right_volume = round(setting['floor-area-metric'], 2) == floor_area and \
                              round(setting['ceiling-height-metric'], 2) == ceiling_height
        is_preset = is_right_volume and \
                    setting['ventilation'] == air_exchange_rate and \
                    setting['recirc-rate'] == recirc_rate and \
                    setting['filtration'] == merv and \
                    setting['rh'] == relative_humidity
        if is_preset:
            preset_dd_value = setting_key
            break

    return preset_dd_value


# Gets the preset dropdown value based on given values. If no preset is found, return 'custom'
def get_human_preset_dd_value(exertion, expiratory_activity, masks, mask_fit, units):
    preset_dd_value = 'custom'
    for setting_key in human_preset_settings:
        setting = human_preset_settings[setting_key]
        is_preset = setting['exertion'] == exertion and \
                    setting['expiratory'] == expiratory_activity and \
                    setting['masks'] == masks and \
                    setting['mask-fit'] == mask_fit
        if is_preset:
            preset_dd_value = setting_key
            break

    return preset_dd_value


# Returns the plotly figure based on the supplied indoor model.
def get_model_figure(indoor_model, language):
    desc_file = get_desc_file(language)
    new_df = calc_n_max_series(indoor_model, 2, 100, 1.0)

    new_fig = go.Figure()
    new_fig.add_trace(go.Scatter(x=new_df["exposure_time"], y=new_df["occupancy_trans"],
                                 mode='lines',
                                 name=desc_file.transient_text,
                                 line=go.scatter.Line(color="#8ad4ed")))
    new_fig.add_trace(go.Scatter(x=new_df["exposure_time"], y=new_df["occupancy_ss"],
                                 mode='lines',
                                 name=desc_file.steady_state_text,
                                 line=go.scatter.Line(color="#2490b5"),
                                 visible='legendonly'))
    new_fig.update_layout(transition_duration=500,
                          title=desc_file.graph_title, height=400,
                          xaxis_title=desc_file.graph_xtitle,
                          yaxis_title=desc_file.graph_ytitle,
                          font_family="Barlow",
                          template="simple_white",
                          hoverlabel=dict(
                              font_family="Barlow"
                          ))
    return new_fig


# Returns the plotly figure based on the supplied indoor model.
# This specifically outputs safe steady-state CO2 concentration (ppm) vs. exposure time.
# risk_mode: conditional, prevalence, or personal
def get_model_figure_co2(indoor_model, risk_mode, language, window_width):
    desc_file = get_desc_file(language)
    is_mobile = window_width <= 600

    recommended_df = pd.DataFrame(columns=['exposure_time', 'co2_recommended'])
    new_df = calc_co2_series(indoor_model, 0.1, 1000, 100, risk_mode)
    safe_df = pd.DataFrame(columns=['exposure_time', 'co2_safe'])
    background_df = pd.DataFrame(columns=['exposure_time', 'co2_background'])
    for exp_time in numpy.logspace(math.log(0.1, 10), math.log(1000, 10), 100):
        safe_co2_limit = indoor_model.get_safe_resp_co2_limit(exp_time)
        recommended_co2_limit = min(safe_co2_limit, indoor_model.calc_co2_exp_time(exp_time, risk_mode))
        # safe_df = safe_df.append(pd.DataFrame({'exposure_time': [exp_time], 'co2_safe': [safe_co2_limit]}))
        safe_df = pd.concat([safe_df, pd.DataFrame({'exposure_time': [exp_time], 'co2_safe': [safe_co2_limit]})])
        # recommended_df = recommended_df.append(pd.DataFrame({'exposure_time': [exp_time],
        #                                                      'co2_rec': [recommended_co2_limit]}))
        recommended_df = pd.concat([recommended_df,
                                    pd.DataFrame({'exposure_time': [exp_time], 'co2_rec': [recommended_co2_limit]})])
        # background_df = background_df.append(pd.DataFrame({'exposure_time': [exp_time],
        #                                                    'co2_background': [indoor_model.atm_co2]}))
        background_df = pd.concat([background_df,
                                   pd.DataFrame({'exposure_time': [exp_time], 'co2_background': [indoor_model.atm_co2]})])

    new_fig = go.Figure()
    recommended_co2_text = desc.recommended_co2_text
    guideline_trace_text = desc.guideline_trace_text
    co2_safe_trace_text = desc.co2_safe_trace_text
    background_co2_text = desc.background_co2_text
    graph_title_co2 = desc.graph_title_co2
    graph_ytitle_co2 = desc.graph_ytitle_co2
    if hasattr(desc_file, "recommended_co2_text"):
        recommended_co2_text = desc_file.recommended_co2_text

    if hasattr(desc_file, "guideline_trace_text"):
        guideline_trace_text = desc_file.guideline_trace_text

    if hasattr(desc_file, "co2_safe_trace_text"):
        co2_safe_trace_text = desc_file.co2_safe_trace_text

    if hasattr(desc_file, "background_co2_text"):
        background_co2_text = desc_file.background_co2_text

    if hasattr(desc_file, "graph_title_co2"):
        graph_title_co2 = desc_file.graph_title_co2

    if hasattr(desc_file, "graph_ytitle_co2"):
        graph_ytitle_co2 = desc_file.graph_ytitle_co2

    ht_rec = desc_file.graph_xtitle + ": %{x:,.1f}<br>" + recommended_co2_text + ": %{y:,.0f} ppm<extra></extra>"
    ht_guideline = desc_file.graph_xtitle + ": %{x:,.1f}<br>" + guideline_trace_text + ": %{y:,.0f} ppm<extra></extra>"
    ht_safe = desc_file.graph_xtitle + ": %{x:,.1f}<br>" + co2_safe_trace_text + ": %{y:,.0f} ppm<extra></extra>"
    ht_bg = desc_file.graph_xtitle + ": %{x:,.1f}<br>" + background_co2_text + ": %{y:,.0f} ppm<extra></extra>"

    new_fig.add_trace(go.Scatter(x=recommended_df["exposure_time"], y=recommended_df["co2_rec"],
                                 mode='lines',
                                 name=recommended_co2_text,
                                 line=go.scatter.Line(color="#de1616"),
                                 hovertemplate=ht_rec))
    # new_fig.add_trace(go.Scatter(x=new_df["exposure_time"], y=new_df["co2_trans"],
    #                              mode='lines',
    #                              name=guideline_trace_text,
    #                              line=go.scatter.Line(color="#730707", dash='dot'),
    #                              hovertemplate=ht_guideline))
    # new_fig.add_trace(go.Scatter(x=safe_df["exposure_time"], y=safe_df["co2_safe"],
    #                              mode='lines',
    #                              name=co2_safe_trace_text,
    #                              line=go.scatter.Line(color="#8ad4ed", dash='dot'),
    #                              hovertemplate=ht_safe))
    new_fig.add_trace(go.Scatter(x=background_df["exposure_time"], y=background_df["co2_background"],
                                 mode='lines',
                                 name=background_co2_text,
                                 line=go.scatter.Line(color="#000000", dash='dot'),
                                 hovertemplate=ht_bg))
    new_fig.update_layout(transition_duration=500,
                          title=graph_title_co2, height=500,
                          xaxis_title=desc_file.graph_xtitle,
                          yaxis_title=graph_ytitle_co2,
                          font_family="Barlow",
                          template="simple_white",
                          hoverlabel=dict(
                              font_family="Barlow",
                          ),
                          hovermode='closest')
    if is_mobile:
        new_fig.update_layout(title="", height=400, showlegend=False)

    new_fig.update_xaxes(type="log", showspikes=True)
    new_fig.update_yaxes(type="log", showspikes=True)

    max_guideline_val = new_df["co2_trans"].max()
    y_max = co2_max_output
    if max_guideline_val * 1.2 > y_max:
        new_fig.update_yaxes(range=[math.log(indoor_model.atm_co2 * 0.8, 10), math.log(y_max, 10)])
    else:
        new_fig.update_yaxes(range=[math.log(indoor_model.atm_co2 * 0.8, 10), math.log(max_guideline_val * 1.2, 10)])

    return new_fig


# Returns the recommended co2 limit given an exposure time
def get_recommended_co2_limit(indoor_model, risk_mode, exp_time):
    safe_co2_conc = indoor_model.calc_co2_exp_time(exp_time, risk_mode)
    max_co2_conc = indoor_model.get_safe_resp_co2_limit(exp_time)
    return min(safe_co2_conc, max_co2_conc)


# Returns the maximum exposure time given a recommended CO2 concentration and risk mode
# Ok this is going to be a messy function so try to clean up later
def get_exp_time_from_co2(indoor_model, risk_mode, co2_conc):
    # discontinuous function, so do binary search to narrow until threshold
    guess = 10  # hours
    # thresh = 0.001  # ppm
    recommended_co2_conc = get_recommended_co2_limit(indoor_model, risk_mode, guess)

    # diff_sq = (recommended_co2_conc - co2_conc) ** 2

    def func(x):
        return [get_recommended_co2_limit(indoor_model, risk_mode, x[0]) - co2_conc]

    root = fsolve(func, [guess])
    return root[0]


# Calculate maximum people allowed in the room across a range of exposure times, returning both transient
# and steady-state outputs
def calc_n_max_series(indoor_model, t_min, t_max, t_step):
    df = pd.DataFrame(columns=['exposure_time', 'occupancy_trans', 'occupancy_ss'])
    for exp_time in numpy.arange(t_min, t_max, t_step):
        n_max_trans = indoor_model.calc_n_max(exp_time)
        n_max_ss = indoor_model.calc_n_max(exp_time, assump='steady-state')
        # df = df.append(pd.DataFrame({'exposure_time': [exp_time], 'occupancy_trans': [n_max_trans],
        #                              'occupancy_ss': [n_max_ss]}))
        df = pd.concat([df, pd.DataFrame({'exposure_time': [exp_time], 'occupancy_trans': [n_max_trans],
                                          'occupancy_ss': [n_max_ss]})])

    return df


# Returns a dataframe of maximum exposure times allowed for each risk mode based on capacity
def get_max_time_series(indoor_model, n_min, n_max, n_step, risk_mode):
    df = pd.DataFrame(columns=['capacity', 'exp-time'])
    for capacity in numpy.arange(n_min, n_max, n_step):
        exp_time = indoor_model.calc_max_time(capacity, risk_mode)
        # df = df.append(pd.DataFrame({'capacity': [capacity], 'exp-time': [exp_time]}))
        df = pd.concat([df, pd.DataFrame({'capacity': [capacity], 'exp-time': [exp_time]})])

    return df


# Calculate safe steady-state CO2 concentration (ppm) across a range of exposure times, returning transient output.
def calc_co2_series(indoor_model, t_min, t_max, t_num, risk_mode):
    df = pd.DataFrame(columns=['exposure_time', 'co2_trans', 'co2_resp', 'co2_rec'])
    for exp_time in numpy.logspace(math.log(t_min, 10), math.log(t_max, 10), t_num):
        co2_trans = indoor_model.calc_co2_exp_time(exp_time, risk_mode)
        co2_resp = indoor_model.get_safe_resp_co2_limit(exp_time)
        co2_rec = min(co2_trans, co2_resp)
        # df = df.append(pd.DataFrame({'exposure_time': [exp_time], 'co2_trans': [co2_trans],
        #                              'co2_resp': [co2_resp], 'co2_rec': [co2_rec]}))
        df = pd.concat([df, pd.DataFrame({'exposure_time': [exp_time], 'co2_trans': [co2_trans],
                                          'co2_resp': [co2_resp], 'co2_rec': [co2_rec]})])

    return df


# Returns the big red output text.
# risk_type: conditional, prevalence, or personal
# recovery_time: Time to recovery in days
# If recovery time is -1, will not limit the output.
def get_model_output_text(indoor_model, risk_type, recovery_time, language):
    output_type = 'occupancy'
    desc_file = get_desc_file(language)
    # Check if we should use the normal n vals, or the big n vals
    n_val_series = model_output_n_vals
    if indoor_model.calc_max_time(model_output_n_vals[-1], risk_type) > 48 or \
            indoor_model.get_six_ft_n() >= model_output_n_vals[-1]:
        n_val_series = model_output_n_vals_big

    model_output_text = ["", "", "", "", ""]
    index = 0
    close_ind_rev = 0
    for n_val in n_val_series:
        # First check: is this a feasible number of people?
        n_max = indoor_model.get_n_max()
        if n_val > n_max:
            close_ind_rev = index - len(n_val_series)
            break
        else:
            max_time = indoor_model.calc_max_time(n_val, risk_type)  # hours
            time_text = time_to_text(max_time, True, recovery_time, language)
            safe_co2 = indoor_model.calc_co2_n(n_val)

            if output_type == 'occupancy':
                if language in sov_languages:
                    base_string = time_text + desc_file.model_output_suffix + desc_file.model_output_base_string
                else:
                    base_string = desc_file.model_output_base_string + time_text

                model_output_text[index] = base_string.format(n_val=n_val)
            else:
                if language in sov_languages:
                    base_string = time_text + desc_file.model_output_suffix + desc_file.model_output_base_string_co2
                else:
                    base_string = desc_file.model_output_base_string_co2 + time_text

                model_output_text[index] = base_string.format(co2=safe_co2)

        index += 1

    # if language == "en":
    #     if close_ind_rev >= -len(model_output_text) + 2:
    #         model_output_text[close_ind_rev - 2] = model_output_text[close_ind_rev - 2] + ' or'
    #     if close_ind_rev >= -len(model_output_text) + 1:
    #         model_output_text[close_ind_rev - 1] = model_output_text[close_ind_rev - 1] + '.'

    return model_output_text


# Returns the six feet distancing text.
def get_six_ft_text(indoor_model, language):
    desc_file = get_desc_file(language)
    six_ft_people = indoor_model.get_six_ft_n()
    if six_ft_people == 1:
        six_ft_text = desc_file.six_ft_base_string_one.format(six_ft_people)
    else:
        six_ft_text = desc_file.six_ft_base_string.format(six_ft_people)

    return six_ft_text


# Returns the six feet distancing time.
# recovery_time: Time to recovery in days
# If recovery time is -1, will not limit the output.
def get_six_ft_exp_time(indoor_model, risk_type, recovery_time, language):
    six_ft_n = indoor_model.get_six_ft_n()
    if six_ft_n < 2:
        six_ft_exp_time = "<" + time_to_text(indoor_model.calc_max_time(2, risk_type), True, recovery_time,
                                             language) + "."
    else:
        six_ft_exp_time = time_to_text(indoor_model.calc_max_time(six_ft_n, risk_type), True, recovery_time,
                                       language) + "."

    return six_ft_exp_time


# Converts a time (in hours) into a text with formatting based on minutes/hours/days.
# keep_hours: Whether to keep hours in the output time along with day/month
# recovery_time: Time to recovery in days
# If recovery time is -1, will not limit the output.
def time_to_text(time, keep_hours, recovery_time, language):
    desc_file = get_desc_file(language)
    pretty_time = time

    if recovery_time != -1:
        if round(time) > recovery_time * 24:
            units = desc_file.units_days
            base_string = '>{val:.0f} ' + units
            return base_string.format(val=recovery_time)

    if round(time) < 2:
        pretty_time_range = "Minutes"
        pretty_time = time * 60
        if round(pretty_time) == 1:
            units = desc_file.units_min_one
        else:
            units = desc_file.units_min
    elif round(time) > month_to_hour:
        pretty_time_range = "Months"
        pretty_time = time / month_to_hour
        if round(pretty_time) == 1:
            units = desc_file.units_month_one
        else:
            units = desc_file.units_months
    elif round(time) > 48:
        pretty_time_range = "Days"
        pretty_time = time / 24
        if round(pretty_time) == 1:
            units = desc_file.units_day_one
        else:
            units = desc_file.units_days
    else:
        pretty_time_range = "Hours"
        if round(pretty_time) == 1:
            units = desc_file.units_hr_one
        else:
            units = desc_file.units_hr

    if keep_hours:
        long_units = units
        if round(time) == 1:
            units = desc_file.units_hr_one
        else:
            units = desc_file.units_hr

        if pretty_time_range == "Hours":
            base_string = '{val:,.0f} ' + units
            return base_string.format(val=time)
        elif pretty_time_range == "Days" or pretty_time_range == "Months":
            base_string = '{val:,.0f} ' + units + ' ({longval:,.0f} ' + long_units + ')'
            return base_string.format(val=time, longval=pretty_time)
        else:
            base_string = '{val:,.0f} ' + long_units
            return base_string.format(val=pretty_time)
    else:
        base_string = '{val:,.0f} ' + units
        return base_string.format(val=pretty_time)


# Gets n max text
def get_n_max_text(n, n_max, language):
    desc_file = get_desc_file(language)
    if n < 2:
        return "<" + desc_file.n_max_base_string.format(2)
    if n > n_max:
        return desc_file.n_max_overflow_base_string.format(n_max)
    else:
        return desc_file.n_max_base_string.format(math.floor(n))


# Returns the output text for the variables of interest, shown in the FAQ/Other Inputs & Outputs tab.
# units: British or Metric.
def get_interest_output_text(indoor_model, units):
    outdoor_air_frac = indoor_model.primary_outdoor_air_fraction
    aerosol_filtration_eff = indoor_model.aerosol_filtration_eff
    breathing_flow_rate = indoor_model.breathing_flow_rate
    infectiousness = indoor_model.exhaled_air_inf
    mask_pass_prob = indoor_model.mask_passage_prob

    # Calculated Values of Interest Output
    if units == "british":
        interest_output = [
            '{:,.2f}'.format(indoor_model.relative_sus),
            '{:,.2f}'.format(outdoor_air_frac),
            '{:,.2f}'.format(aerosol_filtration_eff),
            '{:,.2f} ft\u00B3/min'.format(breathing_flow_rate * 35.3147 / 60),  # m3/hr to ft3/min
            '{:,.2f} quanta/ft\u00B3'.format(infectiousness / 35.3147),  # 1/m3 to 1/ft3
            '{:,.3f}'.format(mask_pass_prob),
            '{:,.0f} ft\u00B3'.format(indoor_model.room_vol),
            '{:,.0f} ft\u00B3/min'.format(indoor_model.fresh_rate),
            '{:,.0f} ft\u00B3/min'.format(indoor_model.recirc_rate),
            '{:,.2f} /hr'.format(indoor_model.air_filt_rate),
            '{:,.2f} \u03bcm'.format(indoor_model.eff_aerosol_radius),
            '{:,.2f} /hr'.format(indoor_model.viral_deact_rate),
            '{:,.2f} ft/min'.format(indoor_model.sett_speed * 3.281 / 60),  # m/hr to ft/min
            '{:,.2f} /hr'.format(indoor_model.conc_relax_rate),
            '{:,.2f} /hr ÷10,000'.format(indoor_model.airb_trans_rate * 10000),
        ]
    elif units == "metric":
        interest_output = [
            '{:,.2f}'.format(indoor_model.relative_sus),
            '{:,.2f}'.format(outdoor_air_frac),
            '{:,.2f}'.format(aerosol_filtration_eff),
            '{:,.2f} m\u00B3/hr'.format(breathing_flow_rate),
            '{:,.2f} quanta/m\u00B3'.format(infectiousness),
            '{:,.3f}'.format(mask_pass_prob),
            '{:,.0f} m\u00B3'.format(indoor_model.room_vol / 35.315),  # ft3 to m3
            '{:,.0f} m\u00B3/hr'.format(indoor_model.fresh_rate / 35.3147 * 60),  # ft3/min to m3/hr
            '{:,.0f} m\u00B3/hr'.format(indoor_model.recirc_rate / 35.3147 * 60),  # ft3/min to m3/hr
            '{:,.2f} /hr'.format(indoor_model.air_filt_rate),
            '{:,.2f} \u03bcm'.format(indoor_model.eff_aerosol_radius),
            '{:,.2f} /hr'.format(indoor_model.viral_deact_rate),
            '{:,.2f} m/hr'.format(indoor_model.sett_speed),
            '{:,.2f} /hr'.format(indoor_model.conc_relax_rate),
            '{:,.2f} /hr ÷10,000'.format(indoor_model.airb_trans_rate * 10000),
        ]

    return interest_output


# Returns the value for Qb given the units.
def get_qb_text(indoor_model, units):
    breathing_flow_rate = indoor_model.breathing_flow_rate
    if units == 'british':
        return '{:,.2f} ft\u00B3/min'.format(breathing_flow_rate * 35.3147 / 60)  # m3/hr to ft3/min
    elif units == 'metric':
        return '{:,.2f} m\u00B3/hr'.format(breathing_flow_rate)


# Returns the value for Cq given the units.
def get_cq_text(indoor_model, units):
    infectiousness = indoor_model.exhaled_air_inf
    if units == 'british':
        return '{:,.2f} q/ft\u00B3'.format(infectiousness / 35.3147),  # 1/m3 to 1/ft3
    elif units == 'metric':
        return '{:,.2f} q/m\u00B3'.format(infectiousness)


# Returns an Excel file of the current model inputs & outputs
# desc_file: Descriptions file used to pull text / labels from
# risk_mode: Selected risk mode at time of export
# model_inputs_combined: list of relevant user inputs required to replicate results
# TODO: Update descriptions files for other languages
def get_excel(indoor_model, desc_file, risk_mode, model_inputs_combined):
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
    param_labels = [desc_file.floor_area_text, desc_file.ceiling_height_text,
                    desc_file.ventilation_text_exp, desc_file.outdoor_air_frac_label_exp,
                    desc_file.aerosol_eff_label_exp, desc_file.humidity_text, desc_file.breathing_rate_label_exp,
                    desc_file.aerosol_radius_text, desc_file.cq_label_exp, desc_file.viral_deact_text_exp,
                    desc_file.mask_pass_prob_label_exp, desc_file.curr_risk_header, "Prevalence",
                    "Background CO2 (ppm)", "Percentage susceptible ps", "Age Factor", "Viral Strain Factor"]
    params_df = pd.DataFrame(list(zip(param_labels, indoor_model.get_params())), columns=["Parameter", "Value"])
    params_df.to_excel(writer, sheet_name="Model Parameters", index=False)

    # Tab 3: Outputs (safe occupancy)
    occ_df = get_max_time_series(indoor_model, 2, indoor_model.get_n_max(), 1, risk_mode)
    occ_df = occ_df.rename(columns={'capacity': "Capacity",
                                    'exp-time': "[Risk Mode: " + risk_mode + "] Maximum Exposure Time (hr)"})
    occ_df.to_excel(writer, sheet_name="Outputs (Safe Occupancy)", index=False)

    # Tab 4: Outputs (safe CO2)
    co2_df = calc_co2_series(indoor_model, 0.1, 1000, 1000, risk_mode)
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


# Parses Excel file and returns a list of model inputs
def parse_excel(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if '.xls' in filename:
            # Assume that the user uploaded an Excel file
            df = pd.read_excel(io.BytesIO(decoded), sheet_name="Model Inputs", engine='openpyxl')
            return df["Value"].tolist()
    except Exception as e:
        print(e)
        return None

    return None


# Returns a dictionary of parameters and values given by the search url.
# Key: Parameter name
# Value: Parameter value
def search_to_params(search):
    output_dict = {}
    if search == "":
        return output_dict

    # remove initial question mark
    search = search[1:]

    params_raw = search.split("&")
    for param in params_raw:
        param_split = param.split("=")
        output_dict[param_split[0]] = param_split[1]

    return output_dict


# Returns text for updating language from the given descriptions file.
def get_lang_text_basic(language, disp_width):
    desc_file = get_desc_file(language)

    humidity_marks = desc_file.humidity_marks
    risk_tol_marks = desc_file.risk_tol_marks
    if disp_width < 1200:
        # use our mobile marks
        humidity_marks = {
            0.01: desc_file.humidity_marks[0.01],
            0.6: desc_file.humidity_marks[0.6],
            0.99: desc_file.humidity_marks[0.99],
        }
        risk_tol_marks = {
            0.1: desc_file.risk_tol_marks[0.1],
            1: desc_file.risk_tol_marks[1]
        }

    main_panel_six_ft_3 = ""
    if hasattr(desc_file, 'main_panel_six_ft_3'):
        main_panel_six_ft_3 = desc_file.main_panel_six_ft_3

    # if a language doesn't have the same amount of viral presets as english, fallback to english
    presets_strain = desc.presets_strain
    if len(desc_file.presets_strain) == len(desc.presets_strain):
        presets_strain = desc_file.presets_strain

    return [desc_file.about_header,
            desc_file.curr_room_header,
            desc_file.presets,
            desc_file.curr_human_header,
            desc_file.presets_human,
            desc_file.curr_age_header,
            desc_file.presets_age,
            desc_file.curr_strain_header,
            presets_strain,
            desc_file.other_risk_modes_desc,
            desc_file.main_panel_s1,
            desc_file.main_panel_six_ft_1,
            desc_file.main_panel_six_ft_2,
            main_panel_six_ft_3,
            desc_file.main_airb_trans_only_disc_basic,
            desc_file.about,
            desc_file.room_header,
            desc_file.room_header,
            desc_file.ventilation_text,
            desc_file.ventilation_types,
            desc_file.filtration_text,
            desc_file.filter_types,
            desc_file.recirc_text,
            desc_file.recirc_types,
            desc_file.humidity_text,
            humidity_marks,
            desc_file.need_more_ctrl_text,
            desc_file.human_header,
            desc_file.human_header,
            desc_file.exertion_text,
            desc_file.exertion_types,
            desc_file.breathing_text,
            desc_file.expiratory_types,
            desc_file.mask_type_text,
            desc_file.mask_types,
            desc_file.mask_fit_text,
            desc_file.mask_fit_marks,
            desc_file.need_more_ctrl_text,
            desc_file.faq_header,
            desc_file.faq_top,
            desc_file.values_interest_desc,
            desc_file.relative_sus_label,
            desc_file.outdoor_air_frac_label,
            desc_file.aerosol_eff_label,
            desc_file.breathing_rate_label,
            desc_file.cq_label,
            desc_file.mask_pass_prob_label,
            desc_file.room_vol_label,
            desc_file.vent_rate_Label,
            desc_file.recirc_rate_label,
            desc_file.air_filt_label,
            desc_file.eff_aerosol_rad_label,
            desc_file.viral_deact_label,
            desc_file.sett_speed_label,
            desc_file.conc_relax_rate_label,
            desc_file.airb_trans_label,
            desc_file.faq_graphs_text,
            desc_file.faq_infect_rate,
            desc_file.assumptions_layout,
            desc_file.n_input_text_1,
            desc_file.n_input_text_2,
            desc_file.n_input_text_3,
            desc_file.t_input_text_1,
            desc_file.t_input_text_2,
            desc_file.t_input_text_3]


# Returns text for updating language from the given descriptions file.
def get_lang_text_adv(language, disp_width):
    desc_file = get_desc_file(language)

    humidity_marks = desc_file.humidity_marks
    risk_tol_marks = desc_file.risk_tol_marks
    mask_type_marks = desc_file.mask_type_marks
    if disp_width < 1200:
        # use our mobile marks
        humidity_marks = {
            0.01: desc_file.humidity_marks[0.01],
            0.6: desc_file.humidity_marks[0.6],
            0.99: desc_file.humidity_marks[0.99],
        }
        risk_tol_marks = {
            0.1: desc_file.risk_tol_marks[0.1],
            1: desc_file.risk_tol_marks[1]
        }
        mask_type_marks = {
            0: desc_file.mask_type_marks[0],
            0.50: desc_file.mask_type_marks[0.50],
            0.90: desc_file.mask_type_marks[0.90]
        }

    main_panel_six_ft_3 = ""
    if hasattr(desc_file, 'main_panel_six_ft_3'):
        main_panel_six_ft_3 = desc_file.main_panel_six_ft_3

    lang_break_age = ""
    if hasattr(desc_file, 'lang_break_age'):
        lang_break_age = desc_file.lang_break_age

    risk_mode_panel_header = desc.risk_mode_panel_header
    if hasattr(desc_file, 'risk_mode_panel_header'):
        risk_mode_panel_header = desc_file.risk_mode_panel_header

    co2_prev_input_1 = desc.co2_prev_input_1
    if hasattr(desc_file, 'co2_prev_input_1'):
        co2_prev_input_1 = desc_file.co2_prev_input_1

    co2_prev_input_2 = desc.co2_prev_input_2
    if hasattr(desc_file, 'co2_prev_input_2'):
        co2_prev_input_2 = desc_file.co2_prev_input_2

    occ_panel_header = desc.occupancy_panel_header
    if hasattr(desc_file, 'occupancy_panel_header'):
        occ_panel_header = desc_file.occupancy_panel_header

    co2_panel_header = desc.co2_title
    if hasattr(desc_file, 'co2_title'):
        co2_panel_header = desc_file.co2_title

    co2_param_desc = desc.co2_param_desc
    if hasattr(desc_file, 'co2_param_desc'):
        co2_param_desc = desc_file.co2_param_desc

    co2_atm_input_1 = desc.co2_atm_input_1
    if hasattr(desc_file, 'co2_atm_input_1'):
        co2_atm_input_1 = desc_file.co2_atm_input_1

    co2_atm_input_2 = desc.co2_atm_input_2
    if hasattr(desc_file, 'co2_atm_input_2'):
        co2_atm_input_2 = desc_file.co2_atm_input_2

    co2_calc_1 = desc.co2_calc_1
    if hasattr(desc_file, 'co2_calc_1'):
        co2_calc_1 = desc_file.co2_calc_1

    co2_calc_2 = desc.co2_calc_2
    if hasattr(desc_file, 'co2_calc_2'):
        co2_calc_2 = desc_file.co2_calc_2

    co2_calc_3 = desc.co2_calc_3
    if hasattr(desc_file, 'co2_calc_3'):
        co2_calc_3 = desc_file.co2_calc_3

    co2_calc_inv_1 = desc.co2_calc_inv_1
    if hasattr(desc_file, 'co2_calc_inv_1'):
        co2_calc_inv_1 = desc_file.co2_calc_inv_1

    co2_calc_inv_2 = desc.co2_calc_inv_2
    if hasattr(desc_file, 'co2_calc_inv_2'):
        co2_calc_inv_2 = desc_file.co2_calc_inv_2

    co2_calc_inv_3 = desc.co2_calc_inv_3
    if hasattr(desc_file, 'co2_calc_inv_3'):
        co2_calc_inv_3 = desc_file.co2_calc_inv_3

    co2_safe_footer = desc.co2_safe_footer
    if hasattr(desc_file, 'co2_safe_footer'):
        co2_safe_footer = desc_file.co2_safe_footer

    return [desc_file.about_header,
            desc_file.curr_room_header,
            desc_file.presets,
            desc_file.curr_risk_header,
            desc_file.curr_human_header,
            desc_file.presets_human,
            desc_file.curr_age_header,
            desc_file.age_group_marks,
            desc_file.curr_strain_header,
            desc_file.viral_strain_marks,
            desc_file.pim_header,
            desc_file.main_panel_six_ft_1,
            desc_file.main_panel_six_ft_2,
            main_panel_six_ft_3,
            desc_file.about,
            desc_file.room_header,
            desc_file.room_header,
            desc_file.ventilation_text_adv,
            desc_file.ventilation_types,
            desc_file.filtration_text_adv,
            desc_file.filter_types,
            desc_file.recirc_text_adv,
            desc_file.humidity_text,
            humidity_marks,
            desc_file.human_header,
            desc_file.human_header,
            desc_file.exertion_text,
            desc_file.exertion_types,
            desc_file.breathing_text,
            desc_file.expiratory_types,
            desc_file.mask_type_text,
            mask_type_marks,
            desc_file.mask_fit_text,
            desc_file.mask_fit_marks,
            risk_tol_marks,
            desc_file.other_io,
            desc_file.pop_immunity_header,
            desc_file.pop_immunity_desc,
            desc_file.perc_immune_label,
            desc_file.perc_infectious_label,
            desc_file.perc_susceptible_label,
            desc_file.other_io,
            desc_file.aerosol_radius_text,
            desc_file.viral_deact_text,
            desc_file.values_interest_header,
            desc_file.relative_sus_label,
            desc_file.outdoor_air_frac_label,
            desc_file.aerosol_eff_label,
            desc_file.breathing_rate_label,
            desc_file.cq_label,
            desc_file.mask_pass_prob_label,
            desc_file.room_vol_label,
            desc_file.vent_rate_Label,
            desc_file.recirc_rate_label,
            desc_file.air_filt_label,
            desc_file.eff_aerosol_rad_label,
            desc_file.viral_deact_label,
            desc_file.sett_speed_label,
            desc_file.conc_relax_rate_label,
            desc_file.airb_trans_label,
            desc_file.graph_output_header,
            " " + desc_file.units_hr,
            lang_break_age,
            desc_file.risk_options,
            co2_prev_input_1,
            co2_prev_input_2,
            desc_file.incidence_rate_refs,
            risk_mode_panel_header,
            occ_panel_header,
            co2_panel_header,
            co2_param_desc,
            co2_atm_input_1,
            co2_atm_input_2,
            co2_calc_1,
            co2_calc_2,
            co2_calc_3,
            co2_calc_inv_1,
            co2_calc_inv_2,
            co2_calc_inv_3,
            co2_safe_footer]


# Get header and footer based on language
def get_header_and_footer_text(language):
    desc_file = get_desc_file(language)
    footer = html.Div([desc_file.footer,
                       html.Div(normal_credits),
                       html.Div(translation_credits)],
                      className='footer-small-text')
    return [desc_file.header,
            desc_file.language_dd,
            desc_file.units_dd,
            desc_file.mode_dd,
            desc_file.unit_settings,
            desc_file.app_modes[0]['label'],
            desc_file.app_modes[1]['label'],
            footer]


# Returns description file based on language
def get_desc_file(language):
    desc_file = desc
    if language == "fr":
        desc_file = desc_fr
    elif language == "cs":
        desc_file = desc_cs
    elif language == "da":
        desc_file = desc_da
    elif language == "de":
        desc_file = desc_de
    elif language == "el":
        desc_file = desc_el
    elif language == "eu":
        desc_file = desc_eu
    elif language == "zh":
        desc_file = desc_zh
    elif language == "zh_tw":
        desc_file = desc_zh_tw
    elif language == "hi":
        desc_file = desc_hi
    elif language == "hu":
        desc_file = desc_hu
    elif language == "id":
        desc_file = desc_id
    elif language == "it":
        desc_file = desc_it
    elif language == "ko":
        desc_file = desc_ko
    elif language == "nl":
        desc_file = desc_nl
    elif language == "es":
        desc_file = desc_es
    elif language == "pt-br":
        desc_file = desc_pt_br
    elif language == "ru":
        desc_file = desc_ru
    elif language == "sv":
        desc_file = desc_sv

    return desc_file


# Converts floor area and ceiling height from one system to another system
def convert_units(from_units, to_units, floor_area, ceiling_height):
    if from_units != to_units:
        # We are switching units, so convert the floor area and ceiling height
        if to_units == "metric":
            floor_area = round(floor_area / m_to_ft / m_to_ft, 2)
            ceiling_height = round(ceiling_height / m_to_ft, 2)
        elif to_units == "british":
            floor_area = round(floor_area * m_to_ft * m_to_ft, 0)
            ceiling_height = round(ceiling_height * m_to_ft, 1)

    return [floor_area, ceiling_height]


# Checks if we switched units, based on search url and current floor area and ceiling height labels
def did_switch_units(search, floor_area_text, ceiling_height_text):
    desc_file = get_desc_file(get_lang(search))
    my_units = get_units(search)
    # Check if we are switching unit systems
    # What unit system are we using?
    curr_units = ""
    if floor_area_text == desc_file.floor_area_text and ceiling_height_text == desc_file.ceiling_height_text:
        curr_units = "british"
    elif floor_area_text == desc_file.floor_area_text_metric and \
            ceiling_height_text == desc_file.ceiling_height_text_metric:
        curr_units = "metric"
    else:
        # Changed languages
        curr_units = ""

    if curr_units != my_units:
        return curr_units
    else:
        return ""
