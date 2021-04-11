import dash_html_components as html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions: Basque

"""

# Header
header = html.Div([
    html.H1(children='COVID-19: Gela itxietarako segurtasun gida'),
    html.Div([
        html.Div([html.Span(html.A(href=links.link_kasim,
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href=links.link_bush,
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ", eta ",
                  html.Span(html.A(href=links.link_bazant,
                                   children="Martin Z. Bazant",
                                   target='_blank')),
                  ""]),
        html.Div([html.Span(["Beyond Six Feet: A Guideline to Limit Indoor Airborne Transmission of COVID-19 ("]),
                  html.Span(html.A(href=links.link_paper,
                                   target='_blank',
                                   children='''Bazant & Bush, 2020''')),
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
language_dd = "Hizkuntza: "

# Unit systems
units_dd = "Unitateak: "
unit_settings = [
    {'label': "Sistema Ingelesa", 'value': "british"},
    {'label': "Sistema Metrikoa", 'value': "metric"},
]

# Modes
mode_dd = "Modua: "
app_modes = [
    {'label': "Basikoa", 'value': "basic"},
    {'label': "Aurreratua", 'value': "advanced"},
]

error_list = {
    "floor_area": "Akatsa: Zoruaren area ezin da hutsik egon.",
    "ceiling_height": "Akatsa: Sabaiaren altuera ezin da hutsik egon.",
    "recirc_rate": "Akatsa: Birzirkulazio tasa ezin da hutsik egon.",
    "aerosol_radius": "Akatsa: Aerosolaren erradioa ezin da hutsik egon.",
    "viral_deact_rate": "Akatsa: Desaktibazio birikoaren tasa ezin da hutsik egon.",
    "n_max_input": "Akatsa: Pertsona kopurua ezin da 2 baino txikiagoa izan.",
    "exp_time_input": "Akatsa: Esposizio denborak 0 baino handiagoa izan behar du. ",
    "air_exchange_rate": "Akatsa: aireberritze-tasak (ACH) 0 baino handiagoa izan behar du.",
    "merv": "Akatsa: Iragazpen Sistema (MERV) ezin da hutsik egon.",
    "prevalence": "Akatsa: Prebalentzia 0 baino haundiagoa izan behar du, eta 100.000 baino txikiagoa.",
    "atm_co2": "Error: Background CO\u2082 level is required."
}

# Main Panel Text
curr_room_header = "Gelaren Ezaugarriak: "
presets = [
    {'label': "Zuk definitu", 'value': 'custom'},
    {'label': "Ikasgela", 'value': 'classroom'},
    {'label': "Egongela", 'value': 'living-room'},
    {'label': "Eliza", 'value': 'church'},
    {'label': "Jatetxea", 'value': 'restaurant'},
    {'label': "Bulegoa", 'value': 'office'},
    {'label': "Treneko bagoia", 'value': 'subway'},
    {'label': "Hegazkin komertziala", 'value': 'airplane'},
]

curr_human_header = "Giza Portaera: "
presets_human = [
    {'label': "Zuk definitu", 'value': 'custom'},
    {'label': "Maskararekin, atseden hartzen", 'value': 'masks-1'},
    {'label': "Maskararekin, hizketan", 'value': 'masks-2'},
    {'label': "Maskararekin, ariketa egiten", 'value': 'masks-3'},
    {'label': "Maskararik gabe, atseden hartzen", 'value': 'no-masks-1'},
    {'label': "Maskararik gabe, hizketan", 'value': 'no-masks-2'},
    {'label': "Maskararik gabe, ariketa egiten", 'value': 'no-masks-3'},
    {'label': "Maskararik gabe, abesten", 'value': 'singing-1'},
]

curr_risk_header = "Arrisku Tolerantzia Maila: "
# presets_risk = [
#     {'label': "Low", 'value': 0.01},
#     {'label': "Medium", 'value': 0.1},
#     {'label': "High", 'value': 1},
# ]
risk_tol_marks = {
    # 0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Seguruagoa', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Arriskutsua'}
}

risk_tolerance_text = "Arrisku Tolerantzia Maila: "
risk_tol_desc = html.Div('''More vulnerable populations such as the elderly or those with preexisting medical 
conditions require a lower risk tolerance (~0.01). A higher risk tolerance will mean more expected 
transmissions during the expected occupancy period (see FAQ for details).''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})

curr_age_header = "Adin Taldea: "
presets_age = [
    {'label': "Umeak (<15 urte)", 'value': 0.23},
    {'label': "Helduak (15-64 urte)", 'value': 0.68},
    {'label': "Adinekoak (>64 urte)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: Umeak (<15 urte)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: Helduak (15-64 urte)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: Adinekoak (>64 urte)', 'style': {'width': '75px'}}
}

curr_strain_header = "Birus anduia: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2 (Wuhaneko Anduia)", 'value': 1},
    {'label': "SARS-CoV-2 - B.1.1.7 (Erresuma Batuko Anduia)", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: Wuhaneko', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: B.1.1.7/UK'}
}

pim_header = "Immune ehunekoa: "
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "Pertsona infektatu bat sartzen bada…"
risk_prevalence_desc = "Infekzioaren prebalentzia emanda…"
risk_personal_desc = "Nire arrisku pertsonala murrizteko…"
risk_options = [
    {'label': risk_conditional_desc, 'value': 'conditional'},
    {'label': risk_prevalence_desc, 'value': 'prevalence'},
    {'label': risk_personal_desc, 'value': 'personal'},
]

main_panel_s1 = '''Eredu honetan oinarrituta, gela honek hurrengo pertsona kopurua edukitzeak segurua* izan beharko 
luke: '''

main_panel_s1_b = html.Span([
    html.Span('''100.000tik '''),
])
main_panel_s2_b = html.Span([
    html.Span('''-ko infekzio prebalentzia'''),
    html.Sup('''1'''),
    html.Span(''' duen populazio batean COVID-19-aren transmisioa* murrizteko, leku honek ___ pertsona baino gutxiago 
    eduki beharko lituzke: ''')
])

main_panel_s1_c = html.Span([
    html.Span('''100.000tik '''),
])
main_panel_s2_c = html.Span([
    html.Span('''-ko infekzio prebalentzia'''),
    html.Sup('''1'''),
    html.Span(''' duen populazio batean, COVID-19z kutsatzeko nire arriskua murrizteko, leku honek ___ 
    pertsona baino gutxiago eduki beharko lituzke: ''')
])

units_hr = 'orduz'
units_min = 'minutuz'
units_days = 'egunez'
units_months = 'hilabeteak'

units_hr_one = 'ordua'
units_min_one = 'minutua'
units_day_one = 'eguna'
units_month_one = 'hilabete'

is_past_recovery_base_string = '{n_val} pertsona >{val:.0f} egunez,'
model_output_base_string = '{n_val} pertsona '
model_output_base_string_co2 = '{co2:.2f} ppm '
nt_bridge_string = " pertsona "
tn_bridge_string = " "

main_panel_six_ft_1 = "Bestalde, bi-metrotako distantzia mantentzeko gomendioaren arabera, gelan "
main_panel_six_ft_2 = " pertsona baino gutxiago eduki beharko lituzke, eta honek "
main_panel_six_fit_3 = " pasa eta gero, ez du segurtasun gidaren gomendioa* betetzen. "

six_ft_base_string = ' {} pertsona'
six_ft_base_string_one = ' {} pertsona'

graph_title = "Pertsona kopurua vs esposizio denbora"
graph_xtitle = "Gehieneko esposizio denbora \u03C4 (hours)"
graph_ytitle = "Gehieneko pertsona kopurua N"
transient_text = "Egora iragankorra"
steady_state_text = "Egoera iraunkorra"
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

main_airb_trans_only_disc = html.Div(["*Segurtasun gidak pertsona infektatu bakoitzetik ",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="aire bitarteko transmisioa",
                                                       target='_blank'), ),
                                      html.Span(''' murrizten du, probabilitatea arrisku tolerantzia (%10) 
                                      baino gutxiagokoa izan dadin zehaztutako esposiozio denbora 
                                      metagarrian.''')], className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*Segurtasun gidak pertsona infektatu bakoitzetik ",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="aire bitarteko transmisioa",
                                                       target='_blank'), ),
                                      html.Span(''' murrizten du, probabilitatea arrisku tolerantzia
                                      baino gutxiagokoa izan dadin zehaztutako esposiozio denbora 
                                      metagarrian.''')], className='airborne-text')

other_risk_modes_desc = html.Div('''Beste arrisku egoera ezberdinak Modu Aurreratuan kontuan hartzen dira. Zehazki, 
infekzioaren prebalentzia populazioan, txerto edo aldez aurreko espozioaren bitartez hartutako immunitatea, eta pertsona zehatz batetiko arriskua.''')

main_airb_trans_only_desc_b = html.Div(["*Segurtasun gidak pertsona infektatu bakoitzeko ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="aire bitarteko transmisio",
                                                         target='_blank'), ),
                                        html.Span(''' baten probabilitatea murrizten du, probabilidatea arrisku 
                                        tolerantzia baino gutxiagokoa izan dadin zehaztutako esposiozio 
                                        denbora metagarrian.''')], className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["*Segurtasun gidak ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="aire bitarteko transmisio",
                                                         target='_blank'), ),
                                        html.Span(''' probabilitea pertsona zehatz batentzat murrizten du, 
                                        probabilidatea arrisku tolerantzia baino gutxiagokoa izan dadin zehaztutako 
                                        esposiozio denbora metagarrian.''')], className='airborne-text')

airb_trans_only_disc = html.Div('''''', className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''Zure bertako prebalentzia zenbatezteko, hurrengo baliabideak lagungarri 
                                izan daitezke: '''),
                                # html.Span(html.A(href=links.link_jhu_dashboard,
                                #                  children="JHU COVID-19 Dashboard",
                                #                  target='_blank')),
                                # html.Span(''', '''),
                                html.Span(html.A(href=links.link_cdc_dashboard,
                                                 children="CDC-ko COVID-19-ko datuen jarraipena",
                                                 target='_blank')),
                                html.Span(", "),
                                html.Span(html.A(href=links.link_jhu_data,
                                                 children="JHU-ko Coronavirusaren Baliabide Zentrua",
                                                 target='_blank')),
                                html.Span(", "),
                                html.A(children="EEBB-ko Immunitate Estimazioak",
                                       href=links.link_cdc_immunity,
                                       target='_blank'),
                                html.Span(", "),
                                html.A(children="Immunitate Estimazio Internatzionalak",
                                       href=links.link_jhu_vaccine,
                                       target='_blank'),
                                ], className='airborne-text')

# Bottom panels text
n_input_text_1 = "Gela honek "
n_max_base_string = ' {:.0f} pertsona'
n_max_overflow_base_string = ' >{:.0f} pertsona'
n_input_text_2 = " pertsona baino gehiago baditu "
n_input_text_3 = " eta gero ez lituzke segurtasun gidaren gomendioak* beteko."

t_input_text_1 = ""
t_input_text_2 = " gora-beherako ordu kopururako, gelan gehienezko pertsona kopuruak "
t_input_text_3 = " izan beharko luke."

# About
about_header = "Sarrera"
about = html.Div([
    html.H6("Sarrera", style={'margin': '0'}),
    html.Div('''COVID-19aren hedapena murrizteko, osasun publikoko organismo ofizialek hainbat muga ezarri dituzte: 
    pertsonen arteko distantzia (2 metro), toki itxietan egoteko gehienezko denbora (15 minutu) eta pertsona kopurua 
    (25 pertsona), edo aireztapen behartua (gutxieneko 6 aireberritze orduro)'''),
    html.Br(),
    html.Div([html.Span('''COVID-19aren aire bitarteko transmisioa erakusten duten '''),
              html.A(children="froga zientifikoen",
                     href=links.link_docs,
                     target='_blank'),
              html.Span(''' kopurua hazten ari da. Horrelako transmisioak gela batean elkarbanatutako airean dauden 
              aerosol tanta infekziosoak arnastean gertatzen dira. Osasun publikoko organismoak aire bitarteko 
              transmisioak onartzen ari dira, baina faktore guztiak kontuan hartzen duen segurtasun gidarik ez dute eman. ''')]),
    html.Br(),
    html.Div([html.Span('''Aplikazio hau Kasim Khanek sortu du, Martin Z. Bazant eta John W. M. Bush-en 
    lankidetzarekin. Aplikazioak gela itxi baterako seguruak diren esposizio-denbora eta pertsona kopurua kalkulatzeko '''),
              html.A(children="modelo teoriko",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' bat erabiltzen du. Gelaren ezaugarriak, aireberritze eta iragazpen tasak, aurpegi-babesaren 
              erabilera, arnasaldiak eta arrisku tolerantzia sartuta, aplikazioak COVID-19aren transmisioa murrizteko 
              aholkuak ematen ditu gela itxi ezberdinetan.''')]),
    # html.Br(),
    # html.Div(['''In Basic mode, you can calculate the limits on safe occupancy following the entrance of a single
    # infected person into an indoor space. In Advanced Mode, you can take into account additional factors,
    # including infection prevalence and population immunity. Advanced Mode also allows you to assess safe occupancy
    # based on average CO2 concentration, which is related to the concentration of infectious aerosols.''']),
    html.Br(),
    html.Div([html.Span('''Aplikazioa oinarritzen den zientzia dohainik, zure erritmora eta online dagoen kurtso (MOOC) 
    batean irakasten da edX-n: '''),
              html.A(children="10.S95x COVID-19-aren Transmisionaren Fisika",
                     href=links.link_mooc,
                     target='_blank')]),
])

# Room Specifications
room_header = "Gelaren espezikifazioak – xehetasunak"

floor_area_text = "Zoruaren area (sq. ft.): "
floor_area_text_metric = "Zoruaren area (m²): "
ceiling_height_text = "Sabaiaren batezbesteko altuera (ft.): "
ceiling_height_text_metric = "Sabaiaren batezbesteko altuera (m): "

ventilation_text = "Aireberritze Sistema: "
vent_type_output_base = "{:.1f} "
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (Kanpoko aire-berritzearen tasa)"])
ventilation_text_adv = html.Span(["Aireberritze Sistema (hr", html.Sup("-1"), ", Kanpoko aire-berritzearen tasa): "])
ventilation_types = [
    {'label': "Leiho itxiak", 'value': 0.3},
    {'label': "Leiho irekiak", 'value': 2},
    {'label': "Aireberritze mekanikoa", 'value': 3},
    {'label': "Leiho irekiak haizagailuekin", 'value': 6},
    {'label': "Aireberritze mekaniko hobea", 'value': 8},
    {'label': "Laborategia, Jatetxea", 'value': 9},
    {'label': "Taberna", 'value': 15},
    {'label': "Ospitalea/Treneko bagoia", 'value': 18},
    {'label': "Laborategi toxikoa/Hegazkina", 'value': 24},
]

filtration_text = "Iragazpen Sistema: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Iragazpen Sistema (MERV): "
filter_types = [
    {'label': "Ezer ez", 'value': 0},
    {'label': "Bizilekua, aire girotu txikia (leihokoa)", 'value': 2},
    {'label': "Bizilekua/Komertziala/Industriala", 'value': 6},
    {'label': "Bizilekua/Komertziala/Ospitalea", 'value': 10},
    {'label': "Ospitalea/Ebakuntza Gelak", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_text = "Birzirkulazio tasa: "
recirc_type_output_base = "{:.1f} "
recirc_type_output_units = html.Span(["hr", html.Sup("-1")])
recirc_text_adv = html.Span(["Birzirkulazio tasa (hr", html.Sup("-1"), "): "])
recirc_types = [
    {'label': "Ezer ez", 'value': 0},
    {'label': "Motela", 'value': 0.3},
    {'label': "Ertaina", 'value': 1},
    {'label': "Azkarra", 'value': 10},
    {'label': "Hegazkina", 'value': 24},
    {'label': "Treneko bagoia", 'value': 54},
]

humidity_text = "Hezetasun erlatiboa: "
humidity_marks = {
    0.01: {'label': '% 1 Oso Lehorra', 'style': {'max-width': '25px'}},
    # 0.2: {'label': '20%: Airplane', 'style': {'max-width': '50px'}},
    0.3: {'label': '% 30 Lehorra'},
    0.6: {'label': '% 60 Ertaina'},
    0.99: {'label': '% 99 Oso Hezea'},
}

need_more_ctrl_text = '''Gelako ezaugarrien kontrol gehiagoren beharrean? Modu Aurreratua hautatu webgune 
hasierako menu zabalgarrian.'''

human_header = "Giza Portaera – xehetasunak"
# Human Behavior
exertion_text = "Arnasa hartzearen erritmoa: "
exertion_types = [
    {'label': "Lasaia/Eserita", 'value': 0.49},
    {'label': "Zutik/Oinez", 'value': 0.54},
    {'label': "Abesten", 'value': 1},
    {'label': "Ariketa fisiko arina", 'value': 1.38},
    {'label': "Ariketa fisiko neurritsua", 'value': 2.35},
    {'label': "Intentsitate handiko ariketa fisikoa", 'value': 3.30},
]

breathing_text = "Arnas Hartzea: "
expiratory_types = [
    {'label': "Arnasketa mantsoa", 'value': 1.1},
    {'label': "Arnasketa normala", 'value': 4.2},
    {'label': "Arnasketa sakona", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Hitz egiten (baxu, xuxurlaka)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Hitz egiten (normala)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Hitz egiten (altu, oihuka)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Abesten", 'value': 970},
]

mask_type_text = "Maskara Iragazpenaren Eraginkortasuna (maskara mota): "
mask_type_marks = {
    0: {'label': "% 0 (Ezer ez, aurpegi babesa)", 'style': {'max-width': '75px'}},
    0.5: {'label': "% 50 (Kotoia, Flanela)", 'style': {'max-width': '50px'}},
    0.7: {'label': "% 70 (Geruza askotako Kotoia, Zeta)", 'style': {'max-width': '75px'}},
    0.90: {'label': "% 90 (Maskara kirurgikoa, erabili eta botatzekoa)", 'style': {'max-width': '75px'}},
    # 0.99: {'label': "99% (N95 resp-irator)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Ezer ez, aurpegi babesa", 'value': 0},
    {'label': "Kotoia, Flanela", 'value': 0.5},
    {'label': "Geruza askotako Kotoia, Zeta", 'value': 0.7},
    {'label': "Maskara kirurgikoa, erabili eta botatzekoa", 'value': 0.9},
    {'label': "N95 maskara", 'value': 0.99},
]

mask_fit_text = "Maskararen estutzea aurpegira: "
mask_fit_marks = {
    0: {'label': '% 0 Ezer ez', 'style': {'max-width': '50px'}},
    0.5: {'label': '% 50 Txarra'},
    0.95: {'label': '% 95 Ona'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Maiz Egindako Galderak"
other_io = "Beste Parametro Batzuk"

faq_top = html.Div([
    html.H6("Maiz Egindako Galderak"),
    html.H5("Zergatik ez da nahikoa 2 metroko distantzia?"),
    html.Div([
        html.Div([html.Span('''Bi metrotako distantziak pertsona infektatu batek eztula egitean botatzen dituen tanta 
        hadietatik babesten zaitu, musukoen modura; baina ez zaitu airean esekita dauden '''),
                  html.A(children="aerosol infekziosoen bitarteko",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' transmisioetatik babesten gelako airea homogeneoki nahasi denean. Gela baten barruan, 
                  hogei metrotako distantziak ez du bi metrotako distantziak baino babes haundiagorik ematen aire 
                  bitarteko transmisioetatik. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Beste transmisio moduak daude?"),
    html.Div([
        html.Div([html.A(children="Uste denez, aire-bitarteko transmisioa ",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' COVID-19aren transmisio modu nagusia da, baina beste transmisio moduak ere badira: 
                  infektatua dagoen azalera batekin zuzeneko kontaktuaren bitartez, tanta haundien bitarteko 
                  transmisioa (infektatua dagoen pertsona eztulka edo doministikuka dabilenean), edota infektatua 
                  dagoen pertsona batengandik denbora luzez oso gertu arnas eginez (hark botatako airea arnasten 
                  dugunean). Azkeneko bi moduak transmisio modu garrantzitsuak dira ere, baina maskarak edo 
                  aurpegi-babesak erabiltzean, transmisio modu hauen arriskua asko txikitzen da (aire-bitarteko 
                  transmisioaren arriskua ez da txikitzen, ordea).''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Gelaren airea nahasketa homogeneoa delako hipotesia egia al da?"),
    html.Div([
        html.Div([html.Span('''Hainbat faktorek sustatzen dute aire nahasketa gela itxi batean: konbekzio naturalak 
        (berogailuetatik, aire girotuetatik edo leihoetatik), konbekzio behartuak (haizagailuetatik), 
        eta gure mugimenduak eta arnas hartzeak. '''),
                  html.A(children="Artikuluan",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''' salbuespen batzuk eztabaidatzen dira, baina nahastea homogeneoa delako hipotesia oso 
                  maiz erabiltzen da aire-bitarteko gaixotasun transmisioak teoretikoki modelatzean. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Zein da aholku hauen balioa oso handiak diren tokietan?"),
    html.Div([
        html.Div([html.Span('''Antzokietan, estadioetan, edo aireztatutako jende ugariko beste tokietan, aire-bitarteko 
        transmisio arriskua nabarmena da eta aholku gida baliogarria. Maskarak edo aurpegi-babesak 
        erabiltzen ez badira, ordea, beste arrisku mota bat dago: irismen-laburreko transmisioak infektatua 
        dagoen pertsona batengandik gertu arnasa egitean; kasu honetarako estimazioak '''),
                  html.A(children="artikuluan",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''' jasotzen dira.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Zergatik da sabaiaren altuera garrantzitsua?"),
    html.Div([
        '''Sabaiaren altuera gelaren guztizko bolumenean eragina dauka eta bolumen hau beharrezkoa da aerosol 
        infekziosoen kontzentrazioa (hau da, aerosol kopurua bolumen unitate bakoitzeko) estimatzeko. 
        Kontzentrazio hau beharrezkoa da gelaren COVID-19 transmisio arriskua estimatzeko.'''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Nire gelako ACH/MERV zenbakiak badakizkit. Non sartu ditzaket?"),
    html.Div('''
        Zure gelako ezaugarrien kontrol handiagoa behar baduzu, “Modu Aurreratua” hautatu webgune hasierako 
        menu zabalgarrian. 
    ''', className='faq-answer'),
    html.Br(),
    html.H5("Zergatik N95 musukoek %99-ko eraginkortasuna dute?"),
    html.Div('''N95 musukoek %95-ko eraginkortasunatik gora dute 0.3 μm-ko partikula tamainarako. Hau airean esekita 
    gelditzen diren COVID-19aren tanten tamaina baina 10 aldiz txikiagoa da. Haundiagoak diren 
    tantentzat, N95 musukoek eraginkortasun haundiagoa daukate, %100-tik gertu.''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Parametro ezkuturik ba al dago Modu Basikoan?"),
    html.Div([html.Span('''Parametro fisiko garrantzitsu guztiak '''),
              html.A(children="artikuluan",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''zehaztu dira. Modu Basikoan, aplikazioak aerosolari 2 μm-ko erradio 
              efektiboa ematen dio (% 60ko hezetasunean) eta 0.6/h (%100eko hezetasunean) 
              gehienezko deaktibazio birikoko tasa. Bi parametro hauek hezetasun erlatiboarekin (RH) 
              hazten dira. Desaktibazio birikoaren tasa zuhurtziaz hautatu da, kontserbatiboki tasa 
              txikietara jota (desaktibazio mantsoa). Desaktibazio birikoaren tasa izpi ultramoreak 
              (UV-C) edo desinfektante kimikoak (adib. hidrogeno peroxidoa, ozonoa) erabiliz bizkortu 
              daiteke. Aplikazioak gaixotasunerako oinarrizkoa den beste parametro baten balioa 
              estimatzen du: gaixo dagoen persona batek arnastutako airea beste pertsona bat gaixotzeko 
              daukan arriskua, C'''),
              html.Sub("q"),
              html.Span(''' (infekzio kantitatea bolumen unitate bakoitzeko). Balio hau erabiltzaileak hautatutako 
              Arnasa Hartzearen opzioa erabiliz estimatzen da, '''),
              html.A(children="artikuluan",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' ematen den Figura 2-ko balioen arabera. Modu Aurreratuan, parametro hauek erabiltzaileak 
              berak zehaztu ditzake:''')],
             className='faq-answer'),
])

aerosol_radius_text = "Aerosolaren erradio efektiboa (RH = %60 rako), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Gehienezko desaktibazio birikoaren tasa (RH = %100-rako), \u03BB", html.Sub('vmax'), " (/hr): "])

pop_immunity_header = "Biztanleriaren Immunitatea: "
perc_immune_label = html.Span(["Immune ehunekoa p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["Infekzioso ehunekoa p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["Txertatutako ehunekoa p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["Aldez aurretik infektatuak izan diren ehunekoa p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["Populazio sentikorraren ehunekoa p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''Biztanleriaren infekziosoen ehunekoa p''', html.Sub('i'), ''' kalkulatzeko, 
beste arrisku egoeren kutxatiletan zehaztutako infekziosoen prebalentzia erabiltzen da (Infekzioaren 
prebalentzia emanda…, Nire arrisku pertsonala murrizteko…). Immune ehunekoaren p''', html.Sub('im'), ''' estimazio 
kontserbadore bat egiten da txertatutako biztanleriaren ehunekoa eta kasu kopuruaren aldaketa kontuan 
hartuz, detektatuak izan ez diren kasuak alde batera utzita. Bi kopuru hauek sentikortasun ehunekoa p''',
                                        html.Sub('s'), ''' kalkulatzeko erabiltzen dira. Modu Basikoan 
                                        eta lehenengo arrisku moduan (Pertsona infektatu bat sartzen 
                                        bada…), ehuneko hau %100-koa hartzen da.''']),
                              html.Br(),
                              html.Div(['''Hemen esteka lagungarri batzuk p''', html.Sub('i'), ''' eta p''',
                                        html.Sub('im'), ''' zehazteko: ''',
                                        html.Span(html.A(href=links.link_cdc_dashboard,
                                                         children="CDC-ko COVID-19-ko datuen jarraipena",
                                                         target='_blank')),
                                        html.Span(", "),
                                        html.Span(html.A(href=links.link_jhu_data,
                                                         children="JHU-ko Coronavirusaren Baliabide Zentrua",
                                                         target='_blank')),
                                        html.Span(", "),
                                        html.A(children="EEBB-ko Immunitate Estimazioak",
                                               href=links.link_cdc_immunity,
                                               target='_blank'),
                                        html.Span(", "),
                                        html.A(children="Immunitate Estimazio Internatzionalak",
                                               href=links.link_jhu_vaccine,
                                               target='_blank'),
                                        ])
                              ])

values_interest_header = "Interesgarriak diren kalkulatutako kantitateak: "
values_interest_desc = html.Div([
    html.H5("Zer kalkulatzen du aplikazioak zehazki?"),
    html.Div([
        html.Div([html.Span('''Aplikazioak gela baten barruan onargarria den gehieneko esposizio denbora 
        metagarria (hau da, gelan dagoen pertsona kopuruaren eta denboraren arteko biderketa) kalkulatzen 
        du. COVID-19aren hedaketa persona infektatu bakoitzeko batez-besteko transmisio zenbakia (hau da,
         gela bateko “erreprodukzio zenbakia“) zehaztutako arrisku tolerantzia baino txikiagoa egitean
          murrizten da. Aplikazioak interesgarriak izan litezkeen beste hainbat kantitate ere kalkulatzen
           ditu, '''),
                  html.A(children="artikuluan",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''' definituta direnak:''')]),
    ], className='faq-answer'),
])
relative_sus_label = html.Span(["Sentikortasun erlatiboa s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["Kanpoko aireko frakzioa Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Aerosol iragazkiaren eraginkortasuna p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Arnas-fluxuaren abiadura Q", html.Sub('b'), ": "])
cq_label = html.Span(["Arnastutako airearen transmisio/infekzio arriskua C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Maskara zeharkatzearen probabilitatea p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Gelaren bolumena V: "])
vent_rate_Label = html.Span(["Aireztapenaren fluxuaren abiadura (kanpoko airea) Q: "])
recirc_rate_label = html.Span(["Bueltatzen den aire-fluxuaren abiadura (birzirkulazioa) Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Aire-iragazpen tasa (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Aerosolaren erradioa, hezetasuna kontuan hartuz r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Desaktibazio birikoaren tasa, hezetasuna kontuan hartuz \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Aerosolaren egonkortze abiadura v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Kontzentrazioaren erlaxazio tasa \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Aire-bitarteko transmisio tasa \u03B2\u2090: "])

graph_output_header = "Graph Output: "
faq_graphs_text = html.Div([
    html.H5("Graph Output: "),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Eredu honek kontuan hartzen al du infekzioaren prebalentzia bertako biztanleriagan?"),
    html.Div(['''Infekzioaren prebalentziaren eragina bertako populazioan Modu Aurreratuan kontuan har daiteke. 
    Modu horretan, “Beste Parametro Batzuk” esaten duen kutxatilan, beste faktore batzuk ere kontuan 
    har daitezke, adibidez, biztaleriaren immunizazio-maila, txerto edo aldez aurreko infekzioetatik 
    lor daitekeena.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("Galdera gehiago?"),
    html.Div([html.Span('''Xehetasun eta erreferentzia gehiagorako "'''),
              html.A(children="2 metrotik gora",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''" (ingelesez) artikulua irakurri eta webgune hasieran jasotako esteketan sartu.''')]),
])

footer = html.Div([
    html.Div([html.Span('''COVID-19 Gela Itxietarako Segurtasun Gida garapenean dagoen tresna da. Erabiltzailea 
    aire-bitarteko COVID19aren transmisioa sustatzen duten faktoreekin ohitzea eta transmisio
     arriskuaren ebaluazio kuantitatiboan laguntzea du helburu. Parametroen ziurgabetasunak eta
      barne-aldakortasunak magnitude orden bateko akatsak eman ditzaketela ohartarazten dugu. Arrisku
       Tolerantzia balio txikiak hautatuz akats horiek kopentsatu daitezke. Gida honek ez ditu
        irismen-laburreko transmisioak kontuan hartzen, eta hauek nabarmenki areagotu dezakete transmisio
         arriskua maskarak edo aurpegi-babesak erabiltzen ez direnean, '''),
              html.A(children="artikuluan",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' (Bazant & Bush, 2020) eztabaidatzen den moduan. COVID-19 Gela Itxietarako 
              Segurtasun Gidaren erabilpena erabiltzailearen erantzukizuna da soilik. Gida inolako 
              bermerik gabe jarri da eskuragai. Egileek ez dute inolako erantzukizunik onartzen.''')]),
    html.Br(),
    html.Div("")
], className='footer-small-text')
