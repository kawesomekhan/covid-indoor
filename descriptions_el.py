import dash_html_components as html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions: Greek

"""

# Header
header = html.Div([
    html.H1(children='COVID-19 - Οδηγίες ασφάλειας εσωτερικού χώρου'),
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
        html.Div([html.Span(["Beyond Six Feet: A Guideline to Limit Indoor Airborne Transmission of COVID-19 ("]),
                  html.Span(html.A(href=links.link_paper,
                                   target='_blank',
                                   children='''Bazant & Bush, 2020''')),
                  html.Span(")")]),
        html.Div([html.Span(["Monitoring carbon dioxide to quantify the risk of indoor airborne transmission of COVID-19 ("]),
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
language_dd = "Γλώσσα: "

# Unit systems
units_dd = "Μονάδες: "
unit_settings = [
    {'label': "Αγγλικό σύστημα", 'value': "british"},
    {'label': "Μετρική", 'value': "metric"},
]

# Modes
mode_dd = "Κατηγορία λειτουργίας: "
app_modes = [
    {'label': "Απλή", 'value': "basic"},
    {'label': "Για προχωρημένους", 'value': "advanced"},
]

output_mode_dd = "Output Mode: "
output_modes = [
    {'label': "Safe Occupancy", 'value': "occupancy"},
    {'label': "Safe CO\u2082 Level", 'value': "co2"},
]

error_list = {
    "floor_area": "Σφάλμα: Πρέπει να εισαχθεί η επιφάνεια του δαπέδου.",
    "ceiling_height": "Σφάλμα: Πρέπει να εισαχθεί το ύψος της οροφής.",
    "recirc_rate": "Σφάλμα: Πρέπει να εισαχθεί ο ρυθμός ανακυκλοφορίας του αέρα",
    "aerosol_radius": "Σφάλμα: Πρέπει να εισαχθεί η ακτίνα των μικρό-σταγονιδίων.",
    "viral_deact_rate": "Σφάλμα: Πρέπει να εισαχθεί ο ρυθμός απενεργοποίησης των ιών.",
    "n_max_input": "Σφάλμα: Ο αριθμός των ατόμων δεν μπορεί να είναι κάτω από 2.",
    "exp_time_input": "Σφάλμα: Ο χρόνος έκθεσης πρέπει να είναι μεγαλύτερος από το 0.",
    "air_exchange_rate": "Σφάλμα: Ο ρυθμός εξαερισμού πρέπει να είναι μεγαλύτερος από το 0.",
    "merv": "Σφάλμα: Το σύστημα φιλτραρίσματος δεν μπορεί να είναι κενό.",
    "prevalence": "Σφάλμα: Η συχνότητα πρέπει να είναι μεγαλύτερη από 0 και μικρότερη από 100.000.",
    "atm_co2": "Σφάλμα: Πρέπει να εισαγάγετε το ιστορικό συγκέντρωσης CO₂"
}


# Main Panel Text
curr_room_header = "Προδιαγραφές δωματίου: "
presets = [
    {'label': "Προσαρμοσμένη επιλογή", 'value': 'custom'},
    {'label': "Αίθουσα διδασκαλίας", 'value': 'classroom'},
    {'label': "Σαλόνι", 'value': 'living-room'},
    {'label': "Εκκλησία", 'value': 'church'},
    {'label': "Εστιατόριο", 'value': 'restaurant'},
    {'label': "Γραφείο", 'value': 'office'},
    {'label': "Βαγόνι μετρό", 'value': 'subway'},
    {'label': "Αεροπλάνο", 'value': 'airplane'},
]

curr_human_header = "Συμπεριφορά ανθρώπων: "
presets_human = [
    {'label': "Προσαρμοσμένη επιλογή", 'value': 'custom'},
    {'label': "Με μάσκες, αδρανείς", 'value': 'masks-1'},
    {'label': "Με μάσκες, Μιλώντας", 'value': 'masks-2'},
    {'label': "Με μάσκες, κάνοντας άσκηση", 'value': 'masks-3'},
    {'label': "Χωρίς μάσκες, σε ξεκούραση", 'value': 'no-masks-1'},
    {'label': "Χωρίς μάσκες, Μιλώντας", 'value': 'no-masks-2'},
    {'label': "Χωρίς μάσκες, κάνοντας άσκηση", 'value': 'no-masks-3'},
    {'label': "Χωρίς μάσκες, κάνοντας άσκηση", 'value': 'singing-1'},
]

curr_risk_header = "Αποδεκτό εύρος ανοχής κινδύνου: "
# presets_risk = [
#     {'label': "Low", 'value': 0.01},
#     {'label': "Medium", 'value': 0.1},
#     {'label': "High", 'value': 1},
# ]
risk_tol_marks = {
    # 0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Ασφαλέστερο', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Μη ασφαλές'}
}

risk_tolerance_text = "Αποδεκτό εύρος ανοχής κινδύνου: "
risk_tol_desc = html.Div('''More vulnerable populations such as the elderly or those with preexisting medical 
conditions require a lower risk tolerance (~0.01). A higher risk tolerance will mean more expected 
transmissions during the expected occupancy period (see FAQ for details).''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})

curr_age_header = "Ηλικιακή ομάδα: "
presets_age = [
    {'label': "Παιδιά (<15 ετών)", 'value': 0.23},
    {'label': "Ενήλικες (15-64 ετών)", 'value': 0.68},
    {'label': "Ηλικιωμένοι (> 64 ετών)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: Παιδιά (<15 ετών)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: Ενήλικες (15-64 ετών)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: Ηλικιωμένοι (> 64 ετών)', 'style': {'width': '75px'}}
}

curr_strain_header = "Ιικό στέλεχος: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2 (στέλεχος Γουχάν)", 'value': 1},
    {'label': "SARS-CoV-2 - B.1.1.7 (Βρετανικό στέλεχος)", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: Γουχάν', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: B.1.1.7/UK'}
}

pim_header = "Ποσοστό ανοσοποίησης: "
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "Εάν ένα μολυσμένο άτομο εισέλθει…"
risk_prevalence_desc = "Δεδομένης της συχνότητας μολύνσεων…"
risk_personal_desc = "Για να περιορίσω τον προσωπικό μου κίνδυνο…"
risk_options = [
    {'label': risk_conditional_desc, 'value': 'conditional'},
    {'label': risk_prevalence_desc, 'value': 'prevalence'},
    {'label': risk_personal_desc, 'value': 'personal'},
]
risk_personal_warning = html.Span([
    html.Span('''Προειδοποίηση: ''', style={'font-weight': 'bold'}),
    html.Span('''η επιλεγμένη λειτουργία κινδύνου (Για να περιορίσω τον προσωπικό μου κίνδυνο ...) εξετάζει την 
    πιθανότητα μόλυνσης ενός συγκεκριμένου ατόμου. Είναι επομένως πολύ λιγότερο περιοριστική 
    και δεν πρέπει να χρησιμοποιείται για τη θέσπιση γενικών οδηγιών ασφάλειας.''')])

risk_mode_panel_header = "Πεδίο ρίσκου"
occupancy_panel_header = "Υπολογισμός ασφαλούς πληρότητας αίθουσας"
main_panel_s1 = '''Για να περιορίσετε τη μετάδοση COVID-19 * όταν ένα μολυσμένο άτομο εισέλθει σε αυτόν τον χώρο, 
δεν πρέπει να υπάρχουν περισσότερα από:'''

main_panel_s1_b = html.Span([
    html.Span('''Για τον περιορισμό της μετάδοσης COVID-19 * σε έναν πληθυσμό με συχνότητα λοίμωξης'''),
    html.Sup('''1'''),
    html.Span(''' ''')
])
main_panel_s2_b = ''' ανά 100.000, αυτός ο χώρος δεν πρέπει να έχει περισσότερο από: '''

main_panel_s1_c = html.Span([
    html.Span('''To limit my chance of being infected by COVID-19 in a population with an infection prevalence'''),
    html.Sup('''1'''),
    html.Span(''' of ''')
])
main_panel_s2_c = ''' per 100,000, this space should have no more than: '''

units_hr = 'ώρες'
units_min = 'λεπτά'
units_days = 'ημέρες'
units_months = 'mήνες'

units_hr_one = 'ώρα'
units_min_one = 'λεπτά'
units_day_one = 'mέρες'
units_month_one = 'mήνας'

is_past_recovery_base_string = '{n_val} άτομα για >{val:.0f} ημέρες,'
model_output_base_string = '{n_val} άτομα για '
model_output_base_string_co2 = '{co2:.2f} ppm for '
nt_bridge_string = " άτομα για "
tn_bridge_string = " για "

main_panel_six_ft_1 = "Αντίθετα, η απόσταση των έξι ποδιών (ή δύο μέτρων) θα περιορίσει την χωρητικότητα σε "
main_panel_six_ft_2 = " που θα παραβίαζαν την οδηγία * μετά από "

six_ft_base_string = ' {} άτομα'
six_ft_base_string_one = ' {} άτομα'

graph_title = "Πληρότητα έναντι χρόνου έκθεσης"
graph_xtitle = "Μέγιστος χρόνος έκθεσης \u03C4 (ώρες)"
graph_ytitle = "Μέγιστη πληρότητα N"
transient_text = "Χρονικά μεταβαλλόμενος"
steady_state_text = "Σταθερός"
co2_safe_trace_text = "Κατώφλι αναπνευστικής ασφάλειας"
guideline_trace_text = "Κατευθυντήρια γραμμή"
background_co2_text = "Ιστορικό CO₂: "
recommended_co2_text = "Προτεινόμενο όριο"

graph_title_co2 = "Ασφαλής συγκέντρωση CO₂ (ppm) έναντι χρόνου έκθεσης"
graph_ytitle_co2 = "Συγκέντρωση CO₂ (ppm)"

co2_title = "Υπολογίστε την ασφαλή συγκέντρωση CO₂"
co2_param_desc = '''Η κατευθυντήρια γραμμή για τις παραμέτρους που επιλέξατε παραπάνω εκφράζεται εδώ ως όριο 
συγκέντρωσης CO₂.'''
co2_prev_input_1 = html.Span(["Συχνότητα", html.Sup('1'), html.Span(": ")])
co2_prev_input_2 = " ανά 100,000"
co2_atm_input_1 = background_co2_text
co2_atm_input_2 = " ppm"
co2_calc_1 = "Για χρόνο έκθεσης "
co2_calc_2 = " ωρών, η υπολογισμένη ασφαλής σταθερή συγκέντρωση CO₂ σε αυτόν τον χώρο είναι "
co2_calc_3 = "."
co2_base_string = '{:,.2f} ppm'

co2_safe_sent_1 = "This limit exceeds that for healthy respiratory activity, which is "
co2_safe_sent_2 = "."

co2_safe_footer = html.Span(['''Το κατώφλι της αναπνευστικής ασφάλειας παρεμβάλλεται βάσει των ''',
                             html.A(href=links.link_usda_co2,
                                    children='''συνιστώμενων ορίων από το USDA''',
                                    target='_blank'),
                             '''.'''])

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

other_risk_modes_desc = html.Div('''Άλλα σενάρια κινδύνου λαμβάνονται υπόψη στη λειτουργία για προχωρημένους. 
Συγκεκριμένα, μπορεί κανείς να εξετάσει την συχνότητα της λοίμωξης στον πληθυσμό, 
την ανοσία που αποκτήθηκε μέσω εμβολιασμού ή προηγούμενης έκθεσης, και τον κίνδυνο 
για ένα συγκεκριμένο άτομο.''')

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
                                html.Span('''Για να εκτιμήσετε την τοπική σας συχνότητα, ακολουθούν ορισμένοι 
                                χρήσιμοι πόροι: '''),
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
n_input_text_1 = "Εάν αυτό το δωμάτιο έχει "
n_max_base_string = ' {:.0f} άτομα'
n_max_overflow_base_string = ' >{:.0f} άτομα'
n_input_text_2 = " άτομα, οι παρευρισκόμενοι θα είναι ασφαλείς για "
n_input_text_3 = "."

t_input_text_1 = "Εάν οι άνθρωποι περνούν περίπου "
t_input_text_2 = " ώρες εδώ, η πληρότητα θα πρέπει να περιοριστεί στα "
t_input_text_3 = "."

# About
about_header = "Σχετικές Πληροφορίες"
about = html.Div([
    html.H6("Σχετικές Πληροφορίες", style={'margin': '0'}),
    html.Div('''Για να μετριαστεί η εξάπλωση του COVID-19, οι οργανισμοί δημόσιας υγείας έχουν επισήμως προτείνει όρια για: την απόσταση από άτομο σε άτομο (6 πόδια / 2 μέτρα), τον χρόνο πληρότητας αιθουσών (15 λεπτά), την μέγιστη πληρότητα (25 άτομα) ή τον ελάχιστο εξαερισμό (6 αλλαγές ανά ώρα).'''),
    html.Br(),
    html.Div([html.Span('''Υπάρχουν αυξανόμενα '''),
              html.A(children="επιστημονικά στοιχεία",
                     href=links.link_docs,
                     target='_blank'),
              html.Span(''' που υποδεικνύουν την αερομεταφερόμενη μετάδοση του COVID-19, η 
              οποία συμβαίνει όταν μολυσματικά σταγονίδια ανταλλάσσονται μέσω της αναπνοής κοινόχρηστου αέρα σε εσωτερικούς χώρους. Ενώ οι οργανισμοί δημόσιας υγείας αρχίζουν να αναγνωρίζουν την αερομεταφερόμενη μετάδοση, δεν έχουν ακόμη παράσχει οδηγίες ασφαλείας που να ενσωματώνουν όλες τις σχετικές μεταβλητές.''')]),
    html.Br(),
    html.Div([html.Span('''Η παρούσα εφαρμογή, η οποία έχει δημιουργηθεί από τον Kasim Khan σε συνεργασία με τους 
    Martin Z. Bazant και John W. M. Bush, χρησιμοποιεί ένα '''),
              html.A(children="θεωρητικό μοντέλο",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''για να υπολογίσει τους ασφαλείς χρόνους έκθεσης και τα ενδεδειγμένα
               επίπεδα πληρότητας σε εσωτερικούς χώρους. Προσαρμόζοντας τις προδιαγραφές των
                αιθουσών, τους ρυθμούς εξαερισμού και φιλτραρίσματος, τη χρήση μάσκας προσώπου, 
                την αναπνευστική δραστηριότητα, και τo αποδεκτό εύρος κινδύνου, μπορείτε να δείτε
                 πώς θα μπορούσατε να μετριάσετε την μετάδοση του COVID-19 σε διάφορους εσωτερικούς 
                 χώρους.''')]),
    html.Br(),
    html.Div(['''Στη βασική λειτουργία, μπορείτε να υπολογίσετε τα όρια για την ασφαλή πληρότητα μετά την είσοδο ενός 
    μόνο μολυσμένου ατόμου σε έναν εσωτερικό χώρο. Στη Σύνθετη λειτουργία, μπορείτε να λάβετε υπόψη 
    επιπλέον παράγοντες, όπως την συχνότητα της λοίμωξης και την ανοσία του πληθυσμού. Η λειτουργία 
    Advanced Mode σας επιτρέπει επίσης να αξιολογήσετε την ασφαλή πληρότητα με βάση τη μέση 
    συγκέντρωση CO2, η οποία σχετίζεται με τη συγκέντρωση μολυσματικών μικροσωματιδίων. ''']),
    html.Br(),
    html.Div([html.Span('''Η επιστήμη πίσω από την εφαρμογή διδάσκεται επίσης σε ένα δωρεάν, μαζικό, ανοιχτό σε 
    απευθείας σύνδεση μάθημα (MOOC) στο edX: '''),
              html.A(children="10. S95x Φυσική της μετάδοσης του COVID-19",
                     href=links.link_mooc,
                     target='_blank')]),
])

# Room Specifications
room_header = "Προδιαγραφές της αίθουσας - λεπτομέρειες"

floor_area_text = "Συνολική επιφάνεια δαπέδου (sq. ft.): "
floor_area_text_metric = "Συνολική επιφάνεια δαπέδου (m²): "
ceiling_height_text = "Μέσο ύψος οροφής (ft.): "
ceiling_height_text_metric = "Μέσο ύψος οροφής (m): "

ventilation_text = "Σύστημα εξαερισμού: "
vent_type_output_base = "{:.1f} "
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (ACH)"])
ventilation_text_adv = html.Span(["Σύστημα εξαερισμού (hr", html.Sup("-1"), ", ACH): "])
ventilation_types = [
    {'label': "Κλειστά παράθυρα", 'value': 0.3},
    {'label': "Ανοικτά παράθυρα", 'value': 2},
    {'label': "Μηχανικός εξαερισμός", 'value': 3},
    {'label': "Ανοικτά παράθυρα με ανεμιστήρες", 'value': 6},
    {'label': "Καλύτερος μηχανικός εξαερισμός", 'value': 8},
    {'label': "Εργαστήριο, Εστιατόριο", 'value': 9},
    {'label': "Μπαρ", 'value': 15},
    {'label': "Νοσοκομείο/ Βαγόνι μετρό", 'value': 18},
    {'label': "Ασφαλές εργαστήριο / αεροπλάνο", 'value': 24},
]

filtration_text = "Σύστημα φιλτραρίσματος: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Σύστημα φιλτραρίσματος (MERV): "
filter_types = [
    {'label': "Κανένα", 'value': 0},
    {'label': "Κλιματιστικό παραθύρου", 'value': 2},
    {'label': "Οικιστικό / Εμπορικό / Βιομηχανικό", 'value': 6},
    {'label': "Οικιστικά / Εμπορικά / Νοσοκομεία", 'value': 10},
    {'label': "Νοσοκομείο & Γενική Χειρουργική", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_text = "Ρυθμός ανακυκλοφορίας του αέρα: "
recirc_type_output_base = "{:.1f} "
recirc_type_output_units = html.Span(["hr", html.Sup("-1")])
recirc_text_adv = html.Span(["Ρυθμός ανακυκλοφορίας του αέρα (hr", html.Sup("-1"), "): "])
recirc_types = [
    {'label': "Κανένα", 'value': 0},
    {'label': "Αργός", 'value': 0.3},
    {'label': "Μεσαίος", 'value': 1},
    {'label': "Γρήγορος", 'value': 10},
    {'label': "Αεροπλάνο", 'value': 24},
    {'label': "Βαγόνι μετρό", 'value': 54},
]

humidity_text = "Σχετική υγρασία: "
humidity_marks = {
    0.01: {'label': '1%: Πολύ ξηρό', 'style': {'max-width': '25px'}},
    # 0.2: {'label': '20%: Airplane', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Ξηρό'},
    0.6: {'label': '60%: Μέτρια'},
    0.99: {'label': '99%: Πολύ υψηλή υγρασία'},
}

need_more_ctrl_text = '''Χρειάζεστε περισσότερο έλεγχο στην εισαγωγή των δεδομένων σας; Μεταβείτε στη Λειτουργία για 
Προχωρημένους χρησιμοποιώντας το αναπτυσσόμενο μενού στο επάνω μέρος της σελίδας.'''

human_header = "Ανθρώπινη συμπεριφορά - λεπτομέρειες"
# Human Behavior
exertion_text = "Ρυθμός αναπνοής: "
exertion_types = [
    {'label': "Καθιστή/ος", 'value': 0.49},
    {'label': "Όρθια/ος", 'value': 0.54},
    {'label': "Τραγουδώντας", 'value': 1},
    {'label': "Χαλαρή άσκηση", 'value': 1.38},
    {'label': "Άσκηση μέτριας έντασης", 'value': 2.35},
    {'label': "Άσκηση υψηλής έντασης", 'value': 3.30},
]

breathing_text = "Αναπνευστική δραστηριότητα: "
expiratory_types = [
    {'label': "Αναπνοή (ελαφριά)", 'value': 1.1},
    {'label': "Αναπνοή (κανονική)", 'value': 4.2},
    {'label': "Αναπνοή (βαριά)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Μιλώντας (ψιθυριστά)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Μιλώντας (κανονικά)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Μιλώντας (δυνατά)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Τραγουδώντας", 'value': 970},
]

mask_type_text = "Αποδοτικότητα φιλτραρίσματος μάσκας (τύπος μάσκας): "
mask_type_marks = {
    0: {'label': "0% (Καμία, Ασπίδα προσώπου)", 'style': {'max-width': '75px'}},
    0.5: {'label': "50% (Βαμβάκι, Φλανέλ)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (Βαμβάκι, Μετάξι)", 'style': {'max-width': '75px'}},
    0.90: {'label': "90% (Χειρουργική)", 'style': {'max-width': '75px'}},
    # 0.99: {'label': "99% (N95 resp-irator)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Καμία, Ασπίδα προσώπου", 'value': 0},
    {'label': "Βαμβάκι, Φλανέλ", 'value': 0.5},
    {'label': "Βαμβάκι, Μετάξι", 'value': 0.7},
    {'label': "Χειρουργική", 'value': 0.9},
    {'label': "Αναπνευστήρας Ν95", 'value': 0.99},
]

mask_fit_text = "Προσαρμογή μάσκας / Συμμόρφωση: "
mask_fit_marks = {
    0: {'label': '0%: Καθόλου', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Φτωχή'},
    0.95: {'label': '95%: Καλή'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Συχνές Ερωτήσεις"
other_io = "Άλλες παράμετροι"

faq_top = html.Div([
    html.H6("Συχνές Ερωτήσεις"),
    html.H5("Γιατί δεν είναι αρκετά τα 6 πόδια / 2 μέτρα;"),
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
    html.H5("Υπάρχουν άλλοι τρόποι μετάδοσης;"),
    html.Div([
        html.Div([html.A(children="Η αερομεταφερόμενη μετάδοση",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' πιστεύεται ότι είναι η κυρίαρχη για τον COVID-19, αλλά είναι δυνατοί και άλλοι τρόποι μετάδοσης, όπως η μετάδοση «fomite» μέσω της επαφής με μολυσματικά  υπολείμματα σε επιφάνειες, η μετάδοση «μεγάλων σταγονιδίων» μέσω βήχα ή φταρνίσματος, καθώς επίσης και η μετάδοση μέσω ‘μικροσταγονιδίων μικρής εμβέλειας’ από τον αναπνευστικό πίδακα ενός μολυσμένου ατόμου μετά από έκθεση για μεγάλο χρονικό διάστημα. Ενώ οι δύο τελευταίοι τρόποι μπορεί να είναι σημαντικοί, σε μεγάλο βαθμό εξαφανίζονται όταν χρησιμοποιούνται οι μάσκες ή οι ασπίδες προσώπου. Ωστόσο, ο κίνδυνος εναέριας μεταφοράς παραμένει. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Μπορούμε πραγματικά να κάνουμε την υπόθεση ότι ο αέρας είναι καλά αναμεμιγμένος μέσα σε μια αίθουσα?"),
    html.Div([
        html.Div([html.Span('''Υπάρχουν πολλοί παράγοντες που συνεισφέρουν στην ανάμιξη του αέρα σε εσωτερικούς χώρους, συμπεριλαμβανομένων των ροών που οφείλονται στην άνωση (από θερμαντήρες, κλιματιστικά ή παράθυρα), την αναγκαστική μεταφορά από αεραγωγούς και ανεμιστήρες, και την ανθρώπινη κίνηση και αναπνοή. Ενώ υπάρχουν εξαιρέσεις, τις οποίες συζητήσαμε στο '''),
                  html.A(children="άρθρο",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''', η υπόθεση της καλής ανάμιξης χρησιμοποιείται ευρέως στη θεωρητική μοντελοποίηση της μετάδοσης των αερομεταφερόμενων νόσων.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Η κατευθυντήρια γραμμή ισχύει και για πολύ μεγάλους χώρους;"),
    html.Div([
        html.Div([html.Span('''Σε αίθουσες συναυλιών, γήπεδα ή άλλους μεγάλους, αεριζόμενους χώρους με μεγάλο αριθμό ατόμων, ο κίνδυνος της μετάδοσης μέσω του αέρα είναι σημαντικός και καταγράφεται σωστά από την κατευθυντήρια γραμμή. Ωστόσο, όταν δεν φοριούνται μάσκες ή ασπίδες προσώπου, υπάρχει ένας επιπλέον κίνδυνος μετάδοσης μικρής εμβέλειας, ο οποίος εκτιμάται στο '''),
                  html.A(children="άρθρο",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Γιατί έχει σημασία το ύψος της οροφής;"),
    html.Div([
        '''Το ύψος της οροφής επηρεάζει τον συνολικό όγκο της αίθουσας, που απαιτείται για την εκτίμηση της συγκέντρωσης μολυσματικών μικροσταγονιδίων (# μικροσταγονιδίων ανά μονάδα όγκου). Αυτή η συγκέντρωση απαιτείται για τον υπολογισμό του κινδύνου μετάδοσης COVID-19 στην αίθουσα. '''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Γνωρίζω τους αριθμούς ACH / MERV. Πού μπορώ να τα εισαγάγω;"),
    html.Div('''
        Εάν χρειάζεστε περισσότερο έλεγχο στις μεταβλητές, μεταβείτε στη Σύνθετη λειτουργία χρησιμοποιώντας το 
        αναπτυσσόμενο μενού στην κορυφή της ιστοσελίδας.
    ''', className='faq-answer'),
    html.Br(),
    html.H5("Γιατί οι αναπνευστήρες N95 έχουν απόδοση 99%;"),
    html.Div('''Οι αναπνευστήρες N95 έχουν τουλάχιστον 95% απόδοση φιλτραρίσματος σε μεγέθη σωματιδίων 0,3 μm, 10 φορές μικρότερη από τα μεγέθη πτώσης στην αερομεταφερόμενη εκπομπή COVID-19. Για μεγαλύτερες σταγόνες, οι αναπνευστήρες N95 είναι ακόμη πιο αποτελεσματικοί, πλησιάζοντας επίπεδα κοντά στο 100%.''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Υπάρχουν κρυμμένες παράμετροι στη Βασική λειτουργία;"),
    html.Div([html.Span('''Όλες οι σχετικές φυσικές παράμετροι περιγράφονται λεπτομερώς στο '''),
              html.A(children="άρθρο",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''. Στη βασική λειτουργία, η εφαρμογή υποθέτει ότι η ακτίνα των μικροσταγονιδίων είναι 2 μm (σε υγρασία 60 %) και ο μέγιστος ρυθμός απενεργοποίησης των ιών είναι 0,6 / ώρα (σε ~ 100 % υγρασία), και τα δύο αυξάνονται με τη σχετική υγρασία (RH). Οι εκτιμήσεις για το ρυθμό απενεργοποίησης του ιού έχουν σφάλματα προς τη συντηρητική πλευρά της βραδύτερης απενεργοποίησης. Ο ρυθμός απενεργοποίησης του ιού μπορεί να αυξηθεί με την υπεριώδη ακτινοβολία (UV-C) ή με χημικά απολυμαντικά (π.χ. υπεροξείδιο του υδρογόνου, όζον). Η εφαρμογή εκτιμά επίσης την βασική παράμετρο της νόσου, τη μολυσματικότητα του εκπνεόμενου αέρα, C'''),
              html.Sub("q"),
              html.Span(''' (κβάντα μόλυνσης ανά μονάδα όγκου), από την καθορισμένη αναπνευστική δραστηριότητα, χρησιμοποιώντας πίνακες τιμών στη δεύτερη εικόνα (Figure 2) του '''),
              html.A(children="άρθρου",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''. Μπορείτε να ορίσετε αυτές τις παραμέτρους μόνοι σας στη Λειτουργία για Προχωρημένους.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Ακτίνα μικροσταγονιδίων (σε RH = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Μέγιστος ρυθμός απενεργοποίησης ιών (σε RH = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

pop_immunity_header = "Ανοσία πληθυσμού: "
perc_immune_label = html.Span(["Ποσοστό ανοσίας p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["Ποσοστό κρουσμάτων p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["Percentage vaccinated p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["Percentage previously infected p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["Ποσοστό ευαίσθητου πληθυσμού p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''Το μολυσματικό ποσοστό p''', html.Sub('i'), ''' στον 
πληθυσμό υπολογίζεται από την μολυσματική συχνότητα που έχει εισαχθεί στις άλλες καρτέλες 
σεναρίων κινδύνου (Δεδομένης της συσχνότητας λοίμωξης…, Για να περιορίσω τον προσωπικό μου 
κίνδυνο…). Το ποσοστό του ανοσίας p''', html.Sub('im'), ''' μπορεί να εκτιμηθεί συντηρητικά από 
το ποσοστό εμβολιασμού του πληθυσμού συν το συνολικό ποσοστό κρουσμάτων στον πληθυσμό, και 
αγνοώντας τη συμβολή από μη ανιχνευόμενες περιπτώσεις. Αυτές οι δύο τιμές χρησιμοποιούνται 
για τον υπολογισμό του ευαίσθητου ποσοστού p''', html.Sub('s'), '''. Στη Βασική Λειτουργία και στον πρώτο υπολογισμό
 κινδύνου (Εάν ένα μολυσμένο άτομο εισέλθει…), αυτή η τιμή θεωρείται ότι είναι 100%.''']),
                              html.Br(),
                              html.Div(['''Ακολουθούν μερικοί χρήσιμοι σύνδεσμοι για να βρείτε p''', html.Sub('i'), ''' και p''',
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

values_interest_header = "Υπολογισμένες τιμές ενδιαφέροντος: "
values_interest_desc = html.Div([
    html.H5("Τι ακριβώς υπολογίζει η εφαρμογή;"),
    html.Div([
        html.Div([html.Span('''Δεδομένου του αποδεκτού εύρους κινδύνου για αερομεταφερόμενη μετάδοση, η εφαρμογή υπολογίζει τον μέγιστο επιτρεπτό χρόνο αθροιστικής έκθεσης, από το γινόμενο της πληρότητας της αίθουσας και του χρόνου παρουσίας ενός μολυσμένου με τον ιό ατόμου. Η εφαρμογή υπολογίζει επίσης άλλες σχετικές ποσότητες, που ορίζονται λεπτομερώς στο '''),
                  html.A(children="άρθρο",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''', οι οποίες μπορεί να ενδιαφέρουν: ''')]),
    ], className='faq-answer'),
])
relative_sus_label = html.Span(["Relative susceptibility s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["Κλάσμα εξωτερικού αέρα Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Απόδοση διήθησης μικροσταγονιδίων p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Ρυθμός ροής αναπνοής Q", html.Sub('b'), ": "])
cq_label = html.Span(["Μολυσματικότητα του εκπνεόμενου αέρα C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Πιθανότητα να διαπεραστεί η μάσκα p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Όγκος αίθουσας V: "])
vent_rate_Label = html.Span(["Ρυθμός εξαερισμού Q: "])
recirc_rate_label = html.Span(["Ρυθμός ροής επιστροφής (ανακυκλοφορίας) του αέρα Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Ρυθμός φιλτραρίσματος αέρα (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Ρυθμιζόμενη-από-την-υγρασία ακτίνα μικροσταγονιδίων r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Ρυθμιζόμενος-από-την-υγρασία ρυθμός απενεργοποίησης ιών \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Τελική μέση ταχύτητα μικροσταγονιδίων v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Ποσοστό χαλάρωσης συγκέντρωσης \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Ρυθμός μετάδοσης μέσω του αέρα \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Αυτό το μοντέλο εξηγεί την γενίκευση της λοίμωξης στον τοπικό πληθυσμό;"),
    html.Div(['''The influence of the prevalence of infection in the local population may be considered in Advanced 
    Mode. There, in the Other Parameters tab, one may also assess the influence of immunity in the population, 
    as may arise through vaccination or previous infection.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("Περισσότερες ερωτήσεις?"),
    html.Div([html.Span('''Για πιο λεπτομερείς εξηγήσεις και αναφορές, ανατρέξτε στην ενότητα "'''),
              html.A(children="Πέρα από τα 6 πόδια",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''" και στους άλλους συνδέσμους που δημοσιεύονται στην κορυφή της ιστοσελίδας.''')]),
])

footer = html.Div([
    html.Div([html.Span('''Η κατευθυντήρια γραμμή εσωτερικής ασφάλειας COVID-19 είναι ένα εξελισσόμενο εργαλείο που έχει ως στόχο να εξοικειώσει τον ενδιαφερόμενο χρήστη με τους παράγοντες που επηρεάζουν τον κίνδυνο εσωτερικής αερομεταφοράς του COVID-19 και να βοηθήσει στην ποσοτική εκτίμηση του κινδύνου σε διάφορες περιστάσεις. Σημειώνουμε ότι η αβεβαιότητα και η εγγενής μεταβλητότητα των παραμέτρων του μοντέλου μπορεί να οδηγήσει σε σφάλματα τόσο μεγάλα όσο μια τάξη μεγέθους, τα οποία μπορεί να αντισταθμιστούν επιλέγοντας μια αρκετά μικρή ανοχή κινδύνου. Η κατευθυντήρια γραμμή δεν λαμβάνει υπόψη τη μετάδοση μικρής εμβέλειας μέσω αναπνευστικών πιδάκων, η οποία μπορεί να αυξήσει σημαντικά τον κίνδυνο όταν δεν χρησιμοποιούνται μάσκες προσώπου, με τρόπο που συζητείται στο '''),
              html.A(children="συνοδευτικό άρθρο",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' (Bazant & Bush, 2020). Η χρήση της κατευθυντήριας γραμμής ασφάλειας εσωτερικού χώρου COVID-19 είναι αποκλειστική ευθύνη του χρήστη. Διατίθεται χωρίς εγγύηση οποιουδήποτε είδους. Οι συγγραφείς δεν αποδέχονται καμία νομική ευθύνη από τη χρήση της.''')]),
    html.Br(),
    html.Div("Πολλές ευχαριστίες στους: ")
], className='footer-small-text')
