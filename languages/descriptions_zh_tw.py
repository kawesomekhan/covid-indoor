from dash import html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions_zh_tw.py: Traditional Chinese

"""

# Header
header = html.Div([
    html.H1(children='COVID-19 (新冠肺炎) 室內安全指南'),
    html.Div([
        html.Div([html.Span(html.A(href="https://www.linkedin.com/in/kasim-k-a92620b1/",
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href=links.link_bush,
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ", 及 ",
                  html.Span(html.A(href=links.link_bazant,
                                   children="Martin Z. Bazant",
                                   target='_blank')),
                  ""]),
        html.Div([html.Span(["Bazant & Bush, 限制新冠肺炎 (COVID-19) 室內空氣傳染指南, "]),
                  html.Span(html.A(href=links.link_paper_pnas,
                                   target='_blank',
                                   children='''PNAS (2021)''')),
                  html.Span(", 六英尺之外, "),
                  html.Span(html.A(href=links.link_paper,
                                   target='_blank',
                                   children='''medRxiv (2020)''')),]),
        html.Div([html.Span(["透過監控二氧化碳量化新冠肺炎 (COVID-19) 室內空氣傳染風險 ("]),
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
language_dd = "語言: "

# Unit systems
units_dd = "單位: "
unit_settings = [
    {'label': "英制", 'value': "british"},
    {'label': "公制", 'value': "metric"},
]

#Modes
mode_dd = "模式: "
app_modes = [
    {'label': "基本", 'value': "basic"},
    {'label': "進階", 'value': "advanced"},
]

output_mode_dd = "結果模式："
output_modes = [
    {'label': "安全人數", 'value': "occupancy"},
    {'label': "安全二氧化碳水平", 'value': "co2"},
]

error_list = {
    "floor_area": "錯誤：地板面積不能是空白。",
    "ceiling_height": "錯誤：天花板高度不能是空白。",
    "recirc_rate": "錯誤：再循環率不能是空白。",
    "aerosol_radius": "錯誤：氣溶膠液滴半徑不能是空白。",
    "viral_deact_rate": "錯誤：病毒失活速率不能是空白。",
    "n_max_input": "錯誤：人數不能少於2。",
    "exp_time_input": "錯誤：暴露時間必須大於0。",
    "air_exchange_rate": "錯誤：通風率（ACH）必須大於0。",
    "merv": "錯誤：過濾系統（MERV）不能是空白。",
    "prevalence": "錯誤：感染率 (每十萬人的感染人數) 必須大於利且小於 100,000。",
    "atm_co2": "錯誤：背景二氧化碳水平為必填。",
    "co2_input": "錯誤：二氧化碳水平為必填。"
}


# Main Panel Text
curr_room_header = "所在房間："
presets = [
    {'label': "自定", 'value': 'custom'},
    {'label': "郊區房屋", 'value': 'house'},
    {'label': "餐館", 'value': 'restaurant'},
    {'label': "安靜的辦公室", 'value': 'office'},
    {'label': "教室", 'value': 'classroom'},
    {'label': "捷運/地鐵", 'value': 'subway'},
    {'label': "飛機", 'value': 'airplane'},
    {'label': "教堂", 'value': 'church'},
]

curr_human_header = "人的行為："
presets_human = [
    {'label': "自定義", 'value': 'custom'},
    {'label': "戴口罩休息", 'value': 'masks-1'},
    {'label': "戴口罩講話", 'value': 'masks-2'},
    {'label': "戴口罩運動", 'value': 'masks-3'},
    {'label': "不戴口罩休息", 'value': 'no-masks-1'},
    {'label': "不戴口罩講話", 'value': 'no-masks-2'},
    {'label': "不戴口罩運動", 'value': 'no-masks-3'},
    {'label': "不戴口罩唱歌", 'value': 'singing-1'},
]

curr_risk_header = "風險承受能力："
# presets_risk = [
#     {'label': "Low", 'value': 0.01},
#     {'label': "Medium", 'value': 0.1},
#     {'label': "High", 'value': 1},
# ]
risk_tol_marks = {
    # 0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: 更安全', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: 不安全'}
}

risk_tolerance_text = "風險承受度："
risk_tol_desc = html.Div('''對於老年人等較脆弱的人群或已經有生病的族群，需要設置較低的風險承受度 (~0.01)。設置較高的風險承
受度，意味著在既定時間內預期會被傳播傳染更多（有關詳細信息，請參閱常見問題解答&解答）。''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})


curr_age_header = "年齡階層："
presets_age = [
    {'label': "兒童（<15歲）", 'value': 0.23},
    {'label': "成人（15-64歲）", 'value': 0.68},
    {'label': "老年人（> 64歲）", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: 兒童（<15歲）', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: 成人（15-64歲）', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: 老年人（> 64歲）', 'style': {'width': '75px'}}
}

curr_strain_header = "病毒株: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2（武漢毒株）", 'value': 1},
    {'label': "SARS-CoV-2 - B.1.1.7（英國毒株）", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: 武漢', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: B.1.1.7 /英國'}
}

pim_header = "免疫率: "
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "如果感染者進入…"
risk_prevalence_desc = "在既定的感染率下..."
risk_personal_desc = "為了減少我個人風險…"
risk_options = [
    {'label': risk_conditional_desc, 'value': 'conditional'},
    {'label': risk_prevalence_desc, 'value': 'prevalence'},
    {'label': risk_personal_desc, 'value': 'personal'},
]
risk_personal_warning = html.Span([
    html.Span('''警告: ''', style={'font-weight': 'bold'}),
    html.Span('''選擇的風險模式 (為了減少我個人風險…) 是以個人被傳染的機率做計算，因此結果較為寬鬆，不應該被用來當作社區安全指導方針。''')])



risk_mode_panel_header = "風險模式"
occupancy_panel_header = "計算安全人數限制"
main_panel_s1 = "為減低當一位感染者進入這個房間的新冠肺炎空氣傳染機率(*)，該空間不得有超過："


main_panel_s1_b = html.Span([
    html.Span('''為了控制新冠肺炎在感染率 1 為每 100,000 中'''),
    html.Sup('''1'''),
    html.Span(''' ''')
])
main_panel_s2_b = ''' 人的人群中的傳播*，該空間不得有超過：'''

main_panel_s1_c = html.Span([
    html.Span('''為了降低我在感染率為每 100,000 中'''),
    html.Sup('''1'''),
    html.Span(''' ''')
])
main_panel_s2_c = ''' 人的人群中感染COVID-19的可能性，此空間不得有超過：'''

units_hr = '小時'
units_min = '分鐘'
units_days = '天'
units_months = '月'

units_hr_one = '小時'
units_min_one = '分鐘'
units_day_one = '天'
units_month_one = '月'

is_past_recovery_base_string = '{n_val} 人，>{val:.0f} 天'
model_output_base_string = '{n_val} 人，'
model_output_base_string_co2 = '{co2:.2f} ppm for '
nt_bridge_string = " 人， "
tn_bridge_string = " "

main_panel_six_ft_1 = "對照之下，六英尺（或兩米）距離的指導方針會將使用人數限制在 "
main_panel_six_ft_2 = " 這會在 "
main_panel_six_ft_3 = " 之後違反本指南*"
six_ft_base_string = ' {} 個人'
six_ft_base_string_one = ' {} 個人'

graph_title = "容納人數 vs. 暴露時間"
graph_xtitle = "最大暴露時間 \u03C4 (小時)"
graph_ytitle = "最大容納人數 N"
transient_text = "短暫"
steady_state_text = "恆定"
co2_safe_trace_text = "呼吸安全臨界值"
guideline_trace_text = "指南"
background_co2_text = "背景二氧化碳: "
recommended_co2_text = "建議限制"

graph_title_co2 = "安全二氧化碳濃度 (ppm) vs. 暴露時間"
graph_ytitle_co2 = "二氧化碳濃度 (ppm)"

co2_title = "計算安全二氧化碳濃度"
co2_param_desc = '''這裡是根據以上所選的參數所計算出來的二氧化碳濃度臨界值。'''

co2_prev_input_1 = html.Span(["感然率", html.Sup('1'), html.Span(": ")])
co2_prev_input_2 = " 每 100,000"
co2_atm_input_1 = background_co2_text
co2_atm_input_2 = " ppm"
co2_calc_1 = "為了暴露 "
co2_calc_2 = " 小時, 計算出的平均二氧化碳濃度在此空間為 "
co2_calc_3 = "。"
co2_calc_inv_1 = "為了二氧化碳濃度"
co2_calc_inv_2 = " ppm*, 會在 "
co2_calc_inv_3 = " 後違反本指南。"
co2_base_string = '{:,.2f} ppm'

co2_safe_sent_1 = "This limit exceeds that for healthy respiratory activity, which is "
co2_safe_sent_2 = "."

# co2_safe_footer = html.Span(['''The respiratory safety threshold is interpolated based on ''',
#                              html.A(href=links.link_usda_co2,
#                                     children='''recommended limits from the USDA''',
#                                     target='_blank'),
#                              '''.'''])
co2_safe_footer = html.Span([html.Div('''CO\u2082 outputs are limited to a maximum of 2,000 ppm, the level
considered safe for long-term exposure to carbon dioxide.'''),
                             html.Div([
                                        html.A(href=links.link_usda_co2,
                                               children='''USDA Respiratory Limits''',
                                               target='_blank'),
                                        html.Span([''', ''']),
                                        html.A(href=links.link_kane_co2,
                                               children='''Kane International Limits''',
                                               target='_blank'),
                                        html.Span(['''.'''])
                             ]),
                             html.Div([html.A(href=links.link_jimenez_co2,
                                               children='''*700 ppm is the conservative limit recommended by J. L.
                                               Jimenez for COVID-19 safety.''',
                                               target='_blank')])
                             ])


main_airb_trans_only_disc = html.Div(["本指南將累計暴露時間內每個感染者通過空氣傳播感染他人的可能性限制在風險承受能力之下。",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="",
                                                       target='_blank'), ),
                                      html.Span("")], className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*本指南將累計暴露時間內每個感染者 ",
                                            html.Span(html.A(href=links.link_docs,
                                                             children="通過空氣傳染他人",
                                                             target='_blank'), ),
                                            html.Span(''' 的可能性限制在風險承受能力（10%）之下。''')], className='airborne-text')




other_risk_modes_desc = html.Div('''「進階模式」考慮了其他風險情景。具體來說，可以考慮人群中的感染率，通過疫苗接種或先前接觸獲得的免疫率，以及對特定個體的風險。''')



main_airb_trans_only_desc_b = html.Div(["本指南將將累計暴露時間內每個感染者透過空氣傳染他人的可能性限制在風險承受能力之下。",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="",
                                                         target='_blank'), ),
                                        html.Span('''''')], className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["本指南將累積暴露時間內特定個體通過空中傳播被感染的可能性限制在風險承受能力以下。",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="",
                                                         target='_blank'), ),
                                        html.Span('''''')], className='airborne-text')





airb_trans_only_disc = html.Div('''僅考慮空氣傳播傳染。''', className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''為了估算您的當地感染率，這裡有一些有用的資源：'''),

                                # html.Span(html.A(href=links.link_jhu_dashboard,
                                #                  children="JHU COVID-19 Dashboard",
                                #                  target='_blank')),
                                # html.Span(''', '''),
                                html.Span(html.A(href=links.link_cdc_dashboard,
                                                 children="美國疾控中心公布的新冠肺炎數據跟蹤系統",
                                                 target='_blank')),
                                html.Span(", "),
                                html.Span(html.A(href=links.link_jhu_data,
                                                 children="約翰霍普金斯大學的冠狀病毒資源中心",
                                                 target='_blank')),
                                html.Span(", "),
                                html.A(children="美國免疫預測分析",
                                       href=links.link_cdc_immunity,
                                       target='_blank'),
                                html.Span(", "),
                                html.A(children="國際免疫預測分析",
                                       href=links.link_jhu_vaccine,
                                       target='_blank'),
                                ], className='airborne-text')

# Bottom panels text
n_input_text_1 = "如果該房間有 "
n_max_base_string = ' {:.0f} 人'
n_max_overflow_base_string = ' >{:.0f} 人'
n_input_text_2 = " 人，根據本指南則不可逗留超過 "
n_input_text_3 = "小時。"

t_input_text_1 = "如果人們在這裡停留約 "
t_input_text_2 = " 個小時，則人數應限制為"
t_input_text_3 = "人。"

# About
about_header = "關於"
about = html.Div([
    html.H6("關於", style={'margin': '0'}),
    html.Div('''為抑制新冠肺炎的傳播，官方公共衛生指南建議限制以下因素：人與人之間的距離（6 英尺/ 2 米），房間占用時間（15 分鐘），房間內最大人數
                （25 人）或最小通風量（每小時換氣 6 次）。'''),


    html.Br(),
    html.Div([html.Span('''越來越多的 '''),
              html.A(children="科學證據",
                     href=links.link_docs,
                     target='_blank'),
              html.Span('''表明，人們在室內可以通過呼吸而吸入有傳染性的氣溶膠，從而導致新冠肺炎可以通過空氣傳播。
                           盡管公共衛生組織開始認識到空氣傳播的重要性，但他們尚未提供包含所有相關變量的安全指南。''')]),


    html.Br(),
    html.Div([html.Span('''本應用程序是由 Kasim Khan 與 Martin Z. Bazant，John W. M. Bush 合作開发，用'''),
              html.A(children="理論模型",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''來計算室內空間的安全暴露時間和可容納人數。通過調整房間規格，通風率和過濾率，使用口罩情況，呼吸活動和風險承受能力
                           （在其他選項卡中），您可以了解如何減輕室內新冠肺炎傳播。''')]),



    html.Br(),
    html.Div(['''In Basic mode, you can calculate the limits on safe occupancy following the entrance of a single
    infected person into an indoor space. In Advanced Mode, you can take into account additional factors,
    including infection prevalence and population immunity. Advanced Mode also allows you to assess safe occupancy
    based on average CO2 concentration, which is related to the concentration of infectious aerosols.''']),
    html.Br(),
    html.Div([html.Span('''The science behind the app is also taught in a free, self-paced massive, open online
course (MOOC) on edX: '''),
              html.A(children="10.S95x Physics of COVID-19 Transmission",
                     href=links.link_mooc,
                     target='_blank')]),
])

# Room Specifications
room_header = "房間規格 - 細節"

floor_area_text = "總地板面積（平方英尺）: "
floor_area_text_metric = "總地板面積 (平方米): "
ceiling_height_text = "平均天花板高度（英尺）："
ceiling_height_text_metric = "平均天花板高度 (米)): "

ventilation_text = "通風系統: "
vent_type_output_base = "{:.1f} ACH"
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (戶外 ACH)"])
ventilation_text_adv = html.Span(["通風系統 (hr", html.Sup("-1"), ", 戶外 ACH): "])
ventilation_types = [
    {'label': "關閉窗戶", 'value': 0.3},
    {'label': "打開窗戶", 'value': 2},
    {'label': "空調", 'value': 3},
    {'label': "打開窗戶搭配風扇", 'value': 6},
    {'label': "高級空調", 'value': 8},
    {'label': "實驗室，餐廳", 'value': 9},
    {'label': "酒吧", 'value': 15},
    {'label': "醫院/地鐵車廂", 'value': 18},
    {'label': "毒物實驗室/飛機上", 'value': 24},
]

filtration_text = "空氣過濾系統: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "空氣過濾系統 (MERV): "
filter_types = [
    {'label': "無", 'value': 0},
    {'label': "家用窗型冷氣", 'value': 2},
    {'label': "住宅/商業/工業空調", 'value': 6},
    {'label': "住宅/商業/醫院空調", 'value': 10},
    {'label': "醫院與外科病房", 'value': 14},
    {'label': "高效濾網 (HEPA)", 'value': 17}
]

recirc_text = "循環率: "
recirc_type_output_base = "{:.1f} 再循環換氣率"
recirc_type_output_units = html.Span(["hr", html.Sup("-1")])
recirc_text_adv = html.Span(["循環率 (hr", html.Sup("-1"), "): "])
recirc_types = [
    {'label': "無", 'value': 0},
    {'label': "慢", 'value': 0.3},
    {'label': "中等", 'value': 1},
    {'label': "快", 'value': 10},
    {'label': "飛機上", 'value': 24},
    {'label': "捷運/地鐵", 'value': 54},
]

humidity_text = "相對濕度："
humidity_marks = {
    0.01: {'label': '1%: 非常乾燥', 'style': {'max-width': '25px'}},
    # 0.2: {'label': '20%: 飛機機艙', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: 乾燥'},
    0.6: {'label': '60%: 一般'},
    0.99: {'label': '99%: 非常潮濕'},
}

need_more_ctrl_text = '''需要控制更多參數嗎？使用頁面頂部的下拉選單切換到進階模式。'''


human_header = "人類行為 - 細節"
# Human Behavior
exertion_text = "活動量："
exertion_types = [
    {'label': "休息", 'value': 0.49},
    {'label': "站立", 'value': 0.54},
    {'label': "唱歌", 'value': 1},
    {'label': "低強度運動", 'value': 1.38},
    {'label': "中強度運動", 'value': 2.35},
    {'label': "高強度運動", 'value': 3.30},
]

breathing_text = "呼吸活動："
expiratory_types = [
    {'label': "呼吸（輕）", 'value': 1.1},
    {'label': "呼吸（中）", 'value': 4.2},
    {'label': "呼吸（重）", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "說話（耳語）", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "說話（正常）", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "說話（大聲）", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "唱歌", 'value': 970},
]

mask_type_text = "口罩 類型/效率："
mask_type_marks = {
    0: {'label': "0% (無、面罩)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (棉布，粗棉)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (絲質、法蘭絨、薄纱)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (一次性手術口罩)", 'style': {'max-width': '50px'}},
    # 0.99: {'label': "99% (N95 口罩)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "無，面罩", 'value': 0},
    {'label': "棉布，法蘭絨", 'value': 0.5},
    {'label': "多層棉質，絲質", 'value': 0.7},
    {'label': "一次性手術口罩", 'value': 0.9},
    {'label': "N95 呼吸器", 'value': 0.99},
]

mask_fit_text = "面罩貼合度/合規性："
mask_fit_marks = {
    0: {'label': '0%: 無', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: 差'},
    0.95: {'label': '95%: 好'}
}

# FAQ/Other Inputs & Outputs
faq_header = "常見問題&解答"
other_io = "其他參數"

faq_top = html.Div([
    html.H6("常見問題&解答"),
    html.H5("為什麽 6 英尺/2 米的距離不夠？"),
    html.Div([
        html.Div([html.Span('''6 英尺/2 米的距離和口罩都可以防止接觸到感染者咳嗽時噴出的大液滴。
        但是這不能防止懸浮在空氣中並且可以在整個房間中擴散混合的具有傳染性的氣溶膠（懸浮微粒）導致的'''),
                  html.A(children="空氣傳播傳染",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span('''。 在室內，6英尺和60英尺的社交距離沒有太大的差別。''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("還有其他傳染方式嗎？"),
    html.Div([
        html.Div([html.A(children="空氣傳播傳染",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span('''被認為是新冠肺炎的主要傳播途徑，但其他方式也是可能的，例如通過直接接觸表面上的傳染性殘留物進行傳染，
                  通過咳嗽或打噴嚏的「大液滴」傳染以及通過長時間吸入被感染人士呼出氣體的「短距離氣溶膠（懸浮微粒）」傳染。
                  戴上口罩或面罩可以大大降低後兩種傳播模式； 但仍有空氣傳播的風險。''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("真的可以假設房間空氣充分混合嗎？"),
    html.Div([
        html.Div([html.Span('''室內空間空氣混合的原因很多，包括浮力驅動的氣流（來自加熱器，空調或窗戶），通風口和風扇的強制對流，
        以及人體運動和呼吸。 除了一些特殊情況（見這篇'''),
                  html.A(children="論文",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span('''的討論），充分混合的假設廣泛應用於空氣傳播疾病的理論模型。''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("該指南適用於非常大的空間嗎？"),
    html.Div([
        html.Div([html.Span('''在音樂廳，體育館或其他人口眾多的大型通風場所中空氣傳播的風險較高，本指南對此有較好的估計。
                            但是，如果不戴口罩或面罩，則還存在通過呼吸射流進行短距離傳播的風險（見這篇'''),
                  html.A(children="論文",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span('''的估計）。''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("為什麽要知道天花板高度？"),
    html.Div([
        '''天花板高度會影響總房間容積，這是估算傳染性氣溶膠濃度（每單位體積的氣溶膠液滴數量）所必需的。 需要此濃度來估算房間的新冠肺炎傳播風險。'''
    ], className='faq-answer'),
    html.Br(),
    html.H5("我知道我的ACH / MERV號碼。 我在哪里可以輸入？"),
    html.Div('''
        如果您需要輸入更多選項，請使用網頁頂部的下拉菜單切換到高級模式。
    ''', className='faq-answer'),
    html.Br(),
    html.H5("為什麽N95呼吸器具有99％的效率？"),
    html.Div('''N95呼吸器對於0.3μm粒徑的液滴具有至少95%的過濾效率。而新冠病毒空氣傳播中液滴大小大概是3μm。對於較大的液滴，N95呼吸器的過濾效率更高，接近100％的水平。''', className='faq-answer'),
])














faq_other_params_text = html.Div([
    html.H5("基本模式下是否有任何隱藏的參數？"),
    html.Div([html.Span(''''''),
              html.A(children="本文",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''詳細介紹了所有相關的物理參數。 在基礎模式下，該應用假定默認有效氣溶膠液滴半徑為2μm（在濕度為60％時），
              最大病毒失活速率為0.6 / hr（在濕度大約為100％時），兩者均隨相對濕度（RH）的增加而增加。 我們保守地低估病毒失活的速率。
              病毒失活速率可因紫外線（UV-C）或化學消毒劑（例如過氧化氫，臭氧）增大。
              該應用程序用了'''),
              html.Span(''''''),
              html.A(children="該文章",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''圖2中表格的數據以及指定的呼吸活動來估算關鍵參數，例如呼出空氣的傳染性Cq（每單位體積的感染量）。
              您可以在“高級模式”中自行定義這些參數。''')],
             className='faq-answer'),
])




aerosol_radius_text = "有效氣溶膠液滴半徑（在RH = 60％時）， r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["最大病毒失活速率（在RH = 100％時）， \u03BB", html.Sub('vmax'), " (/小時): "])

pop_immunity_header = "人群免疫力: "
perc_immune_label = html.Span(["免疫率 p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["感染率 p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["疫苗接種率 p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["已感染率 p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["易感率 p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''人群的感染性 p''', html.Sub('i'), ''' 是根據在”其他風險情景”選項卡中輸入的感染率計算得出的（在......感染率下，
為了限制我被感染的風險，應當…...）。通過計算人群的疫苗接種率加上人群中總发病率（忽略未发現的病例），可以對免疫率 p''', html.Sub('im'), ''' 做保守估計。用這兩個值可以計算易感率 p''', html.Sub('s'), ''' 在”基本模式”和“首位風險”模式下（如果一個感染者進入…...），該值假定為100％。''']),
                              html.Br(),
                              html.Div(['''以下是一些關於 p''', html.Sub('i'), ''' 和 p''',
                                        html.Sub('im'), ''' 的鏈接：''',
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







values_interest_header = "相關量的計算值"
values_interest_desc = html.Div([
    html.H5("這個應用程式究竟在計算什麽？"),
    html.Div([
        html.Div([html.Span('''本程式會計算室內的最大允許累積暴露時間限制，即房間人數和時間的乘積。 這個限制是這樣得到的：要求每個感染個體的預期傳染人數"室內再生數"）小於所選的風險承受能力。如果感興趣，您可以找到本程式計算相關值 '''),
                  html.A(children="（）",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''': ''')]),
    ], className='faq-answer'),
])



relative_sus_label = html.Span(["相對易感性 s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["室外空氣分數 Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Aerosol filtration efficiency p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Breathing flow rate Q", html.Sub('b'), ": "])
cq_label = html.Span(["Infectiousness of exhaled air C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Mask passage probability p", html.Sub('m'), ": "])
room_vol_label = html.Span(["總房間容積 V: "])
vent_rate_Label = html.Span(["Ventilation (outdoor) flow rate Q: "])
recirc_rate_label = html.Span(["Return (recirculation) flow rate Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["空氣過濾率 (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["濕度修正後氣溶膠半徑 r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["濕度修正後病毒失活速率 \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["有效氣溶膠沈降速度 v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["濃度松弛速率 \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["空氣傳播速率 \u03B2\u2090: "])

graph_output_header = "圖表結果："
faq_graphs_text = html.Div([
    html.H5("圖表結果"),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("該模型是否考慮了當地人口的感染率?"),
    html.Div(['''可以在“高級模式”中考慮當地感染率的影響。在“高級模式”的“其他參數”選項卡中，您還可以評估人群免疫率的影響。
    人群免疫率可能會由於疫苗接種或先前感染而升高。'''],
             className='faq-answer'),
])


assumptions_layout = html.Div([
    html.H5("其他問題?"),
    html.Div([html.Span('''有關更多詳細的說明和參考，請參閱'''),
              html.A(children="這篇文章",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''以及頁面頂部的其他連結。''')]),
])

footer = html.Div([
    html.Div([html.Span('''《MIT新冠肺炎室內安全指南》是一個正在被不斷改進的工具，
    旨在使感興趣的用戶熟悉影響新冠肺炎在室內空氣傳播風險的因素，並幫助用戶在各種情況下定量評估風險。我們注意到，
    該模型參數的不確定性和多變性可能導致高達一個數量級的誤差。這種情況下可以通過選擇足夠小的風險承受度來對模型預測進行修正。
    我們的《指南》並未考慮通過呼吸噴出物的短距離傳播，這可能會在未佩戴口罩的情況下大大提高風險（該方式在'''),
              html.A(children="Bazant＆Bush, 2020",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''手稿中進行了討論）。用戶自身須對使用該《 MIT新冠肺炎室內安全指南》負責。
              開发者不作任何形式的保證或擔保，並對其使用不承擔任何責任。''')]),
    html.Br(),
    html.Div("特別鳴謝")
], className='footer-small-text')
