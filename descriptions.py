import dash_html_components as html

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions: English

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"
link_nature = "https://www.nature.com/articles/d41586-020-02058-1"
link_mooc = "https://www.edx.org/course/physics-of-covid-19-transmission?utm_campaign=mitx&utm_medium=partner-marketing&utm_source=affiliate&utm_content=10.s95x-app"

# Header
header = html.Div([
    html.H1(children='COVID-19 Indoor Safety Guideline'),
    html.Div([
        html.Div([html.Span(html.A(href="https://www.linkedin.com/in/kasim-k-a92620b1/",
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href="https://math.mit.edu/~bush/",
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ", and ",
                  html.Span(html.A(href="https://www.mit.edu/~bazant/",
                                   children="Martin Z. Bazant",
                                   target='_blank')),
                  ""]),
        html.Div([html.Span(["Beyond Six Feet: A Guideline to Limit Indoor Airborne Transmission of COVID-19 ("]),
                  html.Span(html.A(href=link_paper,
                                   target='_blank',
                                   children='''Bazant & Bush, 2020''')),
                  html.Span(")")]),
        html.Div([
            html.A(href='http://web.mit.edu/bazant/www/COVID-19/',
                   children='''
                            http://web.mit.edu/bazant/www/COVID-19/
                        ''', target='_blank'),
        ]),
        html.Div([
            html.A(href='https://github.com/kawesomekhan/covid-indoor',
                   children=[
                       "https://github.com/kawesomekhan/covid-indoor"
                   ],
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
    "prevalence": "Error: Prevalence must be greater than 0% and less than 5%."
}

# Main Panel Text
curr_room_header = "Current Room Specifications: "
presets = [
    {'label': "Custom", 'value': 'custom'},
    {'label': "Classroom Lecture", 'value': 'classroom'},
    {'label': "Suburban House", 'value': 'house'},
    {'label': "Church", 'value': 'church'},
    {'label': "Restaurant", 'value': 'restaurant'},
    {'label': "Office/Workplace", 'value': 'office'},
    {'label': "New York City Subway Car", 'value': 'subway'},
    {'label': "Boeing 737", 'value': 'airplane'},
]

curr_human_header = "Current Human Behavior: "
presets_human = [
    {'label': "Custom", 'value': 'custom'},
    {'label': "Masks, Standing & Talking", 'value': 'masks-2'},
    {'label': "Masks, Sitting & Talking", 'value': 'masks-3'},
    {'label': "Masks, Sitting & Whispering", 'value': 'masks-1'},
    {'label': "No Masks, Standing & Talking", 'value': 'no-masks-2'},
    {'label': "No Masks, Sitting & Talking", 'value': 'no-masks-1'},
]

curr_risk_header = "Current Risk Tolerance: "
presets_risk = [
    {'label': "Very Low (vulnerable populations)", 'value': 0.01},
    {'label': "Low", 'value': 0.1},
    {'label': "Moderate (less vulnerable populations)", 'value': 0.3},
]

main_panel_s1 = '''To limit COVID-19 transmission* after an infected person enters this space, 
there should be no more than: '''

main_panel_s1_b = '''To limit COVID-19 transmission* in a population where '''
main_panel_s2_b = '''% are infected, this space should have no more than: '''

main_panel_s1_c = '''To limit my chance of being infected by COVID-19 in a space where '''
main_panel_s2_c = '''% are infected, this space should have no more than: '''

units_hr = 'hours'
units_min = 'minutes'
units_days = 'days'

units_hr_one = 'hour'
units_min_one = 'minute'
units_day_one = 'day'

is_past_recovery_base_string = '{n_val} people for >{val:.0f} days,'
model_output_base_string = '{n_val} people for '

main_panel_six_ft_1 = "In contrast, the six-foot or two-meter distancing guideline would limit occupancy to "
main_panel_six_ft_2 = " which becomes unsafe after "

six_ft_base_string = ' {} people'
six_ft_base_string_one = ' {} person'

graph_title = "Occupancy vs. Exposure Time"
graph_xtitle = "Maximum Exposure Time \u03C4 (hours)"
graph_ytitle = "Maximum Occupancy N"
transient_text = "Transient"
steady_state_text = "Steady-State"

main_airb_trans_only_disc = html.Div(["*The guideline restricts the probability of ",
                                      html.Span(html.A(href=link_docs,
                                                       children="airborne transmissions",
                                                       target='_blank'), ),
                                      html.Span(''' per infected person to be less than the risk tolerance 
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')
main_airb_trans_only_desc_b = html.Div(["*The guideline restricts the probability of one ",
                                      html.Span(html.A(href=link_docs,
                                                       children="airborne transmission",
                                                       target='_blank'), ),
                                      html.Span(''' per infected person to be less than the risk tolerance 
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["*The guideline restricts the probability of ",
                                      html.Span(html.A(href=link_docs,
                                                       children="airborne transmission",
                                                       target='_blank'), ),
                                      html.Span(''' to a particular individual to be less than the risk tolerance 
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')

airb_trans_only_disc = html.Div('''based on consideration of airborne transmission only.''', className='airborne-text')

# Bottom panels text
n_input_text_1 = "If this room has "
n_max_base_string = ' {:.0f} people'
n_max_overflow_base_string = ' >{:.0f} people'
n_input_text_2 = " people, its occupants will become unsafe after "
n_input_text_3 = "."

t_input_text_1 = "If people spend approximately "
t_input_text_2 = " hours here, the occupancy should be limited to "
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
                     href=link_docs,
                     target='_blank'),
              html.Span(''' for airborne transmission of COVID-19, which occurs when 
    infectious aerosol droplets are exchanged by breathing shared indoor air. While public health organizations are 
    beginning to acknowledge airborne transmission, they have yet to provide a safety guideline that incorporates all 
    the relevant variables.''')]),
    html.Br(),
    html.Div([html.Span('''This app, developed by Kasim Khan in collaboration with Martin Z. Bazant and John W. M. Bush, 
    uses a '''),
              html.A(children="theoretical model",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' to calculate safe exposure times and occupancy levels for indoor spaces.  By adjusting 
    room specifications, ventilation and filtration rates, face-mask usage, respiratory activities, 
    and risk tolerance (in the other tabs), you can see how to mitigate indoor COVID-19 transmission in different 
    indoor spaces.''')]),
    html.Br(),
    html.Div([html.Span('''The science behind the app is also taught in a free, self-paced massive, open online 
    course (MOOC) on edX: '''),
              html.A(children="10.S95x Physics of COVID-19 Transmission",
                     href=link_mooc,
                     target='_blank')])
])

# Room Specifications
room_header = "Room Specifications"

floor_area_text = "Total floor area (sq. ft.): "
floor_area_text_metric = "Total floor area (m²): "
ceiling_height_text = "Average ceiling height (ft.): "
ceiling_height_text_metric = "Average ceiling height (m): "

ventilation_text = "Ventilation System: "
vent_type_output_base = "{:.0f} ACH"
ventilation_text_adv = "Ventilation System (ACH): "
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
recirc_type_output_base = "{:.1f} recirculation ACH"
recirc_text_adv = "Recirculation Rate (recirculation ACH): "
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
    0: {'label': '0%: Very Dry', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: Airplane', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Dry'},
    0.6: {'label': '60%: Average'},
    0.99: {'label': '99%: Very Humid'},
}

need_more_ctrl_text = '''Need more control over your inputs? Switch to Advanced Mode using the dropdown at the top of 
                         the page.'''

human_header = "Human Behavior"
# Human Behavior
exertion_text = "Exertion Level: "
exertion_types = [
    {'label': "Resting", 'value': 0.49},
    {'label': "Standing", 'value': 0.54},
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
    0: {'label': "0% (none, face shield)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (cotton, flannel)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (multilayer cotton, silk)", 'style': {'max-width': '50px'}},
    0.90: {'label': "90% (dispos-able surgical)", 'style': {'max-width': '50px'}},
    0.99: {'label': "99% (N95 resp-irator)", 'style': {'max-width': '50px'}},
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

risk_tolerance_text = "Risk Tolerance: "
risk_tol_desc = html.Div('''More vulnerable populations such as the elderly or those with preexisting medical 
conditions require a lower risk tolerance (~0.01). A higher risk tolerance will mean more expected 
transmissions during the expected occupancy period (see FAQ for details).''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})
risk_tol_marks = {
    0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Safe', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Unsafe'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Frequently Asked Questions"
other_io = "Other Inputs & Outputs"

faq_top = html.Div([
    html.H6("Frequently Asked Questions"),
    html.H5("Why isn't 6 feet/2 meter spacing enough?"),
    html.Div([
        html.Div([html.Span('''6 feet/2 meter spacing protects you from large drops ejected by an infected person coughing, 
        as do face masks; however, it doesn’t protect against '''),
                  html.A(children="airborne transmission",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' by infectious aerosols that are 
        suspended in the air and can be mixed throughout a room. Indoors, people are no safer from airborne 
        transmission at 60 feet than 6 feet. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Are there other modes of transmission?"),
    html.Div([
        html.Div([html.A(children="Airborne transmission",
                         href=link_docs,
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
                         href=link_paper,
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
                         href=link_paper,
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
    html.Div('''
    N95 respirators have at least 95% efficiency at particle sizes of 0.3 μm, 10 times smaller than the particles 
    considered in COVID-19 transmission models. At larger particle sizes, N95 respirators become much more
    efficient than 95%, approaching levels close to 100%. ''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Are there any hidden parameters in Basic Mode?"),
    html.Div([html.Span('''All of the relevant physical parameters are detailed in the '''),
              html.A(children="paper",
                     href=link_paper,
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
                     href=link_paper,
                     target='_blank'),
              html.Span('''. You define these parameters yourself in Advanced Mode.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Effective Aerosol Radius (at RH = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Maximum Viral Deactivation Rate (at RH = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

values_interest_header = "Calculated Values of Interest: "
values_interest_desc = html.Div([
    html.H5("What exactly is this app calculating?"),
    html.Div([
        html.Div([html.Span('''The app calculates the maximum allowable cumulative exposure time, 
        the product of room occupancy and time, in an indoor space. The spread of COVID-19 is limited by requiring that 
        the expected number of transmissions per infected individual, the “indoor reproductive number", be less than
        the chosen risk tolerance.
        The app also calculates related quantities, defined in the '''),
                  html.A(children="paper",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', that may be of interest:''')]),
    ], className='faq-answer'),
])
outdoor_air_frac_label = html.Span(["Outdoor air fraction Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Aerosol filtration efficiency p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Breathing flow rate Q", html.Sub('b'), ": "])
cq_label = html.Span(["Infectiousness of exhaled air C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Mask passage probability p", html.Sub('m'), ": "])
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
    html.Div(['''No. To limit the spread of COVID-19, our guideline bounds the expected number of transmissions per 
    infected person, or indoor reproductive number.  To account for the prevalence of infection in the population, 
    the tolerance should be divided by the expected number of infected persons, specifically the product of the 
    prevalence and the occupancy. When the expected number of infected persons in the room approaches zero, 
    the cumulative-exposure-time limit increases proportionally. 
    Consideration of the prevalence of infection may be treated in the Advanced Mode in the near future.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("More Questions?"),
    html.Div([html.Span('''For more detailed explanations and references, see "'''),
              html.A(children="Beyond 6 Feet",
                     href=link_paper,
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
                     href=link_paper,
                     target='_blank'),
              html.Span(''' (Bazant & Bush, 2020). Use of the COVID-19 Indoor Safety Guideline is the sole 
              responsibility of the user. It is being made available without guarantee or warranty of any kind. The 
              authors do not accept any liability from its use.''')]),
    html.Br(),
    html.Div("Special thanks to: ")
], className='footer-small-text')
