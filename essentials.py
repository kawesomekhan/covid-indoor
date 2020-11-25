import plotly.graph_objects as go
import dash_html_components as html

import descriptions as desc
import descriptions_es as desc_es
import descriptions_fr as desc_fr
import descriptions_zh as desc_zh
import descriptions_id as desc_id
import descriptions_ko as desc_ko

"""
essentials.py contains functionality shared by both Basic Mode and Advanced Mode.

"""

normal_credits = '''William H. Green, David Keating, Ann Kinzig, Caeli MacLennan, Michelle Quien, Marc Rosenbaum, 
                 David Stark'''
translation_credits = '''Khoiruddin Ad-Damaki, John Bush, Rafael Suarez Camacho, 
                        Laura Champion, Surya Effendy, Sung Jae Kim, Bonho Koo, John Ochsendorf, Juan Puyo, 
                        Myungjin Seo, Huanhuan Tian, Gede Wenten, Hongbo Zhao, Juner Zhu'''

m_to_ft = 3.28084

# CSS Styles for Tabs (currently known issue in Dash with overriding default css)
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

preset_settings = {
    'house': {
        'floor-area': 2000,
        'ceiling-height': 12,
        'floor-area-metric': 2000 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 12 / m_to_ft,
        'ventilation': 3,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.49,
        'exp-activity': 29,
        'masks': 0.75
    },
    'classroom': {
        'floor-area': 900,
        'ceiling-height': 12,
        'floor-area-metric': 900 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 12 / m_to_ft,
        'ventilation': 3,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.49,
        'exp-activity': 29,
        'masks': 0.75
    },
    'restaurant': {
        'floor-area': 5000,
        'ceiling-height': 12,
        'floor-area-metric': 5000 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 12 / m_to_ft,
        'ventilation': 9,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.49,
        'exp-activity': 72,
        'masks': 0
    },
    'office': {
        'floor-area': 10000,
        'ceiling-height': 12,
        'floor-area-metric': 10000 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 12 / m_to_ft,
        'ventilation': 8,
        'filtration': 10,
        'recirc-rate': 1,
        'exertion': 0.54,
        'exp-activity': 29,
        'masks': 0.75
    },
    'subway': {
        'floor-area': 580,
        'ceiling-height': 10,
        'floor-area-metric': 580 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 10 / m_to_ft,
        'ventilation': 18,
        'filtration': 6,
        'recirc-rate': 54,
        'exertion': 0.54,
        'exp-activity': 29,
        'masks': 0.75
    },
    'bus': {
        'floor-area': 380,
        'ceiling-height': 10,
        'floor-area-metric': 380 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 10 / m_to_ft,
        'ventilation': 8,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.54,
        'exp-activity': 29,
        'masks': 0.75
    },
    'airplane': {
        'floor-area': 1440,
        'ceiling-height': 6.7,
        'floor-area-metric': 1440 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 6.7 / m_to_ft,
        'ventilation': 24,
        'filtration': 17,
        'recirc-rate': 24,
        'exertion': 0.54,
        'exp-activity': 72,
        'masks': 0.75
    },
    'church': {
        'floor-area': 1900,
        'ceiling-height': 30,
        'floor-area-metric': 1900 / m_to_ft / m_to_ft,
        'ceiling-height-metric': 30 / m_to_ft,
        'ventilation': 2,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.54,
        'exp-activity': 72,
        'masks': 0.75
    },
}

ventilation_default = preset_settings['classroom']['ventilation']
filter_default = preset_settings['classroom']['filtration']
recirc_default = preset_settings['classroom']['recirc-rate']

# Nmax values for main red text output
model_output_n_vals = [2, 3, 4, 5, 10, 25, 50, 100]
model_output_n_vals_big = [50, 100, 200, 300, 400, 500, 750, 1000]

# Max time reported in the big red text output
recovery_time = 14  # Days


# Determines what error message we should use, if any
def get_err_msg(floor_area, ceiling_height, air_exchange_rate, merv, recirc_rate, max_aerosol_radius,
                max_viral_deact_rate, language, n_max_input=2, exp_time_input=1):
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
    elif exp_time_input == 0 or exp_time_input is None:
        error_msg = desc_file.error_list["exp_time_input"]
    elif air_exchange_rate == 0 or air_exchange_rate is None:
        error_msg = desc_file.error_list["air_exchange_rate"]
    elif merv is None:
        error_msg = desc_file.error_list["merv"]

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
def get_preset_dd_value(floor_area, ceiling_height, air_exchange_rate, recirc_rate, merv, breathing_flow_rate,
                        infectiousness, mask_eff, units):
    preset_dd_value = 'custom'
    for setting_key in preset_settings:
        setting = preset_settings[setting_key]

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
                    setting['exertion'] == breathing_flow_rate and \
                    setting['exp-activity'] == infectiousness and \
                    setting['masks'] == mask_eff
        if is_preset:
            preset_dd_value = setting_key
            break

    return preset_dd_value


# Returns the plotly figure based on the supplied indoor model.
def get_model_figure(indoor_model, language):
    desc_file = get_desc_file(language)
    new_df = indoor_model.calc_n_max_series(2, 100, 1.0)

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


# Returns the big red output text.
def get_model_output_text(indoor_model, language):
    desc_file = get_desc_file(language)
    # Check if we should use the normal n vals, or the big n vals
    n_val_series = model_output_n_vals
    if indoor_model.calc_max_time(model_output_n_vals[-1]) > 48 or indoor_model.get_six_ft_n() >= 100:
        n_val_series = model_output_n_vals_big

    model_output_text = ["", "", "", "", "", "", "", ""]
    index = 0
    for n_val in n_val_series:
        max_time = indoor_model.calc_max_time(n_val)  # hours
        time_text = time_to_text(max_time, language)

        is_past_recovery = round(max_time) > (24 * recovery_time)
        if is_past_recovery:
            base_string = desc_file.is_past_recovery_base_string
            max_time = recovery_time
            model_output_text[index] = base_string.format(n_val=n_val, val=max_time)
        else:
            base_string = desc_file.model_output_base_string + time_text
            model_output_text[index] = base_string.format(n_val=n_val)

        index += 1

    if language == "en":
        model_output_text[-2] = model_output_text[-2] + ' or'
        model_output_text[-1] = model_output_text[-1] + '.'

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


# Converts a time (in hours) into a text with formatting based on minutes/hours/days
def time_to_text(time, language):
    desc_file = get_desc_file(language)

    if round(time) < 2:
        time = time * 60
        if round(time) == 1:
            units = desc_file.units_min_one
        else:
            units = desc_file.units_min
    elif round(time) > 48:
        time = time / 24
        if round(time) == 1:
            units = desc_file.units_day_one
        else:
            units = desc_file.units_days
    else:
        if round(time) == 1:
            units = desc_file.units_hr_one
        else:
            units = desc_file.units_hr

    base_string = '{val:.0f} ' + units
    return base_string.format(val=time)


# Gets n max text
def get_n_max_text(n, language):
    desc_file = get_desc_file(language)
    return desc_file.n_max_base_string.format(n)


# Returns the output text for the variables of interest, shown in the FAQ/Other Inputs & Outputs tab.
# units: British or Metric.
def get_interest_output_text(indoor_model, units):
    outdoor_air_frac = indoor_model.physical_params[3]
    aerosol_filtration_eff = indoor_model.physical_params[4]
    breathing_flow_rate = indoor_model.physio_params[0]
    infectiousness = indoor_model.disease_params[0]
    mask_pass_prob = indoor_model.prec_params[0]

    # Calculated Values of Interest Output
    if units == "british":
        interest_output = [
            '{:,.2f}'.format(outdoor_air_frac),
            '{:,.2f}'.format(aerosol_filtration_eff),
            '{:,.2f} ft\u00B3/min'.format(breathing_flow_rate * 35.3147 / 60),  # m3/hr to ft3/min
            '{:,.2f} quanta/ft\u00B3'.format(infectiousness / 35.3147),  # 1/m3 to 1/ft3
            '{:,.2f}'.format(mask_pass_prob),
            '{:,.0f} ft\u00B3'.format(indoor_model.room_vol),
            '{:,.0f} ft\u00B3/min'.format(indoor_model.fresh_rate),
            '{:,.0f} ft\u00B3/min'.format(indoor_model.recirc_rate),
            '{:,.2f} /hr'.format(indoor_model.air_filt_rate),
            '{:,.2f} \u03bcm'.format(indoor_model.eff_aerosol_radius),
            '{:,.2f} /hr'.format(indoor_model.viral_deact_rate),
            '{:,.2f} ft/min'.format(indoor_model.sett_speed * 3.281 / 60),  # m/hr to ft/min
            '{:,.2f} /hr'.format(indoor_model.conc_relax_rate),
            '{:,.2f} /hr (x10,000)'.format(indoor_model.airb_trans_rate * 10000),
        ]
    elif units == "metric":
        interest_output = [
            '{:,.2f}'.format(outdoor_air_frac),
            '{:,.2f}'.format(aerosol_filtration_eff),
            '{:,.2f} m\u00B3/hr'.format(breathing_flow_rate),
            '{:,.2f} quanta/m\u00B3'.format(infectiousness),
            '{:,.2f}'.format(mask_pass_prob),
            '{:,.0f} m\u00B3'.format(indoor_model.room_vol / 35.315),  # ft3 to m3
            '{:,.0f} m\u00B3/hr'.format(indoor_model.fresh_rate / 35.3147 * 60),  # ft3/min to m3/hr
            '{:,.0f} m\u00B3/hr'.format(indoor_model.recirc_rate / 35.3147 * 60),  # ft3/min to m3/hr
            '{:,.2f} /hr'.format(indoor_model.air_filt_rate),
            '{:,.2f} \u03bcm'.format(indoor_model.eff_aerosol_radius),
            '{:,.2f} /hr'.format(indoor_model.viral_deact_rate),
            '{:,.2f} m/hr'.format(indoor_model.sett_speed),
            '{:,.2f} /hr'.format(indoor_model.conc_relax_rate),
            '{:,.2f} /hr (x10,000)'.format(indoor_model.airb_trans_rate * 10000),
        ]

    return interest_output


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
def get_lang_text_basic(language):
    desc_file = get_desc_file(language)
    return [desc_file.about_header,
            desc_file.curr_room_header,
            desc_file.presets,
            desc_file.main_panel_s1,
            desc_file.main_panel_six_ft_1,
            desc_file.main_panel_six_ft_2,
            desc_file.main_airb_trans_only_disc,
            desc_file.n_input_text_1,
            desc_file.n_input_text_2,
            desc_file.n_input_text_3,
            desc_file.airb_trans_only_disc,
            desc_file.t_input_text_1,
            desc_file.t_input_text_2,
            desc_file.t_input_text_3,
            desc_file.airb_trans_only_disc,
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
            desc_file.humidity_marks,
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
            desc_file.risk_tolerance_text,
            desc_file.risk_tol_desc,
            desc_file.risk_tol_marks,
            desc_file.need_more_ctrl_text,
            desc_file.faq_header,
            desc_file.faq_top,
            desc_file.values_interest_desc,
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
            desc_file.assumptions_layout]


# Returns text for updating language from the given descriptions file.
def get_lang_text_adv(language):
    desc_file = get_desc_file(language)
    return [desc_file.about_header,
            desc_file.curr_room_header,
            desc_file.presets,
            desc_file.main_panel_s1,
            desc_file.main_panel_six_ft_1,
            desc_file.main_panel_six_ft_2,
            desc_file.main_airb_trans_only_disc,
            desc_file.n_input_text_1,
            desc_file.n_input_text_2,
            desc_file.n_input_text_3,
            desc_file.airb_trans_only_disc,
            desc_file.t_input_text_1,
            desc_file.t_input_text_2,
            desc_file.t_input_text_3,
            desc_file.airb_trans_only_disc,
            desc_file.about,
            desc_file.room_header,
            desc_file.room_header,
            desc_file.ventilation_text,
            desc_file.ventilation_types,
            desc_file.filtration_text,
            desc_file.filter_types,
            desc_file.recirc_text,
            desc_file.humidity_text,
            desc_file.humidity_marks,
            desc_file.human_header,
            desc_file.human_header,
            desc_file.exertion_text,
            desc_file.exertion_types,
            desc_file.breathing_text,
            desc_file.expiratory_types,
            desc_file.mask_type_text,
            desc_file.mask_type_marks,
            desc_file.mask_fit_text,
            desc_file.mask_fit_marks,
            desc_file.risk_tolerance_text,
            desc_file.risk_tol_desc,
            desc_file.risk_tol_marks,
            desc_file.other_io,
            desc_file.other_io,
            desc_file.aerosol_radius_text,
            desc_file.viral_deact_text,
            desc_file.values_interest_header,
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
            desc_file.graph_output_header]


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
            desc_file.app_modes,
            footer]


# Returns description file based on language
def get_desc_file(language):
    desc_file = desc
    if language == "fr":
        desc_file = desc_fr
    elif language == "zh":
        desc_file = desc_zh
    elif language == "id":
        desc_file = desc_id
    elif language == "ko":
        desc_file = desc_ko
    elif language == "es":
        desc_file = desc_es

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





