from dash import html

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

Italian

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

# Header
header = html.Div([
    html.H1(children='Covid-19: Linee Guida per Tutelare Salute e Sicurezza in Ambienti Chiusi'),
    html.Div([
        html.Div([html.Span(html.A(href="https://www.linkedin.com/in/kasim-k-a92620b1/",
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href="https://math.mit.edu/~bush/",
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ", e ",
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
language_dd = "Lingua: "

# Unit systems
units_dd = "Unitá: "
unit_settings = [
    {'label': "Britanniche", 'value': "british"},
    {'label': "Metrica", 'value': "metric"},
]

# Modes
mode_dd = "Modalitá: "
app_modes = [
    {'label': "Base", 'value': "basic"},
    {'label': "Avanzata", 'value': "advanced"},
]

error_list = {
    "floor_area": "Attenzione: Specificare la superficie del suolo.",
    "ceiling_height": "Attenzione: Specificare l’altezza del soffitto.",
    "recirc_rate": "Attenzione: Specificare il tasso di ricambio d’aria.",
    "aerosol_radius": "Attenzione: Specificare il raggio dell’aerosol.",
    "viral_deact_rate": "Attenzione: Specificare la velocitá di disattivazione virale.",
    "n_max_input": "Attenzione: Il numero di occupanti non può essere inferiore a 2.",
    "exp_time_input": "Attenzione: Scegliere un tempo di esposizione maggiore di 0.",
    "air_exchange_rate": "Attenzione: Scegliere un sistema di ventilazione (ACH).",
    "merv": "Attenzione: Specificare l’efficienza del sistema di filtrazione (MERV)."
}

# Main Panel Text
curr_room_header = "Ambiente: "
presets = [
    {'label': "Personalizzato", 'value': 'custom'},
    {'label': "Casa Extraurbana", 'value': 'house'},
    {'label': "Ristorante", 'value': 'restaurant'},
    {'label': "Ufficio Silenzioso", 'value': 'office'},
    {'label': "Classe", 'value': 'classroom'},
    {'label': "Cabina della Metro", 'value': 'subway'},
    {'label': "Aero Boeing 737", 'value': 'airplane'},
    {'label': "Chiesa", 'value': 'church'},
]

main_panel_s1 = "Sulla base di questo modello, la stanza scelta potrebbe ospitare in sicurezza: "

units_hr = 'ore'
units_min = 'minuti'
units_days = 'giorni'

units_hr_one = 'ore'
units_min_one = 'minuti'
units_day_one = 'giorni'

is_past_recovery_base_string = '{n_val} persone per >{val:.0f} giorni,'
model_output_base_string = '{n_val} persone per '

main_panel_six_ft_1 = "Nota bene che la linea guida di 2-metri di distanza indicherebbe che massimo "
main_panel_six_ft_2 = " sarebbero in sicurezza in questa stanza per un periodo di tempo indefinito."

six_ft_base_string = ' {} persone'
six_ft_base_string_one = ' {} persone'

graph_title = "Occupazione vs. Tempo di Esposizione"
graph_xtitle = "Tempo Massimo di Esposizione \u03C4 (ore)"
graph_ytitle = "Occupazione Massima N"
transient_text = "Transitorio"
steady_state_text = "Stato Stazionario"

main_airb_trans_only_disc = html.Div(["Queste linee guida si basano sulla considerazione della ",
                                      html.Span(html.A(href='https://www.nature.com/articles/d41586-020-02058-1',
                                                       children="trasmissione per via aerea",
                                                       target='_blank'), ),
                                      html.Span(''' da una singola persona infetta durante il tempo di esposizione 
                                      cumulativo indicato.''')], className='airborne-text')

airb_trans_only_disc = html.Div('''Queste linee guida si basano sulla considerazione della trasmissione per via aerea da
 una singola persona infetta durante il tempo di esposizione cumulativo indicato.''', className='airborne-text')

# Bottom panels text
n_input_text_1 = "Se in questa stanza ci sono "
n_max_base_string = ' {:.0f} persone'
n_input_text_2 = " persone, gli occupanti dovrebbero essere al sicuro per "
n_input_text_3 = "."

t_input_text_1 = "Se gli occupanti stanno all’interno della stanza per "
t_input_text_2 = " ore, l’occupazione dovrebbe essere limitata a "
t_input_text_3 = "."

# About
about_header = "Informazioni"
about = html.Div([
    html.H6("Informazioni", style={'margin': '0'}),
    html.Div('''Per mitigare la diffusione di infezioni da COVID-19, le linee guida ufficiali degli Stati Uniti date 
    dalla sanitá pubblica hanno raccomandato i seguenti limiti: distanza interpersonale (2 metri), 
    tempo di occupazione (15 minuti), occupazione massima (25 persone), o ventilazione minima (6 ricambi di aria 
    all’ora).'''),
    html.Br(),
    html.Div([html.Span('''Sono in crescita le '''),
              html.A(children="prove scientifiche",
                     href=link_docs,
                     target='_blank'),
              html.Span(''' per la trasmissione aerea del COVID-19, la quale si verifica quando le goccioline di 
              aerosol infettive vengono scambiate respirando all’interno di ambienti chiusi. Nonostante le 
              organizzazioni di sanità pubblica stanno iniziando a riconoscere la trasmissione per via aerea, 
              queste devono ancora fornire una linea guida di sicurezza che incorpori tutte le variabili 
              rilevanti.''')]),
    html.Br(),
    html.Div([html.Span('''Questa applicazione, sviluppata da Kasim Khan in collaborazione con Martin Z. Bazant e 
    John W. M. Bush, utilizza un '''),
              html.A(children="modello teorico",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' per calcolare i tempi di un’esposizione sicura ed i livelli di occupazione sicuri per 
              ambienti chiusi. Impostando le specifiche della stanza, i tassi di ventilazione e filtrazione, 
              l'uso della mascherina, le attività respiratorie e la tolleranza al rischio (nelle altre schede), 
              è possibile calcolare come mitigare la trasmissione interna di COVID-19 in diversi ambienti 
              chiusi.''')]),
])

# Room Specifications
room_header = "Caratteristiche dello Spazio Chiuso"

floor_area_text = "Superficie del suolo (sq. ft.): "
floor_area_text_metric = "Superficie del suolo (m²): "
ceiling_height_text = "Altezza media del soffitto (ft.): "
ceiling_height_text_metric = "Altezza media del soffitto (m): "

ventilation_text = "Sistema di ventilazione: "
vent_type_output_base = "{:.0f} ACH"
ventilation_text_adv = "Sistema di ventilazione (ACH): "
ventilation_types = [
    {'label': "Finestre chiuse", 'value': 0.3},
    {'label': "Finestre aperte", 'value': 2},
    {'label': "Ventilazione meccanica", 'value': 3},
    {'label': "Finestre aperte e ventilazione attivata", 'value': 6},
    {'label': "Buona ventilazione meccanica", 'value': 8},
    {'label': "Laboratorio, Ristorante", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Ospedale / Vagone della metropolitana", 'value': 18},
    {'label': "Laboratorio chimico / aeroplano", 'value': 24},
]

filtration_text = "Sistema di Filtrazione: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Sistema di Filtrazione (MERV): "
filter_types = [
    {'label': "Nessuno", 'value': 0},
    {'label': "Finestra residenziale, aria condizionata", 'value': 2},
    {'label': "Residenziale / Commerciale / Industriale", 'value': 6},
    {'label': "Residenziale / Commerciale / Ospedaliero", 'value': 10},
    {'label': "Ospedale e Chirurgia Generale", 'value': 14},
    {'label': "Filtro HEPA", 'value': 17}
]

recirc_text = "Tasso di ricambio d’aria: "
recirc_type_output_base = "{:.1f} ricircolo ACH"
recirc_text_adv = "Tasso di ricambio d’aria (ricircolo ACH): "
recirc_types = [
    {'label': "Nessuno", 'value': 0},
    {'label': "Lento", 'value': 0.3},
    {'label': "Moderato", 'value': 1},
    {'label': "Veloce", 'value': 10},
    {'label': "Aeromobile", 'value': 24},
    {'label': "Vagone della metropolitana", 'value': 54},
]

humidity_text = "Umidità relativa: "
humidity_marks = {
    0: {'label': '0%: Molto Secco', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: Aeroplano', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Secco'},
    0.6: {'label': '60%: Nella Media'},
    0.99: {'label': '99%: Molto Umido'},
}

need_more_ctrl_text = '''Hai bisogno di un maggiore controllo sui tuoi input? Passa alla modalità avanzata 
utilizzando il menu a discesa nella parte superiore della pagina. '''

human_header = "Comportamento umano"
# Human Behavior
exertion_text = "Livello di sforzo: "
exertion_types = [
    {'label': "A Riposo", 'value': 0.49},
    {'label': "In Piedi", 'value': 0.54},
    {'label': "Esercizio Leggero", 'value': 1.38},
    {'label': "Esercizio Moderato", 'value': 2.35},
    {'label': "Esercizio Intenso", 'value': 3.30},
]

breathing_text = "Attività respiratoria: "
expiratory_types = [
    {'label': "Respirazione (leggera)", 'value': 1.1},
    {'label': "Respirazione (normale)", 'value': 4.2},
    {'label': "Respirazione (pesante)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Parlando (sussurrando)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Parlando (normalmente)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Parlando (ad alta voce)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Cantando", 'value': 970},
]

mask_type_text = "Efficienza di filtrazione della maschera (tipo di maschera): "
mask_type_marks = {
    0: {'label': "0% (nessun, schermo facciale)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (cotone)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (seta, flanella, chiffon)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (chirurgico, cotone)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (macherina di protezione N95)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Nessun, schermo facciale", 'value': 0},
    {'label': "Cotone", 'value': 0.1},
    {'label': "Seta, flanella, chiffon", 'value': 0.5},
    {'label': "Chirurgica, cotone", 'value': 0.9},
    {'label': "Mascherina di protezione N95", 'value': 0.95},
]

mask_fit_text = "Vestibilità / Conformità maschera: "
mask_fit_marks = {
    0: {'label': '0%: Nessuna', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Povera'},
    0.95: {'label': '95%: Buona'}
}

risk_tolerance_text = "Tolleranza al rischio: "
risk_tol_desc = html.Div('''Le persone più vulnerabili, come gli anziani o coloro con condizioni mediche 
preesistenti, richiedono una minore tolleranza al rischio. Una tolleranza al rischio più elevata indica una maggiore 
probabilitá di trasmissione durante il periodo di occupazione previsto (consultare la sezione “domande piú frequenti” 
per ulteriori dettagli).''', style={'font-size': '13px', 'margin-left': '20px'})
risk_tol_marks = {
    0.01: {'label': '0.01: Sicuri-ssimo', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Sicuro', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Non sicuro'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Domande piú frequenti"
other_io = "Altri Ingressi ed Uscite"

faq_top = html.Div([
    html.H6("Domande piú frequenti"),
    html.H5("Perché la distanza di 2 metri non è sufficiente?"),
    html.Div([
        html.Div([html.Span('''La distanza di 2 metri, cosí come la mascherina facciale, ti protegge da grosse gocce 
        espulse da una persona infetta che tossisce; tuttavia, questa non protegge dalla '''),
                  html.A(children="trasmissione per via aerea",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' di aerosol infettivi sospesi nell'aria, i quali tendono a miscelarsi con l’aria di un 
                  ambiente chiuso. Negli spazi chiusi, difatti, la trasmissione aerea di aerosol fa sì che gli 
                  occupanti non siano più al sicuro a 20 metri piuttosto che a 2 metri, essendo la trasmissione aerea 
                  indipendente dalla distanza tra gli occupanti.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Esistono altre modalità di trasmissione?"),
    html.Div([
        html.Div([html.A(children="Si ritiene che la trasmissione per via aerea",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' sia dominante per COVID-19. Tuttavia, sono possibili altre modalità, come la 
                  trasmissione per contatto diretto con superfici contaminate, la trasmissione per "goccioline 
                  grandi" tramite tosse o starnuti e tramissione per "aerosol a corto raggio" dovuto al getto 
                  respiratorio di una persona infetta per un periodo prolungato. Sebbene le ultime due modalità 
                  possano essere significative, vengono in gran parte eliminate quando si indossano le mascherine o 
                  le visiere; ciononostante, il rischio di trasmissione aerea permane.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Possiamo davvero ipotizzare che l’aria di una stanza sia omogenea?"),
    html.Div([
        html.Div([html.Span('''Ci sono molti fattori che contribuiscono all’omogeinizzazione dell’aria negli spazi 
        interni, inclusi flussi guidati dalla convezione naturale (come quelli originati da termosifoni, 
        condizionatori o finestre), convezione forzata da prese d'aria e ventilatori, movimento e respirazione umana. 
        Sebbene vi siano delle eccezioni, come discusso in questo '''),
                  html.A(children="articolo scientifico",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', l’ipotesi di una buona miscelazione è ampiamente utilizzata nei modelli teorici 
                  della trasmissione di malattie per via aerea.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Queste linee guida valgono anche per ampi spazi chiusi?"),
    html.Div([
        html.Div([html.Span('''Nelle sale da concerto, negli stadi o in altri spazi ampi e ventilati con un gran 
        numero di occupanti, il rischio di trasmissione per via aerea è significativo e preso adeguatamente in 
        considerazione da queste linee guida. Tuttavia, quando non si indossano mascherine o visiere, 
        esiste un rischio aggiuntivo di trasmissione a corto raggio attraverso getti respiratori, il quale é stimato 
        in questo '''),
                  html.A(children="articolo",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Perché è importante l'altezza del soffitto?"),
    html.Div([
        '''L'altezza del soffitto influenza il volume totale dello spazio chiuso, il quale é necessario per stimare 
        la concentrazione di aerosol infettivi (numeri di aerosol per unità di volume). Questa concentrazione è 
        fondamentale nella stima del rischio di trasmissione del COVID-19 in un luogo chiuso. '''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Conosco i miei numeri ACH / MERV. Dove posso inserirli?"),
    html.Div('''
        Se hai bisogno di un maggiore controllo sui tuoi parametri d’ingresso, passa alla modalità avanzata utilizzando 
        il menu scorrevole nella parte superiore della pagina web.
    ''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Ci sono parametri nascosti nella modalità di base?"),
    html.Div([html.Span('''Tutti i parametri fisici rilevanti sono descritti in dettaglio '''),
              html.A(children="nell’articolo scientifico",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. Nella modalità di base, l'applicazione ipotizza un raggio di aerosol effettivo 
              predefinito di 2 μm (al 60% di umidità) e un tasso di disattivazione virale massimo di 0,6 / h (a ~ 
              100% di umidità), ed entrambi aumentano con l'umidità relativa (UR). Le stime per il tasso di 
              disattivazione virale errano sul lato conservativo della disattivazione più lenta. Il tasso di 
              disattivazione virale può essere aumentato da radiazioni ultraviolette (UV-C) o disinfettanti chimici (
              ad esempio acqua ossigenata, ozono). L'applicazione stima anche il parametro chiave della malattia, 
              l'infettività dell'aria espirata, C'''),
              html.Sub("q"),
              html.Span(''' (quanti di infezione per unità di volume), in virtù dell’attività respiratoria 
              specificata, utilizzando i valori tabulati nella Figura 2 '''),
              html.A(children="dell’articolo",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. Questi parametri vengono definiti indipendentemente nella modalità avanzata.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Raggio aerosol effettivo (a RH = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Tasso massimo di disattivazione virale (a RH = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

values_interest_header = ""
values_interest_desc = html.Div([
    html.H5("Che cosa calcola esattamente l'applicazione?"),
    html.Div([
        html.Div([html.Span('''Data una tolleranza al rischio relativa alla trasmissione per via aerea, 
        l'applicazione calcola il tempo di esposizione cumulativo massimo consentito, ovvero il prodotto 
        dell'occupazione della stanza e del tempo di esposizione in presenza di una persona infetta. L'applicazione 
        calcola anche le seguenti quantità relative, definite '''),
                  html.A(children="nell’articolo",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', che possono essere di interesse:''')]),
    ], className='faq-answer'),
])
outdoor_air_frac_label = html.Span(["Frazione di aria esterna Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Efficienza di filtrazione aerosol p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Portata respiratoria Q", html.Sub('b'), ": "])
cq_label = html.Span(["Infettività dell'aria espirata C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Probabilità passaggio maschera p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Volume della stanza V: "])
vent_rate_Label = html.Span(["Portata di ventilazione (esterna) Q: "])
recirc_rate_label = html.Span(["Portata di ritorno (ricircolo) Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Velocità di filtrazione dell'aria (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Raggio dell'aerosol regolato in base all'umidità r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Tasso di disattivazione virale aggiustato per l'umidità \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Velocità effettiva di sedimentazione aerosol v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Tasso di rilassamento della concentrazione \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Velocità di trasmissione aerea \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Questo modello tiene conto della prevalenza dell'infezione nella popolazione locale?"),
    html.Div(['''No. Il modello calcola il rischio di trasmissione da una singola persona infetta. Si presume quindi 
    implicitamente che la prevalenza dell'infezione nella popolazione sia relativamente bassa. In questo limite, 
    il rischio di trasmissione aumenta con il numero atteso di persone infette nella stanza, in particolare con il 
    prodotto dell'occupazione e la prevalenza nella popolazione. La tolleranza dovrebbe essere ridotta 
    proporzionalmente a questo numero se supera uno. Al contrario, quando il numero atteso di persone infette nella 
    stanza si avvicina a zero, la tolleranza potrebbe essere proporzionalmente aumentata fino a quando le restrizioni 
    raccomandate non saranno ritenute necessarie.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("Altre domande?"),
    html.Div([html.Span('''Per spiegazioni e riferimenti più dettagliati, riferirsi a "'''),
              html.A(children="Beyond 6 Feet",
                     href=link_paper,
                     target='_blank'),
              html.Span('''" e altri collegamenti pubblicati nella parte superiore della pagina web.''')]),
])

footer = html.Div([
    html.Div([html.Span('''Queste Linee Guida per Tutelare Salute e Sicurezza in Ambienti Chiusi contro il COVID-19 
    sono uno strumento in evoluzione inteso a far familiarizzare l'utente interessato con i fattori che influenzano 
    il rischio di trasmissione aerea interna di COVID-19 e ad aiutare nella valutazione quantitativa del rischio in 
    varie circostanze. Consapevoli che l'incertezza e la variabilità intrinseca dei parametri del modello possono 
    portare a errori fino ad un ordine di grandezza, tali errori possono essere compensati optando per una tolleranza 
    al rischio sufficientemente bassa. Queste Linee Guida non tengono conto della trasmissione a corto raggio 
    attraverso getti respiratori, i quali possono aumentare sostanzialmente il rischio di infezione quando mascherine 
    o visiere non vengono indossate, come discusso '''),
              html.A(children="nell’articolo allegato",
                     href=link_paper,
                     target='_blank'),
              html.Span('''(Bazant & Bush, 2020). L'utilizzo delle Linee Guida per Tutelare Salute e Sicurezza in 
              Ambienti Chiusi contro il COVID-19  è un’esclusiva responsabilità dell'utente ed é reso disponibile 
              senza garanzie di alcun tipo. Gli autori dichiarano di non assumersi alcuna responsabilità dovuta al 
              suo utilizzo.''')]),
    html.Br(),
    html.Div("Un ringraziamento speciale a: ")
], className='footer-small-text')
