import plotly.graph_objects as go

"""
essentials.py contains functionality shared by both Basic Mode and Advanced Mode.

"""

# Default dropdown options shared between basic mode and advanced mode
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
    'font-size': '14px'
}

tab_style_selected = {
    'padding-left': '1em',
    'padding-right': '1em',
    'border-color': '#DDDDDD',
    'border-top-color': '#de1616',
    'font-size': '14px'
}

# Nmax values for main red text output
model_output_n_vals = [2, 3, 4, 5, 10, 25, 50, 100]
model_output_n_vals_big = [50, 100, 200, 300, 400, 500, 750, 1000]

# Max time reported in the big red text output
recovery_time = 14  # Days


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




