import dash_html_components as html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions_hu: Hungarian

"""

# Header
header = html.Div([
    html.H1(children='COVID-19 Beltéri Biztonsági Útmutató'),
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
language_dd = "Nyelv: "

# Unit systems
units_dd = "Mértékegységek: "
unit_settings = [
    {'label': "Angolszász", 'value': "british"},
    {'label': "Metrikus", 'value': "metric"},
]

# Modes
mode_dd = "Mód: "
app_modes = [
    {'label': "Egyszerű", 'value': "basic"},
    {'label': "Haladó", 'value': "advanced"},
]

output_mode_dd = "Output Mode: "
output_modes = [
    {'label': "Biztonságos kihasználtság", 'value': "occupancy"},
    {'label': "Biztonságos CO\u2082 szint", 'value': "co2"},
]

error_list = {
    "floor_area": "Hiba: Az alapterület nem hiányozhat.",
    "ceiling_height": "Hiba: A mennyezet magassága nem hiányozhat.",
    "recirc_rate": "Hiba: A légcsere sebessége (ACH) nem hiányozhat.",
    "aerosol_radius": "Hiba: Az aeroszol sugara nem hiányozhat.",
    "viral_deact_rate": "Hiba: A vírus deaktiválási sebessége nem hiányozhat.",
    "n_max_input": "Hiba: Az emberek száma nem lehet kevesebb, mint 2.",
    "exp_time_input": "Hiba: A kitettségi időnek 0-nál nagyobbnak kell lennie.",
    "air_exchange_rate": "Hiba: A szellőztetési sebességnek (ACH) nagyobbnak kell lennie, mint 0.",
    "merv": "Hiba: A szűrőrendszer (MERV) nem hiányozhat.",
    "prevalence": "Hiba: A gyakoriságnak 0-nál nagyobbnak és 100 000-nél kisebbnek kell lennie.",
    "atm_co2": "Hiba: Háttér CO\u2082 szintet meg kell adni."
}

# Main Panel Text
curr_room_header = "Helyiség:"
presets = [
    {'label': "Egyedi", 'value': 'custom'},
    {'label': "Tanterem", 'value': 'classroom'},
    {'label': "Nappali", 'value': 'living-room'},
    {'label': "Templom", 'value': 'church'},
    {'label': "Étterem", 'value': 'restaurant'},
    {'label': "Iroda", 'value': 'office'},
    {'label': "Metrókocsi", 'value': 'subway'},
    {'label': "Kereskedelmi utasszállító repülőgép", 'value': 'airplane'},
]

curr_human_header = "Emberi tevékenység: "
presets_human = [
    {'label': "Egyedi", 'value': 'custom'},
    {'label': "Maszkban nyugalmi helyzet", 'value': 'masks-1'},
    {'label': "Maszkban beszéd", 'value': 'masks-2'},
    {'label': "Maszkban testmozgás", 'value': 'masks-3'},
    {'label': "Maszk nélküli nyugalmi helyzet", 'value': 'no-masks-1'},
    {'label': "Maszk nélküli beszéd", 'value': 'no-masks-2'},
    {'label': "Maszk nélküli testmozgás", 'value': 'no-masks-3'},
    {'label': "Maszk nélküli éneklés", 'value': 'singing-1'},
]

curr_risk_header = "Kockázat: "
risk_tol_marks = {
    # 0.01: {'label': '0.01: Biztonságosabb', 'style': {'max-width': '30px'}},
    0.1: {'label': '0.10: Biztonságos', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Kockázatos'}
}

risk_tolerance_text = "Kockázattűrés: "
risk_tol_desc = html.Div('''A veszélyeztetett csoportok, mint az idősek vagy az alapbetegséggel rendelkezők alacsonyabb kockázati plafont igényelnek (~0.01).
A magasabb megengedhető kockázat mellett több fertőzés várható adott kitettség és kihasználtság mellett (részletek a Gyakran Ismételt Kérdések alatt).''',
                         style={'font-size': '13px', 'margin-left': '20px'})


curr_age_header = "Korcsoport: "
presets_age = [
    {'label': "Gyermekek (<15 évesek)", 'value': 0.23},
    {'label': "Felnőttek (15-64 évesek)", 'value': 0.68},
    {'label': "Idősek (>64 évesek)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: Gyermekek (<15 évesek)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: Felnőttek (15-64 évesek)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: Idősek (>64 évesek)', 'style': {'width': '100px'}}
}
lang_break_age = html.Br()

curr_strain_header = "Vírusváltozat: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2 (vuhani változat)", 'value': 1},
    {'label': "SARS-CoV-2 - B.1.1.7 (brit változat)", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: vuhani', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: B.1.1.7/brit'}
}

pim_header = "Immunisak aránya:"
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "Ha egy fertőzött személy belép…"
risk_prevalence_desc = "Tekintettel a fertőzés gyakoriságára…"
risk_personal_desc = "Az egyéni kockázatom korlátozása érdekében…"
risk_options = [
    {'label': risk_conditional_desc, 'value': 'conditional'},
    {'label': risk_prevalence_desc, 'value': 'prevalence'},
    {'label': risk_personal_desc, 'value': 'personal'},
]
risk_personal_warning = html.Span([
    html.Span('''Figyelmeztetés: ''', style={'font-weight': 'bold'}),
    html.Span('''a kiválasztott kockázati mód (Az egyéni kockázatom korlátozása érdekében…) egy adott egyén megfertőződésében
gondolkodik. Ezért sokkal megengedőbb, és nem szabad a közösségi biztonsági irányelvek meghatározásához használni.''')])

risk_mode_panel_header = "Kockázati mód"
occupancy_panel_header = "Számoljuk a biztonságos kihasználtságot"
main_panel_s1 = "A COVID-19 továbbadásának* korlátozásához azután, hogy egy fertőzött személy ebbe a térbe lép, nem lehet itt több, mint: "

main_panel_s1_b = html.Span([
    html.Span('''A COVID-19 továbbadásának* korlátozásához egy olyan populációban, amelynek fertőzöttsége'''),
    html.Sup('''1 ''')
])
main_panel_s2_b = ''' / 100 000 fő, ebben a térben lehet legfeljebb: '''

main_panel_s1_c = html.Span([
    html.Span(
        '''Annak érdekében, hogy korlátozzam a saját megfertőződésem esélyét egy olyan populációban, 
        amelynek fertőzési gyakorisága'''),
    html.Sup('''1 ''')
])
main_panel_s2_c = ''' / 100 000 fő, ebben a térben lehet legfeljebb: '''

units_hr = 'órát'
units_min = 'percet'
units_days = 'napot'
units_months = 'hónapot'

units_hr_one = 'órát'
units_min_one = 'percet'
units_day_one = 'napot'
units_month_one = 'hónapot'

is_past_recovery_base_string = '{n_val} fő több mint {val:.0f} nap alatt,'
model_output_base_string = '{n_val} fő '
model_output_base_string_co2 = '{co2:.2f} részecske per millió '
nt_bridge_string = " fő "
tn_bridge_string = " fő "

main_panel_six_ft_1 = "Ezzel szemben a kétméteres távolságtartással lehetséges kihasználtság "
main_panel_six_ft_2 = ", akik az útmutató szerint bent tölthetnének "

six_ft_base_string = ' {} fő'
six_ft_base_string_one = ' {} fő'

graph_title = "Kihasználtság vagy kitettség"
graph_xtitle = "Maximálisan benntölthető idő \u03C4 (óra)"
graph_ytitle = "Maximális létszám N"
transient_text = "Átmeneti"
steady_state_text = "Végleges"
co2_safe_trace_text = "Biztonságos légzési küszöb"
guideline_trace_text = "Javallat"
background_co2_text = "Háttér CO\u2082: "
recommended_co2_text = "Javasolt határ"

graph_title_co2 = "Biztonságos CO\u2082-koncentráció (ppm) vagy kitettség"
graph_ytitle_co2 = "CO\u2082-koncentráció (ppm)"

co2_title = "Biztonságos CO\u2082-koncentráció számítása"
co2_param_desc = '''A fent kiválasztott paraméterekre vonatkozó iránymutatást a CO\u2082-koncentráció küszöbértékeként fejezzük ki..'''
co2_prev_input_1 = html.Span(["Gyakoriság", html.Sup('1'), html.Span(": ")])
co2_prev_input_2 = " / 100,000"
co2_atm_input_1 = background_co2_text
co2_atm_input_2 = " ppm"
co2_calc_1 = ""
co2_calc_2 = " órányi kitettség esetén a számított biztonságos (időátlagolt) CO\u2082-koncentráció ebben a térben"
co2_calc_3 = "."
co2_base_string = '{:,.2f} ppm'

co2_safe_sent_1 = "Ez a határérték meghaladja az egészséges légzés határértékét, ami "
co2_safe_sent_2 = "."

co2_safe_footer = html.Span(['''A légzésbiztonsági küszöbértéket ''',
                             html.A(href=links.link_usda_co2,
                                    children='''az amerikai agrárminisztérium által ajánlott határértékek alapján''',
                                    target='_blank'),
                             ''' interpolálták.'''])

main_airb_trans_only_disc = html.Div(["Ez az ajánlás a megengedett határ alatt tartja a ",
                                      html.Span(html.A(href=links.link_nature,
                                                       children="légúti fertőzés",
                                                       target='_blank'), ),
                                      html.Span(
                                          '''egy fertőzöttre eső valószínűségét az itt látható halmozott kitettség 
                                          időtartama alatt.''')],
                                     className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*Ez az ajánlás a megengedett határ (10%) alatt tartja a ",
                                            html.Span(html.A(href=links.link_docs,
                                                             children="légúti fertőzés",
                                                             target='_blank'), ),
                                            html.Span(''' egy fertőzöttre eső valószínűségét az itt 
                                            látható halmozott kitettség alatt.''')], className='airborne-text')
other_risk_modes_desc = html.Div(
    '''További kockázati forgatókönyvekkel számolhatunk Haladó módban. Konkrétabban figyelembe vehetjük a helyi 
    fertőzöttséget, a korábbi betegséggel vagy oltással szerzett immunitást vagy az egy konkrét személyre jelentett 
    veszélyt.''')

main_airb_trans_only_desc_b = html.Div(["Ez az ajánlás a megengedett határ alatt tartja egyetlen ",
                                      html.Span(html.A(href=links.link_nature,
                                                       children="légúti fertőzés",
                                                       target='_blank'), ),
                                      html.Span(
                                          '''egy fertőzöttre eső valószínűségét az itt látható halmozott kitettség 
                                          időtartama alatt.''')],
                                     className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["Ez az ajánlás a megengedett határ alatt tartja egy konkrét személy ",
                                      html.Span(html.A(href=links.link_nature,
                                                       children="megfertőzésédének",
                                                       target='_blank'), ),
                                      html.Span(
                                          '''valószínűségét az itt látható halmozott kitettség 
                                          időtartama alatt.''')],
                                     className='airborne-text')

airb_trans_only_disc = html.Div('''''', className='airborne-text')

#old: airb_trans_only_disc = html.Div(
#    '''Ez az ajánlás egyetlen fertőző légúti továbbfertőzésével számol, a mutatott halmozott kitettségi idő alatt.''',
#    className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''A helyi gyakoriság becsléséhez hasznosak lehetnek ezek a források: '''),
                                html.Span(html.A(href=links.link_hu_koronamonitor,
                                                 children="Koronamonitor",
                                                 target='_blank')),
                                html.Span(''', '''),
                                html.Span(html.A(href=links.link_cdc_dashboard,
                                                 children="CDC COVID-19 Monitor",
                                                 target='_blank')),
                                html.Span(", "),
                                html.Span(html.A(href=links.link_jhu_data,
                                                 children="Johns Hopkins Egyetem, Koronavírus Központ",
                                                 target='_blank')),
                                html.Span(", "),
                                html.A(children="Amerikai immunitás becslések",
                                       href=links.link_cdc_immunity,
                                       target='_blank'),
                                html.Span(", "),
                                html.A(children="Nemzetközi immunitás becslések",
                                       href=links.link_jhu_vaccine,
                                       target='_blank'),
                                ], className='airborne-text')


# Bottom panels text
n_input_text_1 = "Ha ebben a térben tartózkodik "
n_max_base_string = ' {:.0f}'
n_max_overflow_base_string = ' >{:.0f}'
n_input_text_2 = " fő, ők biztonságban itt tölthetnek "
n_input_text_3 = "."

t_input_text_1 = "Ha itt töltenek "
t_input_text_2 = " órát, nem lehetnek többen, mint "
t_input_text_3 = "."

# About
about_header = "Háttér"
about = html.Div([
    html.H6("Háttér", style={'margin': '0'}),
    html.Div(
        '''A COVID-19 terjedésének mérséklése érdekében a hivatalos közegészségügyi irányelvek korlátozásokat 
        javasolnak az emberektől való távolság (6 láb / 2 méter), a benntartózkodás (15 perc), a maximális 
        kihasználtság (25 fő) vagy a minimális szellőzés (óránként 6 légcsere) vonatkozásában.'''),
    html.Br(),
    html.Div([html.Span('''Egyre több a '''),
              html.A(children="tudományos bizonyíték",
                     href=links.link_docs,
                     target='_blank'),
              html.Span(
                  ''', hogy a COVID-19 levegőn keresztül terjed, amikor fertőző aeroszol cseppeket cserélnek egy 
                  beltéri levegőt lélegző személyek. Bár a közegészségügyi hatóságok kezdik elismerni a levegőn 
                  keresztüli fertőzést, még nem tettek közzé olyan iránymutatást, ami az összes idevágó tényezőt 
                  figyelembe venné.''')]),
    html.Br(),
    html.Div([html.Span(
        '''Ez az alkalmazás, amit Martin Z. Bazant és John W. M. Bush közreműködésével fejlesztett ki Kasim Khan, 
        egy '''),
              html.A(children="elméleti modell",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(
                  '''segítségével számolja ki a beltérben biztonságosan eltölthető időt és kihasználtságot. A szoba 
                  jellemzőit, a szellőzést és a légszűrést, a maszkhasználatot, a légzést vagy a 
                  kockázattűrést (más füleken) átállítva követhető, hogyan korlátozható a COVID-19 továbbadása 
                  különböző beltéri terekben.''')]),
    html.Div(['''Egyszerű módban kiszámíthatja a biztonságos bent tartózkodásra vonatkozó határértékeket, miután egyetlen fertőzött személy belép egy beltéri helyiségbe. Haladó módban további tényezőket vehet figyelembe, beleértve a fertőzés elterjedtségét és a lakosság immunitását. A Haladó mód lehetővé teszi azt is, hogy a biztonságos tartózkodást az átlagos CO\u2082-koncentráció alapján értékelje, amely összefügg a fertőző aeroszolok koncentrációjával.''']),
    html.Br(),
    html.Br(),
    html.Div([html.Span(
        '''Az alkalmazás mögött álló tudományos alapok egy ingyenes, saját ütemben elvégezhető, nyilvános online 
        tanfolyamon (MOOC) is elsajátíthatók az edX platformon: '''),
              html.A(children="10.S95x A COVID-19 fertőzés fizikája",
                     href=links.link_mooc,
                     target='_blank')])
])

# Room Specifications
room_header = "A szoba jellemzői"

floor_area_text = "Teljes alapterület (négyzetláb): "
floor_area_text_metric = "Teljes alapterület (m²): "
ceiling_height_text = "Átlagos belmagasság (láb): "
ceiling_height_text_metric = "Átlagos belmagasság (m): "

ventilation_text = "Szellőzés, légcsere: "
vent_type_output_base = "{:.1f}"
vent_type_output_units = "/óra (kültéri ACH)"
ventilation_text_adv = "Szellőzés, légcsere (/óra (kültéri ACH): "
ventilation_types = [
    {'label': "Zárt ablakok", 'value': 0.3},
    {'label': "Nyitott ablakok", 'value': 2},
    {'label': "Gépi szellőztetés", 'value': 3},
    {'label': "Nyitott ablakok ventilátorokkal", 'value': 6},
    {'label': "Jobb gépi szellőztetés", 'value': 8},
    {'label': "Laboratórium, étterem", 'value': 9},
    {'label': "Bár", 'value': 15},
    {'label': "Kórház, metrókocsi", 'value': 18},
    {'label': "Toxikológiai laboratórium / Repülőgép", 'value': 24},
]


filtration_text = "Szűrőrendszer: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Szűrőrendszer (MERV): "
filter_types = [
    {'label': "Semmilyen", 'value': 0},
    {'label': "Ablakra szerelt légkondicionáló (háztartási)", 'value': 2},
    {'label': "Lakossági / üzleti / ipari", 'value': 6},
    {'label': "Lakossági / üzleti / kórházi", 'value': 10},
    {'label': "Kórház és rendelő", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_text = "Légkeringtetés sebessége: "
recirc_type_output_base = "{:.1f}"
recirc_type_output_units = "/óra"
recirc_text_adv = "Légkeringtetés sebessége (/óra): "
recirc_types = [
    {'label': "Semennyi", 'value': 0},
    {'label': "Lassú", 'value': 0.3},
    {'label': "Mérsékelt", 'value': 1},
    {'label': "Gyors", 'value': 10},
    {'label': "Repülőgép", 'value': 24},
    {'label': "Metrókocsi", 'value': 54},
]

humidity_text = "Relatív páratartalom: "
humidity_marks = {
    0.01: {'label': '1%: Nagyon száraz', 'style': {'max-width': '25px'}},
    # 0.2: {'label': '20%: Repülőgép', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Száraz'},
    0.6: {'label': '60%: Átlagos'},
    0.99: {'label': '99%: Nagyon párás'},
}

need_more_ctrl_text = '''Több mindent szeretne beállítani? Váltson Haladó módra az oldal tetején található legördülő 
menü használatával.'''

human_header = "Emberi viselkedés — Részletek"
# Human Behavior
exertion_text = "Aktivitás: "
exertion_types = [
    {'label': "Nyugalmi", 'value': 0.49},
    {'label': "Álló", 'value': 0.54},
    {'label': "Éneklő", 'value': 1},
    {'label': "Könnyű testmozgás", 'value': 1.38},
    {'label': "Mérsékelt testmozgás", 'value': 2.35},
    {'label': "Intenzív testmozgás", 'value': 3.30},
]

breathing_text = "Légzés: "
expiratory_types = [
    {'label': "Légzés (lassú)", 'value': 1.1},
    {'label': "Légzés (normál)", 'value': 4.2},
    {'label': "Légzés (erőteljes)", 'value': 8.8},
    {'label': "Suttogás", 'value': 29},
    {'label': "Beszélgetés (normál hangon)", 'value': 72},
    {'label': "Hangos beszéd", 'value': 142},
    {'label': "Éneklés", 'value': 970},
]

mask_type_text = "Maszk hatékonysága, maszktípus: "
mask_type_marks = {
    0: {'label': "0% (maszk nélkül vagy arcpajzsban)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (pamut, flanel)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (többrétegű pamut, selyem)", 'style': {'max-width': '50px'}},
    0.90: {'label': "90% (eldobható orvosi)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Nincs vagy csak arcpajzs", 'value': 0},
    {'label': "Pamut, flanel", 'value': 0.5},
    {'label': "Többrétegű pamut, selyem", 'value': 0.7},
    {'label': "Eldobható orvosi", 'value': 0.9},
    {'label': "FFP2 / N95 légzőmaszk", 'value': 0.99},
]

mask_fit_text = "Maszk illeszkedése / Maszkhordási fegyelem: "
mask_fit_marks = {
    0: {'label': '0%: Semmi', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Rossz'},
    0.95: {'label': '95%: Jó'}
}

# FAQ/Other Inputs and Outputs
faq_header = "Gyakran Ismételt Kérdések"
other_io = "Egyéb beállítások és eredmények"

faq_top = html.Div([
    html.H6("Gyakran Ismételt Kérdések"),
    html.H5("Miért nem elegendő a 2 méter távolság?"),
    html.Div([
        html.Div([html.Span(
            '''A kétméteres távolság megvéd a fertőzött személy által kiköhögött nagy cseppektől, ahogy az arcmaszkok 
            is; ugyanakkor nem véd  '''),
                  html.A(children="levegőben szálló",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' és az egész helyiségben keveredő fertőzött aeroszolok általi terjedés ellen. 
                  Beltérben az emberek nincsenek nagyobb biztonságban a levegőben terjedő fertőzéstől 
                  20 méteres távolságban, mint 2 méterre.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Vannak más terjedési módok?"),
    html.Div([
        html.Div([html.A(children="Az aeroszolos átadást",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(
                      '''gondolják sokan meghatározónak a COVID-19 esetében, de más módon is lehetséges a fertőzés, 
                      mint például a „fomit” átvitel a felületeken található fertőző maradványokkal való közvetlen 
                      érintkezés útján, a „nagy cseppek” átvitele köhögés vagy tüsszögés útján, valamint a „rövidtávú 
                      aeroszol” átvitel a fertőzött személy kilégzési légáramában töltött hosszabb idő alatt. Bár az 
                      utóbbi két út akár jelentős is lehet, arcmaszkok vagy pajzsok viseletével nagyrészt 
                      kiküszöbölhetők; azonban továbbra is fennáll a levegőben terjedés kockázata.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Hihetünk a jól kevert szoba feltevésében?"),
    html.Div([
        html.Div([html.Span(
            '''Sok minden hozzájárul a beltéri levegő keveredéséhez, beleértve a felhajtóerő által vezérelt áramlást 
            (fűtőberendezésekből, légkondicionálókból vagy ablakokból), a szellőzőnyílások és ventilátorok erőltetett 
            konvekcióját, valamint az emberi mozgást és légzést. Bár vannak kivételek, ahogy azt a '''),
                  html.A(children="tanulmány",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(
                      '''tárgyalja is, a jól-kevert feltevést széles körben használják a levegőben terjedő betegségek 
                      elméleti modellezésében.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Érvényes az iránymutatás nagyon nagy terekre is?"),
    html.Div([
        html.Div([html.Span(
            '''Koncerttermekben, stadionokban vagy más nagy, szellőztetett helyiségekben, ahol nagy az emberek száma, 
            a levegőben történő továbbadás veszélye jelentős, és ezt az útmutató megfelelően kezeli. Maszkok vagy 
            arcvédő pajzsok viselete nélkül azonban a '''),
                  html.A(children="tanulmány",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''' becslései szerint a kilégzés rövidtávú felhői is további kockázatot jelentenek.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Miért számít a belmagasság?"),
    html.Div([
        '''A belmagasság befolyásolja a szoba teljes térfogatát, amelyre szükség van a fertőző aeroszolok 
        koncentrációjának becsléséhez (aeroszolok száma térfogategységenként). Erre a koncentrációra van szükség a 
        helyiség COVID-19 átadási kockázatának becsléséhez. '''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Tudom az ACH / MERV számaimat. Hol adhatom meg őket?"),
    html.Div('''Ha több beállítási lehetőségre van szüksége, váltson Haladó módra a weboldal tetején található 
    legördülő menü használatával.''', className='faq-answer'),
    html.Br(),
    html.H5("Miért van az N95 légzőkészülékeknek 99%-os hatékonysága?"),
    html.Div('''Az N95 légzőkészülékek legalább 95%-os szűrési hatékonysággal rendelkeznek 0,3 μm-es 
    részecskeméreteknél, ami tízszer kisebb, mint a jellemző cseppméretek a COVID-19 levegőben történő átvitelekor. 
    Nagyobb cseppek esetén az N95 légzőkészülékek még hatékonyabbak, megközelítik a 100% -ot.''',
             className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Vannak rejtett paraméterek az Egyszerű módban?"),
    html.Div([html.Span('''Az összes vonatkozó fizikai paramétert részletesen ismerteti a '''),
              html.A(children="tanulmány",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''. Egyszerű módban, az app alapértelmezett effektív aeroszol sugara 2 um (60% 
              páratartalomnál) , és a maximális virális deaktiválás sebessége 0,6 / óra (~100% páratartalom mellett), 
              mindkettő növekszik a relatív páratartalommal (RH). A vírus deaktiválódásának becslése konzervatív, 
              lassabb dezaktiválást megengedve. A vírus dezaktiválási sebességét ultraibolya sugárzás (UV-C) vagy 
              kémiai fertőtlenítőszerek (pl. hidrogén-peroxid, ózon) növelhetik. Az alkalmazás megbecsüli a betegség 
              legfontosabb paraméterét, a kilélegzett levegő fertőzőképességét, a C'''),
              html.Sub('q'),
              html.Span('''-t (egységnyi térfogatra jutó fertőzési kvantum) a megadott légzési aktivitásból, a '''),
              html.A(children="tanulmány",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' 2. ábráján látható táblázatos értékek felhasználásával. Ezeket a paramétereket Haladó 
              módban Ön adja meg.''')],
             className='faq-answer'),
])
aerosol_radius_text = "Effektív aeroszol sugár  (60% páratartalomnál), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(
    ["Maximális vírus-deaktiválási ráta (100% páratartalomnál), \u03BB", html.Sub('vmax'), " (/óra): "])

pop_immunity_header = "Immunisak aránya a környezetben:"
perc_immune_label = html.Span(["Az immunisak aránya p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["Fertőzők aránya p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["Beoltottak aránya p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["Fertőzésen átesettek aránya p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["Fogékonyak aránya p", html.Sub('s'), " = 1 - (p", html.Sub('im'),
                                    " + p", html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''A populációban a fertőzők p''', html.Sub('i'), ''' százalékos arányát a 
Többi kockázati forgatókönyv fülre beírt fertőző prevalencia alapján számolják (Tekintettel a fertőzés 
prevalenciájára…, A személyes kockázat korlátozásához…). Az immunisak p''', html.Sub('im'),
                                        ''' százalékos arányára konzervatív becslés lehet a védőoltást kapottak 
                                        és a gyógyultak összesített aránya a lakosság körében, amivel eltekintünk 
                                        a felderítetlenül maradt esetektől. Ezt a két értéket használjuk a fogékonyak 
                                        p''', html.Sub('s'),
                                        ''' százalékának kiszámításához. Egyszerű módban és az első kockázati 
                                        módban (Ha egy fertőzött személy belép…) feltételezzük, hogy ez az érték 
                                        100%.''']),
                              html.Br(),
                              html.Div(
                                  ['''Ezek a linkek segíthetnek kideríteni, mekkora p''', html.Sub('i'), ''' és p''',
                                   html.Sub('im'), ''': ''',
                                   html.Span(html.A(href=links.link_hu_koronamonitor,
                                                    children="Koronamonitor",
                                                    target='_blank')),
                                   html.Span(", "),
                                   html.Span(html.A(href=links.link_cdc_dashboard,
                                                    children="CDC COVID-19 Monitor",
                                                    target='_blank')),
                                   html.Span(", "),
                                   html.Span(html.A(href=links.link_jhu_data,
                                                    children="Johns Hopkins Egyetem, Koronavírus Központ",
                                                    target='_blank')),
                                   html.Span(", "),
                                   html.A(children="Amerikai immunitás-becslések",
                                          href=links.link_cdc_immunity,
                                          target='_blank'),
                                   html.Span(", "),
                                   html.A(children="Nemzetközi immunitás-becslések",
                                          href=links.link_jhu_vaccine,
                                          target='_blank'),
                                   ])
                              ])

values_interest_header = "Fontos számított értékek: "
values_interest_desc = html.Div([
    html.H5("Pontosan mit számol az alkalmazás?"),
    html.Div([
        html.Div([html.Span('''Az app kiszámítja a maximálisan megengedett halmozott kitettséget, 
        a szoba kihasználtságának és az időnek a szorzatát beltérben. A COVID-19 terjedésének korlátja, 
        hogy a fertőző egyénre jutó átadások várható száma, a „beltéri reprodukciós szám” kisebb legyen, 
        mint a választott kockázati küszöb. Az alkalmazás kiszámítja a '''),
                  html.A(children="tanulmányban",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''' meghatározott kapcsolódó mennyiségeket is, amelyek érdekesek lehetnek:''')]),
    ], className='faq-answer'),
])

relative_sus_label = html.Span(["Relatív fogékonyság s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["Kültéri levegő aránya Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Az aeroszolszűrés hatékonysága p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Légzési áramlási sebesség Q", html.Sub('b'), ": "])
cq_label = html.Span(["A kilélegzett levegő fertőzősége C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["A maszkon áthaladás valószínűsége p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Helyiség térfogata V: "])
vent_rate_Label = html.Span(["Szellőzés (kültéri) áramlási sebessége Q: "])
recirc_rate_label = html.Span(["Visszatérő (keringtetett) áramlási sebesség Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Légszűrési sebesség (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(
    ["Páratartalom-függő aeroszol-sugár r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(
    ["Páratartalom-függő vírus-deaktiválási sebesség \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Effektív aeroszolos ülepedési sebesség v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["A koncentráció relaxációs sebessége \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Légúti átviteli sebesség \u03B2\u2090: "])

graph_output_header = "Ábra: "
faq_graphs_text = html.Div([
    html.H5("Ábra: "),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Vajon ez a modell figyelembe veszi a fertőzés gyakoriságát a helyi lakosságban?"),
    html.Div([
                 '''A helyi populációban a fertőzés prevalenciájának hatása Haladó módban mérlegelhető. Ott, 
                 az Egyéb paraméterek fülön meg lehet adni az immunitás mértékét is a populációban, ami oltás vagy 
                 korábbi fertőzés következtében felmerülhet.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("Van még kérdése? "),
    html.Div([html.Span('''Részletesebb magyarázatokat és hivatkozásokat a "Hat lábon túl ('''),
              html.A(children="Bazant & Bush, 2020",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''') tanulmányban és egyéb, a weboldal tetején található linkek alatt talál.''')]),
])

footer = html.Div([
    html.Div([html.Span(
        '''A COVID-19 Beltéri Biztonsági Útmutató egy fejlesztés alatt álló eszköz, amelynek célja, 
        hogy megismertesse az érdeklődő felhasználót a COVID-19 beltéri levegőben történő átvitelének kockázatát 
        befolyásoló tényezőkkel, és segítséget nyújtson a kockázat kvantitatív értékelésében különböző körülmények 
        között. Megjegyezzük, hogy a modellparaméterek bizonytalansága és belső változékonysága akár nagyságrendbeli 
        hibákhoz is vezethet, amelyeket azonban kompenzálni lehet egy kellően kicsi kockázattűrés kiválasztásával. 
        Irányelvünk nem veszi figyelembe a rövidtávú légáramokat, amik jelentősen megnövelhetik a kockázatot 
        arcmaszkok viselete nélkül, a kísérő kéziratban tárgyalt módon ('''),
              html.A(children="Bazant & Bush, 2020",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(
                  '''). A COVID-19 Beltéri Biztonsági Útmutató használata a felhasználó kizárólagos felelőssége. 
                  Mindennemű biztosíték vagy garancia nélkül elérhető. A szerzők semmilyen felelősséget nem vállalnak 
                  a használatából eredő következményekért.''')]),
    html.Br(),
    html.Div("Külön köszönet: ")
], className='footer-small-text')
