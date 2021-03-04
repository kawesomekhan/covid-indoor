import dash_html_components as html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

German

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

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
language_dd = "Sprache: "

# Unit systems
units_dd = "Einheiten: "
unit_settings = [
    {'label': "Britisch", 'value': "british"},
    {'label': "Metrisch", 'value': "metric"},
]

# Modes
mode_dd = "Modus: "
app_modes = [
    {'label': "Grundmodus", 'value': "basic"},
    {'label': "Erweitert", 'value': "advanced"},
]

error_list = {
    "floor_area": "Fehler: Flurbereich kann nicht leer sein.",
    "ceiling_height": "Fehler: Deckenhöhe kann nicht leer sein.",
    "recirc_rate": "Fehler: Rezirkulationsrate kann nicht leer sein.",
    "aerosol_radius": "Fehler: Aerosolradius kann nicht leer sein.",
    "viral_deact_rate": "Fehler: Virale Deaktivierungsrate kann nicht leer sein.",
    "n_max_input": "Fehler: Anzahl an Personen kann nicht kleiner als zwei sein.",
    "exp_time_input": "Fehler: Expositionszeit muss größer als 0 sein.",
    "air_exchange_rate": "Fehler: Luftwechselrate (ACH) muss größer als 0 sein.",
    "merv": "Fehler: Luftfiltersystem (MERV) kann nicht leer sein.",
    "prevalence": "Fehler: Die Verbreitung (Prävalenz) muss größer als 0 und kleiner als 100.000 betragen."
}

# Main Panel Text
curr_room_header = "Raumspezifikationen: "
presets = [
    {'label': "Benutzerdefiniert", 'value': 'custom'},
    {'label': "Haus im Stadtrandgebiet", 'value': 'house'},
    {'label': "Restaurant", 'value': 'restaurant'},
    {'label': "Büro", 'value': 'office'},
    {'label': "Klassenzimmer", 'value': 'classroom'},
    {'label': "Wohnzimmer", 'value': 'living-room'},
    {'label': "U-Bahn-Wagen", 'value': 'subway'},
    {'label': "Kommerzielles Linienflugzeug", 'value': 'airplane'},
    {'label': "Kirche", 'value': 'church'},
]

curr_human_header = "Menschliches Verhalten: "
presets_human = [
    {'label': "Benutzerdefiniert", 'value': 'custom'},
    {'label': "Masken, ruhend", 'value': 'masks-1'},
    {'label': "Masken, redend", 'value': 'masks-2'},
    {'label': "Masken, Tätigkeit ausübend", 'value': 'masks-3'},
    {'label': "Ohne Maske, ruhend", 'value': 'no-masks-1'},
    {'label': "Ohne Maske, sprechend", 'value': 'no-masks-2'},
    {'label': "Ohne Maske, Tätigkeit ausübend", 'value': 'no-masks-3'},
    {'label': "Ohne Maske, singend", 'value': 'singing-1'},
]

curr_risk_header = "Risikotoleranz: "
# presets_risk = [
#     {'label': "Low", 'value': 0.01},
#     {'label': "Medium", 'value': 0.1},
#     {'label': "High", 'value': 1},
# ]
risk_tol_marks = {
    # 0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Sicher', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Unsicher'}
}

curr_age_header = "Altersgruppe: "
presets_age = [
    {'label': "Kinder (<15 Jahre)", 'value': 0.23},
    {'label': "Erwachsene (15-64 Jahre)", 'value': 0.68},
    {'label': "Ältere Menschen (>64 Jahre)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: Kinder (<15 Jahre)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: Erwachsene (15-64 Jahre)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: Ältere Menschen (>64 Jahre)', 'style': {'width': '75px'}}
}
lang_break_age = html.Br()

curr_strain_header = "Virusvariante: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2 (Wuhan Variante)", 'value': 1},
    {'label': "SARS-CoV-2 - B.1.1.7 (UK Variante)", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: Wuhan', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: B.1.1.7/UK'}
}

pim_header = "Prozentsatz immun: "
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "Falls eine infizierte Person eintritt…"
risk_prevalence_desc = "Angesichts der Ausbreitung der Infektion…"
risk_personal_desc = "Um mein persönliches Risiko zu begrenzen…"

main_panel_s1 = "Basierend auf diesem Modell, sollte die Situation im Raum sicher sein bei: "

main_panel_s1_b = html.Span([
    html.Span('''Um die COVID-19- Übertragung * in der Bevölkerung mit einer Prävalenz'''),
    html.Sup('''1'''),
    html.Span(''' von ''')
])
main_panel_s2_b = ''' pro 100.000 zu begrenzen, sollte dieser Raum nicht mehr haben als: '''

main_panel_s1_c = html.Span([
    html.Span('''Um mein Risiko, in einer Bevölkerung mit einer Infektionsprävalenz'''),
    html.Sup('''1'''),
    html.Span(''' von ''')
])
main_panel_s2_c = ''' pro 100.000 mit COVID-19 infiziert zu werden, sollte dieser Raum nicht mehr haben als: '''

units_hr = 'Stunden'
units_min = 'Minuten'
units_days = 'Tage'
units_months = 'Monate'

units_hr_one = 'Stunde'
units_min_one = 'Minute'
units_day_one = 'Tag'
units_month_one = 'Monat'

is_past_recovery_base_string = '{n_val} Personen für >{val:.0f} Tage,'
model_output_base_string = '{n_val} Personen für '
nt_bridge_string = " Personen für "
tn_bridge_string = " für "

main_panel_six_ft_1 = "Im Gegensatz dazu würde der Sechs-Fuß- (oder Zwei-Meter-) Abstandsrichtwert die Belegung auf "
main_panel_six_ft_2 = " begrenzen, was nach "
main_panel_six_ft_3 = " gegen die Richtlinie* verstoßen würde."

six_ft_base_string = ' {} Personen'
six_ft_base_string_one = ' {} Personen'

graph_title = "Raumbelegungsdauer vs. Expositionszeit"
graph_xtitle = "Maximale Expositionszeit \u03C4 (Stunden)"
graph_ytitle = "Maximale Personenbelegung N"
transient_text = "Instationärer Zustand"
steady_state_text = "Stationärer Zustand"

main_airb_trans_only_disc = html.Div(["*Die Richtlinie schränkt die Wahrscheinlichkeit von ",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="luftgetragenen Übertragungen ",
                                                       target='_blank'), ),
                                      html.Span(''' pro Person auf weniger als die Risikotoleranz über die angegebene 
                                      kumulative Expositionszeit ein.''')], className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*Die Richtlinie beschränkt die Wahrscheinlichkeit von ",
                                            html.Span(html.A(href=links.link_docs,
                                                             children="luftgetragenen Übertragungen ",
                                                             target='_blank'), ),
                                            html.Span(''' pro infizierter Person auf weniger als die Risikotoleranz (
                                            10 %) über die angegebene kumulative Expositionszeit.''')],
                                           className='airborne-text')

other_risk_modes_desc = html.Div('''Andere Risikoszenarien werden im erweiterten Modus berücksichtigt. Insbesondere 
kann man die Prävalenz der Infektion in der Bevölkerung, die durch Impfung oder frühere Ansteckung erworbene 
Immunität und das Risiko für eine individueller Person berücksichtigen.''')

main_airb_trans_only_desc_b = html.Div(["*Die Richtlinie schränkt die Wahrscheinlichkeit einer einzelnen ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="Übertragung",
                                                         target='_blank'), ),
                                        html.Span(''' über die Luft pro infizierter Person auf weniger als die 
                                        Risikotoleranz über die angegebene kumulative Expositionszeit ein.''')],
                                       className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["*Die Richtlinie schränkt die Wahrscheinlichkeit einer luftgetragenen ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="Übertragung",
                                                         target='_blank'), ),
                                        html.Span(''' auf eine bestimmte Person auf weniger als die Risikotoleranz 
                                        über die angegebene kumulative Expositionszeit ein.''')],
                                       className='airborne-text')

airb_trans_only_disc = html.Div('''''', className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''Um Ihre lokale Prävalenz abzuschätzen, können Sie hier hilfreiche 
                                Informationen finden: '''),
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
n_input_text_1 = "Wenn sich in diesem Raum "
n_max_base_string = ' {:.0f} Personen'
n_max_overflow_base_string = ' >{:.0f} Personen'
n_input_text_2 = " Personen aufhalten, würde der Richtwert nach "
n_input_text_3 = " Stunden verletzt werden."

t_input_text_1 = "Falls sich die Personen etwa "
t_input_text_2 = " Stunden hier aufhalten, sollte die Raumbelegung auf "
t_input_text_3 = " limitiert werden."

# About
about_header = "Über das Projekt"
about = html.Div([
    html.H6("Über das Projekt", style={'margin': '0'}),
    html.Div('''Um die Ausbreitung von COVID-19 einzudämmen, empfehlen offizielle Richtlinien Begrenzungen bei: 
    Abstand zu anderen Personen (2 Meter), maximale Belegungsdauer (15 Minuten), maximale Personenbelegung (25 
    Personen) oder Mindestbelüftung (sechs Luftaustausche pro Stunde).'''),
    html.Br(),
    html.Div([html.Span(''''''),
              # html.A(children="scientific evidence",
              #        href=link_docs,
              #        target='_blank'),
              html.Span('''Es gibt zunehmend den wissenschaftlichen Nachweis für die luftgetragene Aerosolübertragung 
              von COVID-19, welche stattfindet, wenn infektiöse Aerosoltröpfchen durch gemeinsames Atmen von 
              Innenraumluft übertragen werden. Während öffentliche Gesundheitsorganisationen nun erst beginnen, 
              sich mit Aerosolübertragung zu beschäftigen, müssen sie jetzt bereits Sicherheitsrichtlinien zur 
              Verfügung stellen, welche alle relevanten Variablen berücksichtigen.  ''')]),
    html.Br(),
    html.Div([html.Span(''''''),
              # html.A(children="theoretical model",
              #        href=link_paper,
              #        target='_blank'),
              html.Span('''Diese App, entwickelt von Kasim Khan in Zusammenarbeit mit Martin Z. Bazant und John W. M. 
              Bush, verwendet ein theoretisches Modell, um die maximale, sichere Expositionszeit und die Höhe der 
              Personenbelegung in Innenräumen zu ermitteln. Durch Angabe der Raumspezifikationen, der Belüftungs- und 
              Filtrationsraten, die Art des Tragens von Mund-Nasen-Bedeckungen, die Atemaktivität und die 
              Risikotoleranz kann gezeigt werden, wie die Übertragung von COVID-19 in verschiedenen Innenräumen 
              minimiert werden kann.''')]),
    html.Br(),
    html.Div([html.Span('''Die Wissenschaft hinter der App wird auch in einem kostenlosen Massive Open Online Course 
    (MOOC) auf ecX vermittelt: '''),
              html.A(children="10.S95x Physics of COVID-19 Transmission",
                     href=links.link_mooc,
                     target='_blank')])
])

# Room Specifications
room_header = "Raumspezifikationen - Details"

floor_area_text = "Gesamte Raumfläche (sq. ft.): "
floor_area_text_metric = "Gesamte Raumfläche (m²): "
ceiling_height_text = "Durchschnittliche Raumhöhe (ft.): "
ceiling_height_text_metric = "Durchschnittliche Raumhöhe (m): "

ventilation_text = "Belüftungssystem: "
vent_type_output_base = "{:.1f} ACH"
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (ACH draußen)"])
ventilation_text_adv = html.Span(["Belüftungssystem (hr", html.Sup("-1"), ", ACH draußen): "])
ventilation_types = [
    {'label': "Geschlossene Fenster", 'value': 0.3},
    {'label': "Geöffnete Fenster", 'value': 2},
    {'label': "Technische Belüftung", 'value': 3},
    {'label': "Geöffnete Fenster mit Lüfter", 'value': 6},
    {'label': "Bessere technische Belüftung", 'value': 8},
    {'label': "Labor, Restaurant", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Krankenhaus/U-Bahnwagen", 'value': 18},
    {'label': "Gefahrenstofflabor/Flugzeug", 'value': 24},
]

filtration_text = "Luftfiltersystem: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Luftfiltersystem (MERV): "
filter_types = [
    {'label': "Kein", 'value': 0},
    {'label': "Fensterklimagerät", 'value': 2},
    {'label': "Stationär/Kommerziell/Industriell", 'value': 6},
    {'label': "Stationär/Kommerziell/Krankenhaus", 'value': 10},
    {'label': "Krankenhaus & allgemeiner Behandlungsraum", 'value': 14},
    {'label': "Schwebstofffilter (HEPA)", 'value': 17}
]

recirc_text = "Umwälzrate: "
recirc_type_output_base = "{:.1f} Luftwechselrate"
recirc_text_adv = "Umwälzrate (Luftwechselrate): "
recirc_types = [
    {'label': "Keine", 'value': 0},
    {'label': "Langsam", 'value': 0.3},
    {'label': "Moderat", 'value': 1},
    {'label': "Schnell", 'value': 10},
    {'label': "Flugzeug", 'value': 24},
    {'label': "U-Bahnwagen", 'value': 54},
]

humidity_text = "Relative Luftfeuchtigkeit: "
humidity_marks = {
    0.01: {'label': '1%: Sehr trocken', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: Flugzeug', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Trocken'},
    0.6: {'label': '60%: Durchschnittlich'},
    0.99: {'label': '99%: Sehr feucht'},
}

need_more_ctrl_text = '''Sie möchten mehr Kontrolle über Ihre Eingabeparameter? Wechseln Sie zum erweiterten Modus, 
indem Sie das Dropdown-Menü oben auf der Webseite nutzten.'''

human_header = "Menschliches Verhalten - Details"
# Human Behavior
exertion_text = "Atemfrequenz: "
exertion_types = [
    {'label': "Ruhend", 'value': 0.49},
    {'label': "Stehend", 'value': 0.54},
    {'label': "Singend", 'value': 1},
    {'label': "Leichte Tätigkeit", 'value': 1.38},
    {'label': "Moderate Tätigkeit", 'value': 2.35},
    {'label': "Schwere Tätigkeit", 'value': 3.30},
]

breathing_text = "Atemaktivität: "
expiratory_types = [
    {'label': "Atmen (flach)", 'value': 1.1},
    {'label': "Atmen (normal)", 'value': 4.2},
    {'label': "Atmen (schwer)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Sprechen (Flüstern)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Sprechen (normal)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Sprechen (laut)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Singen", 'value': 970},
]

mask_type_text = "Filtrationseffizienz der Mund-Nasen-Bedeckung (Maskentyp): "
mask_type_marks = {
    0: {'label': "0% (Kein, Gesichtsvisier)", 'style': {'max-width': '75px'}},
    0.5: {'label': "50% (Baumwolle, Flanell)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (Mehrlagige Baumwolle, Seide)", 'style': {'max-width': '75px'}},
    0.90: {'label': "90% (Chirurgische Einwegartikel)", 'style': {'max-width': '75px'}},
    # 0.99: {'label': "99% (N95 Atemschutzmaske)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Kein, Gesichtsvisier", 'value': 0},
    {'label': "Baumwolle, Flanell", 'value': 0.5},
    {'label': "Mehrlagige Baumwolle, Seide", 'value': 0.7},
    {'label': "Chirurgische Einwegartikel", 'value': 0.9},
    {'label': "N95 Atemschutzmaske", 'value': 0.99},
]

mask_fit_text = "Passform der Mund-Nasen-Bedeckung / Befolgung der Tragepflicht: "
mask_fit_marks = {
    0: {'label': '0%: Nicht gegeben', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Schlecht'},
    0.95: {'label': '95%: Gut'}
}

risk_tolerance_text = "Risikotoleranz: "
risk_tol_desc = html.Div('''Risikogruppen, wie älterer Menschen oder Menschen mit Vorerkrankungen, erfordern eine 
geringere Risikotoleranz. Eine hohe Risikotoleranz bedeutet eine wahrscheinlichere Übertragung in der angenommenen 
Belegungssituation (für Details siehe FAQ).''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})
risk_tol_marks = {
    # 0.01: {'label': '0.01: Sicherer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Sicher', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Unsicher'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Frequently Asked Questions (FAQ)"
other_io = "Weitere Parameter"

faq_top = html.Div([
    html.H6("Frequently Asked Questions"),
    html.H5("Wieso sind 6 Feet/2 m Abstand nicht ausreichend?"),
    html.Div([
        html.Div([html.Span('''6-Fuß- (oder 2-Meter-) Abstand schützen Sie vor großen Tropfen, die von einer 
        infizierten Person beim Husten ausgestoßen werden, ebenso wie Mund-Nasen-Bedeckungen; er schützt allerdings 
        nicht vor der '''),
                  html.A(children="Übertragung",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' durch infektiöse Aerosole, die in der Luft schweben und sich im Raum verteilen. In 
                  Innenräumen sind Personen mit einem Abstand von 60 Fuß nicht sicherer vor einer Übertragung durch 
                  die Luft als mit einem Abstand von 6 Fuß.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Gibt es andere Arten von Übertragungswegen?"),
    html.Div([
        html.Div([html.A(children="Luftgetragene Aerosolübertragung",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' ist als dominierender Übertragungsweg von COVID-19 angenommen, allerdings sind auch 
                  andere Übertragung möglich, wie beispielsweise die Kontaktübertragung durch direkten Kontakt von 
                  kontaminierten Oberflächen, Übertragung durch größere Tröpfchen ausgestoßen durch Husten oder 
                  Niesen und Kurzdistanzübertragung durch Atemaerosol einer infizierten Person über einen anhaltenden 
                  Zeitraum. Obwohl die beiden letzt genannten Übertragungswege durchaus signifikant sind, können sie 
                  durch Tragen eines Mund-Nasen-Schutzes weitgehend eliminiert werden; allerdings bleibt das Risiko 
                  durch luftgetragenen Aerosolinfektion.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Können wir wirklich von einer gut durchmischten Raumluft ausgehen?"),
    html.Div([
        html.Div([html.Span('''Es gibt eine Vielzahl an Quellen, die zur Durchmischung der Raumluft beitragen, 
        wie auftriebsgetriebene Ströme (von Heizkörpern, Luftbefeuchtern oder Fenstern ausgehend), erzwungenen 
        Konvektion durch Belüftungssysteme oder Ventilatoren sowie menschliche Bewegung und Atmung. Neben Ausnahmen, 
        die im '''),
                  html.A(children="Paper",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''' diskutiert werden, ist die Annahme von gut durchmischter Raumluft in der theoretischen 
                  Modellierung von luftgetragener Infektionsübertragung weit verbreitet. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Ist diese Richtline auch für sehr große Räume gültig?"),
    html.Div([
        html.Div([html.Span('''In Konzerthallen, Stadien oder anderen, großen, belüfteten Räume mit einer hohen 
        Personenanzahl ist das Risiko für luftgetragenen Aerosolübertragung signifikant und wird gut durch diese 
        Richtlichtlinie mit abgedeckt. Allerding gibt es ein zusätzliches Risiko an Kurzdistanzübertragung durch 
        ausgestoßene Atemluft, wenn keine Mund-Nasen-Bedeckungen oder Gesichtsvisiere getragen werden (Bewertung im 
        '''),
                  html.A(children="Paper",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''').''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Wieso ist die Deckenhöhe von Bedeutung?"),
    html.Div([
        '''Die Deckenhöhe bestimmt das Raumvolumen, welches erforderlich ist, um die Konzentration des infektiösen 
        Aerosols (# Aerosol pro Volumeneinheit) zu ermitteln. Diese Konzentration wird für die Bestimmung des 
        Übertragungsrisikos von COVID-19 innerhalb des Raums benötigt.'''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Ich kenne meine ACH/MERV Kennzahlen. Wo kann ich diese angeben?"),
    html.Div('''
        Falls Sie eine bessere Kontrolle über die Input-Werte haben möchten, wechseln Sie zum erweiterten Modus, indem 
        sie das Dropdown-Menü oben auf der Webseite nutzen.
    ''', className='faq-answer'),
    html.Br(),
    html.H5("Warum haben N95-Atemschutzmasken eine Wirksamkeit von 99%?"),
    html.Div('''N95-Atemschutzmasken haben eine Filterwirksamkeit von mindestens 95 % bei Partikelgrößen von 0,3 μm, 
    die 10-mal kleiner sind als die Tropfengrößen bei der luftgetragenen COVID-19-Übertragung. Bei größeren Tropfen 
    sind N95-Atemschutzmasken sogar noch effizienter und nähern sich Werten nahe 100 % an.''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Gibt es versteckte Parameter im Grundmodus?"),
    html.Div([html.Span('''Alle relevanten physikalischen Parameter sind im '''),
              html.A(children="Paper",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' einzeln aufgeführt. Im Grundmodus wird von einem effektiven Standardaerosolradius von 2 μm 
              ausgegangen (bei 60% Luftfeuchte) und einer maximalen Virusinaktivierungsrate von 0,6 /Stunde (bei 100% 
              Luftfeuchte). Beides steigt mit erhöhter relativer Luftfeuchtigkeit (RF). Die Bestimmung der 
              Virusinaktivierungsrate orientiert sich an einer eher konservativen Abschätzung, die zu leichtfügig 
              geringeren Werten der Inaktivierung führt. Die virale Inaktivierungsrate kann durch Ultraviolette 
              Bestrahlung (UV-C) oder chemische Desinfektionsmittel (z. B. Wasserstoffperoxid, Ozon) gesteigert 
              werden. Die App ermittelt zudem als Schlüsselparameter die Infektiosität der ausgestoßenen Luft, C'''),
              html.Sub("q"),
              html.Span(''' (Infektionsmenge pro Volumeneinheit), ausgehend von der Ermittlung der spezifischen 
              Atemaktivität unter Verwendung der Tabellenwerten aus Abbildung 2 des '''),
              html.A(children="Papers",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. Im erweiterten Modus können diese Parameter selbstständig festgelegt werden.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Effektiver Aerosolradius (bei RH = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Maximale Virusinaktivierungsrate (bei RH = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

pop_immunity_header = "Immunität der Bevölkerung: "
perc_immune_label = html.Span(["Prozentsatz immun p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["Prozentsatz infektiös p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["Prozentsatz geimpft p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["Prozentsatz früher infiziert p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["Prozentsatz anfälliger Personen p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''Der infektiöse Prozentsatz p''', html.Sub('i'), ''' in der Bevölkerung 
errechnet sich aus der zum Risikoszenario angegebenen infektösen Prävalenz (Gegeben durch die Prävalenz der 
Infektion..., Um mein persönliches Risiko zu begrenzen...).  Der Prozentsatz der Immunität  p''', html.Sub('im'),
                                        ''' kann grob aus dem Impfprozentsatz der Bevölkerung plus der Gesamtfallrate 
                                        in der Bevölkerung geschätzt werden, indem der Beitrag der unentdeckten Fälle 
                                        vernachlässigt wird. Diese beiden Werte werden verwendet, 
                                        um den empfänglichen Prozentsatz p''', html.Sub('s'), ''' zu berechnen. Im 
                                        Basismodus und im ersten Risikomodus (Wenn eine infizierte Person 
                                        eintritt...) wird dieser Wert mit 100 % angenommen. risk mode (If an infected 
                                        person enters…), this value is assumed to be 100%.''']),
                              html.Br(),
                              html.Div(['''Hier sind einige hilfreiche Links, um p''', html.Sub('i'), ''' und p''',
                                        html.Sub('im'), ''' zu ermitteln: ''',
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

values_interest_header = "Berechnete Werte"
values_interest_desc = html.Div([
    html.H5("Was genau berechnet die App?"),
    html.Div([
        html.Div([html.Span('''Die App berechnet die maximal zulässige kumulative Expositionszeit, das Produkt aus 
        Raumbelegung und Zeit, in einem Innenraum. Die Ausbreitung von COVID-19 wird dadurch begrenzt, 
        dass die erwartete Anzahl von Übertragungen pro infizierter Person, die "Indoor-Reproduktionszahl", 
        kleiner als die gewählte Risikotoleranz sein muss. Die App berechnet auch verwandte Größen, 
        die im verwiesenen '''),
                  html.A(children="Paper",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''' definiert und möglicherweise von Interesse sind:''')]),
    ], className='faq-answer'),
])
relative_sus_label = html.Span(["Relative Anfälligkeit s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["Anteil an Frischluft Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Aerosolfiltrationseffizienz p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Luftstromrate beim Atmen Q", html.Sub('b'), ": "])
cq_label = html.Span(["Infektiosität der ausgestoßenen Luft C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Durchtrittswahrscheinlichkeit durch Maske p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Raumvolumen V: "])
vent_rate_Label = html.Span(["Belüftungsrate mit Außenluft Q: "])
recirc_rate_label = html.Span(["Luftumwälzungsrate Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Luftfiltrationsrate (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Luftfeuchtigkeitsabhängiger Aerosolradius r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Luftfeuchigkeitsabhängige virale Inaktivierungsrate \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Effektive Aerosolsedimentationsgeschwindigkeit v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Konzentrationsrelaxationsgeschwindigkeit \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Luftgetragene Aerosolübertragungsrate \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Berücksichtigt das Modell die Verbreitung der Infektion in der lokalen Bevölkerung?"),
    html.Div(['''Der Einfluss der Prävalenz der Infektion in der lokalen Bevölkerung kann im erweiterten Modus 
    berücksichtigt werden. Dort kann man in der Registerkarte Weitere Parameter auch den Einfluss der Immunität in 
    der Bevölkerung abschätzen, die durch Impfungen oder frühere Infektionen entstehen kann.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("Weitere Fragen?"),
    html.Div([html.Span('''Für weiterführende Erklärungen und Referenzen siehe "'''),
              html.A(children="Beyond 6 Feet",
                     href=link_paper,
                     target='_blank'),
              html.Span('''" und die Links, die oben auf der Webseite aufgeführt sind.''')]),
])

footer = html.Div([
    html.Div([html.Span('''Die COVID-19 Innenraumsicherheitsrichtlinie ein Werkzeug entwickelt zur für den Zweck, 
    dem interessierten Anwender mit den Faktoren, die die luftgetragenen Aerosolübertragung von COVID-19 
    beeinflussen, vertraut zu machen und die quantitative Risikobewertung für Infektion für verschiedenen Umgebungen 
    zu unterstützten. Wir merken an, dass Unsicherheiten und intrinsische Variabilität der Modellparameter 
    möglichweise zu Ungenauigkeiten führen, deren Ausmaß innerhalb einer Größenordnung liegt, die durch Wählen einer 
    ausreichend kleinen Risikotoleranz ausgeglichen wird. Unsere Richtlinie berücksichtigt nicht die 
    Kurzdistanzübertragung durch Atemluft, welche das Risiko, wenn kein Mund-Nasen-Schutz getragen wird, wesentlich 
    erhöht, diskutiert im beigefügten '''),
              html.A(children="Paper",
                     href=link_paper,
                     target='_blank'),
              html.Span('''(Bazant & Bush, 2020). Die Verwendung der COVID-19 Innenraumsicherheitsrichtlinie 
              unterliegt der Eigenverantwortung des Anwenders. Sie ist öffentlich verfügbar ohne eine Garantie oder 
              Gewährleistung jeglicher Art. Die Autoren übernehmen keine Haftung für ihre Verwendung.''')]),
    html.Br(),
    html.Div("Besonderen Dank an: ")
], className='footer-small-text')
