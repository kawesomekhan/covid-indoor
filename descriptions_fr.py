import dash_html_components as html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions_fr: French

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"
link_mooc = "https://www.edx.org/course/physics-of-covid-19-transmission?utm_campaign=mitx&utm_medium=partner-marketing&utm_source=affiliate&utm_content=10.s95x-app"

vent_type_output_base = "{:.0f} ACH"
filt_type_output_base = "MERV {:.0f}"
recirc_type_output_base = "{:.1f} ACH"

# Default dropdown options shared between basic mode and advanced mode
humidity_marks = {
    0.01: {'label': '1%: Très sec', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: Avion', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Sec'},
    0.6: {'label': '60%: Moyen'},
    0.99: {'label': '99%: Très humide'},
}

exertion_types = [
    {'label': "Repos", 'value': 0.49},
    {'label': "Station debout", 'value': 0.54},
    {'label': "Exercice léger", 'value': 1.38},
    {'label': "Exercice modéré", 'value': 2.35},
    {'label': "Exercice intense", 'value': 3.30},
]

expiratory_types = [
    {'label': "Respiration lente", 'value': 1.1},
    {'label': "Respiration normale", 'value': 4.2},
    {'label': "Respiration forte", 'value': 8.8},
    {'label': "Respiration rapide et profonde", 'value': 8.5},
    {'label': "Chuchoter", 'value': 29},
    {'label': "Compter à voix basse", 'value': 37},
    {'label': "Dialoguer, voix normale ", 'value': 72},
    {'label': "Compter à haute voix", 'value': 72},
    {'label': "Crier", 'value': 142},
    {'label': "Fredonnement (murmurer 'aah')", 'value': 103},
    {'label': "Chant", 'value': 970},
]

mask_type_marks = {
    0: {'label': "0% (pas de masque)", 'style': {'max-width': '75px'}},
    0.5: {'label': "50% (coton, flanelle)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (coton multicouches, soie)", 'style': {'max-width': '75px'}},
    0.90: {'label': "90% (chirurgical à usage unique)", 'style': {'max-width': '75px'}},
    # 0.99: {'label': "99% (FFP2 / N95)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Pas de masque", 'value': 0},
    {'label': "Coton, flanelle", 'value': 0.5},
    {'label': "Coton multicouches, soie", 'value': 0.7},
    {'label': "Chirurgical à usage unique", 'value': 0.9},
    {'label': "FFP2 / N95", 'value': 0.99},
]

mask_fit_marks = {
    0: {'label': '0%: Aucun', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Médiocre'},
    0.95: {'label': '95%: Bon'}
}

ventilation_types = [
    {'label': "Fenêtres fermées", 'value': 0.3},
    {'label': "Fenêtres ouvertes", 'value': 2},
    {'label': "Ventilation mécanique", 'value': 3},
    {'label': "Fenêtres ouvertes avec ventilateurs", 'value': 6},
    {'label': "Ventilation mécanique supérieure", 'value': 8},
    {'label': "Laboratoire, Restaurant", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Hôpital, Wagon de métro", 'value': 18},
    {'label': "Laboratoire sécurisé, Avion", 'value': 24},
]

filter_types = [
    {'label': "Aucun", 'value': 0},
    {'label': "Climatiseur de fenêtre (résidentiel)", 'value': 2},
    {'label': "Résidentiel/Commerces/Industrie", 'value': 6},
    {'label': "Résidentiel/Commerces/Hôpital", 'value': 10},
    {'label': "Hôpital & cabinet médical", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_types = [
    {'label': "Aucun", 'value': 0},
    {'label': "Lent", 'value': 0.3},
    {'label': "Modéré", 'value': 1},
    {'label': "Rapide", 'value': 10},
    {'label': "Avion", 'value': 24},
    {'label': "Wagon de métro", 'value': 54},
]

graph_title = "Taux d'occupation vs. taux d'exposition"
graph_xtitle = "Temps d'exposition maximum \u03C4 (heures)"
graph_ytitle = "Occupation maximale N"
transient_text = "Transitoire/temporaire"
steady_state_text = "Continu"
co2_safe_trace_text = "Respiratory Safety Threshold"
guideline_trace_text = "Guideline"

graph_title_co2 = "Safe CO\u2082 Concentration (ppm) vs. Exposure Time"
graph_ytitle_co2 = "CO\u2082 Concentration (ppm)"

co2_title = "Calculate Safe CO\u2082 Concentration"
co2_param_desc = '''The guideline for the parameters chosen above is expressed here in terms of a CO\u2082 
concentration threshold.'''
co2_prev_input_1 = "Prevalence: "
co2_prev_input_2 = " per 100,000"
co2_atm_input_1 = "Background CO\u2082: "
co2_atm_input_2 = " ppm"
co2_calc_1 = "For an exposure time of "
co2_calc_2 = " hours, the calculated safe steady-state CO\u2082 concentration in this space is "
co2_calc_3 = " (based on the guideline)."
co2_base_string = '{:,.2f} ppm'

co2_safe_sent_1 = "This limit exceeds that for healthy respiratory activity, which is "
co2_safe_sent_2 = "."

co2_safe_footer = html.Span(['''The respiratory safety threshold is interpolated based on ''',
                             html.A(href=links.link_usda_co2,
                                    children='''recommended limits from the USDA''',
                                    target='_blank'),
                             '''.'''])

units_hr = 'heures'
units_min = 'minutes'
units_days = 'jours'
units_months = 'mois'

units_hr_one = 'heure'
units_min_one = 'minute'
units_day_one = 'jour'
units_month_one = 'mois'

is_past_recovery_base_string = '{n_val} personnes pendant >{val:.0f} jours,'
model_output_base_string = '{n_val} personnes pendant '
nt_bridge_string = " personnes pendant "
tn_bridge_string = " personnes pendant "

six_ft_base_string = ' {} personnes'
six_ft_base_string_one = ' {} personnes'

presets = [
    {'label': "Customiser", 'value': 'custom'},
    {'label': "Maison individuelle", 'value': 'house'},
    {'label': "Restaurant", 'value': 'restaurant'},
    {'label': "Bureau", 'value': 'office'},
    {'label': "Salle de classe", 'value': 'classroom'},
    {'label': "Salle de séjour", 'value': 'living-room'},
    {'label': "Wagon de métro", 'value': 'subway'},
    {'label': "Avion de ligne", 'value': 'airplane'},
    {'label': "Eglise", 'value': 'church'},
]

curr_human_header = "Comportement des personnes : "
presets_human = [
    {'label': "Customiser", 'value': 'custom'},
    {'label': "Masques, Repos", 'value': 'masks-1'},
    {'label': "Masques, On parle", 'value': 'masks-2'},
    {'label': "Masques, On fait de l'exercice", 'value': 'masks-3'},
    {'label': "Pas de masques, Repos", 'value': 'no-masks-1'},
    {'label': "Pas de masques, On parle", 'value': 'no-masks-2'},
    {'label': "Pas de masques, On fait de l'exercice", 'value': 'no-masks-3'},
    {'label': "Pas de masques, On chante", 'value': 'singing-1'},
]

curr_risk_header = "Seuil de tolérance du risque: "
risk_tol_marks = {
    # 0.01: {'label': '0.01: Plus sûr', 'style': {'max-width': '30px'}},
    0.1: {'label': '0.10: Sûr', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Risqué'}
}

risk_tolerance_text = "Seuil de tolérance du risque: "

curr_age_header = "Groupe d'âge : "
presets_age = [
    {'label': "Enfants (<15 ans)", 'value': 0.23},
    {'label': "Adultes (15-64 ans)", 'value': 0.68},
    {'label': "Personnes âgées (>64 ans)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: Enfants (<15 ans)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: Adultes (15-64 ans)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: Personnes âgées (>64 ans)', 'style': {'width': '100px'}}
}

curr_strain_header = "Souche virale : "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2 (souche Wuhan)", 'value': 1},
    {'label': "SARS-CoV-2 - B.1.1.7 (souche britannique)", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: Wuhan', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: B.1.1.7/UK'}
}

pim_header = "Proportion de personnes immunisées:"
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "Si une personne infectée entre..."
risk_prevalence_desc = "Étant donné le taux d'incidence..."
risk_personal_desc = "Pour limiter mon risque personnel..."

error_list = {
    "floor_area": "Erreur : la surface au sol doit être renseignée.",
    "ceiling_height": "Erreur : la hauteur sous plafond doit être renseignée.",
    "recirc_rate": "Erreur : le taux de recirculation d'air (ACH) doit être renseigné.",
    "aerosol_radius": "Erreur : le rayon de l'aérosol doit être renseigné.",
    "viral_deact_rate": "Erreur : le taux d'inactivation virale doit être renseigné.",
    "n_max_input": "Erreur : le nombre de personnes ne peut pas être inférieur à 2.",
    "exp_time_input": "Erreur : le temps d'exposition doit être supérieur à zéro.",
    "air_exchange_rate": "Erreur : le taux de renouvellement de l'air (ACH) doit être supérieur à zéro.",
    "merv": "Erreur : le système de filtration (MERV) doit être renseigné.",
    "prevalence": "Erreur : L'incidence doit être supérieure à 0 et inférieure à 100 000.",
    "atm_co2": "Error: Background CO\u2082 level is required."
}

# Header
header = html.Div([
    html.H1(children='Recommandations COVID-19 pour limiter la transmission en lieux clos'),
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
language_dd = "Langue: "
units_dd = "Unités: "
mode_dd = "Mode: "

# Unit systems
unit_settings = [
    {'label': "Système impérial", 'value': "british"},
    {'label': "Système métrique", 'value': "metric"},
]

# Modes
app_modes = [
    {'label': "Basique", 'value': "basic"},
    {'label': "Avancé", 'value': "advanced"},
]

# Tabs
about_header = "A propos"
room_header = "Caractéristiques de l'espace - Détails"
human_header = "Comportement humain - Détails"
faq_header = "Questions fréquentes"
other_io = "Autres entrées et résultats"

# About
about = html.Div([
    html.H6("A propos", style={'margin': '0'}),
    html.Div('''Pour réduire la transmission de la COVID-19, les consignes officielles de santé publique
    limitent la distance entre 2 personnes (fixée à 1 ou 2 mètres), le temps et le taux d'occupation d'un espace, et préconisent la ventilation.'''),
    html.Br(),
    html.Div([html.Span('''Il y a de plus en plus de '''),
              html.A(children="preuves scientifiques",
                     href=link_docs,
                     target='_blank'),
              html.Span(''' de la transmission aérienne de la COVID-19. Elle a lieu lorsque des aérosols 
              infectieux sont échangés, en respirant l'air partagé des espaces intérieurs clos. Les autorités de 
              santé publique commencent à reconnaître la transmission par aérosols de la COVID-19, mais elles n'ont 
              pas encore fourni de consignes de sécurité prenant en compte tous les paramètres utiles.''')]),
    html.Br(),
    html.Div([html.Span('''Cett app, développée par Kasim Khan en collaboration avec Martin Z. Bazant et John W. M. 
    Bush, utilise un '''),
              html.A(children="modèle théorique",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' pour calculer la durée d'exposition et le taux d'occupation d'un espace qui seraient acceptables en termes de 
              sécurité, pour des espaces intérieurs. En faisant varier les caractéristiques du lieu, les taux de 
              ventilation et de filtration de l'air, le port de masques, le type d'activité respiratoire ainsi que le 
              degré de risque toléré (dans les autres onglets), vous pourrez mieux comprendre comment limiter le risque 
              de transmission de la COVID-19 dans différents espaces intérieurs.''')]),
    html.Br(),
    html.Div(['''In Basic mode, you can calculate the limits on safe occupancy following the entrance of a single 
infected person into an indoor space. In Advanced Mode, you can take into account additional factors, 
including infection prevalence and population immunity. Advanced Mode also allows you to assess safe occupancy 
based on average CO2 concentration, which is related to the concentration of infectious aerosols.''']),
    html.Br(),
    html.Div([html.Span('''La science au cœur de cette app est aussi enseignée dans un cours en ligne (MOOC) gratuit, en anglais, 
    sur edX: '''),
              html.A(children="10.S95x Physics of COVID-19 Transmission",
                     href=link_mooc,
                     target='_blank')])
])

# Room Specifications
floor_area_text = "Surface au sol totale (sq. ft.): "
floor_area_text_metric = "Surface au sol totale (m²): "

ceiling_height_text = "Hauteur sous plafond (moyenne) (ft.): "
ceiling_height_text_metric = "Hauteur sous plafond (moyenne) (m): "

ventilation_text = "Système de ventilation: "
ventilation_text_adv = "Système de ventilation (ACH): "

filtration_text = "Système de filtration: "
filtration_text_adv = "Système de filtration (MERV): "

recirc_text = "Taux de renouvellement horaire: "
recirc_text_adv = "Taux de renouvellement horaire (ACH): "

humidity_text = "Humidité relative : "

need_more_ctrl_text = '''Si vous souhaitez plus de contrôle sur vos paramètres, passez en Mode avancé, par le 
                      menu en haut de la page.'''

# Human Behavior
exertion_text = "Niveau d'activité: "

breathing_text = "Activité respiratoire: "

mask_type_text = "Efficacité de filtration des masques (type de masque): "

mask_fit_text = "Ajustement des masques / respect du port du masque: "

# FAQ/Other Inputs and Outputs
assumptions_layout = html.Div([
    html.H5("Encore des questions ? "),
    html.Div([html.Span('''Pour des explications plus détaillées et des références, voir "Au-delà des 2 mètres : recommandations pour limiter le risque de transmission aérosol "
                             "de la COVID-19 en lieux clos" ('''),
              html.A(children="Bazant & Bush, 2020",
                     href=link_paper,
                     target='_blank'),
              html.Span(''') et d'autres liens en haut de la page.''')]),
])

faq_top = html.Div([
    html.H6("Questions fréquentes"),
    html.H5("Pourquoi une distance de 2 mètres entre les personnes ne suffit-elle pas ?"),
    html.Div([
        html.Div([html.Span('''Une distance de 2 mètres vous protège contre les grosses gouttelettes éjectées par 
        une personne contaminée qui tousse. Les masques vous en protègent aussi. Cependant, cette distance ne vous 
        protège pas contre la '''),
                  html.A(children="transmission aérienne",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''', via des aérosols infectieux en suspension dans l'air, qui peuvent être répartis dans 
                  toute la pièce. A l'intérieur, une personne n'est pas mieux protégée contre la contamination par les  
                  aérosols à 20 mètres qu'à 2 mètres.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Y a-t-il d'autres modes de transmission ?"),
    html.Div([
        html.Div([html.A(children="La transmission aérosol",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' est considérée comme dominante pour le COVID-19, mais d'autres modes sont possibles. 
                  Parmi eux, la transmission par "fomites" (contact direct avec des résidus infectieux déposés sur 
                  des surfaces), ou par les postillons émis par une personne qui tousse ou 
                  éternue, et enfin la transmission par des "aérosols à courte portée" issus de l'expectoration d'une 
                  personne contaminée, pendant une durée prolongée. Ces derniers modes peuvent être significatifs, 
                  mais ils sont largement éliminés lorsque des masques et visières sont portés ; cependant, 
                  le risque de transmission aérosol demeure. Notez que les masques protègent contre la transmission 
                  aérienne considérée ici, mais que les visières ne procurent aucune protection contre celle-ci. 
                  ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Faut-il faire l'hypothèse d'une pièce où l'air est bien brassé ?"),
    html.Div([
        html.Div([html.Span('''Il y a de nombreux facteurs qui contribuent au brassage de l'air d'un espace 
        intérieur, parmi lesquels les flux de convection naturelle (venus des radiateurs, climatiseurs, fenêtres) ou 
        forcée (grilles de ventilation et ventilateurs), ainsi que les mouvements et la respiration des personnes. S'il 
        y a des exceptions, comme précisé dans '''),
                  html.A(children="l'article de Bazant & Bush",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', l'hypothèse d'un brassage conséquent est cependant généralement utilisée dans la 
                  modélisation théorique de la transmission aérosol des maladies.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Ces recommandations restent-elles valables pour de très grands espaces ?"),
    html.Div([
        html.Div([html.Span('''Dans les salles de concert, stades, ou tout autre grand espace ventilé accueillant un 
        grand nombre de personnes, le risque de transmission aérosol est significatif, et il est pris en compte par 
        nos recommandations. Cependant, en l'absence de masques et de visières, il y a un risque additionnel de 
        transmission à courte distance via les jets respiratoires, estimé dans '''),
                  html.A(children="l'article",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Pourquoi la hauteur du plafond est-elle importante ?"),
    html.Div([
        '''Elle détermine le volume total de la pièce, nécessaire pour estimer la concentration en 
        aérosols contaminants (quantité d'aérosols par unité de volume), ce qui est ensuite nécessaire 
        pour estimer le risque de transmission du COVID-19 dans cet espace.'''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Je connais mes valeurs ACH/MERV. Où puis-je les saisir?"),
    html.Div('''
        Si vous avez besoin de plus de contrôle sur vos paramètres, passez en Mode avancé, par le menu en 
        haut de la page.
    ''', className='faq-answer'),
    html.Br(),
    html.H5("Pourquoi les masques FFP2 ont-ils 99% d'efficacité ?"),
    html.Div('''
					     Les masques FFP2 ont au moins 95% d'efficacité pour des tailles de particules de 0,3 μm, soit 10 fois plus petites que les particules
					     considérées dans les modèles de transmission COVID-19. Pour ces particules plus grosses, le taux d'efficacité des FFP2 dépasse
					     95%, et s'approche de 100%. ''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Y a-t-il des paramètres cachés, en Mode basique ?"),
    html.Div([html.Span('''Tous les paramètres physiques pertinents sont détaillés dans '''),
              html.A(children="l'article",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. En Mode basique, l'app fait l'hypothèse d'un rayon effectif des aérosols par défaut de 2 
              μm (à 60% d'humidité) et d'un taux maximum d'inactivation virale de 0.6 /heure (à ~100% d'humidité), 
              deux facteurs qui augmentent avec l'humidité relative (HR). Nos estimations du taux d'inactivation 
              virale sont prudentes, avec une inactivation lente. Le taux d'inactivation virale peut être augmenté 
              par le rayonnement ultraviolet (UV-C) ou les désinfectants chimiques (peroxyde d'hydrogène, 
              ozone). L'app estime aussi le paramètre clé de la maladie, l'infectiosité de l'air exhalé, C'''),
              html.Sub('q'),
              html.Span('''(quanta 
              d'infection par unité de volume), à partir de l'activité respiratoire spécifiée, en utilisant les 
              données de la Fig. 2 de '''),
              html.A(children="l'article",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. En Mode avancé, vous définissez vous-mêmes ces paramètres.''')],
             className='faq-answer'),
])
aerosol_radius_text = "Rayon effectif des aérosols (à 60% d'humidité), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Taux d'inactivation virale maximum (à HR=100%), \u03BB", html.Sub('vmax'), " (/hr): "])

values_interest_header = "Valeurs calculées d’intérêt : "
values_interest_desc = html.Div([
    html.H5("Que calcule l'app, exactement?"),
    html.Div([
        html.Div([html.Span('''Pour un seuil donné de tolérance du risque de transmission aérosol, l'app calcule le 
        temps maximum d'exposition cumulée autorisé, produit du nombre de personnes dans la pièce et du temps passé 
        en présence d'une personne contagieuse. L'app calcule aussi des quantités liées, définies dans '''),
                  html.A(children="l'article",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', et qui peuvent être intéressantes :''')]),
    ], className='faq-answer'),
])
pop_immunity_header = "Immunité de la population : "
perc_immune_label = html.Span(["Pourcentage d'immunité p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["Pourcentage de personnes infectées p", html.Sub('i'), " = "])
perc_susceptible_label = html.Span(["Pourcentage de personnes sensibles p", html.Sub('s'), " = 1 - (p", html.Sub('im'),
                                    " + p", html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''Le pourcentage infectieux p''', html.Sub('i'), '''dans la population est 
calculé à partir du taux d'incidence saisi dans les onglets des autres scénarios de risque (Étant donné 
la prévalence de l'infection..., Pour limiter mon risque personnel...).  Le pourcentage de p''', html.Sub('im'),
                                        ''' immunitaire peut être estimé de manière conservatrice à partir du 
                                        pourcentage de vaccination de la population plus le taux de cas total dans la 
                                        population, en négligeant la contribution des cas non détectés. Ces deux 
                                        valeurs sont utilisées pour calculer le pourcentage de p''', html.Sub('s'),
                                        '''. En mode de base et dans le premier mode de risque (Si une personne 
                                        infectée entre...), cette valeur est supposée être de 100%.''']),
                              html.Br(),
                              html.Div(['''Voici quelques liens utiles pour trouver p''', html.Sub('i'), ''' et p''',
                                        html.Sub('im'), ''': ''',
                                        html.Span(html.A(href=links.link_fr_covidtracker,
                                                         children="en France, covidtracker",
                                                         target='_blank')),
                                        html.Span(", "),
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
relative_sus_label = html.Span(["Sensibilité relative s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["Proportion d'air extérieur Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Efficacité de filtration des aérosols p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Débit respiratoire Q", html.Sub('b'), ": "])
cq_label = html.Span(["Infectiosité de l'air expiré C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Probabilité de passage à travers le masque p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Volume de la pièce V: "])
vent_rate_Label = html.Span(["Débit de la ventilation (extérieur) Q: "])
recirc_rate_label = html.Span(["Débit de recirculation Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Taux de filtration d'air (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(
    ["Rayon de l'aérosol ajusté en fonction de l'humidité r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(
    ["Taux d'inactivation virale ajusté en fonction de l'humidité \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Vitesse de stabilisation efficace de l'aérosol v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Taux de relaxation de la concentration \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Taux de transmission aérienne \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Ce modèle prend-il en compte le taux d’incidence dans la population locale ?"),
    html.Div(['''L'influence de la prévalence de l'infection dans la population locale peut être considérée en mode 
    avancé. Là, dans l'onglet Autres paramètres, on peut également évaluer l'influence de l'immunité dans la 
    population (résultant de la vaccination ou d'une infection antérieure).'''],
             className='faq-answer'),
])

risk_tol_desc = html.Div('''Les populations les plus vulnérables, comme les personnes âgées ou ayant une pathologie 
préexistante, requièrent un seuil de tolérance plus bas. Une tolérance du risque plus élevée signifiera plus de 
transmissions attendues pendant la période d'occupation du lieu (Cf Questions fréquentes pour plus de détails).''',
                         style={'font-size': '13px', 'margin-left': '20px'})

# Main Panel Text
curr_room_header = "Espace concerné :"
main_panel_s1 = "En se basant sur ce modèle, cet espace devrait être sûr pour: "

main_panel_s1_b = html.Span([
    html.Span('''Pour limiter la transmission de COVID-19* dans une population où l'incidence '''),
    html.Sup('''1'''),
    html.Span(''' est de ''')
])
main_panel_s2_b = ''' pour 100 000, cet espace ne devrait pas accueillir plus de: '''

main_panel_s1_c = html.Span([
    html.Span(
        '''Pour limiter mes risques d'être infecté par COVID-19 dans une population où l'incidence '''),
    html.Sup('''1'''),
    html.Span(''' de ''')
])
main_panel_s2_c = ''' pour 100 000, cet espace ne devrait pas avoir plus de : '''

main_panel_six_ft_1 = "En revanche, la consigne de distance d'un mètre (ou 2 mètres) limiterait l'occupation à "
main_panel_six_ft_2 = ", ce qui serait contraire à la présente recommandation* après "

main_airb_trans_only_disc = html.Div(["Cette recommandation limite la probabilité de ",
                                      html.Span(html.A(href=links.link_nature,
                                                       children="transmission par voie aérienne",
                                                       target='_blank'), ),
                                      html.Span(''' par personne, à un niveau inférieur à la tolérance au risque 
                                      précisée, pendant la durée d'exposition cumulée indiquée.''')],
                                     className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*Cette recommandation limite la probabilité de ",
                                            html.Span(html.A(href=links.link_docs,
                                                             children="transmission par voie aérienne",
                                                             target='_blank'), ),
                                            html.Span(''', par personne infectée, à un niveau inférieur à la 
                                            tolérance au risque (10 %), pendant la durée d'exposition cumulée 
                                            indiquée.''')], className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''Pour estimer votre taux d'incidence local, 
                                voici quelques ressources utiles : '''),
                                html.Span(html.A(href=links.link_fr_covidtracker,
                                                 children="en France, covidtracker",
                                                 target='_blank')),
                                html.Span(''', '''),
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

other_risk_modes_desc = html.Div('''D'autres scénarios de risque sont envisagés en mode avancé. Plus précisément, 
on peut considérer le taux d'incidence dans la population, l'immunité acquise par la vaccination ou une exposition 
antérieure, et le risque pour un individu spécifique.''')

# Bottom panels text
n_input_text_1 = "Si cet espace contient "
n_max_base_string = ' {:.0f}'
n_max_overflow_base_string = ' >{:.0f}'
n_input_text_2 = " personnes, elles devraient être en sécurité pendant "
n_input_text_3 = "."

t_input_text_1 = "Si des personnes passent environ "
t_input_text_2 = " heures dans cet espace, leur nombre devrait être limité à "
t_input_text_3 = "."

airb_trans_only_disc = html.Div('''Cette recommandation est basée sur la prise en compte de la transmission aérienne, 
                                    par une seule personne contaminée, pendant la durée d'exposition 
                                      cumulée indiquée.''', className='airborne-text')

footer = html.Div([
    html.Div([html.Span('''Les présentes Recommandations de sécurité COVID-19 pour les espaces intérieurs sont un 
    outil en cours d'évolution, destiné à familiariser l'utilisateur intéressé avec les facteurs qui influencent le 
    risque de transmission aérienne de la COVID-19 dans les espaces intérieurs, et d'aider à l'évaluation quantitative du risque 
    dans divers environnements. Nous notons que la variabilité intrinsèque des paramètres du modèle, 
    et leur incertitude, peuvent conduire à des erreurs pouvant varier dans un intervalle d'un ordre de grandeur, 
    ce qui peut être compensé en choisissant un seuil de tolérance du risque suffisamment bas. Nos recommandations ne 
    prennent pas en compte la transmission à courte portée par les jets respiratoires, qui peuvent augmenter 
    significativement le risque en l'absence de masques, comme précisé dans le manuscrit qui accompagne cet outil ('''),
              html.A(children="Bazant & Bush, 2020",
                     href=link_paper,
                     target='_blank'),
              html.Span('''). L'usage des Recommandations COVID-19 pour limiter la transmission en lieux clos est placé 
              sous la seule responsabilité de l'utilisateur. L'outil est mis à la disposition du public sans garantie 
              d'aucune sorte. Les auteurs n'acceptent aucune responsabilité liée à son utilisation.''')]),
    html.Br(),
    html.Div("Remerciements à: ")
], className='footer-small-text')
