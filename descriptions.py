import dash_html_components as html

"""
descriptions.py contains all text-heavy descriptions used throughout the app (Basic, Advanced Mode).

"""

error_list = {
    "floor_area": "Error: floor area cannot be empty.",
    "ceiling_height": "Error: ceiling height cannot be empty.",
    "recirc_rate": "Error: recirculation rate cannot be empty.",
    "aerosol_radius": "Error: aerosol radius cannot be empty.",
    "viral_deact_rate": "Error: viral deactivation rate cannot be empty.",
    "n_max_input": "Error: number of people cannot be less than 2.",
    "exp_time_input": "Error: exposure time must be greater than 0.",
    "air_exchange_rate": "Error: Ventilation Rate (ACH) must be greater than 0.",
    "merv": "Error: Filtration System (MERV) cannot be empty."
}

# Header
header = html.Div([
    html.H1(children='MIT COVID-19 Indoor Safety Guideline'),
    html.Div([
        html.Div([html.Span(html.A(href="https://www.linkedin.com/in/kasim-k-a92620b1/",
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href="https://www.mit.edu/~bazant/",
                                   children="Martin Z. Bazant",
                                   target='_blank')),
                  ", and ",
                  html.Span(html.A(href="https://math.mit.edu/~bush/",
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ""]),
        html.Div(children='''
                            medRxiv preprint (2020):
                            "Beyond Six Feet: A Guideline to Limit Indoor Airborne Transmission of COVID-19"
                        '''),
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
    ], style={'font-size': '13px'})
])

# Menu dropdowns
language_dd = "Language: "
units_dd = "Units: "
mode_dd = "Mode: "

# Unit systems
unit_settings = [
    {'label': "British", 'value': "british"},
    {'label': "Metric", 'value': "metric"},
]

# Modes
app_modes = [
    {'label': "Basic", 'value': "basic"},
    {'label': "Advanced", 'value': "advanced"},
]

# Tabs
about_header = "About"
room_header = "Room Specifications"
human_header = "Human Behavior"
faq_header = "Frequently Asked Questions"
other_io = "Other Inputs & Outputs"

# About
about = html.Div([
    html.H6("About", style={'margin': '0'}),
    html.Div('''To mitigate the spread of COVID-19, official guidelines recommend social 
    distancing by setting limits on: distance (1-2 meters in Europe), time (15 minutes in the U.S.), or maximum 
    occupancy (25 people in Massachusetts). However, public health organizations have been slow to acknowledge the 
    role of airborne transmission as revealed by increasing scientific evidence.'''),
    html.Br(),
    html.Div('''Airborne transmission occurs via infectious aerosols released by 
    breathing, speaking, or coughing, and may be mixed throughout an indoor space by ambient air currents. Indoor 
    COVID-19 transmission risk is therefore affected by multiple factors like exposure time, ventilation, filtration, 
    and masks.'''),
    html.Br(),
    html.Div('''This app, developed by Kasim Khan in collaboration with MIT professors Martin Z. Bazant and John W. 
    M. Bush, uses a mathematical model by Bazant & Bush to calculate safe exposure times for indoor spaces at varying 
    occupancy levels.'''),
    html.Br(),
    html.Div('''Adjust room size, ventilation/filtration, human activity, and your risk tolerance in the other 
    tabs and see how different spaces handle indoor COVID-19 transmission.'''),
])

# Room Specifications
floor_area_text = "Total floor area (sq. ft.): "
floor_area_text_metric = "Total floor area (m²): "

ceiling_height_text = "Average ceiling height (ft.): "
ceiling_height_text_metric = "Average ceiling height (m): "

ventilation_text = "Ventilation System: "
ventilation_text_adv = "Ventilation System (ACH): "

filtration_text = "Filtration System: "
filtration_text_adv = "Filtration System (MERV): "

recirc_text = "Recirculation Rate: "
recirc_text_adv = "Recirculation Rate (recirculation ACH): "

need_more_ctrl_text = '''Need more control over your inputs? Switch to Advanced Mode using the dropdown at the top of 
                         the page!'''

# Human Behavior
exertion_text = "Exertion Level: "

breathing_text = "Respiratory Activity: "

mask_type_text = "Mask Type/Efficiency: "

mask_fit_text = "Mask Fit/Compliance: "

risk_tolerance_text = "Risk Tolerance: "

# FAQ/Other Inputs and Outputs
assumptions_layout = html.Div([
    html.H5("I still have questions!"),
    html.Div('''
        If you'd like to see more references and/or further 
        explanation, see the links
        posted at the top of the webpage. You can also consider other features of the model, detailed below:
    ''', className='faq-answer'),
    html.Div([
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
               is discussed extensively in the main text of Bazant & Bush. Using all of the
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
               relaxation time \u03BBc\u03C4 >> 1. The results reported in this
               app are derived from the transient bound. 
            '''),
            html.Div('''
               - The viral deactivation rate \u03BBv is the rate at which
               the aerosol-borne virus loses infectiousness in aerosol form. For SARS-CoV-2,
               this is estimated to lie in the range of 0 to 0.63/hr. This
               can be increased by ultraviolet radiation (UV-C) or chemical
               disinfectants (e.g. hydrogen peroxide, ozone).
            '''),
            html.Div('''- The mean respiratory aerosol droplet size r\u0305 is set by the drop-size distribution,
               and varies between different people
               and types of respiration. This mean size can also affect the infectivity
               of the aerosol droplets. However, a typical range for the most
               common and most infectious droplets is 2-3 \u03bcm, which is
               roughly consistent with the standard definition of aerosol
               droplets in the literature (r\u0305 < 5 \u03bcm).
            '''),
            html.Div('''- MERV filtration efficiencies estimated using ASHRAE Standard 52.2-2017 Minimum Efficiency 
                Reporting Value (MERV)'''),
        ], style={'padding-left': '10px', 'font-size': '13px'}),
        html.Br(),
    ], className='faq-answer')
])

faq_top = html.Div([
    html.H6("Frequently Asked Questions"),
    html.H5("Why isn't 6 feet/2 meter spacing enough?"),
    html.Div([
        html.Div('''6 feet/2 meter spacing doesn’t take into account airborne transmission! Although COVID-19 is 
        transmitted via droplets and close-contact interactions, it can also be transmitted by infectious aerosols that 
        are suspended in the air and can be mixed throughout a room. Whether people stand 6 feet apart or 20 feet apart, 
        airborne transmission presents the same risk either way.'''),
        html.Div('''On the other hand, 6 feet can be too stringent a guideline. If a room is equipped with a 
        state-of-the-art ventilation and filtration system (as most subway cars and airplanes are, for example), 
        aerosols are generally filtered out before they can get a chance to infect others. In any case, masks should 
        still be worn to mitigate short-range droplet transmission.'''),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Why does ceiling height matter?"),
    html.Div([
        '''Ceiling height allows the app to calculate the total room volume, which is required for estimating the 
        concentration of infectious aerosols (# of aerosols per unit volume). This concentration is needed to 
        estimate the room’s COVID-19 transmission risk. '''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Can you really assume a well-mixed room? What about large indoor spaces like malls and concert halls?"),

    html.Br(),
    html.H5("I know my ACH/MERV numbers. Where can I enter them?"),
    html.Div('''
        If you need more control over your inputs, switch to Advanced Mode using the dropdown at the top of
        the webpage!
    ''', className='faq-answer'),
    html.Br(),
    html.H5("What -doesn't- this model account for?"),
    html.Div('''This guideline only accounts for airborne transmission. Other modes of transmission may also be 
    significant. For example, `large-droplet' transmission may occur if a susceptible person is within coughing 
    distance of an infected person, and `short-range aerosol' transmission may arise if a susceptible person is 
    exposed to the respiratory jet of an infected person for a prolonged period. When face masks are worn, 
    both of these modes of transmission are largely eliminated; however, the risk of airborne transmission persists. 
    ''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Does the model assume any other parameters?"),
    html.Div('''The model assumes a well-mixed room, but all parameters are based on scientific studies of COVID-19 
    and aerosol transmission. Based on current scientific literature, the model assumes a minimum aerosol radius (
    i.e. at ~0% humidity) of 1-3 μm and a maximum viral deactivation rate (i.e. at ~100% humidity) of 0.6 /hr, 
    which can be reduced by ultraviolet radiation (UV-C) or chemical disinfectants (H₂O₂, O₃). Aerosol radius scales 
    inversely with relative humidity. Viral deactivation rate scales directly with relative humidity as has been 
    established for influenza A and errs on the conservative side of slower deactivation. These can be 
    modified below:''', className='faq-answer'),
])
aerosol_radius_text = "Minimum Aerosol Radius r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Maximum Viral Deactivation Rate \u03BB", html.Sub('v'), " (/hr): "])

values_interest_header = "Calculated Values of Interest: "
values_interest_desc = html.Div([
    html.H5("What is this model calculating, exactly?"),
    html.Div('''
      See below for a list of parameter values used in calculating
      the output you see.
  ''', className='faq-answer'),
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
sett_speed_label = html.Span(["Effective aerosol settling speed v\u209B(r\u0305): "])
conc_relax_rate_label = html.Span(["Concentration relaxation rate \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Airborne transmission rate \u03B2\u2090: "])

graph_output_header = "Graph Output: "
faq_graphs_text = html.Div([
    html.H5("I like graphs. Do you have any graphs?"),
    html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Does this model assume a certain infection rate among the population?"),
    html.Div([
        html.Div(['''No - it's not needed! Here's why:''']),
        html.Div(['''The model takes each one of your inputs in the other tabs and calculates what we call the Indoor 
        Reproductive Number, R''', html.Sub("in"), '''. This is the indoor analogue of the basic reproduction number 
        Rₒ. Just as pandemics are controlled when Rₒ < 1, airborne disease transmission in indoor spaces is 
        controlled when R''', html.Sub("in"), ''' < 1. For 
        example, values of R''', html.Sub("in"), ''' = 0.5, R''', html.Sub("in"), ''' = 0.1, R''', html.Sub("in"), '''= 
        0.01 will all serve to reduce airborne transmission to increasing degrees. You, the user, are effectively 
        prescribing R''', html.Sub("in"), ''' by choosing the Risk Tolerance, 
        since Risk Tolerance = R''', html.Sub("in"), '''. Lower Risk Tolerance means lower R''', html.Sub("in"), ''', 
        which means less airborne transmission. The model uses the room specifications, human behavior inputs and 
        number of occupants to calculate the exposure time that gives an Rin set by your Risk Tolerance (these are 
        the outputs displayed in large red text). '''],
                 style={'padding-left': '10px', 'font-size': '13px'}),
    ], className='faq-answer'),
])

risk_tol_desc = html.Div('''More vulnerable populations such as the elderly or those with preexisting medical 
conditions require a lower risk tolerance (~0.01). A higher risk tolerance will mean more expected 
transmissions during the expected occupancy period (see FAQ for details).''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})

# Main Panel Text
curr_room_header = "Current Room: "
main_panel_s1 = "Based on this model, it should be safe* for this room to have: "
main_panel_six_ft_1 = "In comparison, current six feet distancing guidelines recommend no more than "
main_panel_six_ft_2 = " in this room."

main_airb_trans_only_disc = html.Div(["*based on consideration of airborne transmission only (",
                                      html.Span(html.A(href='https://www.nature.com/articles/d41586-020-02058-1',
                                                       children="What is airborne transmission?",
                                                       target='_blank'), ),
                                      html.Span(").")])

# Bottom panels text
n_input_text_1 = "If this room has "
n_input_text_2 = " people, its occupants should be safe for "
n_input_text_3 = "."

t_input_text_1 = "If people spend approximately "
t_input_text_2 = " hours here, the occupancy should be limited to "
t_input_text_3 = "."

airb_trans_only_disc = html.Div('''based on consideration of airborne transmission only.''', className='airborne-text')


