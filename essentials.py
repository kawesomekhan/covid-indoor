import plotly.express as px

# Nmax values for main red text output
model_output_n_vals = [2, 3, 4, 5, 10, 25, 50, 100]
model_output_n_vals_big = [50, 100, 200, 300, 400, 500, 750, 1000]


def get_model_figure(indoor_model):
    new_df = indoor_model.calc_n_max_series(2, 100, 1.0)
    new_fig = px.line(new_df, x="Maximum Exposure Time (hours)", y="Maximum Occupancy",
                      title="Occupancy vs. Exposure Time", height=400,
                      color_discrete_map={"Maximum Occupancy": "#de1616"})
    new_fig.update_layout(transition_duration=500)
    return new_fig


def get_model_output_text(indoor_model):
    # Check if we should use the normal n vals, or the big n vals
    n_val_series = model_output_n_vals
    if indoor_model.calc_max_time(model_output_n_vals[-1]) > 48 or indoor_model.get_six_ft_n() >= 100:
        n_val_series = model_output_n_vals_big

    model_output_text = ["", "", "", "", "", "", "", ""]
    index = 0
    for n_val in n_val_series:
        max_time = indoor_model.calc_max_time(n_val)  # hours
        units = 'hours'
        if round(max_time) < 1:
            units = 'minutes'
            max_time = max_time * 60
        elif round(max_time) > 48:
            units = 'days'
            max_time = max_time / 24

        if round(max_time) == 1:
            units = units[:-1]

        base_string = '{n_val} people for {val:.0f} ' + units + ','
        model_output_text[index] = base_string.format(n_val=n_val, val=max_time)
        index += 1

    model_output_text[-2] = model_output_text[-2] + ' or'
    model_output_text[-1] = model_output_text[-1][:-1] + '.'

    return model_output_text


def get_six_ft_text(indoor_model):
    six_ft_people = indoor_model.get_six_ft_n()
    if six_ft_people == 1:
        six_ft_text = ' {} person'.format(six_ft_people)
    else:
        six_ft_text = ' {} people'.format(six_ft_people)

    return six_ft_text


def get_interest_output_text(indoor_model):
    breathing_flow_rate = indoor_model.physio_params[0]
    infectiousness = indoor_model.disease_params[0]
    # Calculated Values of Interest Output
    interest_output = [
        '{:,.2f} ft\u00B3/min'.format(breathing_flow_rate * 35.3147 / 60),  # m3/hr to ft3/min
        '{:,.2f} quanta/hr'.format(infectiousness),
        '{:,.0f} ft\u00B3'.format(indoor_model.room_vol),
        '{:,.0f} ft\u00B3/min'.format(indoor_model.fresh_rate),
        '{:,.0f} ft\u00B3/min'.format(indoor_model.recirc_rate),
        '{:,.2f} /hr'.format(indoor_model.air_filt_rate),
        '{:,.2f} m/hr'.format(indoor_model.sett_speed),
        '{:,.2f} /hr'.format(indoor_model.conc_relax_rate),
        '{:,.2f} /hr (x10,000)'.format(indoor_model.airb_trans_rate * 10000),
    ]

    return interest_output




