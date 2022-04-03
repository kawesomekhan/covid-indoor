import dash_html_components as html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions: English

"""

# Header
header = html.Div([
    html.H1(children='COVID-19 Indoor Safety Guideline'),
    html.Div([
        html.Div([html.Span(html.A(href=links.link_kasim,
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href=links.link_bush,
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ", and ",
                  html.Span(html.A(href=links.link_bazant,
                                   children="Martin Z. Bazant",
                                   target='_blank')),
                  ""]),
        html.Div([html.Span(["Bazant & Bush, A guideline to limit indoor airborne transmission of COVID-19, "]),
                  html.Span(html.A(href=links.link_paper_pnas,
                                   target='_blank',
                                   children='''PNAS (2021)''')),
                  html.Span(", Beyond Six Feet, "),
                  html.Span(html.A(href=links.link_paper,
                                   target='_blank',
                                   children='''medRxiv (2020)''')), ]),
        html.Div([html.Span(
            ["Monitoring carbon dioxide to quantify the risk of indoor airborne transmission of COVID-19 ("]),
                  html.Span(html.A(href=links.link_paper_co2,
                                   target='_blank',
                                   children='''Bazant et al., 2021''')),
                  html.Span(")")]),
        html.Div([
            html.A(href=links.link_bazant_covid,
                   children=links.link_bazant_covid,
                   target='_blank'),
        ]),
        html.Div([
            html.A(href=links.link_github,
                   children=links.link_github,
                   target='_blank'),
        ]),
    ], className='header-small-text')
])

# Menu dropdowns
language_dd = "Language: "

# Unit systems
units_dd = "Units: "
unit_settings = [
    {'label': "British", 'value': "british"},
    {'label': "Metric", 'value': "metric"},
]

# Modes
mode_dd = "Mode: "
app_modes = [
    {'label': "Basic", 'value': "basic"},
    {'label': "Advanced", 'value': "advanced"},
]

output_mode_dd = "Output Mode: "
output_modes = [
    {'label': "Safe Occupancy", 'value': "occupancy"},
    {'label': "Safe CO\u2082 Level", 'value': "co2"},
]

error_list = {
    "floor_area": "Error: Floor area cannot be empty.",
    "ceiling_height": "Error: Ceiling height cannot be empty.",
    "recirc_rate": "Error: Recirculation rate cannot be empty.",
    "aerosol_radius": "Error: Aerosol radius cannot be empty.",
    "viral_deact_rate": "Error: Viral deactivation rate cannot be empty.",
    "n_max_input": "Error: Number of people cannot be less than 2.",
    "exp_time_input": "Error: Exposure time must be greater than 0.",
    "air_exchange_rate": "Error: Ventilation Rate (ACH) must be greater than 0.",
    "merv": "Error: Filtration System (MERV) cannot be empty.",
    "prevalence": "Error: Incidence rate must be greater than 0 and less than 100,000.",
    "atm_co2": "Error: Background CO\u2082 level is required.",
    "co2_input": "Error: CO\u2082 level is required."
}

# Main Panel Text
curr_room_header = "Room Specifications: "
presets = [
    {'label': "Custom", 'value': 'custom'},
    {'label': "Classroom", 'value': 'classroom'},
    {'label': "Living Room", 'value': 'living-room'},
    {'label': "Church", 'value': 'church'},
    {'label': "Restaurant", 'value': 'restaurant'},
    {'label': "Office", 'value': 'office'},
    {'label': "Subway Car", 'value': 'subway'},
    {'label': "Commercial Airliner", 'value': 'airplane'},
]

curr_human_header = "Human Behavior: "
presets_human = [
    {'label': "Custom", 'value': 'custom'},
    {'label': "Masks, Resting", 'value': 'masks-1'},
    {'label': "Masks, Speaking", 'value': 'masks-2'},
    {'label': "Masks, Exercise", 'value': 'masks-3'},
    {'label': "No Masks, Resting", 'value': 'no-masks-1'},
    {'label': "No Masks, Speaking", 'value': 'no-masks-2'},
    {'label': "No Masks, Exercise", 'value': 'no-masks-3'},
    {'label': "No Masks, Singing", 'value': 'singing-1'},
]

curr_risk_header = "Risk Tolerance: "
# presets_risk = [
#     {'label': "Low", 'value': 0.01},
#     {'label': "Medium", 'value': 0.1},
#     {'label': "High", 'value': 1},
# ]
risk_tol_marks = {
    # 0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Safer', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Unsafe'}
}

risk_tolerance_text = "Risk Tolerance: "
risk_tol_desc = html.Div('''More vulnerable populations such as the elderly or those with preexisting medical 
conditions require a lower risk tolerance (~0.01). A higher risk tolerance will mean more expected 
transmissions during the expected occupancy period (see FAQ for details).''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})

curr_age_header = "Age Group: "
presets_age = [
    {'label': "Children (<15 years)", 'value': 0.23},
    {'label': "Adults (15-64 years)", 'value': 0.68},
    {'label': "Elderly (>64 years)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: Children (<15 years)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: Adults (15-64 years)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: Elderly (>64 years)', 'style': {'width': '75px'}}
}

# TODO: Add Omicron to other languages
curr_strain_header = "Viral Strain: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "Wildtype (SARS-CoV-2 Wuhan)", 'value': 1},
    # {'label': "SARS-CoV-2 - B.1.427/429 (California)", 'value': 1.2},
    {'label': "Alpha (B.1.1.7 UK)", 'value': 1.5},
    {'label': "Beta (B.1.351 South Africa)", 'value': 1.501},
    {'label': "Gamma (P.1 Brazil)", 'value': 2.001},  # See viral_strain_marks for why this isn't 2.0
    {'label': "Delta (B.1.617.2 India)", 'value': 2.5},
    {'label': "Omicron (BA.1 South Africa)", 'value': 4.0},
    {'label': "Omicron (BA.2)", 'value': 5.2},
]
viral_strain_marks = {
    1: {'label': 'Wildtype', 'style': {'max-width': '50px'}},
    # 1.2: {'label': 'Cali-fornia', 'style': {'max-width': '50px'}},
    # 1.5: {'label': 'Alpha, Beta', 'style': {'max-width': '50px'}},
    # 2.001: {'label': 'Gamma', 'style': {'max-width': '50px'}},  # For some reason, 2.0 makes the label invisible
    2.5: {'label': 'Delta', 'style': {'max-width': '50px'}},
    4: {'label': 'Omicron BA.1', 'style': {'max-width': '50px'}},
    5.2: {'label': 'BA.2', 'style': {'max-width': '50px'}},
}

pim_header = "Percentage Immune: "
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "If an infected person enters..."
risk_prevalence_desc = "Given the prevalence of infection..."
risk_personal_desc = "To limit my personal risk..."
risk_options = [
    {'label': risk_conditional_desc, 'value': 'conditional'},
    {'label': risk_prevalence_desc, 'value': 'prevalence'},
    {'label': risk_personal_desc, 'value': 'personal'},
]
risk_personal_warning = html.Span([
    html.Span('''Warning: ''', style={'font-weight': 'bold'}),
    html.Span('''the selected risk mode (To limit my personal risk...) considers probability of 
transmission to a particular individual. It is thus far less restrictive and should not be used for establishing 
community safety guidelines.''')])

risk_mode_panel_header = "Risk Mode"
occupancy_panel_header = "Calculate Safe Occupancy"
main_panel_s1 = '''To limit COVID-19 transmission* after an infected person enters this space, 
there should be no more than: '''

main_panel_s1_b = html.Span([
    html.Span('''To limit COVID-19 transmission* in a population with an infection prevalence'''),
    html.Sup('''1'''),
    html.Span(''' of ''')
])
main_panel_s2_b = ''' per 100,000, this space should have no more than: '''

main_panel_s1_c = html.Span([
    html.Span('''To limit my chance of being infected by COVID-19 in a population with an infection prevalence'''),
    html.Sup('''1'''),
    html.Span(''' of ''')
])
main_panel_s2_c = ''' per 100,000, this space should have no more than: '''

units_hr = 'hours'
units_min = 'minutes'
units_days = 'days'
units_months = 'months'

units_hr_one = 'hour'
units_min_one = 'minute'
units_day_one = 'day'
units_month_one = 'month'

is_past_recovery_base_string = '{n_val} people for >{val:.0f} days,'
model_output_base_string = '{n_val} people for '
model_output_base_string_co2 = '{co2:.2f} ppm for '
nt_bridge_string = " people for "
tn_bridge_string = " for "

main_panel_six_ft_1 = "In contrast, the six-foot (or two-meter) rule would limit occupancy to "
main_panel_six_ft_2 = " which would violate the guideline* after "

six_ft_base_string = ' {} people'
six_ft_base_string_one = ' {} person'

graph_title = "Occupancy vs. Exposure Time"
graph_xtitle = "Maximum Exposure Time \u03C4 (hours)"
graph_ytitle = "Maximum Occupancy N"
transient_text = "Transient"
steady_state_text = "Steady-State"
co2_safe_trace_text = "Respiratory Safety Threshold"
guideline_trace_text = "Guideline"
background_co2_text = "Background CO\u2082: "
recommended_co2_text = "Recommended Limit"

graph_title_co2 = "Safe CO\u2082 Concentration (ppm) vs. Exposure Time"
graph_ytitle_co2 = "CO\u2082 Concentration (ppm)"

co2_title = "Calculate Safe CO\u2082 Concentration"
co2_param_desc = '''The guideline for the parameters chosen above is expressed here in terms of a CO\u2082 
concentration threshold.'''
co2_prev_input_1 = html.Span(["Prevalence", html.Sup('1'), html.Span(": ")])
co2_prev_input_2 = " per 100,000"
co2_atm_input_1 = background_co2_text
co2_atm_input_2 = " ppm"
co2_calc_1 = "For an exposure time of "
co2_calc_2 = " hours, the calculated safe time-averaged CO\u2082 concentration in this space is "
co2_calc_3 = "."
co2_calc_inv_1 = "For a CO\u2082 concentration of "
co2_calc_inv_2 = " ppm*, the guideline would be violated after "
co2_calc_inv_3 = "."
co2_base_string = '{:,.2f} ppm'

co2_safe_sent_1 = "This limit exceeds that for healthy respiratory activity, which is "
co2_safe_sent_2 = "."

# co2_safe_footer = html.Span(['''The respiratory safety threshold is interpolated based on ''',
#                              html.A(href=links.link_usda_co2,
#                                     children='''recommended limits from the USDA''',
#                                     target='_blank'),
#                              '''.'''])
co2_safe_footer = html.Span([html.Div('''CO\u2082 outputs are limited to a maximum of 2,000 ppm, the level 
considered safe for long-term exposure to carbon dioxide.'''),
                             html.Div([
                                 html.A(href=links.link_usda_co2,
                                        children='''USDA Respiratory Limits''',
                                        target='_blank'),
                                 html.Span([''', ''']),
                                 html.A(href=links.link_kane_co2,
                                        children='''Kane International Limits''',
                                        target='_blank'),
                                 html.Span(['''.'''])
                             ]),
                             html.Div([html.A(href=links.link_jimenez_co2,
                                              children='''*700 ppm is the conservative limit recommended by J. L. 
                                               Jimenez for COVID-19 safety.''',
                                              target='_blank')])
                             ])

main_airb_trans_only_disc = html.Div(["*The guideline restricts the probability of ",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="airborne transmissions",
                                                       target='_blank'), ),
                                      html.Span(''' per infected person to be less than the risk tolerance 
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*The guideline restricts the probability of ",
                                            html.Span(html.A(href=links.link_docs,
                                                             children="airborne transmissions",
                                                             target='_blank'), ),
                                            html.Span(''' per infected person to be less than the risk tolerance (10%)
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')

other_risk_modes_desc = html.Div('''Other risk scenarios are considered in Advanced Mode. Specifically, one may 
consider the prevalence of infection in the population, immunity acquired through vaccination or previous exposure, 
and the risk to a specific individual.''')

main_airb_trans_only_desc_b = html.Div(["*The guideline restricts the probability of one ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="airborne transmission",
                                                         target='_blank'), ),
                                        html.Span(''' per infected person to be less than the risk tolerance 
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["*The guideline restricts the probability of ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="airborne transmission",
                                                         target='_blank'), ),
                                        html.Span(''' to a particular individual to be less than the risk tolerance 
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')

airb_trans_only_disc = html.Div('''''', className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''To estimate your local prevalence and immunity, 
                                here are some helpful resources: '''),
                                # html.Span(html.A(href=links.link_jhu_dashboard,
                                #                  children="JHU COVID-19 Dashboard",
                                #                  target='_blank')),
                                # html.Span(''', '''),
                                html.Span(html.A(href=links.link_cdc_dashboard,
                                                 children="CDC COVID-19 Data Tracker",
                                                 target='_blank')),
                                html.Span(", "),
                                html.Span(html.A(href=links.link_jhu_data,
                                                 children="JHU Coronavirus Resource Center",
                                                 target='_blank')),
                                html.Span(", "),
                                html.A(children="US Immunity Estimates",
                                       href=links.link_cdc_immunity,
                                       target='_blank'),
                                html.Span(", "),
                                html.A(children="International Immunity Estimates",
                                       href=links.link_jhu_vaccine,
                                       target='_blank'),
                                ], className='airborne-text')

# Bottom panels text
n_input_text_1 = "If this room has "
n_max_base_string = ' {:.0f} people'
n_max_overflow_base_string = ' >{:.0f} people'
n_input_text_2 = " people, the guideline* would be violated after "
n_input_text_3 = "."

t_input_text_1 = "If people spend approximately "
t_input_text_2 = " hours here, the occupancy should be limited* to "
t_input_text_3 = "."

# About
about_header = "About"
about = html.Div([
    html.H6("About", style={'margin': '0'}),
    html.Div('''To mitigate the spread of COVID-19, official public health guidelines have recommended limits on: 
    person-to-person distance (6 feet / 2 meters), occupancy time (15 minutes), maximum occupancy (25 people), 
    or minimum ventilation (6 air changes per hour).'''),
    html.Br(),
    html.Div([html.Span('''There is growing '''),
              html.A(children="scientific evidence",
                     href=links.link_docs,
                     target='_blank'),
              html.Span(''' for airborne transmission of COVID-19, which occurs when 
    infectious aerosol droplets are exchanged by breathing shared indoor air. While public health organizations are 
    beginning to acknowledge airborne transmission, they have yet to provide a safety guideline that incorporates all 
    the relevant variables.''')]),
    html.Br(),
    html.Div([html.Span('''This app, developed by Kasim Khan in collaboration with Martin Z. Bazant and John W. M. Bush, 
    uses a '''),
              html.A(children="theoretical model",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' to calculate safe exposure times and occupancy levels for indoor spaces.  By adjusting 
    room specifications, ventilation and filtration rates, face-mask usage, respiratory activities, 
    and risk tolerance (in the other tabs), you can see how to mitigate indoor COVID-19 transmission in different 
    indoor spaces.''')]),
    html.Br(),
    html.Div(['''In Basic mode, you can calculate the limits on safe occupancy following the entrance of a single 
    infected person into an indoor space. In Advanced Mode, you can take into account additional factors, 
    including infection prevalence and population immunity. Advanced Mode also allows you to assess safe occupancy 
    based on average CO2 concentration, which is related to the concentration of infectious aerosols.''']),
    html.Br(),
    html.Div([html.Span('''The science behind the app is also taught in a free, self-paced massive, open online 
course (MOOC) on edX: '''),
              html.A(children="10.S95x Physics of COVID-19 Transmission",
                     href=links.link_mooc,
                     target='_blank')]),
])

# Room Specifications
room_header = "Room Specifications - Details"

floor_area_text = "Total floor area (sq. ft.): "
floor_area_text_metric = "Total floor area (m²): "
ceiling_height_text = "Average ceiling height (ft.): "
ceiling_height_text_metric = "Average ceiling height (m): "

ventilation_text = "Ventilation: "
vent_type_output_base = "{:.1f} "
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (outdoor ACH)"])
ventilation_text_adv = html.Span(["Ventilation (hr", html.Sup("-1"), ", outdoor ACH): "])
ventilation_text_exp = "Ventilation (hr-1, outdoor ACH): "
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

filtration_text = "Filtration System: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Filtration System (MERV): "
filter_types = [
    {'label': "None", 'value': 0},
    {'label': "Residential Window AC", 'value': 2},
    {'label': "Residential/Commercial/Industrial", 'value': 6},
    {'label': "Residential/Commercial/Hospital", 'value': 10},
    {'label': "Hospital & General Surgery", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_text = "Recirculation Rate: "
recirc_type_output_base = "{:.1f} "
recirc_type_output_units = html.Span(["hr", html.Sup("-1")])
recirc_text_adv = html.Span(["Recirculation Rate (hr", html.Sup("-1"), "): "])
recirc_text_exp = "Recirculation Rate (hr-1): "
recirc_types = [
    {'label': "None", 'value': 0},
    {'label': "Slow", 'value': 0.3},
    {'label': "Moderate", 'value': 1},
    {'label': "Fast", 'value': 10},
    {'label': "Airplane", 'value': 24},
    {'label': "Subway Car", 'value': 54},
]

humidity_text = "Relative Humidity: "
humidity_marks = {
    0.01: {'label': '1%: Very Dry', 'style': {'max-width': '25px'}},
    # 0.2: {'label': '20%: Airplane', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Dry'},
    0.6: {'label': '60%: Average'},
    0.99: {'label': '99%: Very Humid'},
}

need_more_ctrl_text = '''Need more control over your inputs? Switch to Advanced Mode using the dropdown at the top of 
                         the page.'''

human_header = "Human Behavior - Details"
# Human Behavior
exertion_text = "Breathing Rate: "
exertion_types = [
    {'label': "Resting", 'value': 0.49},
    {'label': "Standing", 'value': 0.54},
    {'label': "Singing", 'value': 1},
    {'label': "Light Exercise", 'value': 1.38},
    {'label': "Moderate Exercise", 'value': 2.35},
    {'label': "Heavy Exercise", 'value': 3.30},
]

breathing_text = "Respiratory Activity: "
expiratory_types = [
    {'label': "Breathing (light)", 'value': 1.1},
    {'label': "Breathing (normal)", 'value': 4.2},
    {'label': "Breathing (heavy)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Talking (whisper)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Talking (normal)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Talking (loud)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Singing", 'value': 970},
]

mask_type_text = "Mask Type/Efficiency: "
mask_type_marks = {
    0: {'label': "0% (none, face shield)", 'style': {'max-width': '75px'}},
    0.5: {'label': "50% (cotton, flannel)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (multilayer cotton, silk)", 'style': {'max-width': '75px'}},
    0.90: {'label': "90% (disposable surgical)", 'style': {'max-width': '75px'}},
    # 0.99: {'label': "99% (N95 resp-irator)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "None, Face Shield", 'value': 0},
    {'label': "Cotton, Flannel", 'value': 0.5},
    {'label': "Multilayer Cotton, Silk", 'value': 0.7},
    {'label': "Disposable Surgical", 'value': 0.9},
    {'label': "N95 Respirator", 'value': 0.99},
]

mask_fit_text = "Mask Fit/Compliance: "
mask_fit_marks = {
    0: {'label': '0%: None', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Poor'},
    0.95: {'label': '95%: Good'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Frequently Asked Questions"
other_io = "Other Parameters"

faq_top = html.Div([
    html.H6("Frequently Asked Questions"),
    html.H5("Why isn't 6 feet/2 meter spacing enough?"),
    html.Div([
        html.Div([html.Span('''6 feet (or 2 meter) spacing protects you from large drops ejected by an infected 
        person coughing, as do face masks; however, it doesn’t protect against '''),
                  html.A(children="airborne transmission",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' by infectious aerosols that are suspended in the air and mixed throughout a room. 
                  Indoors, people are no safer from airborne transmission at 60 feet than 6 feet. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Are there other modes of transmission?"),
    html.Div([
        html.Div([html.A(children="Airborne transmission",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' is thought to be dominant for COVID-19, but other modes are possible, such as `fomite’ 
                  transmission through direct contact with infectious residues on surfaces, `large-droplet' 
                  transmission via coughing or sneezing, and `short-range aerosol' transmission from the respiratory 
                  jet of an infected person over a prolonged period. While the latter two modes may be significant, 
                  they are largely eliminated when face masks or shields are worn; however, the risk of airborne 
                  transmission remains.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Can we really assume a well-mixed room?"),
    html.Div([
        html.Div([html.Span('''There are many contributors to mixing in indoor spaces, including buoyancy-driven 
        flows (from heaters, air conditioners or windows), forced convection from vents and fans, and human motion 
        and respiration. While there are exceptions, as discussed in the '''),
                  html.A(children="paper",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''', the assumption of well-mixedness is widely used in the theoretical modeling of 
                  airborne disease transmission.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Does the guideline hold for very large spaces?"),
    html.Div([
        html.Div([html.Span('''In concert halls, stadiums, or other large, ventilated spaces with large numbers of 
        people, the risk of airborne transmission is significant and properly captured by the guideline.  However, 
        when masks or face shields are not worn, there is an additional risk of short-range transmission through 
        respiratory jets, estimated in the '''),
                  html.A(children="paper",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Why does ceiling height matter?"),
    html.Div([
        '''Ceiling height influences the total room volume, which is required for estimating the concentration of 
        infectious aerosols (# of aerosols per unit volume). This concentration is needed to estimate the room’s 
        COVID-19 transmission risk.'''
    ], className='faq-answer'),
    html.Br(),
    html.H5("I know my ACH/MERV numbers. Where can I enter them?"),
    html.Div('''
        If you need more control over your inputs, switch to Advanced Mode using the dropdown at the top of
        the webpage.
    ''', className='faq-answer'),
    html.Br(),
    html.H5("Why do N95 Respirators have 99% efficiency?"),
    html.Div('''N95 respirators have at least 95% filtration efficiency at particle sizes of 0.3 μm, 10 times smaller 
    than the drop sizes in airborne COVID-19 transmission. For larger drops, N95 respirators are even more efficient, 
    approaching levels close to 100%.''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Are there any hidden parameters in Basic Mode?"),
    html.Div([html.Span('''All of the relevant physical parameters are detailed in the '''),
              html.A(children="paper",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''. In Basic Mode, the app assumes a default effective aerosol radius of 2 μm (at 60% 
              humidity) and a maximum viral deactivation rate of 0.6 /hr (at ~100% humidity), both of which increase 
              with relative humidity (RH). Estimates for the viral deactivation rate err on the conservative side of 
              slower deactivation.  The viral deactivation rate can be increased by ultraviolet radiation (UV-C) or 
              chemical disinfectants (e.g. hydrogen peroxide, ozone). The app also estimates the key disease 
              parameter, the infectiousness of exhaled air, C'''),
              html.Sub("q"),
              html.Span(''' (infection quanta per unit volume), from the specified 
              respiratory activity, using tabulated values in Figure 2 of the '''),
              html.A(children="paper",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''. You define these parameters yourself in Advanced Mode.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Effective Aerosol Radius (at RH = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Maximum Viral Deactivation Rate (at RH = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])
viral_deact_text_exp = "Maximum Viral Deactivation Rate (at RH = 100%), \u03BBvmax (/hr): "

pop_immunity_header = "Population Immunity: "
perc_immune_label = html.Span(["Percentage immune p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["Percentage infectious p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["Percentage vaccinated p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["Percentage previously infected p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["Percentage susceptible p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''The infectious percentage p''', html.Sub('i'), ''' in the population is calculated 
from the infectious 
prevalence entered in the other risk scenario tabs (Given the prevalence of infection…, To limit my personal risk…).  
The percentage immune p''', html.Sub('im'), ''' can be conservatively estimated from the vaccination percentage of the 
population plus the total case rate in the population, by neglecting the contribution from undetected cases. These 
two values are used to calculate the susceptible percentage p''', html.Sub('s'), '''. In Basic Mode and in the first 
risk mode (If an 
infected person enters…), this value is assumed to be 100%.''']),
                              html.Br(),
                              html.Div(['''Here are some helpful links to find p''', html.Sub('i'), ''' and p''',
                                        html.Sub('im'), ''': ''',
                                        html.Span(html.A(href=links.link_cdc_dashboard,
                                                         children="CDC COVID-19 Data Tracker",
                                                         target='_blank')),
                                        html.Span(", "),
                                        html.Span(html.A(href=links.link_jhu_data,
                                                         children="JHU Coronavirus Resource Center",
                                                         target='_blank')),
                                        html.Span(", "),
                                        html.A(children="US Immunity Estimates",
                                               href=links.link_cdc_immunity,
                                               target='_blank'),
                                        html.Span(", "),
                                        html.A(children="International Immunity Estimates",
                                               href=links.link_jhu_vaccine,
                                               target='_blank'),
                                        ])
                              ])

values_interest_header = "Calculated Values of Interest: "
values_interest_desc = html.Div([
    html.H5("What exactly is this app calculating?"),
    html.Div([
        html.Div([html.Span('''The app calculates the maximum allowable cumulative exposure time, the product of room 
        occupancy and time, in an indoor space. The spread of COVID-19 is limited by requiring that the expected 
        number of transmissions per infected individual, the “indoor reproductive number", be less than the chosen 
        risk tolerance. The app also calculates related quantities, defined in the '''),
                  html.A(children="paper",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''', that may be of interest:''')]),
    ], className='faq-answer'),
])
relative_sus_label = html.Span(["Relative susceptibility s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["Outdoor air fraction Z", html.Sub('p'), ": "])
outdoor_air_frac_label_exp = "Outdoor air fraction Zp: "
aerosol_eff_label = html.Span(["Aerosol filtration efficiency p", html.Sub('f'), ": "])
aerosol_eff_label_exp = "Aerosol filtration efficiency pf: "
breathing_rate_label = html.Span(["Breathing flow rate Q", html.Sub('b'), ": "])
breathing_rate_label_exp = "Breathing flow rate Qb (m3/hr): "
cq_label = html.Span(["Infectiousness of exhaled air C", html.Sub('q'), ": "])
cq_label_exp = "Infectiousness of exhaled air Cq (quanta/m3): "
mask_pass_prob_label = html.Span(["Mask passage probability p", html.Sub('m'), ": "])
mask_pass_prob_label_exp = "Mask passage probability pm: "
room_vol_label = html.Span(["Room volume V: "])
vent_rate_Label = html.Span(["Ventilation (outdoor) flow rate Q: "])
recirc_rate_label = html.Span(["Return (recirculation) flow rate Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Air filtration rate (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Humidity-adjusted aerosol radius r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Humidity-adjusted viral deactivation rate \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Effective aerosol settling speed v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Concentration relaxation rate \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Airborne transmission rate \u03B2\u2090: "])

graph_output_header = "Graph Output: "
faq_graphs_text = html.Div([
    html.H5("Graph Output: "),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Does this model account for the prevalence of infection in the local population?"),
    html.Div(['''The influence of the prevalence of infection in the local population may be considered in Advanced 
    Mode. There, in the Other Parameters tab, one may also assess the influence of immunity in the population, 
    as may arise through vaccination or previous infection.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("More Questions?"),
    html.Div([html.Span('''For more detailed explanations and references, see "'''),
              html.A(children="Beyond 6 Feet",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''" and other links posted at the top of the webpage.''')]),
])

footer = html.Div([
    html.Div([html.Span('''The COVID-19 Indoor Safety Guideline is an evolving tool intended to familiarize the 
    interested user with the factors influencing the risk of indoor airborne transmission of COVID-19, and to assist 
    in the quantitative assessment of risk in various settings. We note that uncertainty in and intrinsic variability 
    of model parameters may lead to errors as large as an order of magnitude, which may be compensated for by 
    choosing a sufficiently small risk tolerance. Our guideline does not take into account short-range transmission 
    through respiratory jets, which may substantially elevate risk when face masks are not being worn, in a manner 
    discussed in the '''),
              html.A(children="accompanying manuscript",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' (Bazant & Bush, 2020). Use of the COVID-19 Indoor Safety Guideline is the sole 
              responsibility of the user. It is being made available without guarantee or warranty of any kind. The 
              authors do not accept any liability from its use.''')]),
    html.Br(),
    html.Div("Special thanks to: ")
], className='footer-small-text')
