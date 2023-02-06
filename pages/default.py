import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import indoors as ind
from indoors import Indoors

# from index import app
import descriptions as desc
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

# dash Pages
dash.register_page(__name__, name="Basic", path="/")

# COVID-19 Calculator Setup
myInd = ind.Indoors()
fig = ess.get_model_figure(myInd, "en")

# TODO: finish implementing this function / converting query string handling
# def layout(units=None, lang=None, **other_unknown_query_strings):
#     # get the language to populate texts

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
                    id='card-tab',
                    children=[
                        dcc.Tabs(value='tab-1', children=[
                            dcc.Tab(
                                id='tab-a',
                                label=desc.about_header,
                                className='custom-tab',
                                children=html.Span(desc.about, id='about-text')
                            ),
                            dcc.Tab(
                                id='tab-b',
                                label=desc.room_header,
                                className='custom-tab',
                                children=[
                                    html.H6(html.Span(desc.room_header, id='room-header-body')),
                                    html.Div([html.Span(desc.floor_area_text, id='floor-area-text'),
                                              dcc.Input(id='floor-area', value=910,
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
                                                           options=desc.ventilation_types,
                                                           value=ess.ventilation_default,
                                                           searchable=False,
                                                           clearable=False)
                                              ]),
                                    html.Br(),
                                    html.Div([html.Span(desc.filtration_text, id='filtration-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='filter-type-output'),
                                              dcc.Dropdown(id='filter-type',
                                                           options=desc.filter_types,
                                                           value=ess.filter_default,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Div([html.Span(desc.recirc_text, id='recirc-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='recirc-rate-output-2'),
                                              dcc.Dropdown(id='recirc-rate',
                                                           options=desc.recirc_types,
                                                           value=ess.recirc_default,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Div([html.Span(desc.humidity_text, id='humidity-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='humidity-output'),
                                              dcc.Slider(id='relative-humidity',
                                                         min=0.01,
                                                         max=0.99,
                                                         step=0.01,
                                                         value=0.6,
                                                         marks=desc.humidity_marks)]),
                                    html.Br(),
                                    html.Br(),
                                    html.Span(desc.need_more_ctrl_text, id='need-more-ctrl-text'),
                                ]
                            ),
                            dcc.Tab(
                                id='tab-c',
                                label=desc.human_header,
                                className='custom-tab',
                                children=[
                                    html.H6([
                                        html.Span(desc.human_header, id='human-header-body'),
                                    ]),
                                    html.Div([html.Span(desc.exertion_text, id='exertion-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='qb-output'),
                                              dcc.Dropdown(id='exertion-level',
                                                           options=desc.exertion_types,
                                                           value=0.49,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Div([html.Span(desc.breathing_text, id='breathing-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='cq-output'),
                                              dcc.Dropdown(id='exp-activity',
                                                           options=desc.expiratory_types,
                                                           value=72,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Div([html.Span(desc.mask_type_text, id='mask-type-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='mask-eff-output'),
                                              dcc.Dropdown(id='mask-type',
                                                           options=desc.mask_types,
                                                           value=0.90,
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
                                                         value=0.95,
                                                         marks=desc.mask_fit_marks),
                                              ]),
                                    html.Br(),
                                    html.Br(),
                                    html.Span(desc.need_more_ctrl_text, id='need-more-ctrl-text-2'),
                                ]
                            ),
                            dcc.Tab(
                                id='tab-d',
                                label=desc.faq_header,
                                className='custom-tab',
                                children=[
                                    html.Span(desc.faq_top, id='faq-top'),
                                    html.Br(),
                                    html.Span(desc.values_interest_desc, id='values-interest-desc'),
                                    html.Br(),
                                    html.Div([
                                        html.Div([html.Span(desc.relative_sus_label, id='sr-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='sr-output')]),
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
                                        html.Div([html.Span(desc.eff_aerosol_rad_label, id='eff-rad-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='eff-rad-output')]),
                                        html.Div([html.Span(desc.viral_deact_label, id='viral-deact-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='viral-deact-output')]),
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
                                ]
                            )
                        ],
                                 colors={
                                     "border": "#c9c9c9",
                                     "primary": "#de1616"
                                 }),
                        html.Br()
                    ], style=ess.tabs_card_style),
                html.Div(
                    className='card',
                    children=[
                        html.Div(
                            className='grid-presets',
                            children=[
                                html.Div([
                                    html.H6(html.Span(desc.curr_room_header, id='curr-room-header')),
                                    dcc.Dropdown(id='presets',
                                                 options=desc.presets,
                                                 value='classroom',
                                                 searchable=False,
                                                 clearable=False)
                                ], className='card-presets'),
                                html.Div([
                                    html.H6(html.Span(desc.curr_human_header, id='curr-human-header')),
                                    dcc.Dropdown(id='presets-human',
                                                 options=desc.presets_human,
                                                 value='masks-2',
                                                 searchable=False,
                                                 clearable=False)
                                ], className='card-presets'),
                                # html.Div([
                                #     html.H6([
                                #         html.Span(desc.curr_risk_header, id='curr-risk-tol'),
                                #         html.Span(id='risk-tolerance-output')
                                #     ]),
                                #     dcc.Dropdown(id='presets-risk',
                                #                  options=desc.presets_risk,
                                #                  value=0.1,
                                #                  searchable=False,
                                #                  clearable=False)
                                # ], className='card-presets'),
                                html.Div([
                                    html.H6([
                                        html.Span(desc.curr_age_header, id='curr-age-group')
                                    ]),
                                    dcc.Dropdown(id='presets-age',
                                                 options=desc.presets_age,
                                                 value=0.68,
                                                 searchable=False,
                                                 clearable=False)
                                ], className='card-presets'),
                                html.Div([
                                    html.H6([
                                        html.Span(desc.curr_strain_header, id='curr-viral-strain'),
                                    ]),
                                    dcc.Dropdown(id='presets-strain',
                                                 options=desc.presets_strain,
                                                 value=4.0,
                                                 searchable=False,
                                                 clearable=False)
                                ], className='card-presets')
                            ],
                        ),
                    ]
                ),
                html.Div(
                    className='card',
                    children=html.Div(className='output-content', children=[
                                    html.Div([
                                        html.H3(html.Span(desc.main_panel_s1, id='main-panel-s1')),
                                        dcc.Loading(
                                            id='loading',
                                            type='circle',
                                            children=[
                                                html.H4(className='model-output-text', id='model-text-1',
                                                        children="2 people for 31 days"),
                                                html.H4(className='model-output-text', id='model-text-2',
                                                        children="5 people for 8 days"),
                                                html.H4(className='model-output-text', id='model-text-3',
                                                        children="10 people for 3 days"),
                                                html.H4(className='model-output-text', id='model-text-4',
                                                        children="25 people for 31 hours"),
                                                html.H4(className='model-output-text', id='model-text-5',
                                                        children="100 people for 8 hours"),
                                            ],
                                            color='#de1616',
                                        ),
                                        html.Br(),
                                        html.H4([html.Span(desc.main_panel_six_ft_1, id='main-six-ft-1'),
                                                 html.Span(id='six-ft-output',
                                                           children=''' 2 people ''',
                                                           style={'color': '#de1616'}),
                                                 html.Span(desc.main_panel_six_ft_2, id='main-six-ft-2'),
                                                 html.Span(id='six-ft-output-t', style={'color': '#de1616'}),
                                                 html.Span("", id='main-six-ft-3')],
                                                style={'color': '#000000'}),
                                    ], className='panel-main-output'),
                                    html.Br(),
                                    html.Div(desc.main_airb_trans_only_disc_basic, id='main-airb-trans-disc',
                                             className='panel-airb-desc'),
                                    html.Div(desc.other_risk_modes_desc, id='other-risk-modes-desc',
                                             className='panel-airb-desc')
                                ])
                ),
                html.Div(
                    className='card',
                    children=[html.Div(className='output-content', children=[
                        html.Div([
                            html.H3([html.Span(desc.n_input_text_1, id='n-input-text-1'),
                                     html.Span([dcc.Input(id='n-input',
                                                          value=10,
                                                          type='number')]),
                                     html.Span(desc.n_input_text_2, id='n-input-text-2'),
                                     html.Span(id='t-output',
                                               children="8 hours",
                                               style={'color': '#de1616'}),
                                     html.Span(desc.n_input_text_3, id='n-input-text-3')]),
                            html.Br(),
                        ], className='panel-main-output'),
                        html.Div([
                            html.Span(desc.airb_trans_only_disc, id='airb-trans-only-disc-1')
                        ], className='panel-airb-desc')
                    ])]
                ),
                html.Div(
                    className='card',
                    children=[html.Div(className='output-content', children=[
                        html.Div([
                            html.H3([html.Span(desc.t_input_text_1, id='t-input-text-1'),
                                     html.Span([dcc.Input(id='t-input',
                                                          value=4,
                                                          type='number')]),
                                     html.Span(desc.t_input_text_2, id='t-input-text-2'),
                                     html.Span(id='n-output',
                                               children="5 occupants",
                                               style={'color': '#de1616'}),
                                     html.Span(desc.t_input_text_3, id='t-input-text-3')]),
                            html.Br(),
                        ], className='panel-main-output'),
                        html.Div([
                            html.Span(desc.airb_trans_only_disc, id='airb-trans-only-disc-2')
                        ], className='panel-airb-desc'),
                    ])]
                )
            ]
        ),
    ),
])


# Updates all remaining text based on language
@callback(
    [Output('tab-a', 'label'),
     Output('curr-room-header', 'children'),
     Output('presets', 'options'),
     Output('curr-human-header', 'children'),
     Output('presets-human', 'options'),
     Output('curr-age-group', 'children'),
     Output('presets-age', 'options'),
     Output('curr-viral-strain', 'children'),
     Output('presets-strain', 'options'),
     Output('other-risk-modes-desc', 'children'),
     Output('main-panel-s1', 'children'),
     Output('main-six-ft-1', 'children'),
     Output('main-six-ft-2', 'children'),
     Output('main-six-ft-3', 'children'),
     Output('main-airb-trans-disc', 'children'),
     Output('about-text', 'children'),
     Output('tab-b', 'label'),
     Output('room-header-body', 'children'),
     Output('ventilation-text', 'children'),
     Output('ventilation-type', 'options'),
     Output('filtration-text', 'children'),
     Output('filter-type', 'options'),
     Output('recirc-text', 'children'),
     Output('recirc-rate', 'options'),
     Output('humidity-text', 'children'),
     Output('relative-humidity', 'marks'),
     Output('need-more-ctrl-text', 'children'),
     Output('tab-c', 'label'),
     Output('human-header-body', 'children'),
     Output('exertion-text', 'children'),
     Output('exertion-level', 'options'),
     Output('breathing-text', 'children'),
     Output('exp-activity', 'options'),
     Output('mask-type-text', 'children'),
     Output('mask-type', 'options'),
     Output('mask-fit-text', 'children'),
     Output('mask-fit', 'marks'),
     Output('need-more-ctrl-text-2', 'children'),
     Output('tab-d', 'label'),
     Output('faq-top', 'children'),
     Output('values-interest-desc', 'children'),
     Output('sr-label', 'children'),
     Output('z_p-label', 'children'),
     Output('filt-eff-label', 'children'),
     Output('breath-rate-label', 'children'),
     Output('cq-label', 'children'),
     Output('mask-pass-label', 'children'),
     Output('room-vol-label', 'children'),
     Output('fresh-rate-label', 'children'),
     Output('recirc-rate-label', 'children'),
     Output('air-filt-label', 'children'),
     Output('eff-rad-label', 'children'),
     Output('viral-deact-label', 'children'),
     Output('sett-speed-label', 'children'),
     Output('conc-relax-label', 'children'),
     Output('airb-trans-label', 'children'),
     Output('faq-graphs-text', 'children'),
     Output('faq-infect-rate', 'children'),
     Output('assump-layout', 'children'),
     Output('n-input-text-1', 'children'),
     Output('n-input-text-2', 'children'),
     Output('n-input-text-3', 'children'),
     Output('t-input-text-1', 'children'),
     Output('t-input-text-2', 'children'),
     Output('t-input-text-3', 'children')],
    [Input('url', 'search'),
     Input('window-width', 'children')]
)
def update_lang(search, window_width):
    print("URL / window size updated! setting language display to " + ess.get_lang(search))
    return ess.get_lang_text_basic(ess.get_lang(search), int(window_width))


# Model Update & Calculation
# Also updates output if language is changed
# See indoors.py def set_default_params(self) for parameter descriptions.
@callback(
    [Output('safety-graph', 'figure'),
     Output('model-text-1', 'children'),
     Output('model-text-2', 'children'),
     Output('model-text-3', 'children'),
     Output('model-text-4', 'children'),
     Output('model-text-5', 'children'),
     Output('six-ft-output', 'children'),
     Output('six-ft-output-t', 'children'),
     Output('presets', 'value'),
     Output('presets-human', 'value'),
     Output('sr-output', 'children'),
     Output('air-frac-output', 'children'),
     Output('filtration-eff-output', 'children'),
     Output('breath-rate-output', 'children'),
     Output('infect-air-output', 'children'),
     Output('mask-pass-output', 'children'),
     Output('room-vol-output', 'children'),
     Output('fresh-rate-output', 'children'),
     Output('recirc-rate-output', 'children'),
     Output('air-filt-rate-output', 'children'),
     Output('eff-rad-output', 'children'),
     Output('viral-deact-output', 'children'),
     Output('sett-speed-output', 'children'),
     Output('conc-relax-output', 'children'),
     Output('airb-trans-output', 'children'),
     Output('t-output', 'children'),
     Output('n-output', 'children'),
     Output('qb-output', 'children'),
     Output('cq-output', 'children'),
     Output('alert-no-update', 'children'),
     Output('alert-no-update', 'is_open')],
    [Input('floor-area', 'value'),
     Input('ceiling-height', 'value'),
     Input('ventilation-type', 'value'),
     Input('recirc-rate', 'value'),
     Input('filter-type', 'value'),
     Input('relative-humidity', 'value'),
     Input('exertion-level', 'value'),
     Input('exp-activity', 'value'),
     Input('mask-type', 'value'),
     Input('mask-fit', 'value'),
     Input('presets-age', 'value'),
     Input('presets-strain', 'value'),
     Input('n-input', 'value'),
     Input('t-input', 'value'),
     Input('url', 'search')],
    [State('floor-area-text', 'children'),
     State('ceiling-height-text', 'children')]
)
def update_figure(floor_area, ceiling_height, air_exchange_rate, recirc_rate, merv, relative_humidity,
                  breathing_flow_rate, infectiousness, mask_eff, mask_fit, sr_age_factor,
                  sr_strain_factor, n_max_input, exp_time_input, search, floor_area_text, ceiling_height_text):
    risk_tolerance = 0.1
    def_aerosol_radius = 2
    max_viral_deact_rate = 0.6

    language = ess.get_lang(search)
    error_msg = ess.get_err_msg(floor_area, ceiling_height, air_exchange_rate, merv, recirc_rate, def_aerosol_radius,
                                max_viral_deact_rate, language, n_max_input, exp_time_input)

    if error_msg != "":
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, error_msg, True

    # Check our units! Did we switch? If so, convert values before calculating
    my_units = ess.get_units(search)
    curr_units = ess.did_switch_units(search, floor_area_text, ceiling_height_text)
    if curr_units != "":
        [floor_area, ceiling_height] = ess.convert_units(curr_units, my_units, floor_area, ceiling_height)

    print("Updating model with units as " + my_units)

    # Check if we just moved to a preset; if not, change the preset dropdown to custom
    preset_dd_value = ess.get_room_preset_dd_value(floor_area, ceiling_height, air_exchange_rate, recirc_rate, merv,
                                                   relative_humidity, my_units)
    # preset_dd_value = dash.no_update
    human_preset_dd_value = ess.get_human_preset_dd_value(breathing_flow_rate, infectiousness, mask_eff, mask_fit,
                                                          my_units)

    # If metric, convert floor_area and ceiling_height to feet
    if my_units == "metric":
        floor_area = floor_area * 10.764
        ceiling_height = ceiling_height * 3.281

    # Update model with newly-selected parameters
    # mask_passage_prob based on mask fit/compliance
    mask_final_eff = mask_eff * mask_fit
    mask_passage_prob = 1 - mask_final_eff

    # Calculate aerosol filtration efficiency
    aerosol_filtration_eff = Indoors.merv_to_eff(merv, def_aerosol_radius)

    # Convert recirc rate to outdoor air fraction
    outdoor_air_fraction = air_exchange_rate / (air_exchange_rate + recirc_rate)

    myInd.floor_area = floor_area
    myInd.mean_ceiling_height = ceiling_height
    myInd.air_exchange_rate = air_exchange_rate
    myInd.primary_outdoor_air_fraction = outdoor_air_fraction
    myInd.aerosol_filtration_eff = aerosol_filtration_eff
    myInd.relative_humidity = relative_humidity
    myInd.breathing_flow_rate = breathing_flow_rate
    myInd.max_aerosol_radius = def_aerosol_radius
    myInd.exhaled_air_inf = infectiousness
    myInd.max_viral_deact_rate = max_viral_deact_rate
    myInd.mask_passage_prob = mask_passage_prob
    myInd.risk_tolerance = risk_tolerance
    myInd.sr_age_factor = sr_age_factor
    myInd.sr_strain_factor = sr_strain_factor
    myInd.percentage_sus = 1
    myInd.calc_vars()

    # Get human behavior output text
    qb_text = ess.get_qb_text(myInd, my_units)
    cq_text = ess.get_cq_text(myInd, my_units)

    # Update the figure with a new model calculation
    new_fig = ess.get_model_figure(myInd, language)

    # Update the red text output with new model calculations
    # Model values of interest
    interest_output = ess.get_interest_output_text(myInd, my_units)

    # Conditional Outputs (If an infected person enters...)
    model_output_text = ess.get_model_output_text(myInd, 'conditional', ess.covid_recovery_time, language)
    six_ft_text = ess.get_six_ft_text(myInd, language)
    six_ft_exp_time = ess.get_six_ft_exp_time(myInd, 'conditional', ess.covid_recovery_time, language)

    exp_time_text = ess.time_to_text(myInd.calc_max_time(n_max_input, 'conditional'), True, ess.covid_recovery_time,
                                     language)
    n_max_text = ess.get_n_max_text(myInd.calc_n_max(exp_time_input, 'conditional'), myInd.get_n_max(), language)

    # Update all relevant display items (figure, red output text)
    return new_fig, model_output_text[0], model_output_text[1], model_output_text[2], model_output_text[3], \
           model_output_text[4], six_ft_text, six_ft_exp_time, preset_dd_value, human_preset_dd_value, \
           interest_output[0], interest_output[1], interest_output[2], interest_output[3], interest_output[4], \
           interest_output[5], interest_output[6], interest_output[7], interest_output[8], interest_output[9], \
           interest_output[10], interest_output[11], interest_output[12], interest_output[13], interest_output[14], \
           exp_time_text, n_max_text, qb_text, cq_text, error_msg, False


# Update model inputs based on selected presets, also if units changed
# Updates labels depending on selected unit system (and language)
@callback(
    [Output('floor-area', 'value'),
     Output('ceiling-height', 'value'),
     Output('ventilation-type', 'value'),
     Output('recirc-rate', 'value'),
     Output('filter-type', 'value'),
     Output('relative-humidity', 'value'),
     Output('floor-area-text', 'children'),
     Output('ceiling-height-text', 'children')],
    [Input('presets', 'value'),
     Input('url', 'search')],
    [State('floor-area-text', 'children'),
     State('ceiling-height-text', 'children'),
     State('floor-area', 'value'),
     State('ceiling-height', 'value')]
)
def update_room_presets_and_units(preset, search, floor_area_text, ceiling_height_text, curr_floor_area,
                                  curr_ceiling_height):
    desc_file = ess.get_desc_file(ess.get_lang(search))
    my_units = ess.get_units(search)
    curr_units = ess.did_switch_units(search, floor_area_text, ceiling_height_text)
    did_switch = False
    if curr_units != "":
        did_switch = True
        [floor_area, ceiling_height] = ess.convert_units(curr_units, my_units, curr_floor_area, curr_ceiling_height)

    if my_units == "british":
        text_output = [desc_file.floor_area_text, desc_file.ceiling_height_text]
    else:
        text_output = [desc_file.floor_area_text_metric, desc_file.ceiling_height_text_metric]

    # Update the room and behavior options based on the selected preset
    if preset == 'custom':
        if did_switch:
            return floor_area, ceiling_height, dash.no_update, \
                   dash.no_update, dash.no_update, dash.no_update, text_output[0], text_output[1]
        else:
            return dash.no_update, dash.no_update, dash.no_update, \
                   dash.no_update, dash.no_update, dash.no_update, text_output[0], text_output[1]
    else:
        curr_settings = ess.room_preset_settings[preset]
        if not did_switch:
            if my_units == "british":
                floor_area = curr_settings['floor-area']
                ceiling_height = curr_settings['ceiling-height']
            elif my_units == "metric":
                floor_area = round(curr_settings['floor-area-metric'], 2)
                ceiling_height = round(curr_settings['ceiling-height-metric'], 2)

        return floor_area, ceiling_height, curr_settings['ventilation'], \
               curr_settings['recirc-rate'], curr_settings['filtration'], curr_settings['rh'], \
               text_output[0], text_output[1]


# Update options based on selected presets
@callback(
    [Output('exertion-level', 'value'),
     Output('exp-activity', 'value'),
     Output('mask-type', 'value'),
     Output('mask-fit', 'value')],
    [Input('presets-human', 'value')]
)
def update_human_presets(preset):
    # Update the room and behavior options based on the selected preset
    if preset == 'custom':
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update
    else:
        curr_settings = ess.human_preset_settings[preset]
        return curr_settings['exertion'], curr_settings['expiratory'], curr_settings['masks'], \
               curr_settings['mask-fit'],


# Ventilation ACH value display
@callback(
    [Output('ventilation-type-output', 'children')],
    [Input('ventilation-type', 'value'),
     Input('url', 'search')]
)
def update_vent_disp(air_exchange_rate, search):
    desc_file = ess.get_desc_file(ess.get_lang(search))
    if hasattr(desc_file, 'vent_type_output_units'):
        return [html.Span([desc_file.vent_type_output_base.format(air_exchange_rate), desc_file.vent_type_output_units])]
    else:
        return [desc_file.vent_type_output_base.format(air_exchange_rate)]


# Filtration value display
@callback(
    [Output('filter-type-output', 'children')],
    [Input('filter-type', 'value'),
     Input('url', 'search')]
)
def update_filt_disp(merv, search):
    desc_file = ess.get_desc_file(ess.get_lang(search))
    return [desc_file.filt_type_output_base.format(merv)]


# Recirculation value display
@callback(
    [Output('recirc-rate-output-2', 'children')],
    [Input('recirc-rate', 'value'),
     Input('url', 'search')]
)
def update_recirc_disp(recirc_rate, search):
    desc_file = ess.get_desc_file(ess.get_lang(search))
    if hasattr(desc_file, 'recirc_type_output_units'):
        return [html.Span([desc_file.recirc_type_output_base.format(recirc_rate), desc_file.recirc_type_output_units])]
    else:
        return [desc_file.recirc_type_output_base.format(recirc_rate)]


# Relative Humidity slider value display
@callback(
    [Output('humidity-output', 'children')],
    [Input('relative-humidity', 'value')]
)
def update_humid_disp(relative_humidity):
    return ["{:.0f}%".format(relative_humidity * 100)]


# # Risk tolerance slider value display
# @app.callback(
#     [Output('risk-tolerance-output', 'children')],
#     [Input('presets-risk', 'value')]
# )
# def update_risk_tol_disp(risk_tolerance):
#     return ["{:.2f}".format(risk_tolerance)]


# Mask Filtration Efficiency slider value display
@callback(
    [Output('mask-eff-output', 'children')],
    [Input('mask-type', 'value')]
)
def update_mask_type_disp(mask_eff):
    return ["{:.0f}%".format(mask_eff * 100)]


# Mask Fit/Compliance slider value display
@callback(
    [Output('mask-fit-output', 'children')],
    [Input('mask-fit', 'value')]
)
def update_mask_fit_disp(mask_fit):
    return ["{:.0f}%".format(mask_fit * 100)]
