import dash_html_components as html

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions_fr: French

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

vent_type_output_base = "{:.0f} ACH"
filt_type_output_base = "MERV {:.0f}"
recirc_type_output_base = "{:.1f} ACH"

# Default dropdown options shared between basic mode and advanced mode
humidity_marks = {
    0: {'label': '0%: Très sec', 'style': {'max-width': '25px'}},
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
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Chuchotement", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Dialogue normal", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Parler fort", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Chant", 'value': 970},
]

mask_type_marks = {
    0: {'label': "0% (pas de masque, visière)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (coton épais)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (soie, flanelle, mousseline)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (masque chirurgical, coton fin)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (FFP2)", 'style': {'max-width': '50px'}},
}

mask_types = [
    {'label': "Pas de masque, visière", 'value': 0},
    {'label': "Coton épais", 'value': 0.1},
    {'label': "Soie, flanelle, mousseline", 'value': 0.5},
    {'label': "Masque chirurgical, coton fin", 'value': 0.75},
    {'label': "FFP2", 'value': 0.95},
]

mask_fit_marks = {
    0: {'label': '0%: Aucun', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Mediocre'},
    0.95: {'label': '95%: Bon'}
}

risk_tol_marks = {
    0.01: {'label': '0.01: Plus sûr', 'style': {'max-width': '30px'}},
    0.1: {'label': '0.10: Sûr', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Risqué'}
}

ventilation_types = [
    {'label': "Fenêtres fermées", 'value': 0.3},
    {'label': "Fenêtres ouvertes", 'value': 2},
    {'label': "Ventilation mécanique", 'value': 3},
    {'label': "Fenêtres ouvertes avec ventilateurs", 'value': 6},
    {'label': "Ventilation mécanique supérieure", 'value': 8},
    {'label': "Laboratoire, restaurant", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Hôpital/Wagon du métro", 'value': 18},
    {'label': "Laboratoire sécurisé/Avion", 'value': 24},
]

filter_types = [
    {'label': "Aucun", 'value': 0},
    {'label': "Climatiseur de fenêtre (résidentiel)", 'value': 2},
    {'label': "Résidentiel/Commercial/industriel", 'value': 6},
    {'label': "Résidentiel/Commercial/Hôpital", 'value': 10},
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

n_max_base_string = ' {:.0f}'

graph_title = "Taux d'occupation vs. taux d'exposition"
graph_xtitle = "Temps d'exposition maximum \u03C4 (heures)"
graph_ytitle = "Occupation maximale N"
transient_text = "Transitoire/temporaire"
steady_state_text = "Continu"

six_ft_base_string = ' {} personnes'
six_ft_base_string_one = ' {} personnes'

units_hr = 'heures'
units_min = 'minutes'
units_days = 'jours'

units_hr_one = 'heures'
units_min_one = 'minute'
units_day_one = 'jours'

is_past_recovery_base_string = '{n_val} personnes pendant >{val:.0f} jours,'
model_output_base_string = '{n_val} personnes pendant '

presets = [
    {'label': "Customiser", 'value': 'custom'},
    {'label': "Maison individuelle", 'value': 'house'},
    {'label': "Restaurant", 'value': 'restaurant'},
    {'label': "Bureaux calmes", 'value': 'office'},
    {'label': "Cours dans une salle de classe", 'value': 'classroom'},
    {'label': "Wagon de métro", 'value': 'subway'},
    {'label': "Boeing 737", 'value': 'airplane'},
    {'label': "Eglise", 'value': 'church'},
]

error_list = {
    "floor_area": "Erreur : la surface au sol doit être renseignée.",
    "ceiling_height": "Erreur : la hauteur sous plafond doit être renseignée.",
    "recirc_rate": "Erreur : le taux de recirculation d'air doit être renseigné.",
    "aerosol_radius": "Erreur : le rayon de l'aérosol doit être renseigné.",
    "viral_deact_rate": "Erreur : le taux d'inactivation virale doit être renseigné.",
    "n_max_input": "Erreur : le nombre de personnes ne peut pas être inférieur à 2.",
    "exp_time_input": "Erreur : le temps d'exposition doit être supérieur à zéro.",
    "air_exchange_rate": "Erreur : le taux de renouvellement de l'air (ACH) doit être supérieur à zéro.",
    "merv": "Erreur : le système de filtration (MERV) doit être renseigné."
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
        html.Div([html.Span(["Au-delà des 2 mètres : recommandations pour limiter le risque de transmission aérosol "
                             "de la COVID-19 à l'intérieur ("]),
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
room_header = "Caractéristiques de la pièce"
human_header = "Comportement humain"
faq_header = "Questions fréquentes"
other_io = "Autres entrées et résultats"

# About
about = html.Div([
    html.H6("A propos", style={'margin': '0'}),
    html.Div('''Pour atténuer la diffusion de la COVID-19, les recommandations officielles de santé publique posent 
    des limites concernant : la distance entre 2 personnes (2 mètres), le temps d'occupation d'un espace (15 
    minutes), le taux maximum d'occupation (25 personnes), ou la ventilation minimum (6 renouvellements d'air par 
    heure).'''),
    html.Br(),
    html.Div([html.Span('''Il y a de plus en plus de '''),
              html.A(children="preuves scientifiques",
                     href=link_docs,
                     target='_blank'),
              html.Span(''' de la transmission aérienne de la COVID-19. Elle a lieu lorsque des particules aérosol 
              infectieuses sont échangées, en respirant l'air partagé des espaces intérieurs clos. Les autorités de 
              santé publique commencent à reconnaître la transmission par aérosols de la COVID-19, mais elles n'ont 
              pas encore fourni de recommandations de sécurité prenant en compte tous les paramètres pertinents.''')]),
    html.Br(),
    html.Div([html.Span('''Cett app, développée par Karim Khan en collaboration avec Martin Z. Bazant et John W. M. 
    Bush, utilise un '''),
              html.A(children="modèle théorique",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' pour calculer la durée d'exposition et le taux d'occupation acceptables en termes de 
              sécurité, pour des espaces intérieurs. En ajustant les caractéristiques du lieu, les taux de 
              ventilation et de filtration de l'air, l'usage de masques, le type d'activité respiratoire ainsi que le 
              degré de risque toléré (dans les autres tabs), vous pourrez mieux comprendre comment atténuer le risque 
              de transmission de la COVID-19 dans différents espaces intérieurs.''')]),
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

need_more_ctrl_text = '''Si vous souhaitez plus de contrôle sur vos paramètres, passez en Mode avancé en utilisant le 
                      menu en haut de la page.'''

# Human Behavior
exertion_text = "Niveau d'activité: "

breathing_text = "Activité respiratoire: "

mask_type_text = "Efficacité de filtration des masques (type de masque): "

mask_fit_text = "Ajustement des masques / respect du port du masque: "

risk_tolerance_text = "Seuil de tolérance du risque: "

# FAQ/Other Inputs and Outputs
assumptions_layout = html.Div([
    html.H5("Encore des questions? "),
    html.Div([html.Span('''Pour des explications plus détaillées et des références, voir "Au-delà des 2 mètres : recommandations pour limiter le risque de transmission aérosol de la COVID-19 à l'intérieur." ('''),
              html.A(children="Bazant & Bush, 2020",
                     href=link_paper,
                     target='_blank'),
              html.Span(''') et d'autres liens en haut de la page.''')]),
])

faq_top = html.Div([
    html.H6("Questions fréquentes"),
    html.H5("Pourquoi une distance de 2 mètres entre les personnes n'est-elle pas suffisante?"),
    html.Div([
        html.Div([html.Span('''Une distance de deux mètres vous protège contre les grosses gouttelettes éjectées par 
        une personne contaminée qui tousse. Les masques vous en protègent aussi. Cependant, cette distance ne vous 
        protège pas contre la '''),
                  html.A(children="transmission aérienne",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''', via des aérosols infectieux en suspension dans l'air, qui peuvent être répartis dans 
                  toute la pièce. A l'intérieur, une personne n'est pas mieux protégée contre la contamination par 
                  aérosols à 2 mètres qu'à 20 mètres.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Y a-t-il d'autres modes de transmission?"),
    html.Div([
        html.Div([html.A(children="La transmission aérosol",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' est considérée comme dominante pour le COVID-19, mais d'autres modes sont possibles. 
                  Parmi eux, la transmission par "fomites" (contact direct avec des résidus infectieux déposés sur 
                  des surfaces), ou par les gouttelettes (ou postillons) émises par une personne qui tousse ou 
                  éternue, et enfin la transmission par des "aérosols à courte portée" issus de l'expectoration d'une 
                  personne contaminée, pendant une durée prolongée. Ces derniers modes peuvent être significatifs, 
                  mais ils sont largement éliminés lorsque des masques et visières sont portés ; cependant, 
                  le risque de transmission aérosol demeure. Notez que les masques protègent contre la transmission 
                  aérienne considérée ici, mais que les visières ne procurent aucune protection contre celle-ci. 
                  ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Pouvons-nous réellement faire l'hypothèse d'une pièce où l'air est bien brassé?"),
    html.Div([
        html.Div([html.Span('''Il y a de nombreux facteurs qui contribuent au brassage de l'air d'un espace 
        intérieur, parmi lesquels les flux de convection naturelle (venus des radiateurs, climatiseurs, fenêtres) ou 
        forcée (grilles de ventilation et ventilateurs), ainsi que les mouvements et la respiration des humains. S'il 
        y a des exceptions, comme précisé dans '''),
                  html.A(children="l'article de Bazant & Bush",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', l'hypothèse d'un brassage conséquent est cependant généralement utilisée dans la 
                  modélisation théorique de la transmission aérosol des maladies.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Ces recommandations restent-elles valables pour de très grands espaces?"),
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
    html.H5("Pourquoi la hauteur du plafond est-elle importante?"),
    html.Div([
        '''La hauteur du plafond détermine le volume total de la pièce, nécessaire pour estimer la concentration en 
        aérosols contaminants (quantité d'aérosols par unité de volume). Connaître cette concentration est nécessaire 
        pour estimer le risque de transmission du COVID-19 dans cet espace.'''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Je connais mes valeurs ACH/MERV. Où puis-je les saisir?"),
    html.Div('''
        Si vous avez besoin de plus de contrôle sur vos paramètres, passez en Mode avancé en utilisant le menu en 
        haut de la page.
    ''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Y a-t-il des paramètres cachés, en Mode basique?"),
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

values_interest_header = "Calculated Values of Interest: "
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
outdoor_air_frac_label = html.Span(["Proportion d'air extérieur Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Efficacité de filtration des aérosols p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Débit respiratoire Q", html.Sub('b'), ": "])
cq_label = html.Span(["Infectiosité de l'air expiré C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Probabilité de passage à travers le masque p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Volume de la pièce V: "])
vent_rate_Label = html.Span(["Débit de la ventilation (extérieur) Q: "])
recirc_rate_label = html.Span(["Débit de recirculation Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Taux de filtration d'air (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Rayon de l'aérosol ajusté en fonction de l'humidité r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Taux d'inactivation virale ajusté en fonction de l'humidité \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Vitesse de stabilisation efficace de l'aérosol v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Taux de relaxation de la concentration \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Taux de transmission aérienne \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Ce modèle prend-il en compte le taux d’incidence dans la population locale?"),
    html.Div(['''Non. Le modèle calcule le risque de transmission à partir d'une seule personne contaminée. Il part 
    donc du principe que le taux d'incidence dans la population est relativement bas. Dans cette limite, le risque de 
    transmission augmente avec le nombre de personnes contaminées dans la pièce. Spécifiquement, c'est le produit du 
    taux d'occupation et de la prévalence dans la population. La tolérance devrait donc être baissée en fonction de 
    ce nombre, s'il est supérieur à un. A l'inverse quand le nombre de personnes infectées estimées présentes 
    s'approche de zéro, le seuil de tolérance pourrait être augmenté proportionnellement, jusqu'à ce que les 
    restrictions recommandées soient jugées inutiles.'''],
             className='faq-answer'),
])

risk_tol_desc = html.Div('''Les populations les plus vulnérables, comme les personnes âgées ou ayant une pathologie 
préexistante, requièrent un seuil de tolérance plus bas. Une tolérance du risque plus élevée signifiera plus de 
transmissions attendues pendant la période d'occupation du lieu (Cf Questions fréquentes pour plus de détails).''',
                         style={'font-size': '13px', 'margin-left': '20px'})

# Main Panel Text
curr_room_header = "Espace concerné :"
main_panel_s1 = "En se basant sur ce modèle, cet espace devrait être sûr pour: "
main_panel_six_ft_1 = "NB : la règle de distanciation de 2 mètres indiquerait que jusqu'à "
main_panel_six_ft_2 = " seraient en sécurité dans cet espace, pour une durée non définie."

main_airb_trans_only_disc = html.Div(["Les recommandations sont basées sur la prise en compte de la ",
                                      html.Span(html.A(href='https://www.nature.com/articles/d41586-020-02058-1',
                                                       children="transmission aérienne",
                                                       target='_blank'), ),
                                      html.Span(''', par une seule personne contaminée, pendant la durée d'exposition 
                                      cumulée indiquée.''')], className='airborne-text')

# Bottom panels text
n_input_text_1 = "Si cet espace contient "
n_input_text_2 = " personnes, ses occupants devraient être en sécurité pendant "
n_input_text_3 = "."

t_input_text_1 = "Si des personnes passent environ "
t_input_text_2 = " heures dans cet espace, leur nombre devrait être limité à "
t_input_text_3 = "."

airb_trans_only_disc = html.Div('''based on consideration of airborne transmission only.''', className='airborne-text')

footer = html.Div([
    html.Div([html.Span('''Les présentes Recommandations de sécurité COVID-19 pour les espaces intérieurs sont un 
    outil en cours d'évolution, destiné à familiariser l'utilisateur intéressé avec les facteurs qui influencent le 
    risque de transmission aérosol de la COVID-19 à l'intérieur, et d'aider à l'évaluation quantitative du risque 
    dans divers environnements. Nous notons que la variabilité intrinsèque des paramètres du modèle, 
    et leur incertitude, peuvent conduire à des erreurs pouvant varier dans un intervalle d'un ordre de grandeur, 
    ce qui peut être compensé en choisissant un seuil de tolérance du risque suffisamment bas. Nos recommandations ne 
    prennent pas en compte la transmission à courte portée par les jets respiratoires, qui peuvent augmenter 
    significativement le risque en l'absence de masques, comme précisé dans le manuscrit qui accompagne cet outil ('''),
              html.A(children="Bazant & Bush, 2020",
                     href=link_paper,
                     target='_blank'),
              html.Span('''). L'usage des Recommandations de sécurité COVID-19 pour les espaces intérieurs est placé 
              sous la seule responsabilité de l'utilisateur. L'outil est mis à la disposition du public sans garantie 
              d'aucune sorte. Les auteurs n'acceptent aucune responsabilité liée à son utilisation.''')]),
    html.Br(),
    html.Div("Remerciements à William H. Green, David Keating, Ann Kinzig, Caeli MacLennan, Michelle Quien, "
             "Marc Rosenbaum, and David Stark"),
    html.Div("Huanhuan Tian, Hongbo Zhao, Juner Zhu")
], className='footer-small-text')
