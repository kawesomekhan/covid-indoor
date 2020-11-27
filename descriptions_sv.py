import dash_html_components as html

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
    "merv": "Fel: Filtreringssystem (MERV) kan inte vara tomt."
}

# Main Panel Text
curr_room_header = "Typ av utrymme: "
presets = [
    {'label': "Konfigurera fritt", 'value': 'custom'},
    {'label': "Villa", 'value': 'house'},
    {'label': "Restaurang", 'value': 'restaurant'},
    {'label': "Kontor", 'value': 'office'},
    {'label': "Föreläsningsal/klassrum", 'value': 'classroom'},
    {'label': "Tunnelbanevagn", 'value': 'subway'},
    {'label': "Boeing 737", 'value': 'airplane'},
    {'label': "Kyrka", 'value': 'church'},
]

main_panel_s1 = "Baserat på denna modell borde det vara säkert för detta utrymme att ha: "

units_hr = 'timmar'
units_min = 'minuter'
units_days = 'dagar'

units_hr_one = 'timmar'
units_min_one = 'minuter'
units_day_one = 'dagar'

is_past_recovery_base_string = '{n_val} personer i >{val:.0f} dagar,'
model_output_base_string = '{n_val} personer i '

main_panel_six_ft_1 = "Obs: riktlinjer för distansering på två meter (6 fot) indikerar att upp till "
main_panel_six_ft_2 = " bör vara säkra i detta utrymme under obestämd tid."

six_ft_base_string = ' {} personer'
six_ft_base_string_one = ' {} personer'

graph_title = "Beläggning vs. Exponeringstid"
graph_xtitle = "Maximal exponeringstid \u03C4 (timmar)"
graph_ytitle = "Maximal beläggning N"
transient_text = "Övergående"
steady_state_text = "Stabilt tillstånd"

main_airb_trans_only_disc = html.Div(["Rekommendationerna är baserad på övervägande av ",
                                      html.Span(html.A(href='https://www.nature.com/articles/d41586-020-02058-1',
                                                       children="luftburen överföring",
                                                       target='_blank'), ),
                                      html.Span(''' från en enda smittad person under den angivna kumulativa 
                                      exponeringstiden.''')], className='airborne-text')

airb_trans_only_disc = html.Div('''Rekommendationerna är baserad på övervägande av luftburen överföring från en enda 
smittad person under den angivna kumulativa exponeringstiden.''', className='airborne-text')

# Bottom panels text
n_input_text_1 = "Om det här utrymmet har "
n_max_base_string = ' {:.0f} personer'
n_input_text_2 = " personer, bör dessa personer vara säkra i "
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
])

# Room Specifications
room_header = "Konfiguration av utrymme"

floor_area_text = "Total golvyta (sq. ft.): "
floor_area_text_metric = "Total golvyta (m²): "
ceiling_height_text = "Genomsnittlig takhöjd (ft.): "
ceiling_height_text_metric = "Genomsnittlig takhöjd (m): "

ventilation_text = "Ventilationssystem: "
vent_type_output_base = "{:.0f} ACH"
ventilation_text_adv = "Ventilationssystem (ACH): "
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
    0: {'label': '0%: mycket låg', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: flygplan', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: låg'},
    0.6: {'label': '60%: medel'},
    0.99: {'label': '99%: hög'},
}

need_more_ctrl_text = '''Behöver du mer kontroll över dina ingångsvärden? Byt till avancerat läge med 
rullgardinsmenyn högst upp på sidan. '''

human_header = "Mänskligt beteende"
# Human Behavior
exertion_text = "Ansträngningsnivå: "
exertion_types = [
    {'label': "Vilande", 'value': 0.49},
    {'label': "Stående", 'value': 0.54},
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
    0: {'label': "0% (ingen, ansiktsskydd/visir)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (grov bomull)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (silke, flanell, chiffong)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (kirurgisk, bomull)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (N95 andningsskydd)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Ingen, Ansiktsskydd/visir", 'value': 0},
    {'label': "Grov bomull", 'value': 0.1},
    {'label': "Silke, Flanell, Chiffong", 'value': 0.5},
    {'label': "Kirurgisk, Bomull", 'value': 0.75},
    {'label': "N95-andningsskydd", 'value': 0.95},
]

mask_fit_text = "Masktillpassning enligt krav: "
mask_fit_marks = {
    0: {'label': '0%: Ingen', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Dålig'},
    0.95: {'label': '95%: Bra'}
}

risk_tolerance_text = "Risktolerans: "
risk_tol_desc = html.Div('''Mer utsatta grupper som äldre eller personer med redan existerande medicinska tillstånd 
kräver lägre risktolerans. En högre risktolerans innebär fler förväntade överföringar under den förväntade 
beläggningsperioden (se Vanliga Frågor för mer information).''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})
risk_tol_marks = {
    0.01: {'label': '0.01: Säkrare', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Säker', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Osäker'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Vanliga frågor"
other_io = "Andra indata och outputs"

faq_top = html.Div([
    html.H6("Vanliga frågor"),
    html.H5("Varför är 2 meters (6 fots) avstånd inte tillräckligt?"),
    html.Div([
        html.Div([html.Span('''Ett avstånd på 2 meter (6 fot) skyddar dig mot stora droppar som slungas ut av en 
        smittad person som hostar, liksom ansiktsmasker gör. 2 meters avstånd skyddar emellertid inte mot '''),
                  html.A(children="luftburen överföring",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' av smittsamma aerosoler som hänger kvar i luften och kan föras runt i ett utrymme. I 
                  inomhusmiljö är människor inte säkrare från luftburen smitta på 20 meters avstånd än på 2 
                  meter.''')]),
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
viral_deact_text = html.Span(["Maximal viraldeaktiveringshastighet (vid RH = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

values_interest_header = ""
values_interest_desc = html.Div([
    html.H5("Vad exakt beräknar appen?"),
    html.Div([
        html.Div([html.Span('''Givet en risktolerans för luftburen smitta beräknar appen maximal tillåten kumulativ 
        exponeringstid, produkten av utrymmessbeläggning och tid i närvaro av en smittad person. Appen beräknar också 
        relaterade kvantiteter, definierade i '''),
                  html.A(children="artikeln",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', som kan vara av intresse:''')]),
    ], className='faq-answer'),
])
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
    html.Div(['''Nej. Modellen beräknar risken för överföring från en enda smittad person. Den antar således implicit 
    att prevalensen av infektion i befolkningen är relativt låg. Alltså ökar risken för överföring med det förväntade 
    antalet infekterade personer i utrymmet, specifikt produkten av beläggningen och prevalens i befolkningen. 
    Toleransen bör sänkas i proportion till detta nummer om det överstiger ett. Omvänt, när det förväntade antalet 
    infekterade personer i utrymmet närmar sig noll, kan toleransen ökas proportionellt tills de rekommenderade 
    begränsningarna bedöms som onödvändiga.'''],
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
