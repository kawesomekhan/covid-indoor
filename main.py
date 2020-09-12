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
              title="Maximum Occupancy & Exposure Time")

ventilation_types = [
    {'label': "Bedroom, closed windows", 'value': 0.34},
    {'label': "Mechanical Ventilation", 'value': 6},
    {'label': "Restaurant", 'value': 17.5},
    {'label': "Hospital", 'value': 18},
    {'label': "Laboratory", 'value': 17.5},
    {'label': "Toxic Laboratory", 'value': 25},
]

filter_types = [
    {'label': "None", 'value': 0},
    {'label': "HEPA", 'value': 0.9997},
    {'label': "MERVs", 'value': 0.5},
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

def_rt = 0.2 / 10  # default risk tolerance
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

app.layout = html.Div(children=[
    html.H1(children='COVID-19 Indoor Safety Guidelines'),

    html.Div(children='''
        Reference: Martin Z. Bazant and John W. M. Bush, medRxiv preprint (2020):
        "Beyond Six Feet: A Guideline to Limit Indoor Airborne Transmission of COVID-19"
    '''),

    html.Br(),

    dcc.Graph(
        id='safety-graph',
        figure=fig
    ),

    html.Div([
        html.Div([
            html.H6("Room Specifications: "),
            html.Br(),
            html.Div(["Floor Area (sq. ft.): ",
                      dcc.Input(id='floor-area', value=900, type='number')]),
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
                                   value=0)]),
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
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
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
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
        html.Br()
    ])
])


@app.callback(
    Output('safety-graph', 'figure'),
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
                      title="Maximum Occupancy & Exposure Time")
    new_fig.update_layout(transition_duration=500)

    return new_fig


if __name__ == "__main__":
    app.run_server()
