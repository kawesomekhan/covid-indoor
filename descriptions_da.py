import dash_html_components as html

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

Danish

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

# Header
header = html.Div([
    html.H1(children='COVID-19 indendørs sikkerhedsretninglinjer'),
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
language_dd = "Sprog: "

# Unit systems
units_dd = "Enheder: "
unit_settings = [
    {'label': "Britiske", 'value': "british"},
    {'label': "SI", 'value': "metric"},
]

# Modes
mode_dd = "Tilstand: "
app_modes = [
    {'label': "Basal", 'value': "basic"},
    {'label': "Avanceret", 'value': "advanced"},
]

error_list = {
    "floor_area": "Fejl: Gulvarealet kan ikke være tomt.",
    "ceiling_height": "Fejl: Gulvarealet kan ikke være tomt.",
    "recirc_rate": "Fejl: Recirkulationsraten kan ikke være tom.",
    "aerosol_radius": "Fejl: Aerosolradius kan ikke være tom.",
    "viral_deact_rate": "Fejl: Viral deaktiveringsrate kan ikke være tom.",
    "n_max_input": "Fejl: Antal personer kan ikke være mindre end 2.",
    "exp_time_input": "Fejl: Eksponeringstid skal være større end 0.",
    "air_exchange_rate": "Fejl: Ventilationsrate (ACH) skal være større end 0.",
    "merv": "Fejl: Ventilationsrate (ACH) skal være større end 0."
}

# Main Panel Text
curr_room_header = "Det aktuelle lokale: "
presets = [
    {'label': "Brugerdefineret", 'value': 'custom'},
    {'label': "Forstadsvilla", 'value': 'house'},
    {'label': "Restaurant", 'value': 'restaurant'},
    {'label': "Stille kontor", 'value': 'office'},
    {'label': "Klasseværelsesundervisning", 'value': 'classroom'},
    {'label': "New York City Subway vogn", 'value': 'subway'},
    {'label': "Boeing 737", 'value': 'airplane'},
    {'label': "Kirke", 'value': 'church'},
]

main_panel_s1 = "Baseret på denne model, skulle det være sikkert* i dette lokale at have: "

units_hr = 'timer'
units_min = 'minutter'
units_days = 'dage'

units_hr_one = 'timer'
units_min_one = 'minutter'
units_day_one = 'dage'

is_past_recovery_base_string = '{n_val} personer i >{val:.0f} dage,'
model_output_base_string = '{n_val} personer i '

main_panel_six_ft_1 = "Bemærk, at anbefalingen om to-meters (seks-fods) afstand svarer til at op til "
main_panel_six_ft_2 = " ville være sikre i dette lokale i uendelig lang tid."

six_ft_base_string = ' {} personer'
six_ft_base_string_one = ' {} personer'

graph_title = "Antal personer vs. eksponeringstid"
graph_xtitle = "Maksimal  eksponeringstid \u03C4 (timer)"
graph_ytitle = "Maksimalt antal personer N"
transient_text = "Transient tilstand"
steady_state_text = "Stationær tilstand"

main_airb_trans_only_disc = html.Div(["*•	Retningslinjen er baseret på betragtninger omkring ",
                                      html.Span(html.A(href='https://www.nature.com/articles/d41586-020-02058-1',
                                                       children="luftbåren smitte",
                                                       target='_blank'), ),
                                      html.Span(''' fra en enkelt smittet person over den angivne akkumulerede 
                                      eksponeringstid.''')], className='airborne-text')

airb_trans_only_disc = html.Div('''•	Retningslinjen er baseret på betragtninger omkring luftbåren smitte fra en 
enkelt smittet person over den angivne akkumulerede eksponeringstid.''', className='airborne-text')

# Bottom panels text
n_input_text_1 = "Hvis der er "
n_max_base_string = ' {:.0f} personer'
n_input_text_2 = " personer i dette lokale, skulle de være sikre i "
n_input_text_3 = "."

t_input_text_1 = "personer i dette lokale, skulle de være sikre i "
t_input_text_2 = " timer her, skulle der højst være "
t_input_text_3 = "."

# About
about_header = "Baggrund"
about = html.Div([
    html.H6("Baggrund", style={'margin': '0'}),
    html.Div('''For at mindske spredningen af COVID-19, har de officielle offentlige sundhedsretningslinjer anbefalet 
    begrænsninger på: person-til-person afstand (2 meter / 6 fod), opholdstid (15 minutter), maksimalt antal personer 
    (25), eller minimal ventilation (6 luftudskiftninger pr. time).'''),
    html.Br(),
    html.Div([html.Span('''Der er voksende '''),
              html.A(children="videnskablig evidens",
                     href=link_docs,
                     target='_blank'),
              html.Span(''' for luftbåren smitte af COVID-19, som finder sted når inficerede aerosoldråber udveksles 
              gennem indånding af indendørsluft. Selvom offentlige sundhedsorganitioner er begyndt at anerkende 
              luftbåren smitte, er der endnu ikke givet sikkerhedsretningslinjer, der omfatter alle relevante 
              variable.''')]),
    html.Br(),
    html.Div([html.Span('''Denne app, udviklet af Kasim Khan i samarbejde med Martin Z. Bazant og John W. M. Bush, 
    benytter en '''),
              html.A(children="teoretisk model",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' til at beregne sikre niveauer for eksponeringstider og antal personer i indendørs lokaler. 
               Ved at justere specifikationerne for lokalet, dets ventilations- og filtreringsrater, 
               brugen af mundbind, respirationsaktiviteter og risikotolerancer, kan man se hvorledes man kan begrænse 
               smittespredningen indendørs af COVID-19 i givne lokaler. ''')]),
])

# Room Specifications
room_header = "Specifikationer af lokalet"

floor_area_text = "Samlet gulvareal (sq. ft.): "
floor_area_text_metric = "Samlet gulvareal (m²): "
ceiling_height_text = "Gennemsnitlig loftshøjde (ft.): "
ceiling_height_text_metric = "Gennemsnitlig loftshøjde (m): "

ventilation_text = "Ventilationsystem: "
vent_type_output_base = "{:.0f} ACH"
ventilation_text_adv = "Ventilationsystem (ACH): "
ventilation_types = [
    {'label': "Lukkede vinduer", 'value': 0.3},
    {'label': "Åbne vinduer", 'value': 2},
    {'label': "Mekanisk ventilation", 'value': 3},
    {'label': "Åbne vinduer med ventilator", 'value': 6},
    {'label': "Bedre mekanisk ventilation", 'value': 8},
    {'label': "Laboratorium, restaurant", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Hospital/ subway vogn", 'value': 18},
    {'label': "Toksisk laboratorium/flyvemaskine", 'value': 24},
]

filtration_text = "Filtreringssystem: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Filtration System (MERV): "
filter_types = [
    {'label': "Ingen", 'value': 0},
    {'label': "Almindelig aircondition ved vinduer", 'value': 2},
    {'label': "Beboelse/kommercielt/indusrielt", 'value': 6},
    {'label': "Beboelse/kommercielt/hospital", 'value': 10},
    {'label': "Hospital & operationsstue", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_text = "Recirkulationsrate: "
recirc_type_output_base = "{:.1f} recirkulation ACH"
recirc_text_adv = "Recirkulationsrate (recirkulation ACH): "
recirc_types = [
    {'label': "Ingen", 'value': 0},
    {'label': "Langsom", 'value': 0.3},
    {'label': "Moderat", 'value': 1},
    {'label': "Hurtig", 'value': 10},
    {'label': "Flyvemaskine", 'value': 24},
    {'label': "Subway vogn", 'value': 54},
]

humidity_text = "Relative fugtighed: "
humidity_marks = {
    0: {'label': '0%: Meget tør', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: Flyvemaksine', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Tør'},
    0.6: {'label': '60%: Gennemsnitlig'},
    0.99: {'label': '99%: Meget fugtig'},
}

need_more_ctrl_text = '''Ønskes øget kontrol over input? Skift til ”Avanceret tilstand” ved at bruge dropdown-menuen 
øverst på siden.'''

human_header = "Menneskelig opførsel"
# Human Behavior
exertion_text = "Bevægelsesniveau: "
exertion_types = [
    {'label': "Hvile", 'value': 0.49},
    {'label': "Stående", 'value': 0.54},
    {'label': "Let arbejde", 'value': 1.38},
    {'label': "Moderate arbejde", 'value': 2.35},
    {'label': "Kraftigt arbejde", 'value': 3.30},
]

breathing_text = "Åndedrætsaktivitet: "
expiratory_types = [
    {'label': "Åndedræt (let)", 'value': 1.1},
    {'label': "Åndedræt (normalt)", 'value': 4.2},
    {'label': "Åndedræt (kraftigt)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Tale (hvisken)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Tale (normal)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Tale (højt)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Sang", 'value': 970},
]

mask_type_text = "Effektivitet af maskefiltrering (masketype): "
mask_type_marks = {
    0: {'label': "0% (ingen, ansigtsvisir)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (groft bomuld)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (silke, flannel, chiffon)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (medicinsk mundbind)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (N95 respirator)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Ingen, ansigtsvisir", 'value': 0},
    {'label': "Groft bomuld", 'value': 0.1},
    {'label': "Silke, flannel, chiffon", 'value': 0.5},
    {'label': "Medicinsk mundbind", 'value': 0.9},
    {'label': "N95 Respirator", 'value': 0.95},
]

mask_fit_text = "Maskefit/-tilpasning: "
mask_fit_marks = {
    0: {'label': '0%: Ingen', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Dårlig'},
    0.95: {'label': '95%: God'}
}

risk_tolerance_text = "Risikotolerance: "
risk_tol_desc = html.Div('''Mere udsatte befolkningsgrupper så som ældre, overvægtige eller folk med visse kroniske 
sygdomme har brug for en lavere risikotolerance. En højre risikotolerance betyder en øget forventet smittet i løbet 
af den forventede opholdsperiode (se flere detaljer under FAQ). ''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})
risk_tol_marks = {
    0.01: {'label': '0.01: Mere sikker', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Sikker', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Usikker'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Ofte stillede spørgsmål (FAQ)"
other_io = "Andre input & output"

faq_top = html.Div([
    html.H6("Ofte stillede spørgsmål (FAQ)"),
    html.H5("Hvofor er 2 meters (6 fods) afstand ikke nok?"),
    html.Div([
        html.Div([html.Span('''En afstand på 2 meter (6 fod) beskytter dig mod store dråber udsendt fra en smittet 
        person, som hoster. Det samme gælder ansigtsvisirer. Derimod beskytter afstanding ikke imod '''),
                  html.A(children="luftbåren smitte",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' via inficerede aerosoler i luften, som kan sprede sig overalt i lokalet.. Indendørs er 
                  personer ikke mere sikker imod luftbåren smitte ved en afstand på 20 m som på 2 m.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Findes der andre smitteveje?"),
    html.Div([
        html.Div([html.A(children="Luftbåren smitte",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' menes at være dominerende for  COVID-19, men andre smittevej er mulige, så som direkte 
                  eller indirekte kontaktsmitte via inficerede mellemled (så som overflader),  og dråbesmitte via 
                  hoste, nysen, og sprøjt fra en inficeret person. Mens disse smitteveje kan være betydningsfulde, 
                  så elimineres de stort set helt ved brug af mundbind eller ansigtsvisirer. mens luftbåren smitte 
                  består.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Kan vi virkelig antage at luften i et lokale er godt opblandet?"),
    html.Div([
        html.Div([html.Span('''Der er mange bidrag til opblanding af luft i indendørs lokale, så som opdrift-drevne 
        strømninger (fra varmeapparater, airconditionanlæg, eller vinduer), tvungen konvektion fra ventilatorer, 
        and personers bevægelse og respiration. Skønt der er undtagelser, som diskuteret i '''),
                  html.A(children="artiklen",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', så er antagelsen om godt opblandent luft almindelig brugt i teoretisk modeling af 
                  luftbåren smitte af sygdomme. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Holder retningslinjerne for meget store lokaler?"),
    html.Div([
        html.Div([html.Span('''I koncertsale, stadioner eller andre store ventilerede lokaler med et meget stort 
        antal mennesker,  er risikoen for luftbåren smitte meget stor og dårligt beskrevet af retningslinjerne. Men 
        hvis mundbind eller ansigtsvisirer ikke benyttes, så er der en ekstra risiko for dråbesmitte fra 
        udåndingsluft,  som beskrevet i '''),
                  html.A(children="artiklen",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Hvorfor spille loftshøjden en rolle?"),
    html.Div([
        '''Loftshøjden påvirker det samlede volumen af lokalet, og det ingår i bestemmelsen af koncentrationen af de 
        inficerede aerosoler (antal aerosoler pr. volumen). Denne koncentration indgår i beregningen af lokalets 
        COVID-19 smitterisiko. '''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Jeg kender mine ACH/MERV værdier. Hvor kan jeg indtaste dem?"),
    html.Div('''
        Hvis du øsnker øget kontrol over inputværdier, så skift til ”Avanceret tilstand” ved brug af dropdown-menuen 
        øverst på siden.
    ''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Er der skjulte parameterværdier i ”Basal tilstand”?"),
    html.Div([html.Span('''Alle relevante fysiske parameter er beskrevet i '''),
              html.A(children="artiklen",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. I “Basal tilstand” antager app’en en standard aerosol radius på 2 μm (ved 60% 
              luftfugtighed) og en maksimal viral deaktiveringsrate på 0.6 /hr (ved ~100% luftfugtighed), 
              og begge disse værdier øges med den relative luftfugtighed (RH). Estimater af den virale 
              deaktiveringsrate fejler på den konservative side af langesommere deaktivering.  Den virale 
              deaktiveringsrate rate kan øges ved ultraviolet stråling (UV-C) eller kemiske desinfektionsmidler (så 
              som hydrogen peroxid eller ozon). App’en anvender også estimater for centrale sygdomsparametre som 
              smitsomhed af udåndet luftr, C'''),
              html.Sub("q"),
              html.Span(''' (infektionsenheder pr. volumen) fra den angivne respirationsaktivitet, ved brug af de 
              tabellagte værdier i Figur 2 i '''),
              html.A(children="artiklen",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. I ”Avenceret tilstand” kan du selv definere disse parametre.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Effektiv aerosol radius (ved RH = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Maximal viral deaktiveringsrate (ved RH = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

values_interest_header = ""
values_interest_desc = html.Div([
    html.H5("Hvad beregner app’en helt præcist?"),
    html.Div([
        html.Div([html.Span('''For en given risikotolerance for luftbåren smitte, beregner app’en den maksimalt 
        tilladte akkumulerede eksponeringstid, produktet af antal personer og tilstedeværelsestid i selskab med en 
        smittet person. App’en beregner også relaterede størrelser, defineret i '''),
                  html.A(children="artiklen",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', som kan være af interesse:''')]),
    ], className='faq-answer'),
])
outdoor_air_frac_label = html.Span(["Brøkdel af udendørs luft Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Effektiviteten af aerosol filtreringen p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Udåndinsstrømningsraten Q", html.Sub('b'), ": "])
cq_label = html.Span(["Infektiøsitet af udåndingsluft C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Maskepassage sandsynlighed p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Lokalevolume V: "])
vent_rate_Label = html.Span(["Ventilationsstrømningsrate (udendørs) Q: "])
recirc_rate_label = html.Span(["Recirkulationsstrømningsrate Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Luftfiltreringsrate (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Fugtighedsjusteret aerosol radius r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Fugtighedsjusteret viral deaktiveringsrate \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Effective aerosol faldhastighed v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Koncentrationsrelaksationsrate \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Luftbåren smitterate \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Tager modelen højde for forekomsten af infektion i den lokale befolkning?"),
    html.Div(['''Nej. modellen beregner risikoen for smittespredning fra en enkelt smittet person. Det antages derfor 
    implicit, at forekomsten af infektion i befolkningen er relativt lav. I denne grænse øges smittespredningen med 
    det forventede smitteforekomst i lokalet, specifikt som produktet af antal personer med den forventede brøkdel af 
    smittede i befolkningen. Tolerance bør sænkes forholdsmæssig, hvis dette tal skulle blive større end 1. Omvendt, 
    hvis det forventede antal smittede personer i lokalet nærmer sig nul, kunne tolerancen øges proportionalt indtil 
    de anbefalede restriktioner skønnes unødvendige.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("Flere spørgsmål?"),
    html.Div([html.Span('''Ønskes mere detaljerede forklaringer og referencer, så se "'''),
              html.A(children="Beyond 6 Feet",
                     href=link_paper,
                     target='_blank'),
              html.Span('''" og andre links vist øverst på websiden.''')]),
])

footer = html.Div([
    html.Div([html.Span('''”COVID-19 indendørs sikkerhedsretningslinjer” er et redskab under udvikling, som kan 
    hjælpe den interesserede bruger til at blive bekendt med de faktorer, som påvirker risikoen for indendørs 
    luftbåren smitte of COVID-19, og som kan give en kvantitativ vurdering af risikoen i forskellige situationer. Vi 
    bemærker, at  usikkerheden i, og den indre variation af, modelparametre kan føre til fejl så store som en 
    størrelsesorden, hvilket der dog kan kompenseres for ved at vælge en passende lille risikotolerance. Vores 
    retningslinjer medtager ikke dråbesmitte over korte afstande fra åndedrætssprøjt, som kunne øges risikoen 
    betragtelig, hvis der ikke benyttes mundbind, som diskuteret i det '''),
              html.A(children="medfølgende manuskript",
                     href=link_paper,
                     target='_blank'),
              html.Span('''(Bazant & Bush, 2020). Brugen af ”COVID-19 indendørs sikkerhedsretningslinjer” er helt på 
              brugerens eget ansvar, og app’en stilles til rådighed uden nogen form for garanti. Forfatterne påtager 
              sig intet ansvar for brugen af app’en.''')]),
    html.Br(),
    html.Div("En særlig tak rettes til: ")
], className='footer-small-text')
