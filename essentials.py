import plotly.graph_objects as go

import descriptions as desc

"""
essentials.py contains functionality shared by both Basic Mode and Advanced Mode.

"""

# Default dropdown options shared between basic mode and advanced mode
humidity_marks = {
    0: {'label': '0%: Very Dry', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: Airplane', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Dry'},
    0.6: {'label': '60%: Average'},
    0.99: {'label': '99%: Very Humid'},
}

exertion_types = [
    {'label': "Resting", 'value': 0.49},
    {'label': "Standing", 'value': 0.54},
    {'label': "Light Exercise", 'value': 1.38},
    {'label': "Moderate Exercise", 'value': 2.35},
    {'label': "Heavy Exercise", 'value': 3.30},
]

expiratory_types = [
    {'label': "Breathing (light)", 'value': 1.1},
    {'label': "Breathing (normal)", 'value': 4.2},
    {'label': "Breathing (heavy)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Talking (whisper)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Talking (normal)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Talking (loud)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Singing", 'value': 970},
]

mask_type_marks = {
    0: {'label': "0% (none, face shield)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (coarse cotton)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (silk, flannel, chiffon)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (surgical, cotton)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (N95 respirator)", 'style': {'max-width': '50px'}},
}

mask_types = [
    {'label': "None, Face Shield", 'value': 0},
    {'label': "Coarse Cotton", 'value': 0.1},
    {'label': "Silk, Flannel, Chiffon", 'value': 0.5},
    {'label': "Surgical, Cotton", 'value': 0.75},
    {'label': "N95 Respirator", 'value': 0.95},
]

mask_fit_marks = {
    0: {'label': '0%: None', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Poor'},
    0.95: {'label': '95%: Good'}
}

risk_tol_marks = {
    0.01: {'label': '0.01: Safest', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Safe', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Unsafe'}
}

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

presets = [
    {'label': "Custom", 'value': 'custom'},
    {'label': "Suburban House", 'value': 'house'},
    {'label': "Restaurant", 'value': 'restaurant'},
    {'label': "Quiet Office", 'value': 'office'},
    {'label': "Classroom Lecture", 'value': 'classroom'},
    {'label': "New York City Subway Car", 'value': 'subway'},
    {'label': "Boeing 737", 'value': 'airplane'},
    {'label': "Church", 'value': 'church'},
]

preset_settings = {
    'house': {
        'floor-area': 2000,
        'ceiling-height': 12,
        'floor-area-metric': 2000 / 10.764,
        'ceiling-height-metric': 12 / 10.764,
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
        'floor-area-metric': 900 / 10.764,
        'ceiling-height-metric': 12 / 10.764,
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
        'floor-area-metric': 5000 / 10.764,
        'ceiling-height-metric': 12 / 10.764,
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
        'floor-area-metric': 10000 / 10.764,
        'ceiling-height-metric': 12 / 10.764,
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
        'floor-area-metric': 580 / 10.764,
        'ceiling-height-metric': 10 / 10.764,
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
        'floor-area-metric': 380 / 10.764,
        'ceiling-height-metric': 10 / 10.764,
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
        'floor-area-metric': 1440 / 10.764,
        'ceiling-height-metric': 6.7 / 10.764,
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
        'floor-area-metric': 1900 / 10.764,
        'ceiling-height-metric': 30 / 10.764,
        'ventilation': 2,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.54,
        'exp-activity': 72,
        'masks': 0.75
    },
}

# Nmax values for main red text output
model_output_n_vals = [2, 3, 4, 5, 10, 25, 50, 100]
model_output_n_vals_big = [50, 100, 200, 300, 400, 500, 750, 1000]

# Max time reported in the big red text output
recovery_time = 14  # Days


# Determines what error message we should use, if any
def get_err_msg(floor_area, ceiling_height, air_exchange_rate, merv, recirc_rate, max_aerosol_radius,
                max_viral_deact_rate, n_max_input=2, exp_time_input=1):
    error_msg = ""

    # Make sure none of our values are none
    if floor_area is None:
        error_msg = desc.error_list["floor_area"]
    elif ceiling_height is None:
        error_msg = desc.error_list["ceiling_height"]
    elif recirc_rate is None:
        error_msg = desc.error_list["recirc_rate"]
    elif max_aerosol_radius is None:
        error_msg = desc.error_list["aerosol_radius"]
    elif max_viral_deact_rate is None:
        error_msg = desc.error_list["viral_deact_rate"]
    elif n_max_input is None or n_max_input < 2:
        error_msg = desc.error_list["n_max_input"]
    elif exp_time_input == 0 or exp_time_input is None:
        error_msg = desc.error_list["exp_time_input"]
    elif air_exchange_rate == 0 or air_exchange_rate is None:
        error_msg = desc.error_list["air_exchange_rate"]
    elif merv is None:
        error_msg = desc.error_list["merv"]

    return error_msg


# Returns unit selection based on URL search
def get_units(search):
    params = search_to_params(search)
    my_units = "british"
    if "units" in params:
        my_units = params["units"]

    return my_units


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


# # Get preset settings based on preset and units
# def get_preset_settings(preset, units):
#     if units == "british":
#         return preset_settings[preset]
#     elif units == "metric":
#         metric_settings = preset_settings[preset]



# Returns the plotly figure based on the supplied indoor model.
def get_model_figure(indoor_model):
    new_df = indoor_model.calc_n_max_series(2, 100, 1.0)

    new_fig = go.Figure()
    new_fig.add_trace(go.Scatter(x=new_df["exposure_time"], y=new_df["occupancy_trans"],
                                 mode='lines',
                                 name='Transient',
                                 line=go.scatter.Line(color="#8ad4ed")))
    new_fig.add_trace(go.Scatter(x=new_df["exposure_time"], y=new_df["occupancy_ss"],
                                 mode='lines',
                                 name='Steady-State',
                                 line=go.scatter.Line(color="#2490b5"),
                                 visible='legendonly'))
    new_fig.update_layout(transition_duration=500,
                          title="Occupancy vs. Exposure Time", height=400,
                          xaxis_title="Maximum Exposure Time \u03C4 (hours)",
                          yaxis_title="Maximum Occupancy N",
                          font_family="Barlow",
                          template="simple_white",
                          hoverlabel=dict(
                              font_family="Barlow"
                          ))
    return new_fig


# Returns the big red output text.
def get_model_output_text(indoor_model):
    # Check if we should use the normal n vals, or the big n vals
    n_val_series = model_output_n_vals
    if indoor_model.calc_max_time(model_output_n_vals[-1]) > 48 or indoor_model.get_six_ft_n() >= 100:
        n_val_series = model_output_n_vals_big

    model_output_text = ["", "", "", "", "", "", "", ""]
    index = 0
    for n_val in n_val_series:
        max_time = indoor_model.calc_max_time(n_val)  # hours
        time_text = time_to_text(max_time)

        is_past_recovery = round(max_time) > (24 * recovery_time)
        if is_past_recovery:
            base_string = '{n_val} people for >{val:.0f} days,'
            max_time = recovery_time
            model_output_text[index] = base_string.format(n_val=n_val, val=max_time)
        else:
            base_string = '{n_val} people for ' + time_text
            model_output_text[index] = base_string.format(n_val=n_val)

        index += 1

    model_output_text[-2] = model_output_text[-2] + ' or'
    model_output_text[-1] = model_output_text[-1] + '.'

    return model_output_text


# Returns the six feet distancing text.
def get_six_ft_text(indoor_model):
    six_ft_people = indoor_model.get_six_ft_n()
    if six_ft_people == 1:
        six_ft_text = ' {} person'.format(six_ft_people)
    else:
        six_ft_text = ' {} people'.format(six_ft_people)

    return six_ft_text


# Converts a time (in hours) into a text with formatting based on minutes/hours/days
def time_to_text(time):
    units = 'hours'
    if round(time) < 2:
        units = 'minutes'
        time = time * 60
    elif round(time) > 48:
        units = 'days'
        time = time / 24

    if round(time) == 1:
        units = units[:-1]

    base_string = '{val:.0f} ' + units
    return base_string.format(val=time)


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
