import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

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
fig = ess.get_model_figure(myInd)

mask_type_marks = {
    0: {'label': "0% (none)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (quilter's cotton)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (silk, flannel, chiffon)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (surgical, cotton)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (N95 respirator)", 'style': {'max-width': '50px'}},
}

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
                        children=[dcc.Tabs(value='tab-1', children=[
                            dcc.Tab(
                                label=desc.about_header,
                                className='custom-tab',
                                children=html.Span(desc.about, id='adv-about-text'),
                                style=ess.tab_style,
                                selected_style=ess.tab_style_selected
                            ),
                            dcc.Tab(
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
                                ],
                                style=ess.tab_style,
                                selected_style=ess.tab_style_selected
                            ),
                            dcc.Tab(
                                label=desc.human_header,
                                className='custom-tab',
                                children=[
                                    html.H6(html.Span(desc.human_header, id='adv-human-header-body')),
                                    html.Div([html.Span(desc.exertion_text, id='adv-exertion-text'),
                                              dcc.Dropdown(id='adv-exertion-level',
                                                           options=ess.exertion_types,
                                                           value=0.49,
                                                           searchable=False,
                                                           clearable=False)]),
                                    html.Br(),
                                    html.Div([html.Span(desc.breathing_text, id='adv-breathing-text'),
                                              dcc.Dropdown(id='adv-exp-activity',
                                                           options=ess.expiratory_types,
                                                           value=29,
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
                                                         value=0.75,
                                                         marks=mask_type_marks)]),
                                    html.Br(),
                                    html.Br(),
                                    html.Div([html.Span(desc.mask_fit_text, id='adv-mask-fit-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='adv-mask-fit-output'),
                                              dcc.Slider(id='adv-mask-fit',
                                                         min=0,
                                                         max=0.95,
                                                         step=0.01,
                                                         value=0.90,
                                                         marks=ess.mask_fit_marks),
                                              ]),
                                    html.Br(),
                                    html.Br(),
                                    html.Div([html.Span(desc.risk_tolerance_text, id='adv-risk-tol-text'),
                                              html.Span(className='model-output-text-small',
                                                        id='adv-risk-tolerance-output'),
                                              html.Span(desc.risk_tol_desc, id='adv-risk-tol-desc'),
                                              dcc.Slider(id='adv-risk-tolerance',
                                                         min=0.01,
                                                         max=1,
                                                         step=0.01,
                                                         value=0.1,
                                                         marks=ess.risk_tol_marks)
                                              ]),
                                    html.Br(),
                                    html.Br(),
                                ],
                                style=ess.tab_style,
                                selected_style=ess.tab_style_selected
                            ),
                            dcc.Tab(
                                label=desc.other_io,
                                className='custom-tab',
                                children=[
                                    html.H6(html.Span(desc.other_io, id='adv-other-io')),
                                    html.Div([html.Span(desc.aerosol_radius_text, id='adv-aerosol-rad-text'),
                                              dcc.Input(id='adv-aerosol-radius', value=2,
                                                        type='number')]),
                                    html.Br(),
                                    html.Div([html.Span(desc.viral_deact_text, id='adv-viral-deact-text'),
                                              dcc.Input(id='adv-viral-deact-rate',
                                                        value=0.3,
                                                        type='number')]),
                                    html.Br(),
                                    html.H6(html.Span(desc.values_interest_header, id='adv-val-interest-header')),
                                    html.Div([
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
                                ],
                                style=ess.tab_style,
                                selected_style=ess.tab_style_selected
                            )
                        ],
                                           colors={
                                               "border": "#c9c9c9",
                                               "primary": "#de1616"
                                           })], style={'margin': '1em', 'padding': '0', 'border': 'none'}),
                    html.Div(
                        className='card',
                        children=[html.Div(className='output-content', children=[
                            html.H3(html.Span(desc.main_panel_s1, id='adv-main-panel-s1')),
                            dcc.Loading(
                                id='adv-loading',
                                type='circle',
                                children=[
                                    html.H4(className='model-output-text',
                                            id='adv-model-text-1',
                                            children="2 people for 31 days"),
                                    html.H4(className='model-output-text',
                                            id='adv-model-text-2',
                                            children="3 people for 15 days"),
                                    html.H4(className='model-output-text',
                                            id='adv-model-text-3',
                                            children="4 people for 10 days"),
                                    html.H4(className='model-output-text',
                                            id='adv-model-text-4',
                                            children="5 people for 8 days"),
                                    html.H4(className='model-output-text',
                                            id='adv-model-text-5',
                                            children="10 people for 3 days"),
                                    html.H4(className='model-output-text',
                                            id='adv-model-text-6',
                                            children="25 people for 31 hours"),
                                    html.H4(className='model-output-text',
                                            id='adv-model-text-7',
                                            children="50 people for 15 hours"),
                                    html.H4(className='model-output-text',
                                            id='adv-model-text-8',
                                            children="100 people for 8 hours"),
                                ],
                                color='#de1616',
                            ),
                            html.Br(),
                            html.H3([html.Span(desc.main_panel_six_ft_1, id='main-six-ft-1'),
                                     html.Span(id='adv-six-ft-output',
                                               children=''' 2 people ''',
                                               style={'color': '#de1616'}),
                                     html.Span(desc.main_panel_six_ft_2, id='main-six-ft-2')]),
                            html.Span(desc.main_airb_trans_only_disc, id='main-airb-trans-disc')
                        ])]),
                    html.Div(
                        className='card',
                        children=[html.Div(className='output-content', children=[
                            html.H3([html.Span(desc.n_input_text_1, id='adv-n-input-text-1'),
                                     html.Span([dcc.Input(id='adv-n-input',
                                                          value=10,
                                                          type='number')]),
                                     html.Span(desc.n_input_text_2, id='adv-n-input-text-2'),
                                     html.Span(id='adv-t-output',
                                               children="8 hours",
                                               style={'color': '#de1616'}),
                                     html.Span(desc.n_input_text_3, id='adv-n-input-text-3')]),
                            html.Br(),
                            html.Span(desc.airb_trans_only_disc, id='adv-airb-trans-only-disc-1')
                        ])]
                    ),
                    html.Div(
                        className='card',
                        children=[html.Div(className='output-content', children=[
                            html.H3([html.Span(desc.t_input_text_1, id='adv-t-input-text-1'),
                                     html.Span([dcc.Input(id='adv-t-input',
                                                          value=4,
                                                          type='number')]),
                                     html.Span(desc.t_input_text_2, id='adv-t-input-text-2'),
                                     html.Span(id='adv-n-output',
                                               children="5 occupants",
                                               style={'color': '#de1616'}),
                                     html.Span(desc.t_input_text_3, id='adv-t-input-text-3')]),
                            html.Br(),
                            html.Span(desc.airb_trans_only_disc, id='adv-airb-trans-only-disc-2')
                        ])
                                  ]
                    )
                ]
            ),
        ]
    ),
])


# Updates labels based on unit system
@app.callback(
    [Output('adv-floor-area-text', 'children'),
     Output('adv-ceiling-height-text', 'children')],
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
     Output('adv-air-frac-output', 'children'),
     Output('adv-filtration-eff-output', 'children'),
     Output('adv-breath-rate-output', 'children'),
     Output('adv-infect-air-output', 'children'),
     Output('adv-mask-pass-output', 'children'),
     Output('adv-room-vol-output', 'children'),
     Output('adv-fresh-rate-output', 'children'),
     Output('adv-recirc-rate-output', 'children'),
     Output('adv-air-filt-rate-output', 'children'),
     Output('adv-sett-speed-output', 'children'),
     Output('adv-conc-relax-output', 'children'),
     Output('adv-airb-trans-output', 'children'),
     Output('adv-t-output', 'children'),
     Output('adv-n-output', 'children'),
     Output('adv-alert-no-update', 'children'),
     Output('adv-alert-no-update', 'is_open')],
    [Input('adv-floor-area', 'value'),
     Input('adv-ceiling-height', 'value'),
     Input('adv-ventilation-type', 'value'),
     Input('adv-recirc-rate', 'value'),
     Input('adv-filter-type', 'value'),
     Input('adv-exertion-level', 'value'),
     Input('adv-exp-activity', 'value'),
     Input('adv-mask-type', 'value'),
     Input('adv-mask-fit', 'value'),
     Input('adv-risk-tolerance', 'value'),
     Input('adv-aerosol-radius', 'value'),
     Input('adv-viral-deact-rate', 'value'),
     Input('adv-n-input', 'value'),
     Input('adv-t-input', 'value'),
     Input('url', 'search')]
)
def update_figure(floor_area, ceiling_height, air_exchange_rate, recirc_rate, merv,
                  breathing_flow_rate, infectiousness, mask_eff, mask_fit, risk_tolerance, aerosol_radius,
                  viral_deact_rate, n_max_input, exp_time_input, search):
    error_msg = ""

    # Make sure none of our values are none
    if floor_area is None:
        error_msg = desc.error_list["floor_area"]
    elif ceiling_height is None:
        error_msg = desc.error_list["ceiling_height"]
    elif recirc_rate is None:
        error_msg = desc.error_list["recirc_rate"]
    elif aerosol_radius is None:
        error_msg = desc.error_list["aerosol_radius"]
    elif viral_deact_rate is None:
        error_msg = desc.error_list["viral_deact_rate"]
    elif n_max_input is None or n_max_input < 2:
        error_msg = desc.error_list["n_max_input"]
    elif exp_time_input == 0 or exp_time_input is None:
        error_msg = desc.error_list["exp_time_input"]
    elif air_exchange_rate == 0 or air_exchange_rate is None:
        error_msg = desc.error_list["air_exchange_rate"]
    elif merv is None:
        error_msg = desc.error_list["merv"]

    if error_msg != "":
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update, \
               dash.no_update, error_msg, True

    # Check our units!
    params = ess.search_to_params(search)
    my_units = "british"
    if "units" in params:
        my_units = params["units"]

    # If metric, convert floor_area and ceiling_height to feet
    if my_units == "metric":
        floor_area = floor_area * 10.764
        ceiling_height = ceiling_height * 3.281

    # Update model with newly-selected parameters
    # Correct mask_passage_prob based on mask fit/compliance
    mask_real_eff = mask_eff * mask_fit
    mask_passage_prob = 1 - mask_real_eff

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

    # Update transient exposure time based on selected n value
    exp_time_output = myInd.calc_max_time(n_max_input)
    exp_time_text = ess.time_to_text(exp_time_output)

    n_max_output = myInd.calc_n_max(exp_time_input)
    n_max_text = ' {:.0f} people'.format(n_max_output)

    # Update all relevant display items (figure, red output text)
    return new_fig, model_output_text[0], model_output_text[1], model_output_text[2], model_output_text[3], \
           model_output_text[4], model_output_text[5], model_output_text[6], model_output_text[7], \
           six_ft_text, interest_output[0], interest_output[1], interest_output[2], \
           interest_output[3], interest_output[4], interest_output[5], interest_output[6], interest_output[7], \
           interest_output[8], interest_output[9], interest_output[10], interest_output[11], exp_time_text, \
           n_max_text, error_msg, False


# Risk tolerance slider value display
@app.callback(
    [Output('adv-risk-tolerance-output', 'children')],
    [Input('adv-risk-tolerance', 'value')]
)
def update_risk_tol_disp(risk_tolerance):
    return ["{:.2f}".format(risk_tolerance)]


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
