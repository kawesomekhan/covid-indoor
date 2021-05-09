import dash_html_components as html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions: Russian

"""

# Header
header = html.Div([
    html.H1(children='COVID-19 Правила безопасности в помещении'),
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
language_dd = "Язык: "

# Unit systems
units_dd = "Единицы измерения: "
unit_settings = [
    {'label': "Английская система мер", 'value': "british"},
    {'label': "Метрическая система мер", 'value': "metric"},
]

# Modes
mode_dd = "Режим: "
app_modes = [
    {'label': "Основной", 'value': "basic"},
    {'label': "Продвинутый", 'value': "advanced"},
]

error_list = {
    "floor_area": "Ошибка: Площадь помещения не может быть пустой.",
    "ceiling_height": "Ошибка: Высота потолка не может быть пустой.",
    "recirc_rate": "Ошибка: Скорость рециркуляции не может быть пустой. ",
    "aerosol_radius": "Ошибка: Радиус аэрозоля не может быть пустым.",
    "viral_deact_rate": "Ошибка: Темп деактивации вирусов не может быть пустым.",
    "n_max_input": "Ошибка: Количество людей не может быть меньше 2.",
    "exp_time_input": "Ошибка: Время контакта должно быть больше нуля.",
    "air_exchange_rate": "Ошибка: Скорость вентиляции (ACH) должно быть больше нуля.",
    "merv": "Ошибка: Система фильтрации (MERV) не может быть пустой.",
    "prevalence": "Ошибка: Распространенность должна быть больше чем 0 и меньше чем 100,000.",
    "atm_co2": "Ошибка: требуется уровень CO₂ в окружности."
}


# Main Panel Text
curr_room_header = "Характеристики помещения: "
presets = [
    {'label': "Пользовательские", 'value': 'custom'},
    {'label': "Класс", 'value': 'classroom'},
    {'label': "гостинная", 'value': 'living-room'},
    {'label': "Церковь", 'value': 'church'},
    {'label': "Ресторан", 'value': 'restaurant'},
    {'label': "Офис", 'value': 'office'},
    {'label': "вагон метро", 'value': 'subway'},
    {'label': "Коммерческий авиалайнер", 'value': 'airplane'},
]

curr_human_header = "Человеческое поведение: "
presets_human = [
    {'label': "Пользовательские", 'value': 'custom'},
    {'label': "Маски, Отдых", 'value': 'masks-1'},
    {'label': "Маски, Разговор", 'value': 'masks-2'},
    {'label': "Маски, Упражнение", 'value': 'masks-3'},
    {'label': "Без Маски, Отдых", 'value': 'no-masks-1'},
    {'label': "Без Маски, Разговор", 'value': 'no-masks-2'},
    {'label': "Без Маски, Упражнение", 'value': 'no-masks-3'},
    {'label': "Без Маски, Пение", 'value': 'singing-1'},
]

curr_risk_header = "Толерантность к риску: "
# presets_risk = [
#     {'label': "Low", 'value': 0.01},
#     {'label': "Medium", 'value': 0.1},
#     {'label': "High", 'value': 1},
# ]
risk_tol_marks = {
    # 0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Более безопасно', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Не безопасно'}
}

risk_tolerance_text = "Risk Tolerance: "
risk_tol_desc = html.Div('''More vulnerable populations such as the elderly or those with preexisting medical 
conditions require a lower risk tolerance (~0.01). A higher risk tolerance will mean more expected 
transmissions during the expected occupancy period (see FAQ for details).''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})

curr_age_header = "Возрастная группа: "
presets_age = [
    {'label': "Дети (<15 лет)", 'value': 0.23},
    {'label': "Взрослые (15-64 лет)", 'value': 0.68},
    {'label': "Пожилые (> 64 лет)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: Дети (<15 лет)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: Взрослые (15-64 лет)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: Пожилые (> 64 лет)', 'style': {'width': '75px'}}
}
lang_break_age = html.Br()

curr_strain_header = "Вирусный штамм: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2 (Ухань Штамм)", 'value': 1},
    {'label': "SARS-CoV-2 - B.1.1.7 (UK штамм)", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: Ухань', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: B.1.1.7/UK'}
}

pim_header = "Процент иммунитета: "
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "Если заходит инфицированный человек…"
risk_prevalence_desc = "Учитывая распространенность инфекции…"
risk_personal_desc = "Чтобы ограничить мой личный риск…"
risk_options = [
    {'label': risk_conditional_desc, 'value': 'conditional'},
    {'label': risk_prevalence_desc, 'value': 'prevalence'},
    {'label': risk_personal_desc, 'value': 'personal'},
]
risk_personal_warning = html.Span([
    html.Span('''Предупреждение: ''', style={'font-weight': 'bold'}),
    html.Span('''выбранный режим риска (Чтобы ограничить мой личный риск ...) учитывает вероятность заражения 
    конкретного человека. Таким образом, он носит гораздо менее строгий характер и не должен использоваться для 
    установления руководящих принципов общественной безопасности.''')])

risk_mode_panel_header = "Режим риска"
occupancy_panel_header = "Рассчитать безопасное размещение"
main_panel_s1 = '''Чтобы ограничить передачу COVID-19* после того, как инфицированный человек войдет в это 
пространство, должно быть не более: '''

main_panel_s1_b = html.Span([
    html.Span('''Чтобы ограничить передачу COVID-19 среди населения с распространенностью инфекции'''),
    html.Sup('''1'''),
    html.Span(''' ''')
])
main_panel_s2_b = ''' на 100000, в этом помещении должно быть не более: '''

main_panel_s1_c = html.Span([
    html.Span('''Чтобы ограничить мой личный риск заразится COVID-19 среди населения с распространенностью инфекции'''),
    html.Sup('''1'''),
    html.Span(''' ''')
])
main_panel_s2_c = ''' на 100000, в этом помещении должно быть не более: '''

units_hr = 'часов'
units_min = 'минут'
units_days = 'дней'
units_months = 'mесяцы'

units_hr_one = 'час'
units_min_one = 'минуты'
units_day_one = 'день'
units_month_one = 'месяц'

is_past_recovery_base_string = '{n_val} человека на >{val:.0f} days,'
model_output_base_string = '{n_val} человека на '
model_output_base_string_co2 = '{co2:.2f} ppm for '
nt_bridge_string = " человека на "
tn_bridge_string = " на "

main_panel_six_ft_1 = "Напротив, указание о расстоянии шести футов (или двух метров) ограничит вместимость до "
main_panel_six_ft_2 = ", что нарушит указание* через "

six_ft_base_string = ' {} человек'
six_ft_base_string_one = ' {} person'

graph_title = "Вместимость в зависимости от времени контакта"
graph_xtitle = "Максимальное время контакта \u03C4 (часы)"
graph_ytitle = "Максимальная вместимость N"
transient_text = "Переходное состояние"
steady_state_text = "Устойчивое состояние"
co2_safe_trace_text = "Предел респираторной безопасности"
guideline_trace_text = "Руководство"
background_co2_text = "CO₂ в окружности: "
recommended_co2_text = "Рекомендуемый предел"

graph_title_co2 = "Безопасная концентрация CO₂ (ппм) в зависимости от времени воздействия"
graph_ytitle_co2 = "Концентрация CO₂ (ппм)"

co2_title = "Расчёт безопасной концентрации CO₂"
co2_param_desc = '''Ориентировочные значения выбранных выше параметров выражены здесь в терминах предельной 
концентрации CO₂. '''
co2_prev_input_1 = html.Span(["Распространенность", html.Sup('1'), html.Span(": ")])
co2_prev_input_2 = " на 100,000"
co2_atm_input_1 = background_co2_text
co2_atm_input_2 = " ппм"
co2_calc_1 = "Для времени воздействия "
co2_calc_2 = " часов, расчетная безопасная стационарная концентрация CO₂ в этом пространстве составляет "
co2_calc_3 = "."
co2_base_string = '{:,.2f} ппм'

co2_safe_sent_1 = "This limit exceeds that for healthy respiratory activity, which is "
co2_safe_sent_2 = "."

co2_safe_footer = html.Span(['''Предел респираторной безопасности интерполируется на основе рекомендуемых пределов 
Министерства сельского хозяйства ''',
                             html.A(href=links.link_usda_co2,
                                    children='''США''',
                                    target='_blank'),
                             '''.'''])

main_airb_trans_only_disc = html.Div(["*Руководство ограничивает вероятность ",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="передачи инфекции воздушно-капельным путем",
                                                       target='_blank'), ),
                                      html.Span(''' от одного инфицированного человека до уровня ниже допустимого 
                                      уровня риска в течение указанного совокупного 
                                      времени воздействия.''')], className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*Руководство ограничивает вероятность ",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="передачи инфекции воздушно-капельным путем",
                                                       target='_blank'), ),
                                      html.Span(''' от одного инфицированного человека до уровня ниже допустимого 
                                      уровня риска (10%) в течение указанного совокупного 
                                      времени воздействия.''')], className='airborne-text')

other_risk_modes_desc = html.Div('''Другие сценарии риска рассматриваются в продвинутом режиме. В частности, 
можно учитывать распространенность инфекции среди населения, иммунитет, приобретенный в результате вакцинации или 
предыдущего контакта, а также риск для конкретного человека.''')

main_airb_trans_only_desc_b = html.Div(["*Руководство ограничивает вероятность одной ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="передачи воздушно-капельным путем",
                                                         target='_blank'), ),
                                        html.Span(''' от одного инфицированного человека до уровня ниже допустимого уровня риска в течение указанного совокупного времени воздействия.''')], className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["*Руководство ограничивает вероятность ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="передачи вируса воздушно-капельным путем",
                                                         target='_blank'), ),
                                        html.Span(''' конкретному человеку до уровня ниже допустимого уровня риска в течение указанного совокупного времени воздействия.''')], className='airborne-text')

airb_trans_only_disc = html.Div('''''', className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''Чтобы оценить вашу локальную распространенность, вот несколько полезных 
                                ресурсов: '''),
                                # html.Span(html.A(href=links.link_jhu_dashboard,
                                #                  children="JHU COVID-19 Dashboard",
                                #                  target='_blank')),
                                # html.Span(''', '''),
                                html.Span(html.A(href=links.link_cdc_dashboard,
                                                 children="CDC COVID-19 Трекер данных",
                                                 target='_blank')),
                                html.Span(", "),
                                html.Span(html.A(href=links.link_jhu_data,
                                                 children="JHU Ресурсный центр по коронавирусу",
                                                 target='_blank')),
                                html.Span(", "),
                                html.A(children="US Оценка иммунитета",
                                       href=links.link_cdc_immunity,
                                       target='_blank'),
                                html.Span(", "),
                                html.A(children="Международные оценки иммунитета",
                                       href=links.link_jhu_vaccine,
                                       target='_blank'),
                                ], className='airborne-text')

# Bottom panels text
n_input_text_1 = "Если в этой комнате "
n_max_base_string = ' {:.0f} человек'
n_max_overflow_base_string = ' >{:.0f} человек'
n_input_text_2 = " человек, ее обитатели должны быть в безопасности в течение "
n_input_text_3 = "."

t_input_text_1 = "Если люди проводят здесь примерно "
t_input_text_2 = " часов, вместимость следует ограничить до "
t_input_text_3 = "."

# About
about_header = "О приложении"
about = html.Div([
    html.H6("О приложении", style={'margin': '0'}),
    html.Div('''Чтобы уменьшить распространение COVID-19, официальные руководящие принципы общественного 
    здравоохранения рекомендуют ограничения на: расстояние между людьми (2 метра), время пребывания (15 минут), 
    максимальную вместимость (25 человек) или минимальную вентиляцию ( 6 воздухообменов в час).'''),
    html.Br(),
    html.Div([html.Span(''''''),
              html.A(children="Появляется все больше",
                     href=links.link_docs,
                     target='_blank'),
              html.Span(''' научных доказательств передачи COVID-19 воздушным путем, когда происходит обмен каплями инфекционного аэрозоля при вдыхании общего воздуха в помещении. Хотя организации общественного здравоохранения начинают признавать передачу вируса воздушно-капельным путем, они еще не разработали рекомендации по безопасности, включающие все соответствующие переменные. ''')]),
    html.Br(),
    html.Div([html.Span('''Эта приложение, разработанная Касим Ханам в сотрудничестве с Мартином З. Базантом и Джоном В. М. Бушем, использует '''),
              html.A(children="теоретическую модель",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' для расчета безопасного времени воздействия и уровней вместимости для внутренних помещений. Регулируя характеристики помещения, скорость вентиляции и фильтрации, использование лицевой маски, респираторную активность и устойчивость к риску (на других вкладках), вы можете увидеть как уменьшить передачу COVID-19 внутри различных помещениях. ''')]),
    html.Br(),
    html.Div(['''В базовом режиме вы можете рассчитать пределы безопасной занятости после входа одного 
    инфицированного человека в помещение. В расширенном режиме вы можете учитывать дополнительные факторы, 
    включая распространенность инфекции и иммунитет населения. Расширенный режим также позволяет оценить безопасную 
    занятость на основе средней концентрации CO2, которая связана с концентрацией инфекционных аэрозолей.''']),
    html.Br(),
    html.Div([html.Span('''Наука, лежащая в основе приложения, также преподается в бесплатном массовом открытом 
    онлайн-курсе (MOOC) для самостоятельного изучения на edX: '''),
              html.A(children="10.S95x Physics of COVID-19 Transmission",
                     href=links.link_mooc,
                     target='_blank')]),
])

# Room Specifications
room_header = "Характеристики помещения - Подробности"

floor_area_text = "Площадь помещения (sq. ft.): "
floor_area_text_metric = "Площадь помещения (m²): "
ceiling_height_text = "Средняя высота потолка (ft.): "
ceiling_height_text_metric = "Средняя высота потолка (m): "

ventilation_text = "Вентиляционная: "
vent_type_output_base = "{:.1f} "
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (ACH)"])
ventilation_text_adv = html.Span(["Вентиляционная (hr", html.Sup("-1"), ", ACH): "])
ventilation_types = [
    {'label': "Закрытые окна", 'value': 0.3},
    {'label': "Открытые окна", 'value': 2},
    {'label': "Механическая вентиляция", 'value': 3},
    {'label': "Открытые окна с вентиляторами", 'value': 6},
    {'label': "Лучшая механическая вентиляция", 'value': 8},
    {'label': "Лаборатория, Ресторан", 'value': 9},
    {'label': "Бар", 'value': 15},
    {'label': "Больница/Вагон метро", 'value': 18},
    {'label': "Токсическая лаборатория/Самолет", 'value': 24},
]

filtration_text = "Система фильтрации: "
filt_type_output_base = "MERV{:.0f}"
filtration_text_adv = "Система фильтрации (MERV): "
filter_types = [
    {'label': "Нету", 'value': 0},
    {'label': "Оконный кондиционер", 'value': 2},
    {'label': "Жилой / Коммерческий / Промышленный", 'value': 6},
    {'label': "Жилой / Коммерческий / Больница", 'value': 10},
    {'label': "Больница и общая хирургия", 'value': 14},
    {'label': "HEPA (высокоэффективное удержание частиц)", 'value': 17}
]

recirc_text = "Скорость рециркуляции: "
recirc_type_output_base = "{:.1f} "
recirc_type_output_units = html.Span(["hr", html.Sup("-1")])
recirc_text_adv = html.Span(["Скорость рециркуляции (hr", html.Sup("-1"), "): "])
recirc_types = [
    {'label': "Нету", 'value': 0},
    {'label': "Медленный", 'value': 0.3},
    {'label': "Умеренный", 'value': 1},
    {'label': "Быстрый", 'value': 10},
    {'label': "Самолет", 'value': 24},
    {'label': "Вагон метро", 'value': 54},
]

humidity_text = "Относительная влажность: "
humidity_marks = {
    0.01: {'label': '1%: Очень сухо', 'style': {'max-width': '25px'}},
    # 0.2: {'label': '20%: Самолет', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Сухо'},
    0.6: {'label': '60%: Средняя'},
    0.99: {'label': '99%: Очень влажно'},
}

need_more_ctrl_text = '''Хотите больше контроля над вашими данными? Переключитесь в продвинутый режим с помощью 
раскрывающегося списка вверху страницы. '''

human_header = "Человеческое поведение - Подробности"
# Human Behavior
exertion_text = "Частота дыхания: "
exertion_types = [
    {'label': "Отдых", 'value': 0.49},
    {'label': "Стояние", 'value': 0.54},
    {'label': "Пение", 'value': 1},
    {'label': "Лёгкая нагрузка", 'value': 1.38},
    {'label': "Средняя нагрузка", 'value': 2.35},
    {'label': "Тяжелея нагрузка", 'value': 3.30},
]

breathing_text = "Дыхательная активность: "
expiratory_types = [
    {'label': "Легкое дыхание", 'value': 1.1},
    {'label': "Средние дыхание", 'value': 4.2},
    {'label': "Тяжелее дыхание", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Говорить (шепотом)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Говорить (не громко)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Говорить (громко)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Пение", 'value': 970},
]

mask_type_text = "Эффективность фильтрации маски (тип маски): "
mask_type_marks = {
    0: {'label': "0% (Защитная маска, Нету)", 'style': {'max-width': '75px'}},
    0.5: {'label': "50% (Хлопок, фланель)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (Хлопок, Шелк)", 'style': {'max-width': '75px'}},
    0.90: {'label': "90% (Хирургическая)", 'style': {'max-width': '75px'}},
    # 0.99: {'label': "99% (N95 resp-irator)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Защитная маска, Нету", 'value': 0},
    {'label': "Хлопок, фланель", 'value': 0.5},
    {'label': "Хлопок, Шелк", 'value': 0.7},
    {'label': "Хирургическая", 'value': 0.9},
    {'label': "N95 Респиратор", 'value': 0.99},
]

mask_fit_text = "Подходимость маски: "
mask_fit_marks = {
    0: {'label': '0%: Нету', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Плохая'},
    0.95: {'label': '95%: Средняя'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Часто задаваемые вопросы"
other_io = "Прочие параметры"

faq_top = html.Div([
    html.H6("Часто задаваемые вопросы"),
    html.H5("Почему недостаточно расстояния двух метров ?"),
    html.Div([
        html.Div([html.Span('''Двух метровое расстояние защищает вас от больших капель выбрасываемых инфицированным человеком при кашле, так же как и маски для лица; однако оно не защищает от '''),
                  html.A(children="передачи по воздуху",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' инфекционных аэрозолей, которые смешиваются с воздухом в помещений. В закрытом помещении люди не более защищены от передачи по воздуху на расстояние двух метров, чем на расстояние двадцати метров.  ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Есть ли другие способы передачи?"),
    html.Div([
        html.Div([html.Span('''Считается, что '''),
            html.A(children="воздушно-капельная передача",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' COVID-19 является основной, но возможны и другие способы, такие как передача "фомита" при прямом контакте с инфекционными остатками на поверхностях, "крупнокапельная" передача при кашле или чихании и "аэрозоль ближнего действия" передача из дыхательной струи инфицированного человека в течение длительного периода. В то время как последние два режима значительно устраняются при ношении лицевых масок или щитов, риск передачи воздушно-капельным путем сохраняется. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Можем ли мы действительно предположить что воздух в комнате хорошо перемешан?"),
    html.Div([
        html.Div([html.Span('''Есть много факторов, способствующих перемешиванию в помещениях, включая потоки вызываемые плавучестью (от обогревателей, кондиционеров или окон), принудительную конвекцию от вентиляционных отверстий и вентиляторов, а также движение и дыхание человека. Хотя есть исключения, как обсуждается в '''),
                  html.A(children="статье",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''', предположение о хорошей смешанности широко используется при теоретическом моделировании передачи болезней передающихся воздушным путем.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Остаётся ли в силе рекомендация, в случае очень просторных помещений?"),
    html.Div([
        html.Div([html.Span('''В концертных залах, стадионах или других больших вентилируемых помещениях с большим количеством людей, риск передачи воздушно-капельным путем является значительным и должным образом отражен в руководстве. Так же, когда защитные маски не используются, существует дополнительный риск передачи на коротких расстояниях через респираторные потоки, как обсуждается в '''),
                  html.A(children="статье",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Какое значение имеет высота потолка?"),
    html.Div([
        '''Высота потолка влияет на общий объем помещения, требуемый для оценки концентрации инфекционных аэрозолей (
        количество аэрозолей на единицу объема). Эта концентрация необходима для оценки риска передачи COVID-19 в 
        помещении. '''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Я знаю свои номера ACH / MERV. Где я могу ввести их?"),
    html.Div('''
        Если вам нужен дополнительный контроль над вводом, переключитесь в продвинутый режим, используя раскрывающийся 
        список в верхней части веб-страницы.
    ''', className='faq-answer'),
    html.Br(),
    html.H5("Почему респираторы N95 имеют эффективность 99%?"),
    html.Div('''Респираторы N95 имеют эффективность фильтрации не менее 95% при размере частиц 0,3 мкм, что в 10 раз 
    меньше чем размер капель при переносе COVID-19 по воздуху. Для более крупных капель респираторы N95 еще более 
    эффективны, приближаясь к уровням близким к 100%.''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Есть ли какие-либо скрытые параметры в базовом режиме?"),
    html.Div([html.Span('''Все соответствующие физические параметры подробно описаны в '''),
              html.A(children="статье",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''. В базовом режиме приложение предполагает что эффективный радиус аэрозоля равен по умолчанию двум микроном (при влажности 60%) и что максимальная скорость деактивации вирусов равна 0.6 / час (при влажности ~ 100%), оба значения увеличиваются с относительной влажностью. Оценки скорости деактивации вирусов консервативно предпологают более медленную деактивацию. Скорость деактивации вирусов можно повысить с помощью ультрафиолетового излучения или химических дезинфицирующих средств. 
              Приложение также оценивает ключевой параметр заболевания, инфекционность выдыхаемого воздуха, C'''),
              html.Sub("q"),
              html.Span(''' (количество инфекций на единицу объема), исходя из заданной респираторной активности, используя табличные значения на Рисунке 2 в '''),
              html.A(children="статье",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''. Вы сами определяете эти параметры в расширенном режиме.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Эффективный радиус аэрозоля (Когда относительная влажность = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Максимальная скорость деактивации вирусов (Когда относительная влажность = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

pop_immunity_header = "Иммунитет населения: "
perc_immune_label = html.Span(["Процент иммунитета p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["Процент инфекционных p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["Percentage vaccinated p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["Percentage previously infected p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["Процент восприимчивых p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''Инфекционный процент p''', html.Sub('i'), '''среди населения 
рассчитывается на основе инфекционной распространенности введенной на вкладках других сценариев риска (Учитывая 
распространенность инфекции…, Чтобы ограничить мой личный риск…). Процент иммунитета p''', html.Sub('im'),
                                        '''можно консервативно оценить исходя из процента вакцинации населения плюс 
общий уровень заболеваемости среди населения, пренебрегая вкладом невыявленных случаев. Эти два значения используются 
для расчета процента восприимчивых p''', html.Sub('s'), '''. В базовом режиме и в режиме первого риска (если 
зараженный человек входит…) это значение принимается равным 100%.''']),
                              html.Br(),
                              html.Div(['''Вот несколько полезных ссылок для поиска p''', html.Sub('i'), ''' и p''',
                                        html.Sub('im'), ''': ''',
                                        html.Span(html.A(href=links.link_cdc_dashboard,
                                                         children="CDC COVID-19 Трекер данных",
                                                         target='_blank')),
                                        html.Span(", "),
                                        html.Span(html.A(href=links.link_jhu_data,
                                                         children="JHU Ресурсный центр по коронавирусу",
                                                         target='_blank')),
                                        html.Span(", "),
                                        html.A(children="US Оценка иммунитета",
                                               href=links.link_cdc_immunity,
                                               target='_blank'),
                                        html.Span(", "),
                                        html.A(children="Международные оценки иммунитета",
                                               href=links.link_jhu_vaccine,
                                               target='_blank'),
                                        ])
                              ])

values_interest_header = "Расчёт важных значений: "
values_interest_desc = html.Div([
    html.H5("Что именно рассчитывает приложение?"),
    html.Div([
        html.Div([html.Span('''Учитывая допустимую степень риска воздушно-капельной передачи, приложение рассчитывает максимально допустимое совокупное время воздействия, произведение вместительности комнаты и время нахождения в присутствие инфицированного человека. Приложение также вычисляет другие значения определенные в '''),
                  html.A(children="статье",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''', которые могут представлять интерес: ''')]),
    ], className='faq-answer'),
])
relative_sus_label = html.Span(["Relative susceptibility s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["Доля наружного воздуха Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Эффективность фильтрации аэрозолей p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Скорость потока дыхания дыхания Q", html.Sub('b'), ": "])
cq_label = html.Span(["Заразность выдыхаемого воздуха C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Вероятность прохождения маски p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Объем помещения V: "])
vent_rate_Label = html.Span(["Скорость потока вентиляции (наружного воздуха) Q: "])
recirc_rate_label = html.Span(["Скорость обратного (рециркуляционного) потока Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Скорость фильтрации воздуха (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Радиус аэрозоля при данной влажности r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Скорость деактивации вирусов при данной влажности \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Эффективная скорость оседания аэрозоля v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Concentration relaxation rate \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Скорость передачи по воздуху \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Учитывает ли эта модель распространенность инфекции среди местного населения?"),
    html.Div(['''The influence of the prevalence of infection in the local population may be considered in Advanced 
    Mode. There, in the Other Parameters tab, one may also assess the influence of immunity in the population, 
    as may arise through vaccination or previous infection.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("Дополнительные вопросы?"),
    html.Div([html.Span('''Для получения более подробных объяснений и ссылок см. «'''),
              html.A(children="За пределами двух метров",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''» и другие ссылки, размещенные в верхней части веб-страницы.''')]),
])

footer = html.Div([
    html.Div([html.Span('''Руководство по безопасности в помещениях COVID-19 - это постоянно развивающийся 
    инструмент, предназначенный для ознакомления заинтересованного пользователя с факторами влияющими на риск 
    передачи COVID-19 воздушным путем в помещениях, а также для помощи в количественной оценке риска в различных 
    условиях. Отметим, что неопределенность и внутренняя изменчивость параметров модели могут привести к ошибкам до 
    порядка величины, которые можно компенсировать путем выбора достаточно малого допуска к риску. В нашем 
    руководстве не учитывается передача на короткие расстояния через респираторные потоки, что может значительно 
    повысить риск в отсуствие масок, как это описано в '''),
              html.A(children="прилагаемой рукописи",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''(Bazant & Bush, 2020). Пользователь несет исключительную ответственность за соблюдение 
              правил безопасности в помещениях от COVID-19. Он предоставляется без каких-либо гарантий. Авторы не 
              несут ответственности за его использование.''')]),
    html.Br(),
    html.Div("Особая благодарность: ")
], className='footer-small-text')
