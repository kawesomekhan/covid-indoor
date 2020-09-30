import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px
import indoors as ind
from indoors import Indoors

from app import app

# COVID-19 Calculator Setup
myInd = ind.Indoors()
results_df = myInd.calc_n_max_series(2, 100, 1.0)
fig = px.line(results_df, x="Maximum Exposure Time (hours)", y="Maximum Occupancy",
              title="Occupancy vs. Exposure Time",
              height=400, color_discrete_map={"Maximum Occupancy": "#de1616"})

# Dropdown Preset Values

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
    html.H1(children='MIT COVID-19 Indoor Safety Guideline'),
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
        className='main-content',
        children=[
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
                                                               dcc.Input(id='adv-floor-area', value=900,
                                                                         type='number')]),
                                                     html.Br(),
                                                     html.Div(["Ceiling Height (ft.): ",
                                                               dcc.Input(id='adv-ceiling-height', value=12,
                                                                         type='number')]),
                                                     html.Br(),
                                                     html.Div(["Ventilation System (ACH): ",
                                                               dcc.Input(id='adv-ventilation-type', value=3,
                                                                         type='number')]),
                                                     html.Br(),
                                                     html.Div(["Filtration System (MERV): ",
                                                               dcc.Input(id='adv-filter-type', value=6,
                                                                         type='number')]),
                                                     html.Br(),
                                                     html.Div(["Recirculation Rate (ACH): ",
                                                               dcc.Input(id='adv-recirc-rate', value=1,
                                                                         type='number')]),
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
                                                               A higher risk tolerance will mean more expected 
                                                               transmissions during the expected occupancy period, 
                                                               while a lower risk tolerance will mean fewer expected 
                                                               transmissions during the expected occupancy period 
                                                               (see Advanced Input & Output for details). More 
                                                               vulnerable populations such as the elderly or those 
                                                               with preexisting medical conditions will generally 
                                                               require a lower risk tolerance.
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
                                    label='Other Inputs & Assumptions',
                                    className='custom-tab',
                                    children=[
                                        html.Div(className='custom-tab-container',
                                                 children=[
                                                     html.H6("Other Model Inputs: "),
                                                     html.Div(["Aerosol Radius r\u0305 (\u03bcm): ",
                                                               dcc.Input(id='adv-aerosol-radius', value=2, type='number')]),
                                                     html.Br(),
                                                     html.Div(["Viral Deactivation Rate \u03BBv (/hr): ",
                                                               dcc.Input(id='adv-viral-deact-rate', value=0.3,
                                                                         type='number')]),
                                                     html.Br(),
                                                     html.Br(),
                                                     html.H6("Calculated Values of Interest: "),
                                                     html.Div([
                                                         html.Div(["Room volume V: ",
                                                                   html.Span(className='model-output-text-small',
                                                                             id='adv-room-vol-output')]),
                                                         html.Div(["Ventilation (outdoor) flow rate Q: ",
                                                                   html.Span(className='model-output-text-small',
                                                                             id='adv-fresh-rate-output')]),
                                                         html.Div(["Return (recirculation) flow rate Qf: ",
                                                                   html.Span(className='model-output-text-small',
                                                                             id='adv-recirc-rate-output')]),
                                                         html.Div(["Air filtration rate (\u03BBf): ",
                                                                   html.Span(className='model-output-text-small',
                                                                             id='adv-air-filt-rate-output')]),
                                                         html.Div(
                                                             ["Effective aerosol settling speed v\u209B(r\u0305): ",
                                                              html.Span(className='model-output-text-small',
                                                                        id='adv-sett-speed-output')]),
                                                         html.Div(["Concentration relaxation rate \u03BBc: ",
                                                                   html.Span(className='model-output-text-small',
                                                                             id='adv-conc-relax-output')]),
                                                         html.Div(["Airborne transmission rate \u03B2\u2090: ",
                                                                   html.Span(className='model-output-text-small',
                                                                             id='adv-airb-trans-output')]),
                                                     ]),
                                                     html.Br(),
                                                     html.H6("Graph Output: "),
                                                     html.Div([
                                                         dcc.Graph(
                                                             id='adv-safety-graph',
                                                             figure=fig
                                                         ),
                                                     ]),
                                                     html.Br(),
                                                     html.H6("Assumptions: "),
                                                     html.Div('''This guideline provides specific recommendations on 
                                                       how to limit COVID-19 transmission through well-mixed indoor 
                                                       air, but one should also consider various caveats emphasized 
                                                       in the paper and other literature, including the possibility 
                                                       of short-range aerosol transmission in respiratory jets. 
                                                       Such effects, which can lead to large fluctuations in droplet 
                                                       concentrations around their mean values, especially when 
                                                       masks are not worn, are only partially addressed by choosing 
                                                       a sufficiently small tolerance in the well-mixed guideline 
                                                       and will depend on the details of airflow and human behavior 
                                                       in a specific indoor space.'''),
                                                     html.Br(),
                                                     html.Div("This model makes the following assumptions:"),
                                                     html.Div([
                                                         html.Div('''- The volumetric breathing flow rate Qb is determined by
                                                           the level of activity. Average values for healthy males and
                                                           females have been reported as 0.49, 0.54, 1.38, 2.35, and 3.30
                                                           m\u00B3/hr for resting, standing, light exercise, moderate
                                                           exercise, and heavy exercise, respectively, and used in
                                                           simulations of airborne transmission of COVID-19.
                                                       '''),
                                                         html.Div('''
                                                           - The most important disease parameter is the infectiousness
                                                           of exhaled air, Cq (infection quanta per unit volume). This
                                                           is discussed extensively in the main text. Using all of the
                                                           limited information available today, Cq is estimated to be
                                                           30 q/m3 for normal breathing and light activity. This value of
                                                           Cq is then used to estimate Cq values for different
                                                           expiratory activities such as singing, whispering, or heavy
                                                           breathing. 
                                                        '''),
                                                         html.Div('''
                                                           - The risk tolerance represents the probability of a 
                                                           single transmission during the occupancy time of one infected 
                                                           person. The expected number of transmissions is thus prescribed by 
                                                           the product of the tolerance and the prevalence 
                                                           of infection in the population. A lower risk tolerance should 
                                                           be chosen for more vulnerable populations, such
                                                           as the elderly or those with preexisting medical conditions.
                                                        '''),
                                                         html.Div('''
                                                           - This model calculates two results: the transient bound, which
                                                           accounts for the buildup of infectious aerosols in the air 
                                                           after the entrance of an infected person, and the
                                                           steady-state bound, which is reached after the
                                                           relaxation time \u03BBc\u03C4 >> 1. Results reported in this
                                                           app are derived from the transient bound. 
                                                        '''),
                                                         html.Div('''
                                                           - The viral deactivation rate \u03BBv is the rate at which
                                                           the virus loses infectiousness in aerosol form. For SARS-CoV-2,
                                                           this is estimated to lie in the range of 0 to 0.63/hr. This
                                                           can be increased by ultraviolet radiation (UV-C) or chemical
                                                           disinfectants (e.g. hydrogen peroxide, ozone).
                                                        '''),
                                                         html.Div('''- The mean respiratory aerosol droplet size r\u0305
                                                           exists in a distribution of sizes, dependent on different people
                                                           and types of respiration. This size can also affect infectivity
                                                           of the aerosol droplets. However, a typical range for the most
                                                           common and most infectious droplets is 2-3 \u03bcm, which is
                                                           roughly consistent with the standard definition of aerosol
                                                           droplets in the literature (r\u0305 < 5 \u03bcm).
                                                        '''),
                                                     ], style={'padding-left': '10px', 'font-size': '13px'}),
                                                     html.Br(),
                                                     html.Div('''
                                                       For more references and further explanation, see the references
                                                       posted at the top of the webpage. 
                                                    '''),
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
                                    html.Span(id='adv-six-ft-output', children=''' 2 people ''',
                                              style={'color': '#de1616'}),
                                    ''' in this room.''']),
                            ]),
                        ], style={'padding-top': '0px'}),
                ]
            ),
        ]
    ),

    html.Br(),
    html.Div([
        dcc.Link(
            href='/',
            children=[
                html.Button(
                    className='link-button',
                    children=[
                        html.Span('Basic Mode ')
                    ],
                )
            ]
        )
    ], style={'float': 'right',
              'padding-bottom': '10px'}),
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
     Output('adv-six-ft-output', 'children'),
     Output('adv-room-vol-output', 'children'),
     Output('adv-fresh-rate-output', 'children'),
     Output('adv-recirc-rate-output', 'children'),
     Output('adv-air-filt-rate-output', 'children'),
     Output('adv-sett-speed-output', 'children'),
     Output('adv-conc-relax-output', 'children'),
     Output('adv-airb-trans-output', 'children')],
    [Input('adv-floor-area', 'value'),
     Input('adv-ceiling-height', 'value'),
     Input('adv-ventilation-type', 'value'),
     Input('adv-recirc-rate', 'value'),
     Input('adv-filter-type', 'value'),
     Input('adv-exertion-level', 'value'),
     Input('adv-exp-activity', 'value'),
     Input('adv-mask-type', 'value'),
     Input('adv-risk-tolerance', 'value'),
     Input('adv-aerosol-radius', 'value'),
     Input('adv-viral-deact-rate', 'value')]
)
def update_figure(floor_area, ceiling_height, air_exchange_rate, recirc_rate, merv,
                  breathing_flow_rate, infectiousness, mask_passage_prob, risk_tolerance, aerosol_radius,
                  viral_deact_rate):
    # Make sure none of our values are none
    is_none = floor_area is None or ceiling_height is None or recirc_rate is None or aerosol_radius is None or \
                viral_deact_rate is None
    if is_none:
        raise PreventUpdate

    # Update model with newly-selected parameters
    aerosol_filtration_eff = Indoors.merv_to_eff(merv, aerosol_radius)

    # Convert recirc rate to outdoor air fraction
    outdoor_air_fraction = air_exchange_rate / (air_exchange_rate + recirc_rate)

    myInd.physical_params = [floor_area, ceiling_height, air_exchange_rate, outdoor_air_fraction,
                             aerosol_filtration_eff]
    myInd.physio_params = [breathing_flow_rate, aerosol_radius]
    myInd.disease_params = [infectiousness, viral_deact_rate]
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

    # Calculated Values of Interest Output
    interest_output = [
        '{:,.0f} ft\u00B3'.format(myInd.room_vol),
        '{:,.0f} ft\u00B3/min'.format(myInd.fresh_rate),
        '{:,.0f} ft\u00B3/min'.format(myInd.recirc_rate),
        '{:,.2f} /hr'.format(myInd.air_filt_rate),
        '{:,.2f} m/hr'.format(myInd.sett_speed),
        '{:,.2f} /hr'.format(myInd.conc_relax_rate),
        '{:,.2f} /hr (x10,000)'.format(myInd.airb_trans_rate * 10000),
    ]

    # Update all relevant display items (figure, red output text)
    return new_fig, model_output_text[0], model_output_text[1], model_output_text[2], model_output_text[3], \
           model_output_text[4], model_output_text[5], model_output_text[6], model_output_text[7], \
           six_ft_text, interest_output[0], interest_output[1], interest_output[2], \
           interest_output[3], interest_output[4], interest_output[5], interest_output[6],


# Risk tolerance slider value display
@app.callback(
    [Output('adv-risk-tolerance-output', 'children')],
    [Input('adv-risk-tolerance', 'value')]
)
def update_risk_tol_disp(risk_tolerance):
    return ["{:.2f}".format(risk_tolerance)]


