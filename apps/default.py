import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import indoors as ind
from indoors import Indoors

from app import app
import descriptions as desc
import descriptions_fr as desc_fr
import essentials as ess

"""
default.py contains the core functionality of the Dash app Basic Mode. It is responsible for taking inputs,
feeding those inputs to the model (indoors.py), and displaying the model outputs in an effective, concise
manner. This mode is the default mode that all users see when they visit indoor-covid-safety.herokuapp.com,
and is therefore designed to be digestible for the average reader. 

Properties: 
COVID-19 Calculator Setup
Dropdown Preset Values
Tab CSS Styles
Main App (Basic Mode)

Methods: 
def update_figure: Calculate model & update displayed values
def update_presets: Updates options based on selected presets
def update_vent_disp: Updates ventilation ACH number based on dropdown value
def update_filt_disp: Updates filtration MERV number based on dropdown value
def update_recirc_disp: Updates recirculation ACH number based on dropdown value
def update_risk_tol_disp: Update risk tolerance display value
def update_mask_fit_disp: Updates mask fit/compliance filtration display based on slider value
"""

# COVID-19 Calculator Setup
myInd = ind.Indoors()
fig = ess.get_model_figure(myInd)

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
        'ventilation': 2,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.54,
        'exp-activity': 72,
        'masks': 0.75
    },
}

preset_settings_metric = {
    'house': {
        'floor-area': 186,
        'ceiling-height': 3.66,
        'ventilation': 3,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.49,
        'exp-activity': 29,
        'masks': 0.75
    },
    'classroom': {
        'floor-area': 83.6,
        'ceiling-height': 3.66,
        'ventilation': 3,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.49,
        'exp-activity': 29,
        'masks': 0.75
    },
    'restaurant': {
        'floor-area': 465,
        'ceiling-height': 3.66,
        'ventilation': 9,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.49,
        'exp-activity': 72,
        'masks': 0
    },
    'office': {
        'floor-area': 929,
        'ceiling-height': 3.66,
        'ventilation': 8,
        'filtration': 10,
        'recirc-rate': 1,
        'exertion': 0.54,
        'exp-activity': 29,
        'masks': 0.75
    },
    'subway': {
        'floor-area': 54,
        'ceiling-height': 3,
        'ventilation': 18,
        'filtration': 6,
        'recirc-rate': 54,
        'exertion': 0.54,
        'exp-activity': 29,
        'masks': 0.75
    },
    'bus': {
        'floor-area': 54,
        'ceiling-height': 3,
        'ventilation': 8,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.54,
        'exp-activity': 29,
        'masks': 0.75
    },
    'airplane': {
        'floor-area': 134,
        'ceiling-height': 2,
        'ventilation': 24,
        'filtration': 17,
        'recirc-rate': 24,
        'exertion': 0.54,
        'exp-activity': 72,
        'masks': 0.75
    },
    'church': {
        'floor-area': 177,
        'ceiling-height': 9,
        'ventilation': 2,
        'filtration': 6,
        'recirc-rate': 1,
        'exertion': 0.54,
        'exp-activity': 72,
        'masks': 0.75
    },
}

# Dropdown Preset Values
# For changing ventilation types based on language: ventilation_types will be a dictionary in desc_fr with
# the english labels (here) as the keys. We will
# loop through each item in ventilation_types and create a new array of dicts with the french label, then return
# that to the options.
ventilation_default = preset_settings['classroom']['ventilation']
ventilation_types = [
    {'label': "Closed windows", 'value': 0.3},
    {'label': "Open windows", 'value': 2},
    {'label': "Mechanical Ventilation", 'value': 3},
    {'label': "Open windows with fans", 'value': 6},
    {'label': "Better Mechanical Ventilation", 'value': 8},
    {'label': "Laboratory, Restaurant", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Hospital/Subway Car", 'value': 18},
    {'label': "Toxic Laboratory/Airplane", 'value': 24},
]

filter_default = preset_settings['classroom']['filtration']
filter_types = [
    {'label': "None", 'value': 0},
    {'label': "Residential Window AC", 'value': 2},
    {'label': "Residential/Commercial/Industrial", 'value': 6},
    {'label': "Residential/Commercial/Hospital", 'value': 10},
    {'label': "Hospital & General Surgery", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_default = preset_settings['classroom']['recirc-rate']
recirc_types = [
    {'label': "None", 'value': 0},
    {'label': "Slow", 'value': 0.3},
    {'label': "Moderate", 'value': 1},
    {'label': "Fast", 'value': 10},
    {'label': "Airplane", 'value': 24},
    {'label': "Subway Car", 'value': 54},
]

mask_types = [
    {'label': "None", 'value': 0},
    {'label': "Quilter's Cotton", 'value': 0.1},
    {'label': "Silk, Flannel, Chiffon", 'value': 0.5},
    {'label': "Surgical, Cotton", 'value': 0.75},
    {'label': "N95 Respirator", 'value': 0.95},
]

# Main App
layout = html.Div(children=[
    dbc.Alert(
        "Error Alert",
        id='alert-no-update',
        className='error-alert',
        is_open=False,
    ),

    html.Div(
        className='main-content',
        children=html.Div(
            className='grid',
            children=[
                html.Div(
                    className='card',
                    children=[
                        dcc.Tabs(value='tab-1', children=[
                            dcc.Tab(
                                label=desc.about_header,
                                className='custom-tab',
                                children=html.Span(desc.about, id='about-text'),
                                style=ess.tab_style,
                                selected_style=ess.tab_style_selected
                            ),
                            dcc.Tab(
                                label=desc.room_header,
                                className='custom-tab',
                                children=[
                                    html.H6(html.Span(desc.room_header, id='room-header-body')),
                                    html.Div([html.Span(desc.floor_area_text, id='floor-area-text'),
                                              dcc.Input(id='floor-area', value=900,
                                                        type='number')]),
                                    html.Br(),
                                    html.Div([html.Span(desc.ceiling_height_text, id='ceiling-height-text'),
                                              dcc.Input(id='ceiling-height', value=12,
                                                        type='number')]),
                                    html.Br(),
                                    html.Div([html.Span(desc.ventilation_text, id='ventilation-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='ventilation-type-output'),
                                              dcc.Dropdown(id='ventilation-type',
                                                           options=ventilation_types,
                                                           value=ventilation_default,
                                                           searchable=False,
                                                           clearable=False)
                                              ]),
                                    html.Br(),
                                    html.Div([html.Span(desc.filtration_text, id='filtration-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='filter-type-output'),
                                              dcc.Dropdown(id='filter-type',
                                                           options=filter_types,
                                                           value=filter_default,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Div([html.Span(desc.recirc_text, id='recirc-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='recirc-rate-output-2'),
                                              dcc.Dropdown(id='recirc-rate',
                                                           options=recirc_types,
                                                           value=recirc_default,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Span(desc.need_more_ctrl_text, id='need-more-ctrl-text'),
                                ],
                                style=ess.tab_style,
                                selected_style=ess.tab_style_selected
                            ),
                            dcc.Tab(
                                label=desc.human_header,
                                className='custom-tab',
                                children=[
                                    html.H6(html.Span(desc.human_header, id='human-header-body')),
                                    html.Div([html.Span(desc.exertion_text, id='exertion-text'),
                                              dcc.Dropdown(id='exertion-level',
                                                           options=ess.exertion_types,
                                                           value=0.49,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Div([html.Span(desc.breathing_text, id='breathing-text'),
                                              dcc.Dropdown(id='exp-activity',
                                                           options=ess.expiratory_types,
                                                           value=29,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Div([html.Span(desc.mask_type_text, id='mask-type-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='mask-eff-output'),
                                              dcc.Dropdown(id='mask-type',
                                                           options=mask_types,
                                                           value=0.75,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Div([html.Span(desc.mask_fit_text, id='mask-fit-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='mask-fit-output'),
                                              dcc.Slider(id='mask-fit',
                                                         min=0,
                                                         max=0.95,
                                                         step=0.01,
                                                         value=0.90,
                                                         marks=ess.mask_fit_marks),
                                              ]),
                                    html.Br(),
                                    html.Br(),
                                    html.Div([html.Span(desc.risk_tolerance_text, id='risk-tol-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='risk-tolerance-output'),
                                              html.Span(desc.risk_tol_desc, id='risk-tol-desc'),
                                              dcc.Slider(id='risk-tolerance',
                                                         min=0.01,
                                                         max=1,
                                                         step=0.01,
                                                         value=0.1,
                                                         marks=ess.risk_tol_marks)
                                              ]),
                                    html.Br(),
                                    html.Br(),
                                    html.Span(desc.need_more_ctrl_text, id='need-more-ctrl-text-2'),
                                ],
                                style=ess.tab_style,
                                selected_style=ess.tab_style_selected
                            ),
                            dcc.Tab(
                                label=desc.faq_header,
                                className='custom-tab',
                                children=[
                                    html.Span(desc.faq_top, id='faq-top'),
                                    html.Br(),
                                    html.Span(desc.faq_other_params_text, id='faq-other-params-text'),
                                    html.Br(),
                                    html.Div([
                                        html.Div([html.Span(desc.aerosol_radius_text, id='aerosol-rad-text'),
                                                  dcc.Input(id='aerosol-radius', value=2,
                                                            type='number')]),
                                        html.Br(),
                                        html.Div([html.Span(desc.viral_deact_text, id='viral-deact-text'),
                                                  dcc.Input(id='viral-deact-rate', value=0.3,
                                                            type='number')]),
                                    ], className='faq-answer'),
                                    html.Br(),
                                    html.Br(),
                                    html.Span(desc.values_interest_desc, id='values-interest-desc'),
                                    html.Br(),
                                    html.Div([
                                        html.Div([html.Span(desc.outdoor_air_frac_label, id='z_p-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='air-frac-output')]),
                                        html.Div([html.Span(desc.aerosol_eff_label, id='filt-eff-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='filtration-eff-output')]),
                                        html.Div([html.Span(desc.breathing_rate_label, id='breath-rate-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='breath-rate-output')]),
                                        html.Div([html.Span(desc.cq_label, id='cq-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='infect-air-output')]),
                                        html.Div([html.Span(desc.mask_pass_prob_label, id='mask-pass-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='mask-pass-output')]),
                                        html.Div([html.Span(desc.room_vol_label, id='room-vol-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='room-vol-output')]),
                                        html.Div([html.Span(desc.vent_rate_Label, id='fresh-rate-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='fresh-rate-output')]),
                                        html.Div([html.Span(desc.recirc_rate_label, id='recirc-rate-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='recirc-rate-output')]),
                                        html.Div([html.Span(desc.air_filt_label, id='air-filt-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='air-filt-rate-output')]),
                                        html.Div([html.Span(desc.sett_speed_label, id='sett-speed-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='sett-speed-output')]),
                                        html.Div([html.Span(desc.conc_relax_rate_label, id='conc-relax-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='conc-relax-output')]),
                                        html.Div([html.Span(desc.airb_trans_label, id='airb-trans-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='airb-trans-output')]),
                                    ], className='faq-answer'),
                                    html.Br(),
                                    html.Span(desc.faq_graphs_text, id='faq-graphs-text'),
                                    html.Div([
                                        dcc.Graph(
                                            id='safety-graph',
                                            figure=fig
                                        ),
                                    ], className='faq-answer'),
                                    html.Br(),
                                    html.Span(desc.faq_infect_rate, id='faq-infect-rate'),
                                    html.Br(),
                                    html.Span(desc.assumptions_layout, id='assump-layout'),
                                ],
                                style=ess.tab_style,
                                selected_style=ess.tab_style_selected
                            )
                        ],
                                 colors={
                                     "border": "#c9c9c9",
                                     "primary": "#de1616"
                                 }),
                        html.Br()
                    ], style={'margin': '1em', 'padding': '0', 'border': 'none'}),
                html.Div(
                    className='card',
                    children=[html.Div(className='output-content', children=[
                        html.H6(html.Span(desc.curr_room_header, id='curr-room-header')),
                        html.Div(
                            className='grid-preset',
                            children=
                            html.Div(
                                id='presets-div',
                                children=dcc.Dropdown(id='presets',
                                                      options=presets,
                                                      value='classroom',
                                                      searchable=False,
                                                      clearable=False)),
                            style={'max-width': '500px'}
                        ),
                        html.H3(html.Span(desc.main_panel_s1, id='main-panel-s1')),
                        dcc.Loading(
                            id='loading',
                            type='circle',
                            children=[
                                html.H4(className='model-output-text', id='model-text-1',
                                        children="2 people for 31 days"),
                                html.H4(className='model-output-text', id='model-text-2',
                                        children="3 people for 15 days"),
                                html.H4(className='model-output-text', id='model-text-3',
                                        children="4 people for 10 days"),
                                html.H4(className='model-output-text', id='model-text-4',
                                        children="5 people for 8 days"),
                                html.H4(className='model-output-text', id='model-text-5',
                                        children="10 people for 3 days"),
                                html.H4(className='model-output-text', id='model-text-6',
                                        children="25 people for 31 hours"),
                                html.H4(className='model-output-text', id='model-text-7',
                                        children="50 people for 15 hours"),
                                html.H4(className='model-output-text', id='model-text-8',
                                        children="100 people for 8 hours"),
                            ],
                            color='#de1616',
                        ),
                        html.Br(),
                        html.H3([html.Span(desc.main_panel_six_ft_1, id='main-six-ft-1'),
                                 html.Span(id='six-ft-output',
                                           children=''' 2 people ''',
                                           style={'color': '#de1616'}),
                                 html.Span(desc.main_panel_six_ft_2, id='main-six-ft-2')]),
                        html.Span(desc.main_airb_trans_only_disc, id='main-airb-trans-disc')
                    ]),
                ]),
            ]
        ),
    ),
])


# Updates labels & presets depending on selected unit system
@app.callback(
    [Output('floor-area-text', 'children'),
     Output('ceiling-height-text', 'children')],
    [Input('url', 'search')]
)
def update_units(search):
    params = ess.search_to_params(search)
    my_units = "british"
    if "units" in params:
        my_units = params["units"]

    desc_file = desc
    if "lang" in params:
        if params["lang"] == "fr":
            desc_file = desc_fr

    if my_units == "british":
        return [desc_file.floor_area_text, desc_file.ceiling_height_text]
    else:
        return [desc_file.floor_area_text_metric, desc_file.ceiling_height_text_metric]


# Model Update & Calculation
# See indoors.py def set_default_params(self) for parameter descriptions.
@app.callback(
    [Output('safety-graph', 'figure'),
     Output('model-text-1', 'children'),
     Output('model-text-2', 'children'),
     Output('model-text-3', 'children'),
     Output('model-text-4', 'children'),
     Output('model-text-5', 'children'),
     Output('model-text-6', 'children'),
     Output('model-text-7', 'children'),
     Output('model-text-8', 'children'),
     Output('six-ft-output', 'children'),
     Output('presets', 'value'),
     Output('air-frac-output', 'children'),
     Output('filtration-eff-output', 'children'),
     Output('breath-rate-output', 'children'),
     Output('infect-air-output', 'children'),
     Output('mask-pass-output', 'children'),
     Output('room-vol-output', 'children'),
     Output('fresh-rate-output', 'children'),
     Output('recirc-rate-output', 'children'),
     Output('air-filt-rate-output', 'children'),
     Output('sett-speed-output', 'children'),
     Output('conc-relax-output', 'children'),
     Output('airb-trans-output', 'children'),
     Output('alert-no-update', 'children'),
     Output('alert-no-update', 'is_open')],
    [Input('floor-area', 'value'),
     Input('ceiling-height', 'value'),
     Input('ventilation-type', 'value'),
     Input('recirc-rate', 'value'),
     Input('filter-type', 'value'),
     Input('exertion-level', 'value'),
     Input('exp-activity', 'value'),
     Input('mask-type', 'value'),
     Input('mask-fit', 'value'),
     Input('risk-tolerance', 'value'),
     Input('aerosol-radius', 'value'),
     Input('viral-deact-rate', 'value'),
     Input('url', 'search')]
)
def update_figure(floor_area, ceiling_height, air_exchange_rate, recirc_rate, merv,
                  breathing_flow_rate, infectiousness, mask_eff, mask_fit, risk_tolerance, aerosol_radius,
                  viral_deact_rate, search):
    error_msg = ""

    # Make sure none of our values are none
    if floor_area is None:
        error_msg = desc.error_list["floor_area"]
    elif ceiling_height is None:
        error_msg = desc.error_list["ceiling_height"]
    elif aerosol_radius is None:
        error_msg = desc.error_list["aerosol_radius"]
    elif viral_deact_rate is None:
        error_msg = desc.error_list["viral_deact_rate"]

    if error_msg != "":
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, error_msg, True

    # Check our units!
    params = ess.search_to_params(search)
    my_units = "british"
    if "units" in params:
        my_units = params["units"]

    # Check if we just moved to a preset; if not, change the preset dropdown to custom
    preset_dd_value = 'custom'

    if my_units == "british":
        for setting_key in preset_settings:
            setting = preset_settings[setting_key]
            is_preset = setting['floor-area'] == floor_area and \
                        setting['ceiling-height'] == ceiling_height and \
                        setting['ventilation'] == air_exchange_rate and \
                        setting['recirc-rate'] == recirc_rate and \
                        setting['filtration'] == merv and \
                        setting['exertion'] == breathing_flow_rate and \
                        setting['exp-activity'] == infectiousness and \
                        setting['masks'] == mask_eff
            if is_preset:
                preset_dd_value = setting_key
                break
    elif my_units == "metric":
        for setting_key in preset_settings_metric:
            setting = preset_settings_metric[setting_key]
            is_preset = setting['floor-area'] == floor_area and \
                        setting['ceiling-height'] == ceiling_height and \
                        setting['ventilation'] == air_exchange_rate and \
                        setting['recirc-rate'] == recirc_rate and \
                        setting['filtration'] == merv and \
                        setting['exertion'] == breathing_flow_rate and \
                        setting['exp-activity'] == infectiousness and \
                        setting['masks'] == mask_eff
            if is_preset:
                preset_dd_value = setting_key
                break

    # If metric, convert floor_area and ceiling_height to feet
    if my_units == "metric":
        floor_area = floor_area * 10.764
        ceiling_height = ceiling_height * 3.281

    # Update model with newly-selected parameters
    # Correct mask_passage_prob based on mask fit/compliance
    mask_final_eff = mask_eff * mask_fit
    mask_passage_prob = 1 - mask_final_eff

    # Calculate aerosol filtration efficiency
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
    new_fig = ess.get_model_figure(myInd)

    # Update the red text output with new model calculations
    model_output_text = ess.get_model_output_text(myInd)
    six_ft_text = ess.get_six_ft_text(myInd)
    interest_output = ess.get_interest_output_text(myInd, my_units)

    # Update all relevant display items (figure, red output text)
    return new_fig, model_output_text[0], model_output_text[1], model_output_text[2], model_output_text[3], \
           model_output_text[4], model_output_text[5], model_output_text[6], model_output_text[7], \
           six_ft_text, preset_dd_value, interest_output[0], interest_output[1], interest_output[2], \
           interest_output[3], interest_output[4], interest_output[5], interest_output[6], interest_output[7], \
           interest_output[8], interest_output[9], interest_output[10], interest_output[11], error_msg, False


# Update options based on selected presets, also if units changed
@app.callback(
    [Output('floor-area', 'value'),
     Output('ceiling-height', 'value'),
     Output('ventilation-type', 'value'),
     Output('recirc-rate', 'value'),
     Output('filter-type', 'value'),
     Output('exertion-level', 'value'),
     Output('exp-activity', 'value'),
     Output('mask-type', 'value')],
    [Input('presets', 'value'),
     Input('url', 'search')]
)
def update_presets(preset, search):
    # Update the room and behavior options based on the selected preset
    if preset == 'custom':
        raise PreventUpdate
    else:
        params = ess.search_to_params(search)
        my_units = "british"
        if "units" in params:
            my_units = params["units"]

        if my_units == "british":
            curr_settings = preset_settings[preset]
        elif my_units == "metric":
            curr_settings = preset_settings_metric[preset]
        return curr_settings['floor-area'], curr_settings['ceiling-height'], curr_settings['ventilation'], \
               curr_settings['recirc-rate'], curr_settings['filtration'], curr_settings['exertion'], \
               curr_settings['exp-activity'], curr_settings['masks']


# Ventilation ACH value display
@app.callback(
    [Output('ventilation-type-output', 'children')],
    [Input('ventilation-type', 'value')]
)
def update_vent_disp(air_exchange_rate):
    return ["{:.0f} ACH".format(air_exchange_rate)]


# Filtration value display
@app.callback(
    [Output('filter-type-output', 'children')],
    [Input('filter-type', 'value')]
)
def update_filt_disp(merv):
    return ["MERV {:.0f}".format(merv)]


# Recirculation value display
@app.callback(
    [Output('recirc-rate-output-2', 'children')],
    [Input('recirc-rate', 'value')]
)
def update_recirc_disp(recirc_rate):
    return ["{:.1f} recirculation ACH".format(recirc_rate)]


# Risk tolerance slider value display
@app.callback(
    [Output('risk-tolerance-output', 'children')],
    [Input('risk-tolerance', 'value')]
)
def update_risk_tol_disp(risk_tolerance):
    return ["{:.2f}".format(risk_tolerance)]


# Mask Filtration Efficiency slider value display
@app.callback(
    [Output('mask-eff-output', 'children')],
    [Input('mask-type', 'value')]
)
def update_mask_type_disp(mask_eff):
    return ["{:.0f}%".format(mask_eff * 100)]


# Mask Fit/Compliance slider value display
@app.callback(
    [Output('mask-fit-output', 'children')],
    [Input('mask-fit', 'value')]
)
def update_mask_fit_disp(mask_fit):
    return ["{:.0f}%".format(mask_fit * 100)]
