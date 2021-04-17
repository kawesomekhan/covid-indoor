import dash_html_components as html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

Swedish

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

# Header
header = html.Div([
    html.H1(children='COVID-19 Säkerhetsrekommendationer i inomhusmiljö'),
    html.Div([
        html.Div([html.Span(html.A(href="https://www.linkedin.com/in/kasim-k-a92620b1/",
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href="https://math.mit.edu/~bush/",
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ", och ",
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
language_dd = "Språk: "

# Unit systems
units_dd = "Enheter: "
unit_settings = [
    {'label': "Engelska", 'value': "british"},
    {'label': "Metersystemet (or SI)", 'value': "metric"},
]

# Modes
mode_dd = "Läge: "
app_modes = [
    {'label': "Basic", 'value': "basic"},
    {'label': "Avancerad", 'value': "advanced"},
]

error_list = {
    "floor_area": "Fel: Golvyta kan inte vara tomt.",
    "ceiling_height": "Fel: Takhöjd kan inte vara tomt.",
    "recirc_rate": "Fel: Återcirkulationshastighet kan inte vara tomt.",
    "aerosol_radius": "Fel: Aerosolradie kan inte vara tomt.",
    "viral_deact_rate": "Fel: Virusavaktiveringsgrad kan inte vara tomt.",
    "n_max_input": "Fel: Antal personer kan inte vara mindre än 2.",
    "exp_time_input": "Fel: Exponeringstid måste vara längre än 0.",
    "air_exchange_rate": "Fel: Ventilationshastighet (ACH) måste vara större än 0.",
    "merv": "Fel: Filtreringssystem (MERV) kan inte vara tomt.",
    "prevalence": "Fel: Prevalens måste vara större än 0 och mindre än 100.000."
}

# Main Panel Text
curr_room_header = "Typ av utrymme: "
presets = [
    {'label': "Konfigurera fritt", 'value': 'custom'},
    {'label': "Villa", 'value': 'house'},
    {'label': "Vardagsrum", 'value': 'living-room'},
    {'label': "Restaurang", 'value': 'restaurant'},
    {'label': "Kontor", 'value': 'office'},
    {'label': "Klassrum", 'value': 'classroom'},
    {'label': "Tunnelbana/Spårvagn", 'value': 'subway'},
    {'label': "Trafikflyg", 'value': 'airplane'},
    {'label': "Kyrka", 'value': 'church'},
]

curr_human_header = "Mänskligt beteende: "
presets_human = [
    {'label': "Konfigurera fritt", 'value': 'custom'},
    {'label': "Med mask, Vila", 'value': 'masks-1'},
    {'label': "Med mask, Samtal", 'value': 'masks-2'},
    {'label': "Med mask, Tträning/motion", 'value': 'masks-3'},
    {'label': "Utan mask, Vila", 'value': 'no-masks-1'},
    {'label': "Utan mask, Samtal", 'value': 'no-masks-2'},
    {'label': "Utan mask, Träning/motion", 'value': 'no-masks-3'},
    {'label': "Utan mask, Sång", 'value': 'singing-1'},
]

curr_risk_header = "Nivå Risktolerans: "

risk_tolerance_text = "Nivå Risktolerans: "
risk_tol_desc = html.Div('''Mer utsatta grupper som äldre eller personer med redan existerande medicinska tillstånd 
kräver lägre risktolerans. En högre risktolerans innebär fler förväntade överföringar under den förväntade 
beläggningsperioden (se Vanliga Frågor för mer information).''', style={'font-size': '13px',
                                                                        'margin-left': '20px'})
risk_tol_marks = {
    # 0.01: {'label': '0.01: Säkrare', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Säkrare', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Osäker'}
}

curr_age_header = "Åldersgrupp: "
presets_age = [
    {'label': "Barn (<15 år)", 'value': 0.23},
    {'label': "Vuxna (15-64 år)", 'value': 0.68},
    {'label': "Seniorer (>64 år)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: Barn (<15 år)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: Vuxna (15-64 år)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: Seniorer (>64 år)', 'style': {'width': '75px'}}
}

curr_strain_header = "Virusvariant: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2 (Wuhan-varianten)", 'value': 1},
    {'label': "SARS-CoV-2 - B.1.1.7 (Brittiska virusvarianten)", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: Wuhan', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: B.1.1.7/UK'}
}

pim_header = "Procent immune: "
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "Om en smittad person går in…"
risk_prevalence_desc = "Med en infektionsprevalens på…"
risk_personal_desc = "För att begränsa min personliga risk…"
risk_options = [
    {'label': risk_conditional_desc, 'value': 'conditional'},
    {'label': risk_prevalence_desc, 'value': 'prevalence'},
    {'label': risk_personal_desc, 'value': 'personal'},
]

main_panel_s1 = "Baserat på denna modell borde det vara säkert för detta utrymme att ha: "

main_panel_s1_b = html.Span([
    html.Span('''För att begränsa COVID-19 smitta* i en population med en infektionsprevalens'''),
    html.Sup('''1'''),
    html.Span(''' på ''')
])
main_panel_s2_b = ''' per 100.000, bör detta utrymme inte ha fler än: '''

main_panel_s1_c = html.Span([
    html.Span('''För att begränsa min chans att bli smittad av COVID-19 i en befolkning med en infektionsprevalens'''),
    html.Sup('''1'''),
    html.Span(''' på ''')
])
main_panel_s2_c = ''' per 100.000, bör detta utrymme inte ha fler än: '''

units_hr = 'timmar'
units_min = 'minuter'
units_days = 'dagar'
units_months = 'månader'

units_hr_one = 'timme'
units_min_one = 'minut'
units_day_one = 'dag'
units_month_one = 'månad'

is_past_recovery_base_string = '{n_val} personer i >{val:.0f} dagar,'
model_output_base_string = '{n_val} personer i '
nt_bridge_string = " personer i "
tn_bridge_string = " i "

main_panel_six_ft_1 = '''Däremot skulle rekommendationen om 2-meters (sex fots) avståndshållande begränsa antalet 
personer till '''
main_panel_six_ft_2 = " vilket skulle bryta mot rekommendationen* efter "

six_ft_base_string = ' {} personer'
six_ft_base_string_one = ' {} personer'

graph_title = "Beläggning vs. Exponeringstid"
graph_xtitle = "Maximal exponeringstid \u03C4 (timmar)"
graph_ytitle = "Maximal beläggning N"
transient_text = "Övergående"
steady_state_text = "Stabilt tillstånd"

main_airb_trans_only_disc = html.Div(["*Rekommendationen begränsar sannolikheten för ",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="luftburen smitta",
                                                       target='_blank'), ),
                                      html.Span(''' per person till att vara mindre än risktoleransen under den 
                                      kumulativa exponeringstiden som anges.''')], className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*Rekommendationen begränsar sannolikheten för ",
                                            html.Span(html.A(href=links.link_docs,
                                                             children="luftburen smitta",
                                                             target='_blank'), ),
                                            html.Span(''' till att vara mindre än risktoleransen (10%) under den 
                                            kumulativa exponeringstiden som anges.''')], className='airborne-text')

other_risk_modes_desc = html.Div('''Andra riskscenarier beaktas i Avancerat Läge. Särskilt kan man överväga 
förekomsten av infektion i befolkningen, immunitet förvärvad genom vaccination eller tidigare exponering och risken 
för en specifik individ.''')

main_airb_trans_only_desc_b = html.Div(["*Riktlinjen begränsar sannolikheten för att en ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="luftburen",
                                                         target='_blank'), ),
                                        html.Span(''' överföring per smittad person till att vara mindre än 
                                        risktoleransen under den kumulativa exponeringstiden som anges.''')],
                                       className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["*Riktlinjen begränsar sannolikheten för ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="luftburen",
                                                         target='_blank'), ),
                                        html.Span(''' överföring till en specifik individ att vara mindre än 
                                        risktoleransen under den kumulativa exponeringstiden som anges.''')],
                                       className='airborne-text')

airb_trans_only_disc = html.Div('''''', className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''Referera till förljande resurser för att uppskatta din lokala prevalens: 
                                '''),
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
n_input_text_1 = "Om det i utrymmet finns "
n_max_base_string = ' {:.0f} personer'
n_max_overflow_base_string = ' >{:.0f} personer'
n_input_text_2 = " personer skulle riktlinjen att överskridas efter "
n_input_text_3 = "."

t_input_text_1 = "Om folk tillbringar ungefär "
t_input_text_2 = " timmar här bör beläggningen begränsas till "
t_input_text_3 = "."

# About
about_header = "Om appen"
about = html.Div([
    html.H6("Om appen", style={'margin': '0'}),
    html.Div('''För att mildra spridningen av COVID-19 har officiella riktlinjer för folkhälsa rekommenderat gränser 
    för: avstånd till andra personer (2 meter / 6 fot), beläggningstid (15 minuter), maximalt antal personer (25) 
    eller minimal ventilation (6 luftombyten per timme).'''),
    html.Br(),
    html.Div([html.Span('''Det finns växande '''),
              html.A(children="vetenskapliga bevis",
                     href=link_docs,
                     target='_blank'),
              html.Span(''' för luftburen överföring av COVID-19, som inträffar när smittsamma aerosoldroppar byts ut 
              genom andning av delad inomhusluft. Medan folkhälsoorganisationer börjar erkänna luftburen överföring 
              har de ännu inte tillhandahållit säkerhetsrekommendationer som innehåller alla relevanta 
              variabler.''')]),
    html.Br(),
    html.Div([html.Span('''Denna app, utvecklad av Kasim Khan i samarbete med Martin Z. Bazant och John W. M. Bush, 
    använder en '''),
              html.A(children="teoretisk modell",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' för att beräkna säkra exponeringstider och beläggningsnivåer för inomhusutrymmen. Genom 
              att justera utrymmessspecifikationer, ventilations- och filtreringshastigheter, användning av 
              ansiktsmasker, andningsaktiviteter och risktolerans (i de andra flikarna) kan man se hur man kan minska 
              överföringen av  COVID-19 i inomhusmiljöer av olika slag.''')]),
    html.Br(),
    html.Div([html.Span('''Metodiken bakom appen undervisas i en gratis, storskalig, självgående, öppen nätkurs (
    MOOC) via edX.org: '''),
              html.A(children="10.S95x Physics of COVID-19 Transmission",
                     href=links.link_mooc,
                     target='_blank')])
])

# Room Specifications
room_header = "Utrymmesspecifikation – Detaljer"

floor_area_text = "Total golvyta (sq. ft.): "
floor_area_text_metric = "Total golvyta (m²): "
ceiling_height_text = "Genomsnittlig takhöjd (ft.): "
ceiling_height_text_metric = "Genomsnittlig takhöjd (m): "

ventilation_text = "Ventilationssystem: "
vent_type_output_base = "{:.1f} "
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (utomhus ACH)"])
ventilation_text_adv = html.Span(["Ventilationssystem (hr", html.Sup("-1"), ", utomhus ACH): "])
ventilation_types = [
    {'label': "Stängda fönster", 'value': 0.3},
    {'label': "Öppna fönster", 'value': 2},
    {'label': "Mekanisk ventilation", 'value': 3},
    {'label': "Öppna fönster med fläktar", 'value': 6},
    {'label': "Bättre mekanisk ventilation", 'value': 8},
    {'label': "Laboratorium, Restaurang", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Sjukhus / tunnelbana", 'value': 18},
    {'label': "Kemi-laboratorium / flygplan", 'value': 24},
]

filtration_text = "Filtreringssystem: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Filtreringssystem (MERV): "
filter_types = [
    {'label': "Saknas", 'value': 0},
    {'label': "AC enhet under fönster", 'value': 2},
    {'label': "Bostäder / Kommersiella / Industriella", 'value': 6},
    {'label': "Bostäder / Kommersiella / Sjukhus", 'value': 10},
    {'label': "Sjukhus & Allmänkirurgi", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_text = "Återcirkulationshastighet: "
recirc_type_output_base = "{:.1f} återcirkulation ACH"
recirc_text_adv = "Återcirkulationshastighet (återcirkulation ACH): "
recirc_types = [
    {'label': "Ingen", 'value': 0},
    {'label': "Långsam", 'value': 0.3},
    {'label': "Måttlig", 'value': 1},
    {'label': "Hastig", 'value': 10},
    {'label': "Flygplan", 'value': 24},
    {'label': "Tunnelbanevagn", 'value': 54},
]

humidity_text = "Relativ luftfuktighet: "
humidity_marks = {
    0.01: {'label': '1%: mycket låg', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: flygplan', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: låg'},
    0.6: {'label': '60%: medel'},
    0.99: {'label': '99%: hög'},
}

need_more_ctrl_text = '''Behöver du mer kontroll över dina ingångsvärden? Byt till avancerat läge med 
rullgardinsmenyn högst upp på sidan. '''

human_header = "Mänskligt beteende – Detaljer"
# Human Behavior
exertion_text = "Andningsfrekvens: "
exertion_types = [
    {'label': "Vilande", 'value': 0.49},
    {'label': "Stående", 'value': 0.54},
    {'label': "Sång", 'value': 1},
    {'label': "Lätt träning", 'value': 1.38},
    {'label': "Måttlig träning", 'value': 2.35},
    {'label': "Hård träning", 'value': 3.30},
]

breathing_text = "Andningsaktivitet: "
expiratory_types = [
    {'label': "Andning (lätt)", 'value': 1.1},
    {'label': "Andning (normal)", 'value': 4.2},
    {'label': "Andning (tung)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Tal (viskning)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Tal (normal samtalsnivå)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Tal (högt)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Sång", 'value': 970},
]

mask_type_text = "Maskfiltreringseffektivitet (masktyp): "
mask_type_marks = {
    0: {'label': "0% (ingen, ansiktsvisir)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (bomull, flanell)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (multi-skikt bomull, silke)", 'style': {'max-width': '50px'}},
    0.90: {'label': "90% (kirurgisk engångsmask)", 'style': {'max-width': '50px'}},
    # 0.99: {'label': "99% (N95 ansiktsmask)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Ingen, ansiktsvisir", 'value': 0},
    {'label': "Bomull, Flanell", 'value': 0.5},
    {'label': "Multi-skikt Bomull, Silke", 'value': 0.7},
    {'label': "Kirurgisk engångsmask", 'value': 0.9},
    {'label': "N95 ansiktsmask", 'value': 0.99},
]

mask_fit_text = "Masktillpassning enligt krav: "
mask_fit_marks = {
    0: {'label': '0%: Ingen', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Dålig'},
    0.95: {'label': '95%: Bra'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Vanliga frågor"
other_io = "Andra parametrar"

faq_top = html.Div([
    html.H6("Vanliga frågor"),
    html.H5("Varför är 2 meters (6 fots) avstånd inte tillräckligt?"),
    html.Div([
        html.Div([html.Span('''Ett avstånd på 2 meter (eller 6 fot) skyddar dig mot stora droppar som sprids av en 
        smittad person som hostar, liksom ansiktsmasker gör. Emellertid skyddar den inte mot '''),
                  html.A(children="luftburen överföring",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' av infektiösa aerosoler som hänger i luften och blandas i ett utrymme. Inomhus är 
                  människor inte säkrare från luftburen transmission på 20 meters avstånd än på 2 meter.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Finns det andra överföringssätt?"),
    html.Div([
        html.Div([html.A(children="Luftburen överföring",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' anses vara det dominerande överföringssättet för COVID-19, men andra sätt är möjliga, 
                  såsom överföring av "fomite" genom direktkontakt med smittsamma rester på ytor, överföring av 
                  "stora droppar" via hosta eller nysningar samt aerosolöverföring på kort distans via 
                  utandningsluften hos en infekterad person under en längre tid. Även om de två sistnämnda sätten kan 
                  vara betydelsefulla elimineras de till stor del när ansiktsmasker eller sköldar bärs; dock kvarstår 
                  risken för luftburen överföring.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Kan vi verkligen anta ett utrymme med väl blandad luft?"),
    html.Div([
        html.Div([html.Span('''Det finns många bidrag till omblandning av luften i inomhusutrymmen, inklusive 
        flytkraftsdrivna flöden (från värmare, luftkonditioneringsapparater eller fönster), forcerad konvektion från 
        ventiler och fläktar och mänsklig rörelse och andning. Även om det finns undantag, som diskuteras i '''),
                  html.A(children="artikeln",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', används antagandet om väl omblandad luft i stor utsträckning i den teoretiska 
                  modelleringen av den luftburna överföringen av sjukdomar.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Gäller samma rekommendationer i mycket stora utrymmen?"),
    html.Div([
        html.Div([html.Span('''I konserthallar, arenor eller andra stora, ventilerade utrymmen med ett stort antal 
        människor är risken för luftburen överföring betydande och korrekt behandlad i rekommendationerna. Om masker 
        eller ansiktsskydd inte bärs, finns det dock en ytterligare risk för kortdistansöverföring via 
        utandningsluft, uppskattat i '''),
                  html.A(children="artikeln",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Vilken roll spelar takhöjden?"),
    html.Div([
        '''Takhöjden påverkar den totala utrymmesvolymen, som krävs för att uppskatta koncentrationen av infektiösa 
        aerosoler (antal aerosoler per volymenhet). Denna koncentration behövs för att uppskatta överföringsrisken 
        för COVID-19 i utrymmet. '''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Jag vet mina ACH / MERV-värden. Var kan jag skriva in dem?"),
    html.Div('''
        Om du behöver mer kontroll över dina ingångsvärden, byt till Avancerat Läge med rullgardinsmenyn högst upp på 
        webbsidan.
    ''', className='faq-answer'),
    html.Br(),
    html.H5("Varför har N95 andningsskydd 99% effektivitet?"),
    html.Div('''N95-andningsskydd har minst 95% filtreringseffektivitet för en partikelstorlek på 0.3 μm, vilket är 
    10 gånger mindre än droppstorlekarna vid luftburen COVID-19-transmission. För större droppar är N95-andningsskydd 
    ännu effektivare och når nivåer nära 100%.''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Finns det några dolda parametrar i Basic-läge?"),
    html.Div([html.Span('''Alla relevanta fysiska parametrar beskrivs i '''),
              html.A(children="artikeln",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. I Basic-läge antar appen ett standardvärde för effektiv aerosolradie på 2 μm (vid 60% 
              luftfuktighet) och en maximal viral deaktiveringshastighet på 0,6 / h (vid ~ 100% luftfuktighet), 
              som båda ökar med relativ luftfuktighet (RH). Uppskattningar för viral deaktiveringshastighet avviker 
              mot det konservativa hållet av långsammare deaktivering. Viraldeaktiveringshastigheten kan ökas genom 
              ultraviolett strålning (UV-C) eller kemiska desinfektionsmedel (t.ex. väteperoxid, ozon). Appen 
              uppskattar också den viktigaste sjukdomsparametern, infektionsnivån hos utandad luft, C'''),
              html.Sub("q"),
              html.Span(''' (infektionsmängd per volymenhet), från den angivna andningsaktiviteten, med hjälp av 
              tabellvärden i figur 2 i '''),
              html.A(children="artikeln",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. Du definierar dessa parametrar själv i Avancerat Läge.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Effektiv aerosolradie (vid RH = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(
    ["Maximal viraldeaktiveringshastighet (vid RH = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

pop_immunity_header = "Befolkningsimmunitet: "
perc_immune_label = html.Span(["Procent immune p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["Procent smittsamma p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["Procent vaccinerade p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["Procent tidigare infekterade p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["Procent mottagliga p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''Den infektiösa procentandelen p''', html.Sub('i'), ''' i populationen 
beräknas från den infektiösa prevalens som anges i flikarna för andra riskscenarier (med tanke på förekomsten av 
infektion…, För att begränsa min personliga risk ...). Procentandelen immuna p''', html.Sub('im'), ''' kan uppskattas 
konservativt från vaccinationsprocenten av befolkningen plus det totala antalet sjukdomsfall i befolkningen genom att 
försumma bidraget från oupptäckta fall. Dessa två värden används för att beräkna procentandelen mottagliga  p''',
                                        html.Sub('s'), '''. I grundläget och i det första riskläget (om en infekterad 
                                        person går in i…) antas detta värde vara 100%.''']),
                              html.Br(),
                              html.Div(['''Några informativa länkar för att bedöma p''', html.Sub('i'), ''' and p''',
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

values_interest_header = "Beräknade värden av intresse"
values_interest_desc = html.Div([
    html.H5("Vad exakt beräknar appen?"),
    html.Div([
        html.Div([html.Span('''Appen beräknar den maximala tillåtna kumulativa exponeringstiden, produkten av antalet 
        personer och tid, i ett inomhusutrymme. Spridningen av COVID-19 begränsas genom att det förväntade antalet 
        överföringar per infekterad individ, "inomhusreproduktivt nummer", är mindre än den valda risktoleransen. 
        Appen beräknar också relaterade kvantiteter, definierade i '''),
                  html.A(children="papperet",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', som kan vara av intresse:''')]),
    ], className='faq-answer'),
])
relative_sus_label = html.Span(["Relativ mottaglighet s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["Luftfraktion utomhus Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Aerosolfiltreringseffektivitet p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Andningsflöde Q", html.Sub('b'), ": "])
cq_label = html.Span(["Smittsamhet hos utandad luft C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Sannolikhet för passage genom mask p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Utrymmesvolym V: "])
vent_rate_Label = html.Span(["Ventilationsflödeshastighet(utomhus) Q: "])
recirc_rate_label = html.Span(["Retursflödeshastighet(recirkulation) Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Luftfiltreringshastighet (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Luftfuktighetsjusterad aerosolradie r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Luftfuktighetsjusterad viral deaktiveringshastighet \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Effektiv aerosoldepositionsshastighet v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Koncentrationsreduktionsshastighet \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Luftburen överföringshastighet \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Tar denna modell hänsyn till infektionsprevalens i lokalbefolkningen?"),
    html.Div(['''Påverkan av förekomsten av infektion i den lokala befolkningen kan övervägas i avancerat läge. På 
    fliken “Övriga parametrar” kan man också bedöma påverkan av immunitet i befolkningen, vilket kan uppstå genom 
    vaccinering eller tidigare infektion.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("Fler frågor?"),
    html.Div([html.Span('''För mer detaljerade förklaringar och referenser, se "'''),
              html.A(children="Beyond 6 Feet",
                     href=link_paper,
                     target='_blank'),
              html.Span('''" och andra länkar som läggs upp högst upp på webbsidan.''')]),
])

footer = html.Div([
    html.Div([html.Span('''COVID-19 Säkerhetsrekommendationer Inomhus är ett verktyg under utveckling som syftar till 
    att göra den intresserade användaren bekant med de faktorer som påverkar risken för luftburen överföring av 
    COVID-19 i inomhusmiljöer och för att hjälpa till med den kvantitativa riskbedömningen i dessa miljöer. Vi 
    noterar att osäkerhet och inneboende variation i modellparametrarna kan leda till fel så stora som en 
    storleksordning, vilket kan kompenseras genom att välja en tillräckligt låg risktolerans. Våra rekommendationer 
    tar inte hänsyn till kortdistansöverföring genom utandningsstrålar, vilket väsentligt kan höja risken när 
    ansiktsmasker inte bärs, på ett sätt som diskuteras i '''),
              html.A(children="medföljande manuskript",
                     href=link_paper,
                     target='_blank'),
              html.Span('''(Bazant & Bush, 2020). Användning av COVID-19 Säkerhetsrekommendationer Inomhus  är 
              användarens eget ansvar. Verktyget görs tillgängligt utan garanti av något slag. Författarna tar inget 
              ansvar för dess användning.''')]),
    html.Br(),
    html.Div("Särskilt tack till: ")
], className='footer-small-text')
