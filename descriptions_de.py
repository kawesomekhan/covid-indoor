import dash_html_components as html

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
    "merv": "Fehler: Luftfiltersystem (MERV) kann nicht leer sein."
}

# Main Panel Text
curr_room_header = "Aktueller Raum: "
presets = [
    {'label': "Benutzerdefiniert", 'value': 'custom'},
    {'label': "Haus im Stadtrandgebiet", 'value': 'house'},
    {'label': "Restaurant", 'value': 'restaurant'},
    {'label': "Leises Büro", 'value': 'office'},
    {'label': "Klassenzimmer", 'value': 'classroom'},
    {'label': "New Yorker U-Bahn-Wagen", 'value': 'subway'},
    {'label': "Boeing 737", 'value': 'airplane'},
    {'label': "Kirche", 'value': 'church'},
]

main_panel_s1 = "Basierend auf diesem Modell, sollte die Situation im Raum sicher sein bei: "

units_hr = 'Stunden'
units_min = 'Minuten'
units_days = 'Tage'

units_hr_one = 'Stunden'
units_min_one = 'Minuten'
units_day_one = 'Tage'

is_past_recovery_base_string = '{n_val} Personen für >{val:.0f} Tage,'
model_output_base_string = '{n_val} Personen für '

main_panel_six_ft_1 = "Beachte, dass die 2 m-Distanzrichtlinie besagt, dass bis zu "
main_panel_six_ft_2 = " in diesem Raum für eine unbegrenzte Zeitdauer sicher wären."

six_ft_base_string = ' {} Personen'
six_ft_base_string_one = ' {} Personen'

graph_title = "Raumbelegungsdauer vs. Expositionszeit"
graph_xtitle = "Maximale Expositionszeit \u03C4 (Stunden)"
graph_ytitle = "Maximale Personenbelegung N"
transient_text = "Instationärer Zustand"
steady_state_text = "Stationärer Zustand"

main_airb_trans_only_disc = html.Div(["Die Richtlinie basiert auf der Betrachtung der luftgetragenen ",
                                      html.Span(html.A(href='https://www.nature.com/articles/d41586-020-02058-1',
                                                       children="Aerosolübertragung",
                                                       target='_blank'), ),
                                      html.Span(''' ausgehend von einer einzelnen, infizierten Person über die 
                                      angegebene kumulative Expositionszeit.  ''')], className='airborne-text')

airb_trans_only_disc = html.Div('''Die Richtlinie basiert auf der Betrachtung der luftgetragenen 
Aerosolübertragung ausgehend von einer einzelnen, infizierten Person über die angegebene kumulative Expositionszeit.  
''', className='airborne-text')

# Bottom panels text
n_input_text_1 = "Falls sich in diesem Raum "
n_max_base_string = ' {:.0f} Personen'
n_input_text_2 = " Personen befinden, sind diese für "
n_input_text_3 = " sicher."

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
])

# Room Specifications
room_header = "Raumspezifikationen"

floor_area_text = "Gesamte Raumfläche (sq. ft.): "
floor_area_text_metric = "Gesamte Raumfläche (m²): "
ceiling_height_text = "Durchschnittliche Raumhöhe (ft.): "
ceiling_height_text_metric = "Durchschnittliche Raumhöhe (m): "

ventilation_text = "Belüftungssystem: "
vent_type_output_base = "{:.0f} ACH"
ventilation_text_adv = "Belüftungssystem (ACH): "
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
    0: {'label': '0%: Sehr trocken', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: Flugzeug', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Trocken'},
    0.6: {'label': '60%: Durchschnittlich'},
    0.99: {'label': '99%: Sehr feucht'},
}

need_more_ctrl_text = '''Sie möchten mehr Kontrolle über Ihre Eingabeparameter? Wechseln Sie zum erweiterten Modus, 
indem Sie das Dropdown-Menü oben auf der Webseite nutzten.'''

human_header = "Menschliches Verhalten"
# Human Behavior
exertion_text = "Betätigungslevel: "
exertion_types = [
    {'label': "Ruhend", 'value': 0.49},
    {'label': "Stehend", 'value': 0.54},
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
    0: {'label': "0% (Keine, Gesichtsvisier)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (Grob gewebte Baumwolle)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (Seide, Flannel, Chiffon)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (Chirurgisch, Baumwolle)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (N95-Maske)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Keine, Gesichtsvisier", 'value': 0},
    {'label': "Grob gewebte Baumwolle", 'value': 0.1},
    {'label': "Seide, Flannel, Chiffon", 'value': 0.5},
    {'label': "Chirurgisch, Baumwolle", 'value': 0.75},
    {'label': "N95-Maske", 'value': 0.95},
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
    0.01: {'label': '0.01: Sicherer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Sicher', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Unsicher'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Frequently Asked Questions (FAQ)"
other_io = "Weitere Inputs & Outputs"

faq_top = html.Div([
    html.H6("Frequently Asked Questions"),
    html.H5("Wieso sind 6 Feet/2 m Abstand nicht ausreichend?"),
    html.Div([
        html.Div([html.Span(''''''),
                  # html.A(children="airborne transmission",
                  #        href=link_docs,
                  #        target='_blank'),
                  html.Span('''6 Feet/2 m Abstand schützen vor großen Tröpfchen, die durch Husten von infizierten 
                  Personen ausgestoßen werden, wie es auch der Mund-Nasen-Schutz tut. Allerdings schützt der Abstand 
                  nicht vor luftgetragene Übertragung durch infektiöse Aerosole, welche in der Luft schweben und sich 
                  in der gesamten Raumluft verteilen können. Innerhalb von Räumen sind Personen mit 20 m Abstand 
                  nicht geschützter vor Aerosolübertragung als Personen mit 2 m Abstand.''')]),
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

values_interest_header = ""
values_interest_desc = html.Div([
    html.H5("Was genau berechnet die App?"),
    html.Div([
        html.Div([html.Span('''Eine gegebene Risikotoleranzen berücksichtigend berechnet die App die maximale 
        kumulative Aufenthaltsdauer, sowie das Produkt aus Personenbelegung und Raumbelegungsdauer in Anwesenheit 
        einer infizierten Person. Die App ermittelt außerdem die folgenden Größen, die im '''),
                  html.A(children="Paper",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''' definiert und gegebenenfalls von Interesse sind:''')]),
    ], className='faq-answer'),
])
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
    html.Div(['''Nein. Das Modell ermittelt das Risiko der Übertragung ausgehend von einer einzelnen, infizierten 
    Person. Damit ist impliziert, dass die Verbreitung der Infektion innerhalb der Bevölkerung relative gering ist. 
    Innerhalb dieser Grenzen steigt das Übertragungsrisiko mit der erwarteten Anzahl an infizierten Personen in einem 
    Raum, genauer das Produkt an Raumbelegung und Verbreitung innerhalb der Bevölkerung. Die Toleranz sollte somit im 
    Verhältnis zum Wert der erwarteten infizierten Personen gesenkt werden, falls dieser eins übersteigt. Umgekehrt, 
    kann die Toleranz proportional erhöht werden, wenn die erwartete Anzahl an infizierten Personen innerhalb des 
    Raums Null annähert, bis die empfohlenen Restriktionen als nicht mehr erforderlich erachtet werden.'''],
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
