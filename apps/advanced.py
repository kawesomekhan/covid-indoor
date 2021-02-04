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

# Main App
layout = html.Div(children=[
    dbc.Alert(
        "Error Alert",
        id='adv-alert-no-update',
        className='error-alert',
        is_open=False,
    ),

    html.Div(
        className='main-content',
        children=[
            html.Div(
                className='grid',
                children=[
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
                                              dcc.Input(id='adv-floor-area', value=900,
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
                                                         min=0,
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
                                        html.H5(desc.risk_conditional_desc, id='adv-risk-conditional-desc'),
                                        html.Div([html.Span(desc.perc_susceptible_label, id='adv-ps-label-conditional'),
                                                  html.Span(className='model-output-text-small',
                                                            children="100%")]),
                                        html.H5(desc.risk_prevalence_desc, id='adv-risk-prevalence-desc'),
                                        html.Div([html.Span(desc.perc_infectious_label, id='adv-pi-label-prevalence'),
                                                  html.Span(className='model-output-text-small',
                                                            id='adv-pi-output-prevalence')]),
                                        html.Div([html.Span(desc.perc_susceptible_label, id='adv-ps-label-prevalence'),
                                                  html.Span(className='model-output-text-small',
                                                            id='adv-ps-output-prevalence')]),
                                        html.H5(desc.risk_personal_desc, id='adv-risk-personal-desc'),
                                        html.Div([html.Span(desc.perc_infectious_label, id='adv-pi-label-personal'),
                                                  html.Span(className='model-output-text-small',
                                                            id='adv-pi-output-personal')]),
                                        html.Div([html.Span(desc.perc_susceptible_label, id='adv-ps-label-personal'),
                                                  html.Span(className='model-output-text-small',
                                                            id='adv-ps-output-personal')]),
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
                        children=[
                            html.Div(
                                className='grid-presets',
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
                                        html.Div([html.Br()], id='adv-mobile-risk-break')
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
                                                   value=0.33,
                                                   marks=desc.pim_marks),
                                    ], className='card-presets')
                                ],
                            ),
                        ]
                    ),
                    html.Div(
                        className='card',
                        children=[
                            dcc.Tabs([
                                dcc.Tab(
                                    id='adv-output-panel-tab-a',
                                    label=desc.risk_conditional_desc,
                                    className='custom-tab',
                                    children=html.Div(className='output-content', children=[
                                        html.Div([
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
                                            html.H4([
                                                html.Span([dcc.Input(id='adv-n-input',
                                                                     value=10,
                                                                     type='number')]),
                                                html.Span(" people for ", style={'color': '#000000'}),
                                                html.Span(id='adv-t-output', children="8 hours"),
                                            ], className='model-output-text', style={'padding-bottom': '.2em'}),
                                            html.H4([
                                                html.Span(id='adv-n-output', children="5 people"),
                                                html.Span(" for ", style={'color': '#000000'}),
                                                html.Span([dcc.Input(id='adv-t-input',
                                                                     value=4,
                                                                     type='number')]),
                                                html.Span(" hours", style={'color': '#000000'})
                                            ], className='model-output-text'),
                                            html.Br(),
                                            html.H4([html.Span(desc.main_panel_six_ft_1, id='adv-main-six-ft-1'),
                                                     html.Span(id='adv-six-ft-output',
                                                               children=''' 2 people ''',
                                                               style={'color': '#de1616'}),
                                                     html.Span(desc.main_panel_six_ft_2, id='adv-main-six-ft-2'),
                                                     html.Span(id='adv-six-ft-output-t', style={'color': '#de1616'})],
                                                    style={'color': '#000000'}),
                                        ], className='panel-main-output'),
                                        html.Br(),
                                        html.Div([
                                            html.Span(desc.main_airb_trans_only_disc, id='adv-main-airb-trans-disc')
                                        ], className='panel-airb-desc')
                                    ]),
                                ),
                                dcc.Tab(
                                    id='adv-output-panel-tab-b',
                                    label=desc.risk_prevalence_desc,
                                    className='custom-tab',
                                    children=html.Div(className='output-content', children=[
                                        html.Div([
                                            html.H3([
                                                html.Span(desc.main_panel_s1_b, id='adv-main-panel-s1-b'),
                                                html.Span(dcc.Input(id='adv-prev-input-b',
                                                                    value=100,
                                                                    type='number')),
                                                html.Span(desc.main_panel_s2_b, id='adv-main-panel-s2-b')
                                            ]),
                                            dcc.Loading(
                                                id='adv-loading-b',
                                                type='circle',
                                                children=[
                                                    html.H4(className='model-output-text', id='adv-model-text-1-b',
                                                            children="2 people for 31 days"),
                                                    html.H4(className='model-output-text', id='adv-model-text-2-b',
                                                            children="5 people for 8 days"),
                                                    html.H4(className='model-output-text', id='adv-model-text-3-b',
                                                            children="10 people for 3 days"),
                                                    html.H4(className='model-output-text', id='adv-model-text-4-b',
                                                            children="25 people for 31 hours"),
                                                    html.H4(className='model-output-text', id='adv-model-text-5-b',
                                                            children="100 people for 8 hours"),
                                                ],
                                                color='#de1616',
                                            ),
                                            html.Br(),
                                            html.H4([
                                                html.Span([dcc.Input(id='adv-n-input-b',
                                                                     value=10,
                                                                     type='number')]),
                                                html.Span(" people for ", style={'color': '#000000'}),
                                                html.Span(id='adv-t-output-b', children="8 hours"),
                                            ], className='model-output-text', style={'padding-bottom': '.2em'}),
                                            html.H4([
                                                html.Span(id='adv-n-output-b', children="5 people"),
                                                html.Span(" for ", style={'color': '#000000'}),
                                                html.Span([dcc.Input(id='adv-t-input-b',
                                                                     value=4,
                                                                     type='number')]),
                                                html.Span(" hours", style={'color': '#000000'})
                                            ], className='model-output-text'),
                                            html.Br(),
                                            html.H4([html.Span(desc.main_panel_six_ft_1, id='adv-main-six-ft-1-b'),
                                                     html.Span(id='adv-six-ft-output-b',
                                                               children=''' 2 people ''',
                                                               style={'color': '#de1616'}),
                                                     html.Span(desc.main_panel_six_ft_2, id='adv-main-six-ft-2-b'),
                                                     html.Span(id='adv-six-ft-output-t-b', style={'color': '#de1616'})],
                                                    style={'color': '#000000'})
                                        ], className='panel-main-output'),
                                        html.Br(),
                                        html.Div(desc.main_airb_trans_only_desc_b, id='adv-main-airb-trans-desc-b',
                                                 className='panel-airb-desc'),
                                        html.Div(desc.incidence_rate_refs, id='adv-incidence-rate-refs-b',
                                                 className='panel-airb-desc')
                                    ]),
                                ),
                                dcc.Tab(
                                    id='adv-output-panel-tab-c',
                                    label=desc.risk_personal_desc,
                                    className='custom-tab',
                                    children=html.Div(className='output-content', children=[
                                        html.Div([
                                            html.H3([
                                                html.Span(desc.main_panel_s1_c, id='adv-main-panel-s1-c'),
                                                html.Span(dcc.Input(id='adv-prev-input-c',
                                                                    value=100,
                                                                    type='number')),
                                                html.Span(desc.main_panel_s2_c, id='adv-main-panel-s2-c')
                                            ]),
                                            dcc.Loading(
                                                id='adv-loading-c',
                                                type='circle',
                                                children=[
                                                    html.H4(className='model-output-text', id='adv-model-text-1-c',
                                                            children="2 people for 31 days"),
                                                    html.H4(className='model-output-text', id='adv-model-text-2-c',
                                                            children="5 people for 8 days"),
                                                    html.H4(className='model-output-text', id='adv-model-text-3-c',
                                                            children="10 people for 3 days"),
                                                    html.H4(className='model-output-text', id='adv-model-text-4-c',
                                                            children="25 people for 31 hours"),
                                                    html.H4(className='model-output-text', id='adv-model-text-5-c',
                                                            children="100 people for 8 hours"),
                                                ],
                                                color='#de1616',
                                            ),
                                            html.Br(),
                                            html.H4([
                                                html.Span([dcc.Input(id='adv-n-input-c',
                                                                     value=10,
                                                                     type='number')]),
                                                html.Span(" people for ", style={'color': '#000000'}),
                                                html.Span(id='adv-t-output-c', children="8 hours"),
                                            ], className='model-output-text', style={'padding-bottom': '.2em'}),
                                            html.H4([
                                                html.Span(id='adv-n-output-c', children="5 people"),
                                                html.Span(" for ", style={'color': '#000000'}),
                                                html.Span([dcc.Input(id='adv-t-input-c',
                                                                     value=4,
                                                                     type='number')]),
                                                html.Span(" hours", style={'color': '#000000'})
                                            ], className='model-output-text'),
                                            html.Br(),
                                            html.H4([html.Span(desc.main_panel_six_ft_1, id='adv-main-six-ft-1-c'),
                                                     html.Span(id='adv-six-ft-output-c',
                                                               children=''' 2 people ''',
                                                               style={'color': '#de1616'}),
                                                     html.Span(desc.main_panel_six_ft_2, id='adv-main-six-ft-2-c'),
                                                     html.Span(id='adv-six-ft-output-t-c', style={'color': '#de1616'})],
                                                    style={'color': '#000000'})
                                        ], className='panel-main-output'),
                                        html.Br(),
                                        html.Div(desc.main_airb_trans_only_desc_c, id='adv-main-airb-trans-desc-c',
                                                 className='panel-airb-desc'),
                                        html.Div(desc.incidence_rate_refs, id='adv-incidence-rate-refs-c',
                                                 className='panel-airb-desc')
                                    ]),
                                ),
                            ],
                                colors={
                                    "border": "#c9c9c9",
                                    "primary": "#de1616"
                                })
                        ], style=ess.tabs_card_style
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
     Output('adv-main-panel-s1', 'children'),
     Output('adv-main-six-ft-1', 'children'),
     Output('adv-main-six-ft-2', 'children'),
     Output('adv-main-airb-trans-disc', 'children'),
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
     Output('adv-other-io', 'children'),
     Output('adv-aerosol-rad-text', 'children'),
     Output('adv-viral-deact-text', 'children'),
     Output('adv-val-interest-header', 'children'),
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
     Output('adv-graph-output-header', 'children')],
    [Input('url', 'search'),
     Input('window-width', 'children')]
)
def update_lang(search, window_width):
    return ess.get_lang_text_adv(ess.get_lang(search), int(window_width))


# Model Update & Calculation
# See indoors.py def set_default_params(self) for parameter descriptions.
@app.callback(
    [Output('adv-safety-graph', 'figure'),
     Output('adv-model-text-1', 'children'),
     Output('adv-model-text-2', 'children'),
     Output('adv-model-text-3', 'children'),
     Output('adv-model-text-4', 'children'),
     Output('adv-model-text-5', 'children'),
     Output('adv-model-text-1-b', 'children'),
     Output('adv-model-text-2-b', 'children'),
     Output('adv-model-text-3-b', 'children'),
     Output('adv-model-text-4-b', 'children'),
     Output('adv-model-text-5-b', 'children'),
     Output('adv-model-text-1-c', 'children'),
     Output('adv-model-text-2-c', 'children'),
     Output('adv-model-text-3-c', 'children'),
     Output('adv-model-text-4-c', 'children'),
     Output('adv-model-text-5-c', 'children'),
     Output('adv-six-ft-output', 'children'),
     Output('adv-six-ft-output-t', 'children'),
     Output('adv-six-ft-output-b', 'children'),
     Output('adv-six-ft-output-t-b', 'children'),
     Output('adv-six-ft-output-c', 'children'),
     Output('adv-six-ft-output-t-c', 'children'),
     Output('adv-presets', 'value'),
     Output('adv-presets-human', 'value'),
     Output('adv-pi-output-prevalence', 'children'),
     Output('adv-ps-output-prevalence', 'children'),
     Output('adv-pi-output-personal', 'children'),
     Output('adv-ps-output-personal', 'children'),
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
     Output('adv-t-output', 'children'),
     Output('adv-n-output', 'children'),
     Output('adv-t-output-b', 'children'),
     Output('adv-n-output-b', 'children'),
     Output('adv-t-output-c', 'children'),
     Output('adv-n-output-c', 'children'),
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
     Input('adv-n-input-b', 'value'),
     Input('adv-t-input-b', 'value'),
     Input('adv-n-input-c', 'value'),
     Input('adv-t-input-c', 'value'),
     Input('adv-prev-input-b', 'value'),
     Input('adv-prev-input-c', 'value'),
     Input('url', 'search')],
    [State('adv-floor-area-text', 'children'),
     State('adv-ceiling-height-text', 'children')]
)
def update_figure(floor_area, ceiling_height, air_exchange_rate, recirc_rate, merv, relative_humidity,
                  breathing_flow_rate, infectiousness, mask_eff, mask_fit, risk_tolerance, sr_age_factor,
                  sr_strain_factor, pim_input, def_aerosol_radius,
                  max_viral_deact_rate, n_max_input, exp_time_input, n_max_input_b, exp_time_input_b, n_max_input_c,
                  exp_time_input_c, prevalence_b, prevalence_c, search, floor_area_text, ceiling_height_text):
    language = ess.get_lang(search)
    error_msg = ess.get_err_msg(floor_area, ceiling_height, air_exchange_rate, merv, recirc_rate, def_aerosol_radius,
                                max_viral_deact_rate, language, n_max_input, exp_time_input, n_max_input_b,
                                exp_time_input_b, n_max_input_c, exp_time_input_c, prevalence_b, prevalence_c)

    if error_msg != "":
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, error_msg, True

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

    # Prevalence Outputs (Given the prevalence of infection...)
    pi_prevalence = prevalence_b / 100000
    ps_prevalence = 1 - (pi_prevalence + pim_input)
    myInd.prevalence = pi_prevalence
    myInd.percentage_sus = ps_prevalence
    pi_prevalence_text = '{:.3f}%'.format(pi_prevalence * 100)
    ps_prevalence_text = '{:.2f}%'.format(ps_prevalence * 100)
    model_output_text_b = ess.get_model_output_text(myInd, 'prevalence', -1, language)
    six_ft_text_b = ess.get_six_ft_text(myInd, language)
    six_ft_exp_time_b = ess.get_six_ft_exp_time(myInd, 'personal', -1, language)

    exp_time_text_b = ess.time_to_text(myInd.calc_max_time(n_max_input_b, 'prevalence'), True, -1,
                                       language)
    n_max_text_b = ess.get_n_max_text(myInd.calc_n_max(exp_time_input_b, 'prevalence'), myInd.get_n_max(), language)

    # Personal Outputs (To limit my personal risk...)
    pi_personal = prevalence_c / 100000
    ps_personal = 1 - (pi_personal + pim_input)
    myInd.prevalence = pi_personal
    myInd.percentage_sus = ps_personal
    pi_personal_text = '{:.3f}%'.format(pi_personal * 100)
    ps_personal_text = '{:.2f}%'.format(ps_personal * 100)
    model_output_text_c = ess.get_model_output_text(myInd, 'personal', -1, language)
    six_ft_text_c = ess.get_six_ft_text(myInd, language)
    six_ft_exp_time_c = ess.get_six_ft_exp_time(myInd, 'personal', -1, language)

    exp_time_text_c = ess.time_to_text(myInd.calc_max_time(n_max_input_c, 'personal'), True, -1,
                                       language)
    n_max_text_c = ess.get_n_max_text(myInd.calc_n_max(exp_time_input_c, 'personal'), myInd.get_n_max(), language)

    # Update all relevant display items (figure, red output text)
    return new_fig, model_output_text[0], model_output_text[1], model_output_text[2], model_output_text[3], \
           model_output_text[4], model_output_text_b[0], model_output_text_b[1], model_output_text_b[2], \
           model_output_text_b[3], model_output_text_b[4], model_output_text_c[0], model_output_text_c[1], \
           model_output_text_c[2], model_output_text_c[3], model_output_text_c[4], six_ft_text, six_ft_exp_time, \
           six_ft_text_b, six_ft_exp_time_b, six_ft_text_c, six_ft_exp_time_c, preset_dd_value, human_preset_dd_value, \
           pi_prevalence_text, ps_prevalence_text, pi_personal_text, ps_personal_text, \
           interest_output[0], interest_output[1], interest_output[2], interest_output[3], interest_output[4], \
           interest_output[5], interest_output[6], interest_output[7], interest_output[8], interest_output[9], \
           interest_output[10], interest_output[11], interest_output[12], interest_output[13], interest_output[14], \
           exp_time_text, n_max_text, exp_time_text_b, n_max_text_b, exp_time_text_c, n_max_text_c, qb_text, cq_text, \
           error_msg, False


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
    [Input('adv-prev-input-b', 'value'),
     Input('adv-prev-input-c', 'value')],
    [State('adv-pim-input', 'value')]
)
def update_pim_slider_max(prev_b, prev_c, curr_pim):
    prev_b = prev_b / 100000
    prev_c = prev_c / 100000
    pim_max = 1 - max(prev_b, prev_c) - 0.001
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
