import dash_html_components as html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions: Brazilian Portuguese

"""

# Header
header = html.Div([
    html.H1(children='COVID-19 Diretriz de Segurança em Ambientes Fechados'),
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
language_dd = "Idioma: "

# Unit systems
units_dd = "Sistema de Unidades: "
unit_settings = [
    {'label': "Britânico", 'value': "british"},
    {'label': "Métrico", 'value': "metric"},
]

# Modes
mode_dd = "Modo: "
app_modes = [
    {'label': "Básico", 'value': "basic"},
    {'label': "Avançado", 'value': "advanced"},
]

error_list = {
    "floor_area": "Erro: A área do cômodo não pode estar vazia.",
    "ceiling_height": "Erro: A altura do teto não pode estar vazia.",
    "recirc_rate": "Erro: Taxa de recirculação não pode estar vazia.",
    "aerosol_radius": "Erro: Raio do aerossol não pode estar vazio.",
    "viral_deact_rate": "Erro: Taxa de desativação viral não pode estar vazia.",
    "n_max_input": "Erro: O número de pessoas não pode ser inferior a 2.",
    "exp_time_input": "Erro: O tempo de exposição deve ser maior que 0.",
    "air_exchange_rate": "Erro: A taxa de ventilação (ACH) deve ser maior que 0.",
    "merv": "Erro: Sistema de filtração (MERV) não pode estar vazio.",
    "prevalence": "Erro: A prevalência deve ser maior do que 0 e menor do que 100.000.",
    "atm_co2": "Erro: Nível de CO₂ ambiente é necessário."
}


# Main Panel Text
curr_room_header = "Especificações do Ambiente: "
presets = [
    {'label': "Personalizado", 'value': 'custom'},
    {'label': "Sala de aula", 'value': 'classroom'},
    {'label': "Sala de estar", 'value': 'living-room'},
    {'label': "Igreja", 'value': 'church'},
    {'label': "Restaurante", 'value': 'restaurant'},
    {'label': "Escritório", 'value': 'office'},
    {'label': "Vagão de metrô", 'value': 'subway'},
    {'label': "Vôo Comercial", 'value': 'airplane'},
]

curr_human_header = "Comportamento das Pessoas: "
presets_human = [
    {'label': "Personalizado", 'value': 'custom'},
    {'label': "Máscaras, Parados", 'value': 'masks-1'},
    {'label': "Máscaras, Falando", 'value': 'masks-2'},
    {'label': "Máscaras, Exercitando", 'value': 'masks-3'},
    {'label': "Sem Máscaras, Parados", 'value': 'no-masks-1'},
    {'label': "Sem Máscaras, Falando", 'value': 'no-masks-2'},
    {'label': "Sem Máscaras, Exercitando", 'value': 'no-masks-3'},
    {'label': "Sem Máscaras, Cantando", 'value': 'singing-1'},
]

curr_risk_header = "Tolerância a riscos: "
# presets_risk = [
#     {'label': "Low", 'value': 0.01},
#     {'label': "Medium", 'value': 0.1},
#     {'label': "High", 'value': 1},
# ]
risk_tol_marks = {
    # 0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Mais seguro', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Inseguro'}
}

risk_tolerance_text = "Risk Tolerance: "
risk_tol_desc = html.Div('''More vulnerable populations such as the elderly or those with preexisting medical 
conditions require a lower risk tolerance (~0.01). A higher risk tolerance will mean more expected 
transmissions during the expected occupancy period (see FAQ for details).''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})

curr_age_header = "Faixa etária: "
presets_age = [
    {'label': "Crianças (<15 anos)", 'value': 0.23},
    {'label': "Adultos (15-64 anos)", 'value': 0.68},
    {'label': "Idosos (>64 anos)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: Crianças (<15 anos)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: Adultos (15-64 anos)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: Idosos (>64 anos)', 'style': {'width': '75px'}}
}
lang_break_age = html.Br()

curr_strain_header = "Cepa Viral: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2 (Cepa de Wuhan)", 'value': 1},
    {'label': "SARS-CoV-2 - B.1.1.7 (Cepa do Reino Unido)", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: Wuhan', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: B.1.1.7/Reino Unido', 'style': {'width': '100px'}}
}

pim_header = "Porcentagem de Imunizados: "
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "Se uma pessoa infectada entrar..."
risk_prevalence_desc = "Dada a prevalência de infecção..."
risk_personal_desc = "Para limitar o meu risco pessoal..."
risk_options = [
    {'label': risk_conditional_desc, 'value': 'conditional'},
    {'label': risk_prevalence_desc, 'value': 'prevalence'},
    {'label': risk_personal_desc, 'value': 'personal'},
]
risk_personal_warning = html.Span([
    html.Span('''Cuidado: ''', style={'font-weight': 'bold'}),
    html.Span('''o modo de risco selecionado (Para limitar o meu risco pessoal…) considera a 
    probabilidade de infecção de um só indivíduo. Por isso, o modo é mais restritivo e não 
    deveria ser utilizado para estabelecer normas de segurança para a população.''')])

risk_mode_panel_header = "Modo de Risco"
occupancy_panel_header = "Calcular Ocupação Segura"
main_panel_s1 = '''Com base neste modelo, este ambiente seria seguro* com: '''

main_panel_s1_b = html.Span([
    html.Span('''Para limitar a transmissão de COVID-19* em uma população com uma prevalência de infecção'''),
    html.Sup('''1'''),
    html.Span(''' de ''')
])
main_panel_s2_b = ''' em 100.000, este espaço não deve ter mais do que: '''

main_panel_s1_c = html.Span([
    html.Span('''Para limitar minha chance de ser infectado por COVID-19 em uma população com uma prevalência 
    de infecção'''),
    html.Sup('''1'''),
    html.Span(''' de ''')
])
main_panel_s2_c = ''' em 100.000, este espaço não deve ter mais do que: '''

units_hr = 'horas'
units_min = 'minutos'
units_days = 'dias'
units_months = 'meses'

units_hr_one = 'hora'
units_min_one = 'minuto'
units_day_one = 'dia'
units_month_one = 'mês'

is_past_recovery_base_string = '{n_val} pessoas por >{val:.0f} dias,'
model_output_base_string = '{n_val} pessoas por '
model_output_base_string_co2 = '{co2:.2f} ppm por '
nt_bridge_string = " pessoas por "
tn_bridge_string = " por "

main_panel_six_ft_1 = "Em contraste, a diretriz de distanciamento de seis pés (ou dois metros) limitaria a ocupação a "
main_panel_six_ft_2 = ", o que violaria a diretriz* após "

six_ft_base_string = ' {} pessoas'
six_ft_base_string_one = ' {} pessoa'

graph_title = "Ocupação vs. Tempo de Exposição"
graph_xtitle = "Tempo Máximo de Exposição \u03C4 (horas)"
graph_ytitle = "Ocupação Máxima N"
transient_text = "Estado Transitório"
steady_state_text = "Estado Estacionário"
co2_safe_trace_text = "Nível Respiratório Seguro"
guideline_trace_text = "Diretriz"
background_co2_text = "CO\u2082 ambiente: "
recommended_co2_text = "Limite recomendado"

graph_title_co2 = "Concentração de CO₂ Segura (ppm) contra Tempo de Exposição"
graph_ytitle_co2 = "Concentração de CO₂ (ppm)"

co2_title = "Calcular Concentração de CO\u2082 Segura"
co2_param_desc = '''A diretriz para os parâmetros escolhidos acima é expressa aqui em termos de um nível de concentração
 de CO₂.'''
co2_prev_input_1 = html.Span(["Prevalência", html.Sup('1'), html.Span(": ")])
co2_prev_input_2 = " por 100,000"
co2_atm_input_1 = background_co2_text
co2_atm_input_2 = " ppm"
co2_calc_1 = "Para um tempo de exposição de "
co2_calc_2 = " horas, a concentração de CO₂ segura calculada em estado estacionário neste espaço é de "
co2_calc_3 = "."
co2_base_string = '{:,.2f} ppm'

co2_safe_sent_1 = "This limit exceeds that for healthy respiratory activity, which is "
co2_safe_sent_2 = "."

co2_safe_footer = html.Span(['''O Nível Respiratório Seguro é interpolado com base nos limites ''',
                             html.A(href=links.link_usda_co2,
                                    children='''recomendados pelo USDA''',
                                    target='_blank'),
                             '''.'''])

main_airb_trans_only_disc = html.Div(["*A diretriz restringe a probabilidade de ",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="transmissão aérea",
                                                       target='_blank'), ),
                                      html.Span(''' por pessoa infectada a ser menor que a tolerância de risco
                                      durante o tempo de exposição cumulativo listado.''')], className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*A diretriz restringe a probabilidade de ",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="transmissão aérea",
                                                       target='_blank'), ),
                                      html.Span(''' por pessoa infectada a ser menor que a tolerância de risco (10%) 
                                      durante o tempo de exposição cumulativo listado.''')], className='airborne-text')

other_risk_modes_desc = html.Div('''Outros cenários de risco são considerados no Modo Avançado. Especificamente, 
pode-se considerar a prevalência de infecção na população, imunidade adquirida através da 
vacinação ou exposição anterior, e o risco para um indivíduo específico.''')

main_airb_trans_only_desc_b = html.Div(["*A diretriz restringe a probabilidade de uma ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="transmissão aérea",
                                                         target='_blank'), ),
                                        html.Span(''' por pessoa infectada a ser menor do que a tolerância de risco 
                                        pelo tempo de exposição cumulativa listado.''')], className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["*The guideline restricts the probability of ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="airborne transmission",
                                                         target='_blank'), ),
                                        html.Span(''' to a particular individual to be less than the risk tolerance 
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')

airb_trans_only_disc = html.Div('''''', className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''Para estimar a prevalência no seu local, aqui estão alguns recursos úteis: '''),
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
n_input_text_1 = "Se este ambiente tiver "
n_max_base_string = ' {:.0f} pessoas'
n_max_overflow_base_string = ' >{:.0f} pessoas'
n_input_text_2 = " pessoas, a diretriz* seria violada após "
n_input_text_3 = "."

t_input_text_1 = "Se as pessoas passarem aproximadamente "
t_input_text_2 = " horas aqui, a ocupação deve ser limitada a "
t_input_text_3 = "."

# About
about_header = "Sobre"
about = html.Div([
    html.H6("Sobre", style={'margin': '0'}),
    html.Div('''Para mitigar a propagação de COVID-19, as diretrizes oficiais de saúde pública recomendaram limites 
    de: distância de pessoa a pessoa (6 pés / 2 metros), tempo de ocupação (15 minutos), ocupação 
    máxima (25 pessoas), ou ventilação mínima (6 trocas de ar por hora).'''),
    html.Br(),
    html.Div([html.Span('''Há '''),
              html.A(children="evidências científicas",
                     href=links.link_docs,
                     target='_blank'),
              html.Span(''' crescentes para a transmissão por via aérea de COVID-19, que ocorre quando gotículas 
              infectadas de aerossol são trocadas por meio da respiração de ar interno compartilhado. 
              Embora as organizações de saúde pública estejam começando a reconhecer a transmissão por 
              via aérea, elas ainda precisam fornecer uma diretriz de segurança que incorpore todas as 
              variáveis relevantes.''')]),
    html.Br(),
    html.Div([html.Span('''Este aplicativo, desenvolvido por Kasim Khan em colaboração com Martin Z. Bazant e 
    John W. M. Bush, usa um '''),
              html.A(children="modelo teórico",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' para calcular tempos de exposição e níveis de ocupação seguros para ambientes internos. 
              Ao ajustar as especificações do ambiente, as taxas de ventilação e filtragem, o uso de 
              máscaras faciais, atividades respiratórias e tolerância a riscos (nas outras guias), você 
              pode ver como mitigar a transmissão de COVID-19 em diferentes ambientes internos.''')]),
    html.Br(),
    html.Div(['''No modo Básico, é possível calcular os limites de ocupação segura após a entrada 
    de uma única pessoa infectada em um espaço interno. No Modo Avançado, você pode levar em conta 
    fatores adicionais, incluindo a prevalência da infecção e a imunidade da população. No Modo 
    Avançado também é possível avaliar a ocupação segura com base na concentração média de CO2, 
    que está relacionada com a concentração de aerossóis infecciosos.''']),
    html.Br(),
    html.Div([html.Span('''A pesquisa científica por trás do aplicativo também é ensinada em um curso online gratuito, 
    auto-gerenciado e aberto (MOOC) no edX: '''),
              html.A(children="10.S95x Physics of COVID-19 Transmission",
                     href=links.link_mooc,
                     target='_blank')]),
])

# Room Specifications
room_header = "Especificações do ambiente- Detalhes"

floor_area_text = "Área total do ambiente (sq. ft.): "
floor_area_text_metric = "Área total do ambiente (m²): "
ceiling_height_text = "Altura média do teto (ft.): "
ceiling_height_text_metric = "Altura média do teto (m): "

ventilation_text = "Sistema de ventilação: "
vent_type_output_base = "{:.1f} "
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (trocas de ar ao ar livre)"])
ventilation_text_adv = html.Span(["Sistema de ventilação (hr", html.Sup("-1"), ", trocas de ar ao ar livre): "])
ventilation_types = [
    {'label': "Janelas fechadas", 'value': 0.3},
    {'label': "Janelas abertas", 'value': 2},
    {'label': "Ventilação mecânica", 'value': 3},
    {'label': "Janelas abertas com ventiladores", 'value': 6},
    {'label': "Melhor Ventilação Mecânica", 'value': 8},
    {'label': "Laboratório, Restaurante", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Hospital/Vagão de metrô", 'value': 18},
    {'label': "Laboratório Tóxico/Avião", 'value': 24},
]

filtration_text = "Sistema de filtragem: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Sistema de filtragem (MERV): "
filter_types = [
    {'label': "Nenhum", 'value': 0},
    {'label': "Ar condicionado janela residencial", 'value': 2},
    {'label': "Residencial/Comercial/Industrial", 'value': 6},
    {'label': "Residencial/Comercial/Hospitalar", 'value': 10},
    {'label': "Hospitalar & Cirurgia Geral", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_text = "Taxa de recirculação: "
recirc_type_output_base = "{:.1f} "
recirc_type_output_units = html.Span(["hr", html.Sup("-1")])
recirc_text_adv = html.Span(["Taxa de recirculação (hr", html.Sup("-1"), "): "])
recirc_types = [
    {'label': "Nenhuma", 'value': 0},
    {'label': "Lenta", 'value': 0.3},
    {'label': "Moderada", 'value': 1},
    {'label': "Rápida", 'value': 10},
    {'label': "Avião", 'value': 24},
    {'label': "Vagão de metrô", 'value': 54},
]

humidity_text = "Umidade relativa: "
humidity_marks = {
    0.01: {'label': '1%: Muito seco', 'style': {'max-width': '25px'}},
    # 0.2: {'label': '20%: Avião', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Seco'},
    0.6: {'label': '60%: Média'},
    0.99: {'label': '99%: Muito úmido'},
}

need_more_ctrl_text = '''Precisa de mais controle sobre suas opções? Mude para o Modo Avançado usando o menu no 
topo da página.'''

human_header = "Comportamento das Pessoas - Detalhes"
# Human Behavior
exertion_text = "Taxa de Respiração: "
exertion_types = [
    {'label': "Parados", 'value': 0.49},
    {'label': "Em pé", 'value': 0.54},
    {'label': "Exercício Leve", 'value': 1},
    {'label': "Exercício Moderado", 'value': 1.38},
    {'label': "Exercício Pesado", 'value': 2.35},
    {'label': "Cantando", 'value': 3.30},
]

breathing_text = "Atividade Respiratória: "
expiratory_types = [
    {'label': "Respirando (leve)", 'value': 1.1},
    {'label': "Respirando (normal)", 'value': 4.2},
    {'label': "Respirando (pesada)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Conversando (sussurro)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Conversando (normal)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Conversando (alto)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Cantando", 'value': 970},
]

mask_type_text = "Eficiência de Filtração da Máscara (tipo de máscara): "
mask_type_marks = {
    0: {'label': "0% (Nenhuma, Protetor facial)", 'style': {'max-width': '75px'}},
    0.5: {'label': "50% (Algodão, flanela)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (Algodão multicamadas, seda)", 'style': {'max-width': '75px'}},
    0.90: {'label': "90% (Cirúrgica descartável)", 'style': {'max-width': '75px'}},
    # 0.99: {'label': "99% (N95 resp-irator)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Nenhuma, Protetor facial", 'value': 0},
    {'label': "Algodão, flanela", 'value': 0.5},
    {'label': "Algodão multicamadas, seda", 'value': 0.7},
    {'label': "Cirúrgica descartável", 'value': 0.9},
    {'label': "Respirador N95", 'value': 0.99},
]

mask_fit_text = "Uso de Máscara: "
mask_fit_marks = {
    0: {'label': '0%: Nenhum', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Pouco'},
    0.95: {'label': '95%: Bom'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Perguntas Frequentes"
other_io = "Outros parâmetros"

faq_top = html.Div([
    html.H6("Perguntas Frequentes"),
    html.H5("Por que o distanciamento de 6 pés/2 metros não é suficiente?"),
    html.Div([
        html.Div([html.Span('''O distanciamento de 6 pés (ou 2 metros) protege contra gotas grandes ejetadas por uma 
        pessoa infectada tossindo, assim como as máscaras faciais; no entanto, não protege contra a '''),
                  html.A(children="transmissão",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' pelo ar por aerossóis infecciosos que ficam suspensos no ar e misturados por toda uma 
                  sala. Em ambientes internos, mais distância não necessariamente significa mais segurança.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Existem outros modos de transmissão?"),
    html.Div([
        html.Div([html.A(children="A transmissão por via aérea",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' é considerada dominante para COVID-19, mas outros modos são possíveis, 
                  tais como a transmissão por "fômites" através do contato direto com resíduos 
                  infecciosos em superfícies, a transmissão por "gotas grandes" através de tosse 
                  ou espirros, e a transmissão de "curto alcance" pela respiração de uma pessoa 
                  infectada por um período prolongado. Embora os dois últimos modos possam ser 
                  significativos, eles são em grande parte eliminados quando máscaras ou escudos 
                  faciais (Face Shield) são usados; entretanto, o risco de transmissão por via 
                  aérea permanece.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Podemos realmente assumir que o ar em uma sala está bem misturado?"),
    html.Div([
        html.Div([html.Span('''Há muitos fatores que contribuem para a mistura do ar em espaços 
        internos, incluindo fluxos impulsionados pela flutuação (de aquecedores, ar condicionado 
        ou janelas), convecção forçada de ventiladores, e movimento e respiração humana. Embora 
        haja exceções, como discutido no '''),
                  html.A(children="artigo",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''', a suposição de ar bem misturado é amplamente utilizada na modelagem teórica da 
                  transmissão de doenças transmitidas pelo ar. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("A diretriz é válida para espaços muito grandes?"),
    html.Div([
        html.Div([html.Span('''Em salas de concertos, estádios ou outros espaços grandes e 
        ventilados com grande número de pessoas, o risco de transmissão por via aérea é significativo 
        e devidamente capturado pela diretriz.  Entretanto, quando máscaras ou escudos faciais
         (Face Shield) não são usados, há um risco adicional de transmissão de curto alcance através
          de jatos respiratórios, estimado no '''),
                  html.A(children="artigo",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Por que a altura do teto é importante?"),
    html.Div([
        '''A altura do teto influencia o volume total da sala, o que é necessário para estimar a 
        concentração de aerossóis infecciosos (quantidade de aerossóis por unidade de volume). Esta 
        concentração é necessária para estimar o risco de transmissão de COVID-19 da sala.'''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Eu sei os valores de ACH/MERV do meu filtro. Onde posso inseri-los?"),
    html.Div('''
        Se você precisar de mais controle sobre suas entradas, mude para o Modo Avançado usando o menu no topo da 
        página.
    ''', className='faq-answer'),
    html.Br(),
    html.H5("Por que os Respiradores N95 têm 99% de eficiência?"),
    html.Div('''Os respiradores N95 têm pelo menos 95% de eficiência de filtragem em partículas de
     tamanho de 0,3 μm, 10 vezes menor que os tamanhos de gotas na transmissão de COVID-19 por
      via aérea. Para gotas maiores, os respiradores N95 são ainda mais eficientes, chegando a
       níveis próximos a 100%.''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Há algum parâmetro oculto no Modo Básico?"),
    html.Div([html.Span('''Todos os parâmetros físicos relevantes estão detalhados no '''),
              html.A(children="artigo",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''. No Modo Básico, o aplicativo assume um raio de aerossol efetivo padrão de
               2 μm (com 60% de umidade) e uma taxa máxima de desativação viral de 0,6 /hr (com 
               ~100% de umidade), ambos aumentando com a umidade relativa (UR). As estimativas 
               para a taxa de desativação viral erram para o lado conservador de uma desativação 
               mais lenta.  A taxa de desativação viral pode ser aumentada pela radiação 
               ultravioleta (UV-C) ou por desinfetantes químicos (por exemplo, peróxido de 
               hidrogênio, ozônio). 
O aplicativo também estima o parâmetro chave da doença, a infecciosidade do ar exalado, C'''),
              html.Sub("q"),
              html.Span(''' (quanta de infecção por unidade de volume), a partir da atividade respiratória 
              especificada, usando valores tabulados na Figura 2 do '''),
              html.A(children="artigo",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''. Você mesmo define estes parâmetros no Modo Avançado.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Raio Aerosol Efetivo (em UR = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Taxa máxima de desativação viral (em UR = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

pop_immunity_header = "Imunidade da população: "
perc_immune_label = html.Span(["Porcentagem de imunidade p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["Porcentagem infecciosa p", html.Sub('i'), " = "])
perc_susceptible_label = html.Span(["Porcentagem suscetível p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''A porcentagem infecciosa p''', html.Sub('i'), ''' na população é calculada a partir da prevalência de infecção informada nas outras guias de cenários de risco (Dada a prevalência de infecção...
Para limitar o meu risco pessoal...).  A porcentagem de imunidade p''', html.Sub('im'), ''' pode ser 
estimada de forma conservadora a partir da porcentagem de vacinação da população mais a taxa total
 de casos na população, ignorando a contagem de casos não detectados. Estes dois valores são usados
  para calcular a porcentagem suscetível, p''', html.Sub('s'), '''. No Modo Básico e no primeiro modo de risco (Se uma 
  pessoa infectada entrar...), este valor é assumido como sendo de 100%.''']),
                              html.Br(),
                              html.Div(['''Aqui estão alguns links úteis para encontrar p''', html.Sub('i'), ''' e p''',
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

values_interest_header = "Valores de Interesse Calculados: "
values_interest_desc = html.Div([
    html.H5("O que exatamente é calculado pelo aplicativo?"),
    html.Div([
        html.Div([html.Span('''O aplicativo calcula o tempo máximo de exposição cumulativa permitido,
         o produto da ocupação do ambiente e do tempo, em um espaço interno. A propagação de COVID-19 
         é limitada ao exigir que o número esperado de transmissões por indivíduo infectado, o 
         chamado "número reprodutivo em ambientes internos", seja menor do que a tolerância de 
         risco escolhida. O aplicativo também calcula as quantidades relacionadas, definidas no '''),
                  html.A(children="artigo",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''',  que podem ser de interesse:''')]),
    ], className='faq-answer'),
])
relative_sus_label = html.Span(["Suscetibilidade relativa s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["Fração de ar exterior Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Eficiência da filtragem dos aerossóis p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Taxa de fluxo respiratório Q", html.Sub('b'), ": "])
cq_label = html.Span(["Infecciosidade do ar exalado C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Probabilidade de passagem pela máscara p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Volume da sala V: "])
vent_rate_Label = html.Span(["Vazão de ventilação (ao ar livre) Q: "])
recirc_rate_label = html.Span(["Vazão de retorno (recirculação) Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Taxa de filtragem do ar (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Raio de aerossol ajustado à umidade r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Taxa de desativação viral ajustada à umidade \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Velocidade efetiva de assentamento do aerossol v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Taxa de relaxamento da concentração \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Taxa de transmissão por via aérea \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
])

faq_infect_rate = html.Div([
    html.H5("Este modelo é responsável pela prevalência da infecção na população local?"),
    html.Div(['''A influência da prevalência de infecção na população local pode ser considerada no 
    Modo Avançado. Lá, na guia “Outros parâmetros”, pode-se também avaliar a influência da imunidade
     na população, que pode surgir através da vacinação ou infecção anterior.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("Mais perguntas?"),
    html.Div([html.Span('''Para explicações e referências mais detalhadas, consulte o artigo "'''),
              html.A(children="Beyond 6 Feet",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''" e outros links publicados no topo da página.''')]),
])

footer = html.Div([
    html.Div([html.Span('''COVID-19: Diretriz de Segurança em Ambientes Internos é uma ferramenta 
    em evolução destinada a familiarizar o usuário interessado com os fatores que influenciam o
     risco de transmissão aérea de COVID-19 em ambientes internos, e a auxiliar na avaliação 
     quantitativa do risco em vários ambientes. Observamos que a incerteza e a variabilidade 
     intrínseca dos parâmetros do modelo podem levar a erros tão grandes como uma ordem de 
     grandeza, que podem ser compensados pela escolha de uma tolerância ao risco suficientemente
      pequena. Nossa diretriz não leva em conta a transmissão de curto alcance através de jatos 
      respiratórios, que pode elevar substancialmente o risco quando as máscaras faciais não estão
       sendo usadas, de uma forma discutida no '''),
              html.A(children="artigo",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' que acompanha esta ferramenta (Bazant & Bush, 2020). O uso de 
              COVID-19: Diretriz de Segurança em Ambientes Internos é de responsabilidade 
              exclusiva do usuário. Esta ferramenta está sendo disponibilizada sem qualquer 
              tipo de garantia. Os autores se isentam de qualquer responsabilidade por seu uso.''')]),
    html.Br(),
    html.Div("Agradecimentos especiais a: ")
], className='footer-small-text')
