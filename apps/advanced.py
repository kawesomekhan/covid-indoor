import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import indoors as ind
from indoors import Indoors

from app import app
import descriptions as desc
import descriptions_fr as desc_fr
import essentials as ess

"""
advanced.py contains the core functionality of the Dash app Advanced Mode. It is responsible for taking inputs,
feeding those inputs to the model (indoors.py), and displaying the model outputs in an effective, concise
manner. This mode is designed to be used by people who know their specific MERV and ACH values, so it is
less geared towards the general public and more focused on additional features and functionality. 

Properties: 
COVID-19 Calculator Setup
Dropdown Preset Values
Tab CSS Styles
Main App (Advanced Mode)

Methods: 
def update_figure: Calculate model & update displayed values
def update_t_output: Returns transient exposure time based on n max value
def update_n_output: Returns transient n max based on exposure time
def update_presets: Updates options based on selected presets
def update_risk_tol_disp: Update risk tolerance display value
def update_mask_fit_disp: Updates mask fit/compliance filtration display based on slider value
"""

# COVID-19 Calculator Setup
myInd = ind.Indoors()
fig = ess.get_model_figure(myInd, "en")
fig_co2 = ess.get_model_figure_co2(myInd, 'conditional', "en", 1920)
co2_graph_config_desktop = {'displayModeBar': 'hover'}
co2_graph_config_mobile = {'displayModeBar': False}

# Main App
layout = html.Div(children=[
    dbc.Alert(
        "Error Alert",
        id='adv-alert-no-update',
        className='error-alert',
        is_open=False,
    ),

    dbc.Alert(
        "Personal Risk Alert",
        id='adv-risk-alert',
        className='risk-alert',
        is_open=False,
    ),

    html.Div(
        className='main-content',
        children=[
            html.Div(
                className='adv-grid',
                children=[
                    html.Div(
                        className='card',
                        id='adv-card-risk-mode',
                        children=[
                            html.Div([
                                html.H6(html.Span(desc.risk_mode_panel_header, id='adv-risk-mode-header')),
                                dcc.Dropdown(id='adv-risk-mode',
                                             options=desc.risk_options,
                                             value='conditional',
                                             searchable=False,
                                             clearable=False),
                                html.Br(),
                                html.Div([
                                    html.H5([
                                        html.Span(desc.co2_prev_input_1, id='adv-co2-prev-input-1'),
                                        html.Span(dcc.Input(id='adv-prev',
                                                            value=100,
                                                            type='number')),
                                        html.Span(desc.co2_prev_input_2, id='adv-co2-prev-input-2'),
                                    ]),
                                    html.Div(desc.incidence_rate_refs, id='adv-incidence-rate-refs',
                                             className='panel-airb-desc')
                                ], id='adv-prev-block'),
                            ]),
                        ]
                    ),
                    html.Div(
                        className='card',
                        id='adv-card-presets',
                        children=[
                            html.Div(
                                className='adv-grid-presets',
                                children=[
                                    html.Div([
                                        html.H6(html.Span(desc.curr_room_header, id='adv-curr-room-header')),
                                        dcc.Dropdown(id='adv-presets',
                                                     options=desc.presets,
                                                     value='classroom',
                                                     searchable=False,
                                                     clearable=False)
                                    ], className='card-presets'),
                                    html.Div([
                                        html.H6(html.Span(desc.curr_human_header, id='adv-curr-human-header')),
                                        dcc.Dropdown(id='adv-presets-human',
                                                     options=desc.presets_human,
                                                     value='masks-2',
                                                     searchable=False,
                                                     clearable=False)
                                    ], className='card-presets'),
                                    html.Div([
                                        html.H6([
                                            html.Span(desc.curr_risk_header, id='adv-curr-risk-tol'),
                                            html.Span(id='adv-risk-tolerance-output')
                                        ]),
                                        dcc.Slider(id='adv-risk-tolerance',
                                                   min=0.01,
                                                   max=1,
                                                   step=0.01,
                                                   value=0.1,
                                                   marks=desc.risk_tol_marks),
                                        html.Div([html.Br()], className='mobile-break')
                                    ], className='card-presets'),
                                    html.Div([
                                        html.H6([
                                            html.Span(desc.curr_age_header, id='adv-curr-age-group'),
                                            html.Span(id='adv-age-group-output')
                                        ]),
                                        dcc.Slider(id='adv-age-group',
                                                   min=0.01,
                                                   max=1,
                                                   step=0.01,
                                                   value=0.68,
                                                   marks=desc.age_group_marks),
                                        html.Div([], id='adv-lang-break-age'),
                                        html.Div([html.Br()], className='mobile-break')
                                    ], className='card-presets'),
                                    html.Div([
                                        html.H6([
                                            html.Span(desc.curr_strain_header, id='adv-curr-viral-strain'),
                                            html.Span(id='adv-viral-strain-output')
                                        ]),
                                        dcc.Slider(id='adv-viral-strain',
                                                   min=0.1,
                                                   max=2,
                                                   step=0.01,
                                                   value=1,
                                                   marks=desc.viral_strain_marks),
                                        html.Div([html.Br()], className='mobile-break')
                                    ], className='card-presets'),
                                    html.Div([
                                        html.H6([
                                            html.Span(desc.pim_header, id='adv-pim-header'),
                                            html.Span(id='adv-pim-output')
                                        ]),
                                        dcc.Slider(id='adv-pim-input',
                                                   min=0,
                                                   max=1,
                                                   step=0.01,
                                                   value=0),
                                    ], className='card-presets')
                                ],
                            ),
                        ]
                    ),
                    html.Div(
                        className='card',
                        id='adv-card-tab',
                        children=[dcc.Tabs(value='tab-1', children=[
                            dcc.Tab(
                                id='adv-tab-a',
                                label=desc.about_header,
                                className='custom-tab',
                                children=html.Span(desc.about, id='adv-about-text')
                            ),
                            dcc.Tab(
                                id='adv-tab-b',
                                label=desc.room_header,
                                className='custom-tab',
                                children=[
                                    html.H6(html.Span(desc.room_header, id='adv-room-header-body')),
                                    html.Div([html.Span(desc.floor_area_text, id='adv-floor-area-text'),
                                              dcc.Input(id='adv-floor-area', value=910,
                                                        type='number')]),
                                    html.Br(),
                                    html.Div([html.Span(desc.ceiling_height_text, id='adv-ceiling-height-text'),
                                              dcc.Input(id='adv-ceiling-height', value=12,
                                                        type='number')]),
                                    html.Br(),
                                    html.Div([html.Span(desc.ventilation_text_adv, id='adv-ventilation-text'),
                                              dcc.Input(id='adv-ventilation-type',
                                                        value=3,
                                                        type='number')]),
                                    html.Br(),
                                    html.Div([html.Span(desc.filtration_text_adv, id='adv-filtration-text'),
                                              dcc.Input(id='adv-filter-type', value=6,
                                                        type='number')]),
                                    html.Br(),
                                    html.Div([html.Span(desc.recirc_text_adv, id='adv-recirc-text'),
                                              dcc.Input(id='adv-recirc-rate', value=1,
                                                        type='number')]),
                                    html.Br(),
                                    html.Div([html.Span(desc.humidity_text, id='adv-humidity-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='adv-humidity-output'),
                                              dcc.Slider(id='adv-relative-humidity',
                                                         min=0.01,
                                                         max=0.99,
                                                         step=0.01,
                                                         value=0.6,
                                                         marks=desc.humidity_marks)]),
                                ]
                            ),
                            dcc.Tab(
                                id='adv-tab-c',
                                label=desc.human_header,
                                className='custom-tab',
                                children=[
                                    html.H6(html.Span(desc.human_header, id='adv-human-header-body')),
                                    html.Div([html.Span(desc.exertion_text, id='adv-exertion-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='adv-qb-output'),
                                              dcc.Dropdown(id='adv-exertion-level',
                                                           options=desc.exertion_types,
                                                           value=0.49,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Div([html.Span(desc.breathing_text, id='adv-breathing-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='adv-cq-output'),
                                              dcc.Dropdown(id='adv-exp-activity',
                                                           options=desc.expiratory_types,
                                                           value=72,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Div([html.Span(desc.mask_type_text, id='adv-mask-type-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='adv-mask-eff-output'),
                                              dcc.Slider(id='adv-mask-type',
                                                         min=0,
                                                         max=1,
                                                         step=0.01,
                                                         value=0.90,
                                                         marks=desc.mask_type_marks)]),
                                    html.Br(),
                                    html.Br(),
                                    html.Br(),
                                    html.Div([html.Span(desc.mask_fit_text, id='adv-mask-fit-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='adv-mask-fit-output'),
                                              dcc.Slider(id='adv-mask-fit',
                                                         min=0,
                                                         max=0.95,
                                                         step=0.01,
                                                         value=0.95,
                                                         marks=desc.mask_fit_marks),
                                              ]),
                                    html.Br(),
                                    html.Br(),
                                ]
                            ),
                            dcc.Tab(
                                id='adv-tab-d',
                                label=desc.other_io,
                                className='custom-tab',
                                children=[
                                    html.H6(desc.pop_immunity_header, id='adv-pop-immunity-header'),
                                    html.Div(desc.pop_immunity_desc, id='adv-pop-immunity-desc'),
                                    html.Br(),
                                    html.Div([
                                        html.Div([html.Span(desc.perc_immune_label, id='adv-pim-label-other'),
                                                  html.Span(className='model-output-text-small',
                                                            id='adv-pim-output-other')]),
                                        html.Div([html.Span(desc.perc_infectious_label, id='adv-pi-label'),
                                                  html.Span(className='model-output-text-small',
                                                            id='adv-pi-output')]),
                                        html.Div([html.Span(desc.perc_susceptible_label, id='adv-ps-label'),
                                                  html.Span(className='model-output-text-small',
                                                            id='adv-ps-output')]),
                                    ], className='faq-answer'),
                                    html.Br(),
                                    html.H6(html.Span(desc.other_io, id='adv-other-io')),
                                    html.Div([html.Span(desc.aerosol_radius_text, id='adv-aerosol-rad-text'),
                                              dcc.Input(id='adv-aerosol-radius', value=2,
                                                        type='number')]),
                                    html.Br(),
                                    html.Div([html.Span(desc.viral_deact_text, id='adv-viral-deact-text'),
                                              dcc.Input(id='adv-viral-deact-rate',
                                                        value=0.6,
                                                        step=0.1,
                                                        type='number')]),
                                    html.Br(),
                                    html.H6(html.Span(desc.values_interest_header, id='adv-val-interest-header')),
                                    html.Div([
                                        html.Div([html.Span(desc.relative_sus_label, id='adv-sr-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-sr-output')]),
                                        html.Div([html.Span(desc.outdoor_air_frac_label, id='adv-z_p-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-air-frac-output')]),
                                        html.Div([html.Span(desc.aerosol_eff_label, id='adv-filt-eff-label'),
                                                  html.Sub('f'), ": ",
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-filtration-eff-output')]),
                                        html.Div([html.Span(desc.breathing_rate_label, id='adv-breath-rate-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-breath-rate-output')]),
                                        html.Div([html.Span(desc.cq_label, id='adv-cq-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-infect-air-output')]),
                                        html.Div([html.Span(desc.mask_pass_prob_label, id='adv-mask-pass-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-mask-pass-output')]),
                                        html.Div([html.Span(desc.room_vol_label, id='adv-room-vol-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-room-vol-output')]),
                                        html.Div([html.Span(desc.vent_rate_Label, id='adv-fresh-rate-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-fresh-rate-output')]),
                                        html.Div([html.Span(desc.recirc_rate_label, id='adv-recirc-rate-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-recirc-rate-output')]),
                                        html.Div([html.Span(desc.air_filt_label, id='adv-air-filt-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-air-filt-rate-output')]),
                                        html.Div([html.Span(desc.eff_aerosol_rad_label, id='adv-eff-rad-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-eff-rad-output')]),
                                        html.Div([html.Span(desc.viral_deact_label, id='adv-viral-deact-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-viral-deact-output')]),
                                        html.Div([html.Span(desc.sett_speed_label, id='adv-sett-speed-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-sett-speed-output')]),
                                        html.Div([html.Span(desc.conc_relax_rate_label, id='adv-conc-relax-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-conc-relax-output')]),
                                        html.Div([html.Span(desc.airb_trans_label, id='adv-airb-trans-label'),
                                                  html.Span(
                                                      className='model-output-text-small',
                                                      id='adv-airb-trans-output')]),
                                    ]),
                                    html.Br(),
                                    html.H6(html.Span(desc.graph_output_header, id='adv-graph-output-header')),
                                    html.Div([
                                        dcc.Graph(
                                            id='adv-safety-graph',
                                            figure=fig
                                        ),
                                    ]),
                                ]
                            )
                        ],
                                           colors={
                                               "border": "#c9c9c9",
                                               "primary": "#de1616"
                                           })], style={'margin': '1em', 'padding': '0', 'border': 'none'}),
                    html.Div(
                        className='card',
                        id='adv-card-occ',
                        children=[html.Div(className='output-content', children=[
                            html.Div([
                                html.H4(desc.occupancy_panel_header, id='adv-occ-panel-header'),
                                html.H3(html.Span(desc.main_panel_s1, id='adv-main-panel-s1')),
                                dcc.Loading(
                                    id='adv-loading',
                                    type='circle',
                                    children=[
                                        html.H4(className='model-output-text', id='adv-model-text-1',
                                                children="2 people for 31 days"),
                                        html.H4(className='model-output-text', id='adv-model-text-2',
                                                children="5 people for 8 days"),
                                        html.H4(className='model-output-text', id='adv-model-text-3',
                                                children="10 people for 3 days"),
                                        html.H4(className='model-output-text', id='adv-model-text-4',
                                                children="25 people for 31 hours"),
                                        html.H4(className='model-output-text', id='adv-model-text-5',
                                                children="100 people for 8 hours"),
                                    ],
                                    color='#de1616',
                                ),
                                html.Br(),
                                html.Div([
                                    html.H4([
                                        html.Span("", id='adv-n-input-pretext'),
                                        html.Span([dcc.Input(id='adv-n-input',
                                                             value=10,
                                                             type='number')]),
                                        html.Span("", id='adv-n-input-posttext'),
                                    ], className='model-output-text', style={'padding-bottom': '.2em'}),
                                    html.H4([
                                        html.Span("", id='adv-t-input-pretext'),
                                        html.Span([dcc.Input(id='adv-t-input',
                                                             value=4,
                                                             type='number')]),
                                        html.Span(" " + desc.units_hr, id='adv-tn-tail-string'),
                                        html.Span("", id='adv-t-input-posttext'),
                                    ], className='model-output-text')]),
                                html.Br(),
                                html.H4([html.Span(desc.main_panel_six_ft_1, id='adv-main-six-ft-1'),
                                         html.Span(id='adv-six-ft-output',
                                                   children=''' 2 people ''',
                                                   style={'color': '#de1616'}),
                                         html.Span(desc.main_panel_six_ft_2, id='adv-main-six-ft-2'),
                                         html.Span(id='adv-six-ft-output-t', style={'color': '#de1616'}),
                                         html.Span("", id='adv-main-six-ft-3')],
                                        style={'color': '#000000'}),
                            ], className='panel-main-output'),
                            html.Br(),
                            html.Div([
                                html.Span(desc.main_airb_trans_only_disc, id='adv-main-airb-trans-disc')
                            ], className='panel-airb-desc')])]),
                    html.Div(
                        className='card',
                        id='adv-card-co2',
                        children=[
                            html.H4(desc.co2_title, id='adv-co2-panel-header'),
                            html.Div(desc.co2_param_desc, id='adv-co2-param-desc'),
                            html.Br(),
                            html.H5([
                                html.Span(desc.co2_atm_input_1, id='adv-co2-atm-input-1'),
                                html.Span(dcc.Input(id='adv-atm-input-co2',
                                                    value=410,
                                                    type='number')),
                                html.Span(desc.co2_atm_input_2, id='adv-co2-atm-input-2'),
                            ]),
                            html.Div([
                                dcc.Graph(
                                    id='adv-co2-output-graph',
                                    figure=fig_co2,
                                    config=co2_graph_config_desktop,
                                ),
                            ]),
                            html.H3([
                                html.Span(desc.co2_calc_1, id='adv-co2-calc-1'),
                                html.Span(
                                    dcc.Input(id='adv-exp-time-input-co2',
                                              value=8,
                                              type='number')
                                ),
                                html.Span(desc.co2_calc_2, id='adv-co2-calc-2'),
                                dcc.Loading(
                                    html.Span(id='adv-co2-output'),
                                    parent_style={'display': 'inline-block'},
                                    type='circle',
                                    color='#de1616',
                                ),
                                html.Span(desc.co2_calc_3, id='adv-co2-calc-3'),
                            ]),
                            html.Div([
                                desc.co2_safe_footer
                            ], className='panel-airb-desc', id='adv-co2-safe-footer')
                        ]
                    )
                ]
            ),
        ]
    ),
])


# Updates all remaining text based on language
@app.callback(
    [Output('adv-tab-a', 'label'),
     Output('adv-curr-room-header', 'children'),
     Output('adv-presets', 'options'),
     Output('adv-curr-risk-tol', 'children'),
     Output('adv-curr-human-header', 'children'),
     Output('adv-presets-human', 'options'),
     Output('adv-curr-age-group', 'children'),
     Output('adv-age-group', 'marks'),
     Output('adv-curr-viral-strain', 'children'),
     Output('adv-viral-strain', 'marks'),
     Output('adv-pim-header', 'children'),
     Output('adv-main-six-ft-1', 'children'),
     Output('adv-main-six-ft-2', 'children'),
     Output('adv-main-six-ft-3', 'children'),
     Output('adv-about-text', 'children'),
     Output('adv-tab-b', 'label'),
     Output('adv-room-header-body', 'children'),
     Output('adv-ventilation-text', 'children'),
     Output('adv-ventilation-type', 'options'),
     Output('adv-filtration-text', 'children'),
     Output('adv-filter-type', 'options'),
     Output('adv-recirc-text', 'children'),
     Output('adv-humidity-text', 'children'),
     Output('adv-relative-humidity', 'marks'),
     Output('adv-tab-c', 'label'),
     Output('adv-human-header-body', 'children'),
     Output('adv-exertion-text', 'children'),
     Output('adv-exertion-level', 'options'),
     Output('adv-breathing-text', 'children'),
     Output('adv-exp-activity', 'options'),
     Output('adv-mask-type-text', 'children'),
     Output('adv-mask-type', 'marks'),
     Output('adv-mask-fit-text', 'children'),
     Output('adv-mask-fit', 'marks'),
     Output('adv-risk-tolerance', 'marks'),
     Output('adv-tab-d', 'label'),
     Output('adv-pop-immunity-header', 'children'),
     Output('adv-pop-immunity-desc', 'children'),
     Output('adv-pim-label-other', 'children'),
     Output('adv-pi-label', 'children'),
     Output('adv-ps-label', 'children'),
     Output('adv-other-io', 'children'),
     Output('adv-aerosol-rad-text', 'children'),
     Output('adv-viral-deact-text', 'children'),
     Output('adv-val-interest-header', 'children'),
     Output('adv-sr-label', 'children'),
     Output('adv-z_p-label', 'children'),
     Output('adv-filt-eff-label', 'children'),
     Output('adv-breath-rate-label', 'children'),
     Output('adv-cq-label', 'children'),
     Output('adv-mask-pass-label', 'children'),
     Output('adv-room-vol-label', 'children'),
     Output('adv-fresh-rate-label', 'children'),
     Output('adv-recirc-rate-label', 'children'),
     Output('adv-air-filt-label', 'children'),
     Output('adv-eff-rad-label', 'children'),
     Output('adv-viral-deact-label', 'children'),
     Output('adv-sett-speed-label', 'children'),
     Output('adv-conc-relax-label', 'children'),
     Output('adv-airb-trans-label', 'children'),
     Output('adv-graph-output-header', 'children'),
     Output('adv-tn-tail-string', 'children'),
     Output('adv-lang-break-age', 'children'),
     Output('adv-risk-mode', 'options'),
     Output('adv-co2-prev-input-1', 'children'),
     Output('adv-co2-prev-input-2', 'children'),
     Output('adv-incidence-rate-refs', 'children'),
     Output('adv-risk-mode-header', 'children'),
     Output('adv-occ-panel-header', 'children'),
     Output('adv-co2-panel-header', 'children'),
     Output('adv-co2-param-desc', 'children'),
     Output('adv-co2-atm-input-1', 'children'),
     Output('adv-co2-atm-input-2', 'children'),
     Output('adv-co2-calc-1', 'children'),
     Output('adv-co2-calc-2', 'children'),
     Output('adv-co2-calc-3', 'children'),
     Output('adv-co2-safe-footer', 'children')],
    [Input('url', 'search'),
     Input('window-width', 'children')]
)
def update_lang_adv(search, window_width):
    language = ess.get_lang(search)
    return ess.get_lang_text_adv(language, int(window_width))


# Model Update & Calculation
# See indoors.py def set_default_params(self) for parameter descriptions.
@app.callback(
    [Output('adv-safety-graph', 'figure'),
     Output('adv-co2-output-graph', 'figure'),
     Output('adv-co2-output-graph', 'config'),
     Output('adv-co2-output', 'children'),
     Output('adv-model-text-1', 'children'),
     Output('adv-model-text-2', 'children'),
     Output('adv-model-text-3', 'children'),
     Output('adv-model-text-4', 'children'),
     Output('adv-model-text-5', 'children'),
     Output('adv-six-ft-output', 'children'),
     Output('adv-six-ft-output-t', 'children'),
     Output('adv-presets', 'value'),
     Output('adv-presets-human', 'value'),
     Output('adv-pi-output', 'children'),
     Output('adv-ps-output', 'children'),
     Output('adv-sr-output', 'children'),
     Output('adv-air-frac-output', 'children'),
     Output('adv-filtration-eff-output', 'children'),
     Output('adv-breath-rate-output', 'children'),
     Output('adv-infect-air-output', 'children'),
     Output('adv-mask-pass-output', 'children'),
     Output('adv-room-vol-output', 'children'),
     Output('adv-fresh-rate-output', 'children'),
     Output('adv-recirc-rate-output', 'children'),
     Output('adv-air-filt-rate-output', 'children'),
     Output('adv-eff-rad-output', 'children'),
     Output('adv-viral-deact-output', 'children'),
     Output('adv-sett-speed-output', 'children'),
     Output('adv-conc-relax-output', 'children'),
     Output('adv-airb-trans-output', 'children'),
     Output('adv-n-input-pretext', 'children'),
     Output('adv-n-input-posttext', 'children'),
     Output('adv-t-input-pretext', 'children'),
     Output('adv-t-input-posttext', 'children'),
     Output('adv-qb-output', 'children'),
     Output('adv-cq-output', 'children'),
     Output('adv-alert-no-update', 'children'),
     Output('adv-alert-no-update', 'is_open')],
    [Input('adv-floor-area', 'value'),
     Input('adv-ceiling-height', 'value'),
     Input('adv-ventilation-type', 'value'),
     Input('adv-recirc-rate', 'value'),
     Input('adv-filter-type', 'value'),
     Input('adv-relative-humidity', 'value'),
     Input('adv-exertion-level', 'value'),
     Input('adv-exp-activity', 'value'),
     Input('adv-mask-type', 'value'),
     Input('adv-mask-fit', 'value'),
     Input('adv-risk-tolerance', 'value'),
     Input('adv-age-group', 'value'),
     Input('adv-viral-strain', 'value'),
     Input('adv-pim-input', 'value'),
     Input('adv-aerosol-radius', 'value'),
     Input('adv-viral-deact-rate', 'value'),
     Input('adv-n-input', 'value'),
     Input('adv-t-input', 'value'),
     Input('adv-risk-mode', 'value'),
     Input('adv-prev', 'value'),
     Input('adv-atm-input-co2', 'value'),
     Input('adv-exp-time-input-co2', 'value'),
     Input('url', 'search')],
    [State('adv-floor-area-text', 'children'),
     State('adv-ceiling-height-text', 'children'),
     State('window-width', 'children')]
)
def update_figure(floor_area, ceiling_height, air_exchange_rate, recirc_rate, merv, relative_humidity,
                  breathing_flow_rate, infectiousness, mask_eff, mask_fit, risk_tolerance, sr_age_factor,
                  sr_strain_factor, pim_input, def_aerosol_radius,
                  max_viral_deact_rate, n_max_input, exp_time_input, risk_mode, prevalence, atm_co2, exp_time_co2,
                  search, floor_area_text, ceiling_height_text, window_width):
    window_width = float(window_width)
    language = ess.get_lang(search)
    error_msg = ess.get_err_msg(floor_area, ceiling_height, air_exchange_rate, merv, recirc_rate, def_aerosol_radius,
                                max_viral_deact_rate, language, n_max_input, exp_time_input,
                                exp_time_co2, prevalence, atm_co2)

    if error_msg != "":
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               error_msg, True

    # Check our units! Did we switch? If so, convert values before calculating
    my_units = ess.get_units(search)
    curr_units = ess.did_switch_units(search, floor_area_text, ceiling_height_text)
    if curr_units != "":
        [floor_area, ceiling_height] = ess.convert_units(curr_units, my_units, floor_area, ceiling_height)

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
    # Correct mask_passage_prob based on mask fit/compliance
    mask_real_eff = mask_eff * mask_fit
    mask_passage_prob = 1 - mask_real_eff

    # Calculate aerosol filtration efficiency
    aerosol_filtration_eff = Indoors.merv_to_eff(merv, def_aerosol_radius)

    # Convert recirc rate to outdoor air fraction
    outdoor_air_fraction = air_exchange_rate / (air_exchange_rate + recirc_rate)

    myInd.physical_params = [floor_area, ceiling_height, air_exchange_rate, outdoor_air_fraction,
                             aerosol_filtration_eff, relative_humidity]
    myInd.physio_params = [breathing_flow_rate, def_aerosol_radius]
    myInd.disease_params = [infectiousness, max_viral_deact_rate]
    myInd.prec_params = [mask_passage_prob, risk_tolerance]
    myInd.sr_age_factor = sr_age_factor
    myInd.sr_strain_factor = sr_strain_factor
    ps_conditional = 1 - pim_input
    ps_conditional_text = '{:.2f}%'.format(ps_conditional * 100)
    myInd.percentage_sus = ps_conditional
    myInd.calc_vars()

    # Get human behavior output text
    qb_text = ess.get_qb_text(myInd, my_units)
    cq_text = ess.get_cq_text(myInd, my_units)

    # Update the figure with a new model calculation
    new_fig = ess.get_model_figure(myInd, language)

    # Outputs
    if risk_mode == 'conditional':
        prevalence = 0

    pi = prevalence / 100000
    ps = 1 - (pi + pim_input)
    pi_text = '{:.3f}%'.format(pi * 100)
    ps_text = '{:.2f}%'.format(ps * 100)
    myInd.prevalence = pi
    myInd.percentage_sus = ps
    model_output_text = ess.get_model_output_text(myInd, risk_mode, ess.covid_recovery_time, language)
    six_ft_text = ess.get_six_ft_text(myInd, language)
    six_ft_exp_time = ess.get_six_ft_exp_time(myInd, risk_mode, ess.covid_recovery_time, language)

    exp_time_text = ess.time_to_text(myInd.calc_max_time(n_max_input, risk_mode), True, ess.covid_recovery_time,
                                     language)
    n_max_text = ess.get_n_max_text(myInd.calc_n_max(exp_time_input, risk_mode), myInd.get_n_max(), language)

    # Get n pretext and posttext
    desc_file = ess.get_desc_file(language)
    n_input_pretext = ""
    n_input_posttext = desc_file.nt_bridge_string + exp_time_text
    if language in ess.sov_languages:
        n_input_pretext = exp_time_text + desc_file.nt_bridge_string
        n_input_posttext = desc_file.people_string

    t_input_pretext = n_max_text + desc_file.tn_bridge_string
    t_input_posttext = ""
    if language in ess.sov_languages:
        t_input_pretext = ""
        t_input_posttext = desc_file.tn_bridge_string + n_max_text

    # Now take care of the CO2 panel
    myInd.atm_co2 = atm_co2
    new_fig_co2 = ess.get_model_figure_co2(myInd, risk_mode, language, window_width)
    safe_co2_conc = myInd.calc_co2_exp_time(exp_time_co2, risk_mode)
    co2_base_string = '{:,.0f} ppm'
    if hasattr(desc_file, 'safe_co2_conc'):
        co2_base_string = desc_file.co2_base_string

    max_co2_conc = ess.get_safe_resp_co2_limit(exp_time_co2)
    recommended_co2_conc = min(safe_co2_conc, max_co2_conc)
    recommended_co2_conc_text = co2_base_string.format(recommended_co2_conc)

    co2_graph_config = co2_graph_config_desktop
    if window_width < 1200:
        co2_graph_config = co2_graph_config_mobile

    # Update the red text output with new model calculations
    # Model values of interest
    interest_output = ess.get_interest_output_text(myInd, my_units)

    # Update all relevant display items (figure, red output text)
    return new_fig, new_fig_co2, co2_graph_config, recommended_co2_conc_text, \
           model_output_text[0], model_output_text[1], model_output_text[2], model_output_text[3], \
           model_output_text[4], six_ft_text, six_ft_exp_time, preset_dd_value, human_preset_dd_value, pi_text, \
           ps_text, \
           interest_output[0], interest_output[1], interest_output[2], interest_output[3], \
           interest_output[4], interest_output[5], interest_output[6], interest_output[7], interest_output[8], \
           interest_output[9], interest_output[10], interest_output[11], interest_output[12], interest_output[13], \
           interest_output[14], n_input_pretext, n_input_posttext, t_input_pretext, t_input_posttext, qb_text, \
           cq_text, error_msg, False


# Update main panel (occupancy panel) first sentence based on the selected language, prevalence, and risk mode.
@app.callback(
    [Output('adv-main-panel-s1', 'children'),
     Output('adv-main-airb-trans-disc', 'children')],
    [Input('adv-risk-mode', 'value'),
     Input('adv-prev', 'value'),
     Input('url', 'search')]
)
def update_occupancy_panel_sentence(risk_mode, prevalence, search):
    language = ess.get_lang(search)
    desc_file = ess.get_desc_file(language)
    if risk_mode == 'conditional':
        children_main = desc_file.main_panel_s1
        children_disc = desc_file.main_airb_trans_only_disc
    elif risk_mode == 'prevalence':
        children_main = html.Span([
            html.Span(desc_file.main_panel_s1_b),
            html.Span('{:,.0f} '.format(prevalence)),
            html.Span(desc_file.main_panel_s2_b),
        ])
        if hasattr(desc_file, "main_airb_trans_only_desc_b"):
            children_disc = desc_file.main_airb_trans_only_desc_b
        else:
            children_disc = ess.get_desc_file("en").main_airb_trans_only_desc_b
    elif risk_mode == 'personal':
        children_main = html.Span([
            html.Span(desc_file.main_panel_s1_c),
            html.Span('{:,.0f} '.format(prevalence)),
            html.Span(desc_file.main_panel_s2_c),
        ])
        if hasattr(desc_file, "main_airb_trans_only_desc_c"):
            children_disc = desc_file.main_airb_trans_only_desc_c
        else:
            children_disc = ess.get_desc_file("en").main_airb_trans_only_desc_c

    return [children_main, children_disc]


# Update prevalence input (enabled/disabled) depending on selected risk mode.
@app.callback(
    [Output('adv-prev-block', 'style')],
    [Input('adv-risk-mode', 'value')]
)
def update_prev_co2_vis(risk_mode):
    if risk_mode == 'conditional':
        return [{'display': 'none'}]
    else:
        return [{'display': 'inline'}]


# Update risk alert display (open/closed) depending on selected risk mode
@app.callback(
    [Output('adv-risk-alert', 'children'),
     Output('adv-risk-alert', 'is_open')],
    [Input('adv-risk-mode', 'value'),
     Input('url', 'search')]
)
def update_risk_alert(risk_mode, search):
    language = ess.get_lang(search)
    desc_file = ess.get_desc_file(language)

    if risk_mode == 'personal':
        if hasattr(desc_file, "risk_personal_warning"):
            return [desc_file.risk_personal_warning, True]
        else:
            return ["", False]
    else:
        return ["", False]


# Update options based on selected presets, also if units changed
# Updates labels depending on selected unit system (and language)
@app.callback(
    [Output('adv-floor-area', 'value'),
     Output('adv-ceiling-height', 'value'),
     Output('adv-ventilation-type', 'value'),
     Output('adv-recirc-rate', 'value'),
     Output('adv-filter-type', 'value'),
     Output('adv-relative-humidity', 'value'),
     Output('adv-floor-area-text', 'children'),
     Output('adv-ceiling-height-text', 'children')],
    [Input('adv-presets', 'value'),
     Input('url', 'search')],
    [State('adv-floor-area-text', 'children'),
     State('adv-ceiling-height-text', 'children'),
     State('adv-floor-area', 'value'),
     State('adv-ceiling-height', 'value')]
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
@app.callback(
    [Output('adv-exertion-level', 'value'),
     Output('adv-exp-activity', 'value'),
     Output('adv-mask-type', 'value'),
     Output('adv-mask-fit', 'value')],
    [Input('adv-presets-human', 'value')]
)
def update_human_presets(preset):
    # Update the room and behavior options based on the selected preset
    if preset == 'custom':
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update
    else:
        curr_settings = ess.human_preset_settings[preset]
        return curr_settings['exertion'], curr_settings['expiratory'], curr_settings['masks'], \
               curr_settings['mask-fit'],


# Update max pim slider value
@app.callback(
    [Output('adv-pim-input', 'max'),
     Output('adv-pim-input', 'value')],
    [Input('adv-prev', 'value')],
    [State('adv-pim-input', 'value')]
)
def update_pim_slider_max(prev, curr_pim):
    prev = prev / 100000
    pim_max = 1 - prev - 0.001
    new_pim = curr_pim
    if curr_pim >= pim_max:
        new_pim = pim_max - 0.01

    return [pim_max, new_pim]


# Relative Humidity slider value display
@app.callback(
    [Output('adv-humidity-output', 'children')],
    [Input('adv-relative-humidity', 'value')]
)
def update_humid_disp(relative_humidity):
    return ["{:.0f}%".format(relative_humidity * 100)]


# Risk tolerance slider value display
@app.callback(
    [Output('adv-risk-tolerance-output', 'children')],
    [Input('adv-risk-tolerance', 'value')]
)
def update_risk_tol_disp(risk_tolerance):
    return ["{:.2f}".format(risk_tolerance)]


# Age Group slider value display
@app.callback(
    [Output('adv-age-group-output', 'children')],
    [Input('adv-age-group', 'value')]
)
def update_age_group_disp(age_factor):
    return ["{:.2f}".format(age_factor)]


# Viral Strain slider value display
@app.callback(
    [Output('adv-viral-strain-output', 'children')],
    [Input('adv-viral-strain', 'value')]
)
def update_viral_strain_disp(strain_factor):
    return ["{:.2f}".format(strain_factor)]


# Percentage Immune slider value display
@app.callback(
    [Output('adv-pim-output', 'children'),
     Output('adv-pim-output-other', 'children')],
    [Input('adv-pim-input', 'value')]
)
def update_viral_strain_disp(pim):
    pim_output = "{:.0f}%".format(pim * 100)
    return [pim_output, pim_output]


# Mask Filtration Efficiency slider value display
@app.callback(
    [Output('adv-mask-eff-output', 'children')],
    [Input('adv-mask-type', 'value')]
)
def update_mask_type_disp(mask_eff):
    return ["{:.0f}%".format(mask_eff * 100)]


# Mask Fit/Compliance slider value display
@app.callback(
    [Output('adv-mask-fit-output', 'children')],
    [Input('adv-mask-fit', 'value')]
)
def update_mask_fit_disp(mask_fit):
    return ["{:.0f}%".format(mask_fit * 100)]
