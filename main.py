import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import indoors as ind

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

myInd = ind.Indoors()
results_df = myInd.calc_n_max_series(2, 100, 1.0)
fig = px.line(results_df, x="Maximum Exposure Time (hours)", y="Maximum Occupancy",
              title="Occupancy vs. Exposure Time",
              height=400, color_discrete_map={"Maximum Occupancy": "#de1616"})

ventilation_types = [
    {'label': "Bedroom, closed windows", 'value': 0.34},
    {'label': "Mechanical Ventilation", 'value': 6},
    {'label': "Restaurant", 'value': 17.5},
    {'label': "Hospital", 'value': 18},
    {'label': "Laboratory", 'value': 17.5},
    {'label': "Toxic Laboratory", 'value': 25},
]

# source: https://www.energyvanguard.com/blog/can-your-hvac-system-filter-out-coronavirus
filter_types = [
    {'label': "None", 'value': 0},
    {'label': "Residential Window AC (MERV 1-4)", 'value': 0.01},
    {'label': "Residential/Commercial/Industrial (MERV 5-8)", 'value': 0.05},
    {'label': "Residential/Commercial/Hospital Laboratories (MERV 9-12)", 'value': 0.575},
    {'label': "Hospital & General Surgery (MERV 13-16)", 'value': 0.9},
    {'label': "HEPA", 'value': 0.9997}
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

def_rt = 0.008  # default risk tolerance
age_levels = [
    {'label': "Ages 0-4", 'value': def_rt / 0.025},
    {'label': "Ages 5-17", 'value': def_rt / 0.008},
    {'label': "Ages 18-49", 'value': def_rt / 0.2},
    {'label': "Ages 50-64", 'value': def_rt / 0.61},
    {'label': "Ages 75-84", 'value': def_rt / 1.30},
    {'label': "Ages >85", 'value': def_rt / 1.45},
]

mask_types = [
    {'label': "None", 'value': 1},
    {'label': "Cloth", 'value': 0.15},
    {'label': "N95 Surgical", 'value': 0.05},
]

model_output_n_vals = [2, 3, 5, 10, 25, 50, 100]

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>COVID-19 Indoor Safety</title>
        {%favicon%}
        {%css%}
        <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@200&display=swap" rel="typography">
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-143756813-2"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
        
          gtag('config', 'UA-143756813-2');
        </script>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>'''

app.layout = html.Div(children=[
    html.H1(children='MIT COVID-19 Indoor Safety Guideline'),

    html.Div(children='''
        Kasim Khan (2020)
    '''),
    html.Div(children='''
        https://github.com/kawesomekhan/covid-indoor
    '''),
    html.Div(children='''
        Reference: Martin Z. Bazant and John W. M. Bush, medRxiv preprint (2020):
        "Beyond Six Feet: A Guideline to Limit Indoor Airborne Transmission of COVID-19"
    '''),
    html.Div('''
        http://web.mit.edu/bazant/www/COVID-19/
    '''),

    html.Br(),
    html.Br(),
    html.Div(
        className='grid',
        children=[
            html.Div(
                className='card',
                children=[
                    dcc.Tabs(className='custom-tabs', value='tab-1', children=[
                        dcc.Tab(
                            label='Room Specifications',
                            className='custom-tab',
                            children=[
                                html.H6("Room Specifications: "),
                                html.Br(),
                                html.Div(["Floor Area (sq. ft.): ",
                                          dcc.Input(id='floor-area', value=200, type='number')]),
                                html.Br(),
                                html.Div(["Ceiling Height (ft.): ",
                                          dcc.Input(id='ceiling-height', value=12, type='number')]),
                                html.Br(),
                                html.Div(["Ventilation System: ",
                                          dcc.Dropdown(id='ventilation-type',
                                                       options=ventilation_types,
                                                       value=0.34)]),
                                html.Br(),
                                html.Div(["Filtration System: ",
                                          dcc.Dropdown(id='filter-type',
                                                       options=filter_types,
                                                       value=0.01)]),
                                html.Br(),
                                html.Div(["Outdoor Air Fraction: ",
                                          dcc.Slider(id='outdoor-air-fraction',
                                                     min=0.01,
                                                     max=1,
                                                     step=0.01,
                                                     value=0.2,
                                                     marks={
                                                         0.01: {'label': '0 (closed room)'},
                                                         1: {'label': '1 (outdoors)'}
                                                     })])
                            ]
                        ),
                        dcc.Tab(
                            label='Human Behavior',
                            className='custom-tab',
                            children=[
                                html.H6("Human Behavior: "),
                                html.Br(),
                                html.Div(["Exertion Level: ",
                                          dcc.Dropdown(id='exertion-level',
                                                       options=exertion_types,
                                                       value=0.49)]),
                                html.Br(),
                                html.Div(["Expiratory Activity: ",
                                          dcc.Dropdown(id='exp-activity',
                                                       options=expiratory_types,
                                                       value=29)]),
                                html.Br(),
                                html.Div(["Age Group: ",
                                          dcc.Dropdown(id='risk-tolerance',
                                                       options=age_levels,
                                                       value=def_rt / 0.2)]),
                                html.Br(),
                                html.Div(["Masks? ",
                                          dcc.Dropdown(id='mask-type',
                                                       options=mask_types,
                                                       value=0.15)])
                            ]
                        ),
                        dcc.Tab(
                            label='Graph Output',
                            className='custom-tab',
                            children=[
                                html.H6("Graph Output: "),
                                html.Div([
                                    dcc.Graph(
                                        id='safety-graph',
                                        figure=fig
                                    ),
                                ])
                            ]
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
                        html.H4(className='model-output-text', id='model-text-1'),
                        html.H4(className='model-output-text', id='model-text-2'),
                        html.H4(className='model-output-text', id='model-text-3'),
                        html.H4(className='model-output-text', id='model-text-4'),
                        html.H4(className='model-output-text', id='model-text-5'),
                        html.H4(className='model-output-text', id='model-text-6'),
                        html.H4(className='model-output-text', id='model-text-7'),
                        html.Br(),
                        html.H3([
                            '''In comparison, current six feet distancing guidelines recommend no more than''',
                            html.Span(id='six-ft-output', children=''' 2 people ''', style={'color': '#de1616'}),
                            ''' in this room.''']),
                    ]),
                ]),
        ]
    )
])


@app.callback(
    [Output('safety-graph', 'figure'),
     Output('model-text-1', 'children'),
     Output('model-text-2', 'children'),
     Output('model-text-3', 'children'),
     Output('model-text-4', 'children'),
     Output('model-text-5', 'children'),
     Output('model-text-6', 'children'),
     Output('model-text-7', 'children'),
     Output('six-ft-output', 'children')],
    [Input('floor-area', 'value'),
     Input('ceiling-height', 'value'),
     Input('ventilation-type', 'value'),
     Input('outdoor-air-fraction', 'value'),
     Input('filter-type', 'value'),
     Input('exertion-level', 'value'),
     Input('exp-activity', 'value'),
     Input('mask-type', 'value'),
     Input('risk-tolerance', 'value')]
)
def update_figure(floor_area, ceiling_height, air_exchange_rate, outdoor_air_fraction, aerosol_filter_eff,
                  breathing_flow_rate, infectiousness, mask_passage_prob, risk_tolerance):
    myInd.physical_params = [floor_area, ceiling_height, air_exchange_rate, outdoor_air_fraction,
                             aerosol_filter_eff]
    myInd.physio_params = [breathing_flow_rate, 2]
    myInd.disease_params = [infectiousness, 0.3]
    myInd.prec_params = [mask_passage_prob, risk_tolerance]
    new_df = myInd.calc_n_max_series(2, 100, 1.0)
    new_fig = px.line(new_df, x="Maximum Exposure Time (hours)", y="Maximum Occupancy",
                      title="Occupancy vs. Exposure Time", height=400,
                      color_discrete_map={"Maximum Occupancy": "#de1616"})
    new_fig.update_layout(transition_duration=500)

    model_output_text = ["", "", "", "", "", "", ""]
    index = 0
    for n_val in model_output_n_vals:
        max_time = myInd.calc_max_time(n_val)  # hours
        units = 'hours'
        if max_time < 1:
            units = 'minutes'
            max_time = max_time * 60

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

    return new_fig, model_output_text[0], model_output_text[1], model_output_text[2], model_output_text[3], \
           model_output_text[4], model_output_text[5], model_output_text[6], six_ft_text


if __name__ == "__main__":
    app.run_server(debug=False)
