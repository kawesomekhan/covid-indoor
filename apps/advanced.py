import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px
import indoors as ind
from indoors import Indoors

from app import app

"""
main.py contains the core functionality of the Dash app. It is responsible for taking inputs,
feeding those inputs to the model (indoors.py), and displaying the model outputs in an effective, concise
manner.

Properties: 
Dash App Setup
COVID-19 Calculator Setup
Dropdown Preset Values
Tab CSS Styles
Custom HTML Headers
Main App 

Methods: 
def update_figure: Calculate model & update displayed values
def update_risk_tol_disp: Update risk tolerance display value
def update_air_frac_disp: Update air fraction display value
"""

# COVID-19 Calculator Setup
myInd = ind.Indoors()
results_df = myInd.calc_n_max_series(2, 100, 1.0)
fig = px.line(results_df, x="Maximum Exposure Time (hours)", y="Maximum Occupancy",
              title="Occupancy vs. Exposure Time",
              height=400, color_discrete_map={"Maximum Occupancy": "#de1616"})

# Dropdown Preset Values
ventilation_default = 3
is_custom_vent = False
ventilation_types = [
    {'label': "Custom (see Advanced)", 'value': -1},
    {'label': "Closed windows (0.3 Outdoor ACH)", 'value': 0.3},
    {'label': "Open windows (2 Outdoor ACH)", 'value': 2},
    {'label': "Mechanical Ventilation (3 Outdoor ACH)", 'value': 3},
    {'label': "Open windows with fans (6 Outdoor ACH)", 'value': 6},
    {'label': "Mechanical Ventilation (8 Outdoor ACH)", 'value': 8},
    {'label': "Laboratory, Restaurant (9 Outdoor ACH)", 'value': 9},
    {'label': "Bar (15 Outdoor ACH)", 'value': 15},
    {'label': "Hospital (18 Outdoor ACH)", 'value': 18},
    {'label': "Toxic Laboratory (25 Outdoor ACH)", 'value': 25},
]

filter_default = 2
is_custom_filter = False
filter_types = [
    {'label': "Custom (see Advanced)", 'value': -1},
    {'label': "None", 'value': 0},
    {'label': "Residential Window AC (MERV 1-4)", 'value': 2},
    {'label': "Residential/Commercial/Industrial (MERV 5-8)", 'value': 6},
    {'label': "Residential/Commercial/Hospital (MERV 9-12)", 'value': 10},
    {'label': "Hospital & General Surgery (MERV 13-16)", 'value': 14},
    {'label': "HEPA (MERV 17-20)", 'value': 17}
]

recirc_default = 1
is_custom_recirc = False
recirc_types = [
    {'label': "Custom (see Advanced)", 'value': -1},
    {'label': "None (0 ACH)", 'value': 0},
    {'label': "Slow (0.3 ACH)", 'value': 0.3},
    {'label': "Moderate (1 ACH)", 'value': 1},
    {'label': "Fast (10 ACH)", 'value': 10},
]

exertion_types = [
    {'label': "Resting", 'value': 0.49},
    {'label': "Standing", 'value': 0.54},
    {'label': "Light Exercise", 'value': 1.38},
    {'label': "Moderate Exercise", 'value': 2.35},
    {'label': "Heavy Exercise", 'value': 3.30},
]

expiratory_types = [
    {'label': "Breathing (nose)", 'value': 1.1},
    {'label': "Breathing (nose-nose)", 'value': 8.8},
    {'label': "Breathing (deep-fast)", 'value': 4.2},
    {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Speaking (quiet speech)", 'value': 29},
    {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Speaking (normal speech)", 'value': 72},
    {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Speaking (loud speech)", 'value': 142},
    {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Singing (voiced 'aah')", 'value': 970},
]

mask_types = [
    {'label': "None (0% filtration)", 'value': 1},
    {'label': "Bandana (5% filtration)", 'value': 0.95},
    {'label': "Neck Gaiter (10% filtration)", 'value': 0.90},
    {'label': "2-layer cloth (20% filtration)", 'value': 0.80},
    {'label': "2-layer silk (30% filtration)", 'value': 0.70},
    {'label': "2-ply Batik cotton (50% filtration)", 'value': 0.50},
    {'label': "Surgical (85% filtration)", 'value': 0.15},
    {'label': "N95 Respirator (95% filtration)", 'value': 0.05},
    {'label': "2-ply cloth/MBP filter (98% filtration)", 'value': 0.02},
]

# Nmax values for main red text output
model_output_n_vals = [2, 3, 4, 5, 10, 25, 50, 100]
model_output_n_vals_big = [50, 100, 200, 300, 400, 500, 750, 1000]

# CSS Styles for Tabs (currently known issue in Dash with overriding default css)
tab_style = {
    'padding-left': '1em',
    'padding-right': '1em'
}

# Main App
layout = html.Div(children=[
    html.H1(children='MIT COVID-19 Indoor Safety Guideline - Advanced'),
    html.Div([
        html.Div(children='''
        Kasim Khan (2020)
    '''),
        html.Div(children='''
        Martin Z. Bazant and John W. M. Bush, medRxiv preprint (2020):
        "Beyond Six Feet: A Guideline to Limit Indoor Airborne Transmission of COVID-19"
    '''),
        html.Div([
            html.A(href='http://web.mit.edu/bazant/www/COVID-19/',
                   children='''
                http://web.mit.edu/bazant/www/COVID-19/
            '''),
        ]),
        html.Div([
            html.A(href='https://github.com/kawesomekhan/covid-indoor',
                   children='''
                https://github.com/kawesomekhan/covid-indoor
            '''),
        ]),

    ], style={'font-size': '13px'}),

    html.Br(),
    html.Div(
        className='grid',
        children=[
            html.Div(
                className='card',
                children=[
                    dcc.Tabs(value='tab-1', children=[
                        dcc.Tab(
                            label='About',
                            className='custom-tab',
                            children=[
                                html.Div(className='custom-tab-container',
                                         children=[
                                             html.H6("About: "),
                                             html.Div('''
                                                    COVID-19 has been spreading in homes, restaurants, bars, classrooms, and other
                                                    enclosed spaces via tiny, infective aerosol droplets suspended in the air.
                                                    To mitigate this spread, official public health guidelines have taken the form 
                                                    of minimum social distancing rules (6 feet in the U.S.) or maximum occupancy 
                                                    (25 people in Massachusetts). 
                                                '''),
                                             html.Br(),
                                             html.Div('''
                                                    However, public health has been slow to catch up with rapidly advancing science.
                                                    Naturally, the risk of COVID-19 transmission would not only depend on physical 
                                                    distance, but also on factors such as exposure time, mask usage, and ventilation
                                                    systems, among other factors.
                                                '''),
                                             html.Br(),
                                             html.Div('''
                                                    This app uses a mathematical model, developed by MIT professors Martin Z. Bazant 
                                                    and John Bush, to improve upon
                                                    current distancing guidelines by providing a more accurate description of
                                                    indoor COVID-19 transmission risk.
                                                '''),
                                             html.Br(),
                                             html.Div('''
                                                    Adjust parameters in the other tabs and see how different spaces handle
                                                    indoor COVID-19 transmission.
                                                '''),
                                         ]),

                            ],
                            style=tab_style,
                            selected_style=tab_style
                        ),
                        dcc.Tab(
                            label='Room Specifications',
                            className='custom-tab',
                            children=[
                                html.Div(className='custom-tab-container',
                                         children=[
                                             html.H6("Room Specifications: "),
                                             html.Br(),
                                             html.Div(["Floor Area (sq. ft.): ",
                                                       dcc.Input(id='adv-floor-area', value=900, type='number')]),
                                             html.Br(),
                                             html.Div(["Ceiling Height (ft.): ",
                                                       dcc.Input(id='adv-ceiling-height', value=12, type='number')]),
                                             html.Br(),
                                             html.Div(className='card-dropdown',
                                                      children=[html.Div(["Ventilation System: "])]),
                                             html.Div(className='card-dropdown',
                                                      children=[dcc.Dropdown(id='adv-ventilation-type',
                                                                             options=ventilation_types,
                                                                             value=ventilation_default,
                                                                             searchable=False,
                                                                             clearable=False)]),
                                             html.Br(),
                                             html.Div(["Filtration System: ",
                                                       dcc.Dropdown(id='adv-filter-type',
                                                                    options=filter_types,
                                                                    value=filter_default,
                                                                    searchable=False,
                                                                    clearable=False)]),
                                             html.Br(),
                                             html.Div(["Recirculation Rate: ",
                                                       dcc.Dropdown(id='adv-recirc-rate',
                                                                    options=recirc_types,
                                                                    value=recirc_default,
                                                                    searchable=False,
                                                                    clearable=False)]),
                                         ]),
                            ],
                            style=tab_style,
                            selected_style=tab_style
                        ),
                        dcc.Tab(
                            label='Human Behavior',
                            className='custom-tab',
                            children=[
                                html.Div(className='custom-tab-container',
                                         children=[
                                             html.H6("Human Behavior: "),
                                             html.Br(),
                                             html.Div(["Exertion Level: ",
                                                       dcc.Dropdown(id='adv-exertion-level',
                                                                    options=exertion_types,
                                                                    value=0.49,
                                                                    searchable=False,
                                                                    clearable=False)]),
                                             html.Br(),
                                             html.Div(["Expiratory Activity: ",
                                                       dcc.Dropdown(id='adv-exp-activity',
                                                                    options=expiratory_types,
                                                                    value=29,
                                                                    searchable=False,
                                                                    clearable=False)]),
                                             html.Br(),
                                             html.Div(["Masks? ",
                                                       dcc.Dropdown(id='adv-mask-type',
                                                                    options=mask_types,
                                                                    value=0.15,
                                                                    searchable=False,
                                                                    clearable=False)]),
                                             html.Br(),
                                             html.Div(["Risk Tolerance: ",
                                                       html.Span(id='adv-risk-tolerance-output'),
                                                       html.Div('''
                                                                   This represents the number of expected transmissions during the
                                                                   occupancy period. A vulnerable population, due to age or
                                                                   preexisting medical conditions, will generally require
                                                                   a lower risk tolerance. 
                                                          ''', style={'font-size': '13px', 'margin-left': '20px'}),
                                                       dcc.Slider(id='adv-risk-tolerance',
                                                                  min=0.01,
                                                                  max=1,
                                                                  step=0.01,
                                                                  value=0.1,
                                                                  marks={
                                                                      0.01: {'label': '0.01: Contact Tracing',
                                                                             'style': {'max-width': '50px'}},
                                                                      1: {'label': '1.0: Unsafe'}
                                                                  })
                                                       ])
                                         ]),
                            ],
                            style=tab_style,
                            selected_style=tab_style
                        ),
                        dcc.Tab(
                            label='Advanced',
                            className='custom-tab',
                            children=[
                                html.Div(className='custom-tab-container',
                                         children=[
                                             html.H6("Graph Output: "),
                                             html.Div([
                                                 dcc.Graph(
                                                     id='adv-safety-graph',
                                                     figure=fig
                                                 ),
                                             ])
                                         ]),
                            ],
                            style=tab_style,
                            selected_style=tab_style
                        )
                    ],
                             colors={
                                 "border": "#c9c9c9",
                                 "primary": "#de1616"
                             }),
                    html.Br()
                ]),
            html.Div(
                className='card',
                children=[
                    html.Div([
                        html.H3([
                            '''Based on this model, it should be safe for this room to have:
                    ''']),
                        html.H4(className='model-output-text', id='adv-model-text-1'),
                        html.H4(className='model-output-text', id='adv-model-text-2'),
                        html.H4(className='model-output-text', id='adv-model-text-3'),
                        html.H4(className='model-output-text', id='adv-model-text-4'),
                        html.H4(className='model-output-text', id='adv-model-text-5'),
                        html.H4(className='model-output-text', id='adv-model-text-6'),
                        html.H4(className='model-output-text', id='adv-model-text-7'),
                        html.H4(className='model-output-text', id='adv-model-text-8'),
                        html.Br(),
                        html.H3([
                            '''In comparison, current six feet distancing guidelines recommend no more than''',
                            html.Span(id='adv-six-ft-output', children=''' 2 people ''', style={'color': '#de1616'}),
                            ''' in this room.''']),
                    ]),
                ], style={'padding-top': '0px'}),
        ]
    ),
    html.Br(),
    html.Form(
        action=''
    )
])


# Model Update & Calculation
# See indoors.py def set_default_params(self) for parameter descriptions.
@app.callback(
    [Output('adv-safety-graph', 'figure'),
     Output('adv-model-text-1', 'children'),
     Output('adv-model-text-2', 'children'),
     Output('adv-model-text-3', 'children'),
     Output('adv-model-text-4', 'children'),
     Output('adv-model-text-5', 'children'),
     Output('adv-model-text-6', 'children'),
     Output('adv-model-text-7', 'children'),
     Output('adv-model-text-8', 'children'),
     Output('adv-six-ft-output', 'children')],
    [Input('adv-floor-area', 'value'),
     Input('adv-ceiling-height', 'value'),
     Input('adv-ventilation-type', 'value'),
     Input('adv-recirc-rate', 'value'),
     Input('adv-filter-type', 'value'),
     Input('adv-exertion-level', 'value'),
     Input('adv-exp-activity', 'value'),
     Input('adv-mask-type', 'value'),
     Input('adv-risk-tolerance', 'value')]
)
def update_figure(floor_area, ceiling_height, air_exchange_rate, recirc_rate, merv,
                  breathing_flow_rate, infectiousness, mask_passage_prob, risk_tolerance):
    # Make sure none of our values are none
    is_none = floor_area is None or ceiling_height is None or recirc_rate is None
    if is_none:
        raise PreventUpdate

    # Update model with newly-selected parameters
    aerosol_radius = 2
    aerosol_filtration_eff = Indoors.merv_to_eff(merv, aerosol_radius)

    # Convert recirc rate to outdoor air fraction
    outdoor_air_fraction = air_exchange_rate / (air_exchange_rate + recirc_rate)

    myInd.physical_params = [floor_area, ceiling_height, air_exchange_rate, outdoor_air_fraction,
                             aerosol_filtration_eff]
    myInd.physio_params = [breathing_flow_rate, aerosol_radius]
    myInd.disease_params = [infectiousness, 0.3]
    myInd.prec_params = [mask_passage_prob, risk_tolerance]
    myInd.calc_vars()

    # Update the figure with a new model calculation
    new_df = myInd.calc_n_max_series(2, 100, 1.0)
    new_fig = px.line(new_df, x="Maximum Exposure Time (hours)", y="Maximum Occupancy",
                      title="Occupancy vs. Exposure Time", height=400,
                      color_discrete_map={"Maximum Occupancy": "#de1616"})
    new_fig.update_layout(transition_duration=500)

    # Update the red text output with new model calculations
    model_output_text = ["", "", "", "", "", "", "", ""]
    index = 0

    # Check if we should use the normal n vals, or the big n vals
    n_val_series = model_output_n_vals
    if myInd.calc_max_time(model_output_n_vals[-1]) > 48:
        n_val_series = model_output_n_vals_big

    for n_val in n_val_series:
        max_time = myInd.calc_max_time(n_val)  # hours
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

    six_ft_people = myInd.get_six_ft_n()
    if six_ft_people == 1:
        six_ft_text = ' {} person'.format(six_ft_people)
    else:
        six_ft_text = ' {} people'.format(six_ft_people)

    # Update all relevant display items (figure, red output text)
    return new_fig, model_output_text[0], model_output_text[1], model_output_text[2], model_output_text[3], \
           model_output_text[4], model_output_text[5], model_output_text[6], model_output_text[7], \
           six_ft_text


# Risk tolerance slider value display
@app.callback(
    [Output('adv-risk-tolerance-output', 'children')],
    [Input('adv-risk-tolerance', 'value')]
)
def update_risk_tol_disp(risk_tolerance):
    return ["{:.2f}".format(risk_tolerance)]


