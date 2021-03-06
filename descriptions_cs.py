import dash_html_components as html

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

Czech

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

# Header
header = html.Div([
    html.H1(children='Bezpečnostní doporučení ke COVID-19 ve vnitřních prostorách'),
    html.Div([
        html.Div([html.Span(html.A(href="https://www.linkedin.com/in/kasim-k-a92620b1/",
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href="https://math.mit.edu/~bush/",
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ", a ",
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
language_dd = "Jazyk: "

# Unit systems
units_dd = " Jednotky: "
unit_settings = [
    {'label': "Imperiální", 'value': "british"},
    {'label': "SI (metrické)", 'value': "metric"},
]

# Modes
mode_dd = "Režim: "
app_modes = [
    {'label': "Základní", 'value': "basic"},
    {'label': "Rozšířený", 'value': "advanced"},
]

error_list = {
    "floor_area": "Chyba: Prázdné pole pro obsah podlahy.",
    "ceiling_height": "Chyba: Prázdné pole pro výšku stropu.",
    "recirc_rate": "Chyba: Prázdné pole pro rychlost recirkulace.",
    "aerosol_radius": "Chyba: Prázdné pole pro poloměr částice aerosolu.",
    "viral_deact_rate": "Chyba: Prázdné pole pro rychlost deaktivace viru.",
    "n_max_input": "Chyba: Počet osob nemůže být menší než 2.",
    "exp_time_input": "Chyba: Doba vystavení musí být větší než 0.",
    "air_exchange_rate": "Chyba: Rychlost ventilace (ACH) musí být vyšší než 0.",
    "merv": "Chyba: Prázdné pole pro třídu filtračního systému (MERV).",
    "prevalence": "Chyba: Prevalence (počet nakažených na 100 000 lidí) musí být větší než 0 a menší než 100 000."
}

# Main Panel Text
curr_room_header = "Volba místnosti: "
presets = [
    {'label': "Vlastní", 'value': 'custom'},
    {'label': "Rodinný dům", 'value': 'house'},
    {'label': "Restaurace", 'value': 'restaurant'},
    {'label': "Tichá kancelář", 'value': 'office'},
    {'label': "Školní třída", 'value': 'classroom'},
    {'label': "Vůz metra v New Yorku", 'value': 'subway'},
    {'label': "Boeing 737", 'value': 'airplane'},
    {'label': "Kostel", 'value': 'church'},
]

main_panel_s1 = "Na základě modelu by mělo být pro tuto místnost bezpečné*: "

units_hr = 'hodin'
units_min = 'minut'
units_days = 'dní'

units_hr_one = 'hodin'
units_min_one = 'minut'
units_day_one = 'dní'

is_past_recovery_base_string = '{n_val} lidé po dobu >{val:.0f} dní,'
model_output_base_string = '{n_val} lidí po dobu '

main_panel_six_ft_1 = "Poznámka: Samotné doporučení dodržovat dvoumetrové rozestupy by říkalo, že by v této místnosti " \
                      "bylo v bezpečí až "
main_panel_six_ft_2 = " po neomezenou dobu."

six_ft_base_string = ' {} osob'
six_ft_base_string_one = ' {} osob'

graph_title = "Závislost počtu osob na době vystavení"
graph_xtitle = "Maximální doba vystavení \u03C4 (hod)"
graph_ytitle = "Maximální počet osob N"
transient_text = "Přechodný stav"
steady_state_text = "Ustálený stav"

main_airb_trans_only_disc = html.Div(["*",
                                      html.Span(html.A(href='https://www.nature.com/articles/d41586-020-02058-1',
                                                       children="Doporučení jsou založena na předpokladu, že se "
                                                                "infekce šíří vzduchem od jedné nakažené osoby "
                                                                "kumulativně po specifikovanou dobu vystavení.",
                                                       target='_blank'), ),
                                      html.Span('''''')], className='airborne-text')

airb_trans_only_disc = html.Div('''Doporučení jsou založena na předpokladu, že se infekce šíří vzduchem od jedné 
nakažené osoby kumulativně po specifikovanou dobu vystavení.''', className='airborne-text')

# Bottom panels text
n_input_text_1 = "Pokud je v této místnosti "
n_max_base_string = ' {:.0f} osob'
n_input_text_2 = " osob, měly by být v bezpečí po dobu "
n_input_text_3 = "."

t_input_text_1 = "Pokud zde lidé stráví přibližně "
t_input_text_2 = " hodin, neměl by jejich počet překročit "
t_input_text_3 = "."

# About
about_header = "O aplikaci"
about = html.Div([
    html.H6("O aplikaci", style={'margin': '0'}),
    html.Div('''Oficiální doporučení pro ochranu veřejného zdraví stanovují pro zamezení přenosu nemoci COVID-19 
    následující omezení: Vzdálenost mezi lidmi (6 stop, tj. 2 metry), doba přítomnosti v místnosti (15 minut), 
    maximální počet osob (25 lidí) nebo minimální úroveň ventilace (6 ACH, tj. 6 obměn vzduchu za hodinu). '''),
    html.Br(),
    html.Div([html.Span(''''''),
              # html.A(children="scientific evidence",
              #        href=link_docs,
              #        target='_blank'),
              html.Span('''Přibývá vědeckých důkazů svědčících o vzdušném přenosu nemoci COVID-19 pomocí infekčních 
              kapének aerosolu šířících se dýcháním ve sdílených vnitřních prostorách. Ačkoliv organizace zabývající 
              se ochranou veřejného zdraví už začínají uznávat důležitost přenosu vzduchem, nevydaly ještě 
              bezpečnostní doporučení zahrnující všechny relevantní proměnné. ''')]),
    html.Br(),
    html.Div([html.Span('''Tato aplikace, kterou vyvinul Kasim Khan ve spolupráci s Martinem. Z. Bazantem a Johnem W. 
    M. Bushem, využívá teoretický model pro výpočet bezpečných dob vystavení a počtu osob ve vnitřních prostorách. 
    Volbou specifikací místnosti, ventilace, úrovně filtrace, míry použití roušek, úrovně aktivit spojených s 
    dýcháním a tolerance rizika (v ostatních záložkách) uvidíte, jak omezit přenos nemoci COVID-19 v různých typech 
    vnitřních prostor.'''),
              # html.A(children="theoretical model",
              #        href=link_paper,
              #        target='_blank'),
              html.Span('''''')]),
])

# Room Specifications
room_header = "Specifikace místnosti"

floor_area_text = "Celková plocha (sq. ft.): "
floor_area_text_metric = "Celková plocha (m²): "
ceiling_height_text = "Průměrná výška stropu (ft.): "
ceiling_height_text_metric = "Průměrná výška stropu (m): "

ventilation_text = "Systém ventilace: "
vent_type_output_base = "{:.0f} ACH (obměny vzduchu za hodinu)"
ventilation_text_adv = "Ventilation System (ACH, obměny vzduchu za hodinu): "
ventilation_types = [
    {'label': "Zavřená okna", 'value': 0.3},
    {'label': "Otevřená okna", 'value': 2},
    {'label': "Mechanická ventilace", 'value': 3},
    {'label': "Otevřená okna s větráky", 'value': 6},
    {'label': "Lepší mechanická ventilace", 'value': 8},
    {'label': "Laboratoř, Restaurace", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Nemocnice, Vůz metra", 'value': 18},
    {'label': "Laboratoř pro práci s toxickými látkami / Letadlo", 'value': 24},
]

filtration_text = "Systém filtrace: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Systém filtrace (MERV): "
filter_types = [
    {'label': "Žádný", 'value': 0},
    {'label': "Běžná rezidenční klimatizace (v okně)", 'value': 2},
    {'label': "Rezidenční/Komerční/Průmyslový", 'value': 6},
    {'label': "Rezidenční/Komerční/Nemocniční", 'value': 10},
    {'label': "Nemocnice & Chirurgie", 'value': 14},
    {'label': "HEPA filtr", 'value': 17}
]

recirc_text = "Rychlost recirkulace: "
recirc_type_output_base = "{:.1f} ACH (obměn vzduchu za hodinu) Žádná"
recirc_text_adv = "Recirculation Rate (ACH (obměn vzduchu za hodinu) Žádná): "
recirc_types = [
    {'label': "Žádný", 'value': 0},
    {'label': "Pomalá", 'value': 0.3},
    {'label': "Střední", 'value': 1},
    {'label': "Rychlá", 'value': 10},
    {'label': "Letadlo", 'value': 24},
    {'label': "Vůz metra", 'value': 54},
]

humidity_text = "Relativní vlhkost: "
humidity_marks = {
    0: {'label': '0%: Velmi sucho', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: Letadlo', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Sucho'},
    0.6: {'label': '60%: Normální vlhkost'},
    0.99: {'label': '99%: Velmi vlhko'},
}

need_more_ctrl_text = '''Potřebujete ještě detailnější nastavení? Přepněte do Rozšířeného režimu pomocí rozbalovacího 
menu v horní části stránky. '''

human_header = "Chování lidí v místnosti"
# Human Behavior
exertion_text = "Úroveň zátěže: "
exertion_types = [
    {'label': "Klid", 'value': 0.49},
    {'label': "Stání", 'value': 0.54},
    {'label': "Lehké cvičení", 'value': 1.38},
    {'label': "Středně náročné cvičení", 'value': 2.35},
    {'label': "Náročné cvičení", 'value': 3.30},
]

breathing_text = "Dechová aktivita: "
expiratory_types = [
    {'label': "Dýchání (mělké)", 'value': 1.1},
    {'label': "Dýchání (normální)", 'value': 4.2},
    {'label': "Dýchání (intenzivní)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Mluvení (šeptání)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Mluvení (normální)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Mluvení (hlasité)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Zpěv", 'value': 970},
]

mask_type_text = "Účinnost roušky (typ ochrany): "
mask_type_marks = {
    0: {'label': "0% (žádné, obličejový štít)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (rouška s hrubé bavlny)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (hedvábí, flanel, šifon)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (chirurgická rouška, jemná bavlna)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (respirátor KN95)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Žádné, obličejový štít", 'value': 0},
    {'label': "Rouška z hrubé bavlny", 'value': 0.1},
    {'label': "Rouška z hedvábí, flanelu nebo šifonu", 'value': 0.5},
    {'label': "Chirurgická rouška nebo rouška z jemné bavlny", 'value': 0.9},
    {'label': "Respirátor KN95", 'value': 0.95},
]

mask_fit_text = "Přiléhavost roušek/Podíl osob s rouškou: "
mask_fit_marks = {
    0: {'label': '0%: Žádná', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Špatná'},
    0.95: {'label': '95%: Dobrá'}
}

risk_tolerance_text = "Tolerance rizika: "
risk_tol_desc = html.Div('''Ohroženější osoby, například lidé starší nebo s dalšími zdravotními komplikacemi, 
potřebují nižší toleranci rizika. Naopak vyšší tolerance vede k vyšší možnosti přenosu nemoci během dané doby 
vystavení (více detailů ve FAQ). ''', style={'font-size': '13px', 'margin-left': '20px'})
risk_tol_marks = {
    0.01: {'label': '0.01: Bezpeč-nější', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Bezpečné', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Nebezpečné'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Často kladené dotazy (FAQ)"
other_io = "Ostatní vstupy a výstupy"

faq_top = html.Div([
    html.H6("Často kladené dotazy (FAQ)"),
    html.H5("Proč nejsou dvoumetrové (6 stop) rozestupy dostatečné?"),
    html.Div([
        html.Div([html.Span('''Dvoumetrové (6 stop) rozestupy (a stejně tak roušky) chrání před většími kapénkami, 
        které se šíří od infikované osoby kýcháním či kašláním. Rozestupy však nechrání před '''),
                  html.A(children="vzdušným přenosem",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' pomocí infekčního aerosolu, který se pohybuje ve vzduchu po celé místností. Ve 
                  vnitřních prostorách jsou však lidé ve stejném nebezpečí při dvacetimetrových (60 stop) jako při 
                  dvoumetrových (6 stop) rozestupech.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Existují další způsoby přenosu?"),
    html.Div([
        html.Div([html.A(children="",
                         href=link_docs,
                         target='_blank'),
                  html.Span('''Za dominantní způsob přenosu nemoci COVID-19 je považován přenos vzduchem, 
                  ale existují i další způsoby, například přenos přímým kontaktem s infikovaným povrchem, 
                  přenos velkými kapénkami při kašlání a kýchání nebo krátkodosahovým aerosolem z vydechovaného 
                  proudu vzduchu při delší době kontaktu. Přestože poslední dva zmíněné způsoby přenosu mohou hrát 
                  důležitou roli, dají se do velké míry eliminovat nošením roušek nebo obličejových štítů. Riziko 
                  vzdušného přenosu aerosolem však zůstává.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Je předpoklad dobrého promíchání vzduchu v místnosti opodstatněný?"),
    html.Div([
        html.Div([html.Span('''K promíchávání vzduchu ve vnitřních prostorách přispívá řada faktorů jako třeba 
        proudění způsobené vztlakem (od topení, klimatizací nebo oken), konvekce vyvolaná větráky a ventilací nebo 
        pohyb lidí a jejich dýchání. Přestože existují výjimky, jak je diskutováno v přiloženém '''),
                  html.A(children="článku",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', předpoklad dobrého promíchání vzduchu v místnosti je široce používán při teoretickém 
                  modelování přenosu chorob vzduchem.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Platí tato doporučení i pro velmi rozlehlé prostory?"),
    html.Div([
        html.Div([html.Span('''Na stadionech, v koncertních sálech nebo jiných velkých odvětrávaných místnostech s 
        velkým počtem osob hraje riziko vzdušného přenosu nemoci důležitou roli a je náležitě zachyceno v těchto 
        doporučení. Pokud navíc osoby v místnosti nemají nasazené roušky nebo obličejové štíty, vyvstává další riziko 
        přenosu na krátkou vzdálenost skrze vydechovaný proud vzduchu, viz odhad v přiloženém '''),
                  html.A(children="článku",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Proč hraje roli výška stropu?"),
    html.Div([
        '''Výška stropu ovlivňuje celkový objem místnosti, který se použije pro odhad koncentrace infekčního aerosolu 
        (počet částic na jednotku objemu). Výsledná koncentrace se pak používá pro odhad rizika přenosu nemoci 
        COVID-19. '''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Znám svá čísla ACH/MERV. Kam je mám zadat?"),
    html.Div('''Potřebujete-li více kontroly nad vstupními parametry, například nad počtem obměn vzduchu za hodinu (
    ACH) nebo třídou filtrace (MERV), přepněte aplikaci do Rozšířeného režimu pomocí rozbalovacího menu v horní části 
    stránky.''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Jsou v Základním režimu nějaké skryté parametry?"),
    html.Div([html.Span('''Všechny relevantní fyzikální parametry jsou detailně diskutovány v přiloženém '''),
              html.A(children="článku",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. Aplikace v Základním režimu předpokládá poloměr částice aerosolu 2 μm (při vlhkosti 60%) 
              a maximální rychlost deaktivace viru 0.6/h (při cca 100%-ní vlhkostí), přičemž obě hodnoty se zvyšují s 
              rostoucí relativní vlhkosti (φ). Odhad rychlosti deaktivace viru je spíše konzervativní (tedy spíše 
              nižší rychlost) a tato hodnota může být zvýšena pomocí ultrafialového záření (UV C) nebo pomocí 
              chemických dezinfekcí (např. peroxid vodíku nebo ozón). Aplikace také odhaduje ze zadané intenzity 
              dýchání (pomocí hodnot tabelovaných v obr. 2 článku) klíčový parametr, kterým je infekčnost 
              vydechovaného vzduchu C'''),
              html.Sub("q"),
              html.Span(''' (množství infekčních dávek, kvant, na jednotku objemu),. Tyto parametry se dají nastavit v 
              Rozšířeném režimu.'''),
              # html.A(children="paper",
              #        href=link_paper,
              #        target='_blank'),
              html.Span('''''')],
             className='faq-answer'),
])

aerosol_radius_text = "Efektivní poloměr částice aerosolu (při vlhkosti 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Maximální rychlost deaktivace viru (při vlhkosti 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

values_interest_header = ""
values_interest_desc = html.Div([
    html.H5("Co přesně aplikace počítá?"),
    html.Div([
        html.Div([html.Span('''Pro zadanou toleranci rizika přenosu infekce vzduchem počítá aplikace maximální 
        kumulativní dobu vystavení, tedy součin počtu osob v místnosti a doby, po kterou jsou v přítomnosti 
        infikované osoby. Kromě toho aplikace také vypočítá další příbuzné veličiny definované v '''),
                  html.A(children="článku",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', které mohou být zajímavé.''')]),
    ], className='faq-answer'),
])
outdoor_air_frac_label = html.Span(["Podíl venkovního vzduchu Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Účinnost filtrace aerosolu p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Průtok vzduchu při dýchání Q", html.Sub('b'), ": "])
cq_label = html.Span(["Infekčnost vydechovaného vzduchu C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Pravděpodobnost průchodu rouškou p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Objem místnosti V: "])
vent_rate_Label = html.Span(["Průtok ventilací (venkovní) Q: "])
recirc_rate_label = html.Span(["Zpětný průtok vzduchu (recirkulace) Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Úroveň filtrace vzduchu (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Poloměr aerosolu upravený podle vlhkosti r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Rychlost deaktivace viru upravená podle vlhkosti \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Efektivní rychlost usazování aerosolu  v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Rychlost relaxace koncentrace \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Rychlost vzdušného přenosu \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Zohledňuje model množství nakažených v místní populaci (prevalenci)?"),
    html.Div(['''Ne. Tento model počítá nebezpečí přenosu od jedné infikované osoby a předpokládá tedy, že množství 
    nakažených osob v populaci je relativně malé. Riziko přenosu infekce za tohoto předpokladu roste se zvyšujícím se 
    počtem nakažených osob v místnosti, konkrétně se součinem počtu osob v místnosti a prevalence v populaci. 
    Tolerance rizika by měla být snížena úměrně tomu, jak počet nakažených osob v místnosti převyšuje číslo jedna. Na 
    druhou stranu může být tolerance  zvýšena úměrně tomu, jak v místnosti klesá počet nakažených osob k nule, 
    až do bodu, kdy doporučená omezení přestávají být relevantními.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("Další otázky?"),
    html.Div([html.Span('''Další detaily a zdroje jsou k nalezení v '''),
              html.A(children="Beyond 6 Feet",
                     href=link_paper,
                     target='_blank'),
              html.Span('''" a na odkazech v horní části této stránky.''')]),
])

footer = html.Div([
    html.Div([html.Span('''Bezpečnostní doporučení ke COVID-19 ve vnitřních prostorách je stále se vyvíjejícím 
    nástrojem za účelem seznámení uživatele s faktory ovlivňujícími riziko vzdušného přenosu nemoci COVID-19 ve 
    vnitřních prostorách a za účelem usnadnění kvalifikovaného odhadu rizika v různých situacích. Nejistota a vnitřní 
    variabilita parametrů modelu může vést k chybám o velikosti až jednoho řádu, jež mohou být kompenzovány volbou 
    dostatečně nízké tolerance rizika. Naše doporučení nezahrnují krátkodosahové přenosy pomocí proudu vydechovaného 
    vzduchu, které mohou výrazně zvýšit nebezpečí přenosu při nenošení roušek, viz. diskuze v přiloženém '''),
              html.A(children="článku",
                     href=link_paper,
                     target='_blank'),
              html.Span('''(Bazant & Bush, 2020). Používání této aplikace a doporučení z ní vyplývajících je výlučně 
              na zodpovědnosti uživatele. Doporučení jsou zpřístupněna bez záruky jakéhokoliv druhu. Autoři nenesou 
              žádnou právní odpovědnost za používání této aplikace ani doporučení z ní plynoucích.''')]),
    html.Br(),
    html.Div("Zvláštní poděkování si zasluhují: ")
], className='footer-small-text')
