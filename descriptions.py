import dash_html_components as html
import dash_core_components as dcc

"""
descriptions.py contains all text-heavy descriptions used throughout the app (Basic, Advanced Mode).

"""

header = html.Div(className='grid-header', children=[
    html.Div(className='card-header', children=[
        html.H1(children='MIT COVID-19 Indoor Safety Guideline'),
        html.Div([
            html.Div(children='''
                            Kasim Khan (2020)
                        '''),
            html.Div(children='''
                            Martin Z. Bazant and John W. M. Bush, medRxiv preprint (2020):
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
                       children='''
                            https://github.com/kawesomekhan/covid-indoor
                        ''', target='_blank'),
            ]),

        ], style={'font-size': '13px'}),
    ]),
    html.Div(className='card-header', children=[
        html.Div(id='header-left', children=[

        ])
    ]),

])

about = html.Div([
    html.H6("About"),
    html.Div('''
        COVID-19 has been spreading in homes, restaurants, bars, classrooms, and other
        enclosed spaces via tiny, infective aerosol droplets suspended in the air.
        To mitigate this spread, official public health guidelines have taken the form 
        of minimum social distancing rules (6 feet in the U.S.) or maximum occupancy 
        (25 people in Massachusetts). 
    '''),
    html.Br(),
    html.Div('''
        However, public health has been slow to catch up with rapidly advancing science.
        Naturally, the risk of COVID-19 transmission would not only depend on physical 
        distance, but also on factors such as exposure time, mask usage, and ventilation
        systems, among other factors.
    '''),
    html.Br(),
    html.Div('''
        This app uses a mathematical model, developed by MIT professors Martin Z. Bazant 
        and John Bush, to improve upon
        current distancing guidelines by providing a more accurate description of
        indoor COVID-19 transmission risk.
    '''),
    html.Br(),
    html.Div('''
        Adjust parameters in the other tabs and see how different spaces handle
        indoor COVID-19 transmission.
    '''),
])

assumptions_layout = html.Div([
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
           is discussed extensively in the main text. Using all of the
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
           relaxation time \u03BBc\u03C4 >> 1. Results reported in this
           app are derived from the transient bound. 
        '''),
        html.Div('''
           - The viral deactivation rate \u03BBv is the rate at which
           the virus loses infectiousness in aerosol form. For SARS-CoV-2,
           this is estimated to lie in the range of 0 to 0.63/hr. This
           can be increased by ultraviolet radiation (UV-C) or chemical
           disinfectants (e.g. hydrogen peroxide, ozone).
        '''),
        html.Div('''- The mean respiratory aerosol droplet size r\u0305
           exists in a distribution of sizes, dependent on different people
           and types of respiration. This size can also affect infectivity
           of the aerosol droplets. However, a typical range for the most
           common and most infectious droplets is 2-3 \u03bcm, which is
           roughly consistent with the standard definition of aerosol
           droplets in the literature (r\u0305 < 5 \u03bcm).
        '''),
        html.Div('''- Mask filtration efficiencies are taken from a study in ACS Nano 
            by Konda, et al: "Aerosol Filtration Efficiency of Common Fabrics Used in Respiratory Cloth Masks"
        '''),
        html.Div('''- MERV filtration efficiencies estimated using https://www.lakeair.com/merv-rating-explanation/'''),
        html.Div('''- This app uses the transient form of the guideline.'''),
    ], style={'padding-left': '10px', 'font-size': '13px'}),
    html.Br(),
], className='faq-answer')

faq_top = html.Div([
    html.H6("Frequently Asked Questions"),
    html.H5("I know my ACH/MERV numbers. Where can I enter them?"),
    html.Div('''
        If you need more control over your inputs, check out Advanced Mode by clicking the button at the bottom of
        the webpage!
    ''', className='faq-answer'),
    html.Br(),
    html.H5("What -doesn't- this model account for?"),
    html.Div('''
            This guideline does not account for transmission methods other than airborne transmission, like 
            droplet transmission. This guideline also does not explicitly account for the possibility 
               of short-range aerosol transmission in respiratory jets.
               Such effects, which can lead to large fluctuations in droplet 
               concentrations around their mean values, especially when 
               masks are not worn, can be partially addressed by choosing 
               a sufficiently small risk tolerance in this guideline,
               and will depend on the details of airflow and human behavior 
               in the specific indoor space.
    ''', className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Does this model assume a certain infection rate among the population?"),
    html.Div([
        html.Div(['''No - it's not needed! Here's why:''']),
        html.Div(['''The model takes each one of your inputs in the other tabs and 
        calculates what we call the Indoor Reproductive Number, R''', html.Sub('in'), '''. This is the indoor analogue of 
        the basic
        reproduction number R\u2092. Much like how pandemics are controlled when R\u2092 < 1, airborne disease transmission 
        within indoor spaces is controlled when R''', html.Sub('in'), ''' < 1. For example, 
        values of R''', html.Sub('in'), ''' = 0.5, R''', html.Sub('in'), ''' = 0.1, R''', html.Sub('in'), ''' = 0.01 will 
        all help reduce airborne transmission to varying degrees. In fact, you, the user, are limiting 
        R''', html.Sub('in'), ''' in this way, 
        by modifying the Risk Tolerance, where R''', html.Sub('in'), ''' = Risk Tolerance! 
        A lower Risk Tolerance value forces a lower R''', html.Sub('in'), ''' 
        value, which means less airborne transmission. The model uses all the room specification and human behavior 
        inputs to calculate allowed exposure times for a range of occupancy numbers (2 people, 3 people, 4 people, 
        5 people, 10 people, etc.) that give an R''', html.Sub('in'), ''' equal to your 
        Risk Tolerance (these are the outputs displayed in 
        large red text). The physical and epidemiological equations that govern this calculation do not require an 
        assumed infection rate among the local population - it's all about how easily aerosols (specifically, infectious 
        COVID-19 aerosols) are transmitted throughout the room.'''], style={'padding-left': '10px', 'font-size': '13px'}),
    ], className='faq-answer'),
])

risk_tol_desc = html.Div('''
   A higher risk tolerance will mean more expected 
   transmissions during the expected occupancy period
   (see FAQ for details). More 
   vulnerable populations such as the elderly or those 
   with preexisting medical conditions will generally 
   require a lower risk tolerance.
''', style={'font-size': '13px', 'margin-left': '20px'})

