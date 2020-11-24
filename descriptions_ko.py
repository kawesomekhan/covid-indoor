import dash_html_components as html

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

descriptions: Korean

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

vent_type_output_base = "시간 당 {:.0f} 회 순환"
filt_type_output_base = "MERV {:.0f}"
recirc_type_output_base = "시간 당 {:.1f} 회 공기 재순환"

# Default dropdown options shared between basic mode and advanced mode
humidity_marks = {
    0: {'label': '0%: 매우 건조함', 'style': {'max-width': '50px'}},
    0.2: {'label': '20%: 기내', 'style': {'max-width': '25px'}},
    0.3: {'label': '30%: 건조함', 'style': {'max-width': '25px'}},
    0.6: {'label': '60%: 평균'},
    0.99: {'label': '99%: 매우 습함'},
}

exertion_types = [
    {'label': "휴식", 'value': 0.49},
    {'label': "기립", 'value': 0.54},
    {'label': "가벼운 활동", 'value': 1.38},
    {'label': "일반적 활동", 'value': 2.35},
    {'label': "격한 활동", 'value': 3.30},
]

expiratory_types = [
    {'label': "가벼운 호흡", 'value': 1.1},
    {'label': "평소 호흡", 'value': 4.2},
    {'label': "격한 호흡", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "대화(귓속말)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "대화(일반적)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "대화(크게)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "노래부르기", 'value': 970},
]

mask_type_marks = {
    0: {'label': "0% (없음, 안면 보호막)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (거친 면)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (실크, 플란넬, 시폰)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (수술용 면)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (N95 마스크)", 'style': {'max-width': '50px'}},
}

mask_types = [
    {'label': "없음, 안면 보호막", 'value': 0},
    {'label': "거친 면", 'value': 0.1},
    {'label': "실크, 플란넬, 시폰", 'value': 0.5},
    {'label': "수술용 면", 'value': 0.75},
    {'label': "N95 마스크", 'value': 0.95},
]

mask_fit_marks = {
    0: {'label': '0%: 안함', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: 부족'},
    0.95: {'label': '95%: 준수'}
}

risk_tol_marks = {
    0.01: {'label': '0.01: 매우 안전', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: 안전', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: 불안전'}
}

ventilation_types = [
    {'label': "창문 닫음", 'value': 0.3},
    {'label': "창문 개방", 'value': 2},
    {'label': "장비를 이용한 환기", 'value': 3},
    {'label': "창문 개방 및 환풍기 가동", 'value': 6},
    {'label': "고성능 장비를 이용한 환기", 'value': 8},
    {'label': "실험실, 식당", 'value': 9},
    {'label': "바(술집)", 'value': 15},
    {'label': "병원/지하철 객실", 'value': 18},
    {'label': "유독성 실험실/기내", 'value': 24},
]

filter_types = [
    {'label': "없음", 'value': 0},
    {'label': "가정용 창문형 환풍기", 'value': 2},
    {'label': "가정용/상업용/산업용", 'value': 6},
    {'label': "가정용/상업용/병원용", 'value': 10},
    {'label': "병원용&일반 수술용", 'value': 14},
    {'label': "헤파 필터", 'value': 17}
]

recirc_types = [
    {'label': "없음", 'value': 0},
    {'label': "느림", 'value': 0.3},
    {'label': "보통", 'value': 1},
    {'label': "빠름", 'value': 10},
    {'label': "기내", 'value': 24},
    {'label': "지하철 객실", 'value': 54},
]

n_max_base_string = ' {:.0f} 명'

graph_title = "수용 인원 vs. 노출 시간"
graph_xtitle = "최대 노출 시간 \u03C4 (시간)"
graph_ytitle = "최대 수용 인원 N"
transient_text = "일시적"
steady_state_text = "지속적"

six_ft_base_string = ' {} 명'
six_ft_base_string_one = ' {} 명'

units_hr = '시간 동안 생활'
units_min = '분 동안 생활'
units_days = '일 동안 생활'

units_hr_one = '시간 동안 생활'
units_min_one = '분 동안 생활'
units_day_one = '일 동안 생활'

is_past_recovery_base_string = '{n_val} 명의 인원이 >{val:.0f} 일 동안 생활,'
model_output_base_string = '{n_val} 명의 인원이 '

presets = [
    {'label': "직접 입력", 'value': 'custom'},
    {'label': "교외 주택", 'value': 'house'},
    {'label': "식당", 'value': 'restaurant'},
    {'label': "한산한 사무실", 'value': 'office'},
    {'label': "강의실", 'value': 'classroom'},
    {'label': "뉴욕 시 지하철 열차 칸", 'value': 'subway'},
    {'label': "보잉 737", 'value': 'airplane'},
    {'label': "교회", 'value': 'church'},
]

error_list = {
    "floor_area": "오류: 바닥 면적 란을 비워둘 수 없습니다.",
    "ceiling_height": "오류: 천장 높이 란을 비워둘 수 없습니다.",
    "recirc_rate": "오류: 재순환율 란을 비워둘 수 없습니다.",
    "aerosol_radius": "오류: 에어로졸 반지름 란을 비워둘 수 없습니다.",
    "viral_deact_rate": "오류: 바이러스 비활성화율 란을 비워둘 수 없습니다.",
    "n_max_input": "오류:인원 수는 2 미만일 수 없습니다.",
    "exp_time_input": "오류: 노출 시간은 0 을 초과해야합니다.",
    "air_exchange_rate": "오류: 환기율(시간 당 공기 순환율)은 0을 초과해야 합니다.",
    "merv": "오류: 필터 시스템 (MERV) 란은 비워둘 수 없습니다."
}

# Header
header = html.Div([
    html.H1(children='코로나19 실내 안전 가이드라인'),
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
        html.Div([html.Span(["6 피트 이상 거리두기: 코로나19의 실내 공기 중 전파의 한계에 대한 가이드라인 ("]),
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
language_dd = "언어: "
units_dd = "단위: "
mode_dd = "모드:: "

# Unit systems
unit_settings = [
    {'label': "야드파운드법", 'value': "british"},
    {'label': "미터법", 'value': "metric"},
]

# Modes
app_modes = [
    {'label': "기본", 'value': "basic"},
    {'label': "고급", 'value': "advanced"},
]

# Tabs
about_header = "소개"
room_header = "공간 규격"
human_header = "활동"
faq_header = "FAQ (자주 묻는 질문)"
other_io = "기타 입력 & 결과"

# About
about = html.Div([
    html.H6("소개", style={'margin': '0'}),
    html.Div('''코로나19의 전파 방지를 위한 공식 보건 가이드라인은 다음과 같습니다. 사람 간 거리 두기(6피트 / 2 미터), 기거 시간(15 분), 
    최대 수용 인원(25명), 또는 최소 환기율(시간 당 6회 공기 순환)'''),
    html.Br(),
    html.Div([html.Span('''코로나19의 공기 중 전파는 공유된 실내 공기를 호흡하는 과정에서 감염력을 가진 비말의 교환으로 이뤄진다는 과학적 
    증거가 제시되고 있습니다. 공중 보건 기관들이 공기를 통한 감염이 발생할 수 있음을 인정하기 시작했지만, 이에 대해 모든 관련성 요인들을 
    포함한 가이드라인은 아직 제공하고 있지 않습니다.''')]),
    html.Br(),
    html.Div([html.Span('''Kasim Khan이 Martin Z. Bazant및 John W. M. Bush와 함께 협업하여 개발한 이 앱은 실내 공간의 최대 수용 
    기간과 수용 인원을 계산하는 이론적 모델을 기반으로 만들어졌습니다. 본 앱을 통해, 여러 종류의 실내 공간에서 공간의 규격, 환기율과 여과율, 
    마스크 사용 여부, 호흡기 활동, 위험 감수율(다른 탭에 있습니다.)에 따른 코로나19의 전파를 막을 수 있는 방법을 확인할 수 있습니다.''')])
])

# Room Specifications
floor_area_text = "총 바닥 면적 (제곱 피트): "
floor_area_text_metric = "총 바닥 면적 (m²): "

ceiling_height_text = "평균 천장 높이 (피트): "
ceiling_height_text_metric = "평균 천장 높이 (m): "

ventilation_text = "환기 시스템: "
ventilation_text_adv = "환기 시스템 (시간 당 _ 회 순환): "

filtration_text = "환기 시스템: "
filtration_text_adv = "Filtration System (MERV): "

recirc_text = "재순환율: "
recirc_text_adv = "재순환율 (시간 당 _ 회 공기 재순환): "

humidity_text = "상대 습도: "

need_more_ctrl_text = '''더 다양하게 입력하고 싶나요? 페이지 상단의 메뉴를 통해 고급 모드로 전환하세요.'''

# Human Behavior
exertion_text = "활동 수준: "

breathing_text = "호흡기 활동: "

mask_type_text = "마스크 여과 효율(마스크 소재): "

mask_fit_text = "마스크 착용법 준수: "

risk_tolerance_text = "위험 감수율: "

# FAQ/Other Inputs and Outputs
assumptions_layout = html.Div([
    html.H5("더 궁금한 것이 있나요?"),
    html.Div([html.Span('''더 자세한 설명과 참고 자료를 보려면, "'''),
              html.A(children="“6 피트 이상 거리두기”",
                     href=link_paper,
                     target='_blank'),
              html.Span('''와 웹페이지 상단의 다른 링크를 참고하세요.''')]),
])

faq_top = html.Div([
    html.H6("FAQ (자주 묻는 질문)"),
    html.H5("왜 6 피트/2미터 거리두기가 충분하지 않나요?"),
    html.Div([
        html.Div([html.Span('''6피트/2미터 거리두기는 안면 마스크와 같이 감염자의 기침으로 나오는 큰 비말을 피하기에는 안전합니다. 
                            하지만, 실내 공기를 통해 확산되는 것으로 추정되는 감염성 에어로졸에 의한 '''),
                  html.A(children="공기 중 전파",
                         href=link_docs,
                         target='_blank'),
                  html.Span('''로부터 보호하기에는 충분하지는 않습니다. 실내의 공기 중 전파의 경우 60 피트가 아닌 
                            6피트라면 안전하지 않은 것입니다.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("다른 종류의 전파 경로도 있나요?"),
    html.Div([
        html.Span('''코로나19의 경우 '''),
        html.Div([html.A(children="공기 중 전파",
                         href=link_docs,
                         target='_blank'),
                  html.Span('''가 주된 전파 경로로 추정되고 있으나, 감염 물질이 있는 표면을 통한 ‘비생체 접촉’ 전파, 
                            기침 또는 콧물을 통한 ‘비말’ 전파, 그리고 감염자 호흡에 장시간 노출에 의한 ‘단거리 에어로졸’ 
                            전파 또한 가능합니다. 후자의 두 전파 경로 또한 유의미할 수 있으나, 해당 경로는 마스크 또는 
                            보호막을 통해 상당 부분 예방할 수 있습니다. 하지만, 공기 중 전파의 위험은 여전히 존재합니다.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("진짜로 실내 공기가 잘 혼합되나요?"),
    html.Div([
        html.Div([html.Span('''히터, 에어컨, 창문과 같이 부력에 의해 일어나는 공기의 흐름을 포함해, 환풍구와 환충구와 같은 장치에 의한 
                            대류, 사람의 움직임과 호흡 등 실내 공기가 혼합되는 많은 요인들이 있습니다. 링크된 '''),
                  html.A(children="논문",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''에서 언급된 바와 같이 예외의 경우도 있지만, 공기의 혼합은 공기 중 질병 전파의 이론적 모델링에 널리 
                  적용되는 가정입니다.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("이 가이드라인이 아주 넓은 공간에서도 적용되나요?"),
    html.Div([
        html.Div([html.Span('''콘서트 홀, 경기장 등 크고 환기가 잘 되며 사람이 많은 공간에서는, 공기 중 전파의 위험성이 더욱 강조되며 
                            본 가이드라인이 적합하게 적용될 수 있습니다. 하지만, 링크된 '''),
                  html.A(children="논문",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''에서 언급된 바와 같이, 마스크 또는 안면 보호막을 착용하지 않은 경우 단거리 호흡기 비말 전파의 추가적인 
                  위험성이 있습니다.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("왜 천장 높이가 중요한가요?"),
    html.Div([
        '''천장의 높이는 감염성 에어로졸의 농도(부피 당 에어로졸의 개수)를 추정하기 위해 필요한 공간의 총 부피에 영향을 줍니다. 
        에어로졸의 농도는 코로나19의 전파 위험성을 추정하기 위해 필요한 수치입니다.'''
    ], className='faq-answer'),
    html.Br(),
    html.H5("ACH 혹은 MERV 값을 알고 있는데, 어디에 입력해야 하나요?"),
    html.Div('''
        더 많은 종류의 값을 입력하려면, 웹 페이지 상단의 메뉴를 통해 고급 모드로 전환하세요.
    ''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("기본 모드에 숨겨진 변수가 있나요?"),
    html.Div([html.Span('''모델과 관련된 모든 물리적 변수는 링크된 '''),
              html.A(children="논문",
                     href=link_paper,
                     target='_blank'),
              html.Span('''에 설명되어 있습니다. 기본 모드에서는 에어로졸의 유효반지름이 2um로(습도 60%), 최대 바이러스 비활성화율은 
              0.6/시간으로 (습도~100%) 가정하고 있습니다. 상대 습도가 증가하면 이 수치들은 증가하게 됩니다. 바이러스가 느리게 비활성화될 
              것이라는 가정으로 인해 바이러스 비활성화율에 다소 오차가 발생할 수 있습니다. 바이러스 비활성화율은 자외선(UV-C) 혹은 화학적 
              소독제(예. 과산화수소, 오존)를 이용하여 증가시킬 수 있습니다. 이 앱은 질병의 핵심 변수인 날숨 공기의 감염성 Cq 
              (단위 부피 당 감염 수치)를 링크된 '''),
              html.A(children="논문",
                     href=link_paper,
                     target='_blank'),
              html.Span('''의 그림 2에 작성된 표를 이용하여 호흡기 활동량에 따라 추정할 수 있습니다. 이러한 변수는 고급 모드를 통해 
              직접 입력할 수 있습니다.''')],
             className='faq-answer'),
])
aerosol_radius_text = "유효 에어로졸 반지름 (상대습도=60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["최대 바이러스 비활성화율 (상대습도=100%), \u03BB", html.Sub('vmax'), " (/hr): "])

values_interest_header = "이 앱이 정확히 무엇을 계산하는 건가요?"
values_interest_desc = html.Div([
    html.H5("이 앱이 정확히 무엇을 계산하는 건가요?"),
    html.Div([
        html.Div([html.Span('''이 앱은 제시된 공기 전파의 위험 감수율에 따른 최대 누적 노출 시간을 계산하여, 감염자가 
                            존재할 경우 공간의 수용 인원 및 시간을 계산합니다. 또한 본 앱은 링크된 '''),
                  html.A(children="논문",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''에 정의된 관련 수치를 계산합니다:''')]),
    ], className='faq-answer'),
])
outdoor_air_frac_label = html.Span(["실외 공기 비율 Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["에어로졸 여과 효율 p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["호흡 공기량 Q", html.Sub('b'), ": "])
cq_label = html.Span(["날숨 공기의 감염성 C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["마스크 통과 확률 p", html.Sub('m'), ": "])
room_vol_label = html.Span(["공간의 부피 V: "])
vent_rate_Label = html.Span(["(실외) 환기량 Q: "])
recirc_rate_label = html.Span(["재순환 공기량 Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["공기 여과율 (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["습도에 따른 에어로졸 반지름 r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["습도에 따른 바이러스 비활성화율 \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["유효 에어로졸 침전 속도 v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["농도 완화율 \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["공기 중 전파율 \u03B2\u2090: "])

graph_output_header = "Graph Output: "
faq_graphs_text = html.Div([
    html.H5("Graph Output: "),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("이 모델이 다수의 감염자가 있을 때도 예측할 수 있나요?"),
    html.Div(['''아닙니다. 이 모델은 한 명의 감염자가 있을 때의 전파 위험을 계산합니다. 따라서 이 모델은 수용 인원의 감염이 적게 
    진행되었을 때를 가정합니다. 이러한 가정 하에 전파 위험성은 공간 내 기대 감염자 수(공간 내 인원과 감염자 비율의 곱)에 비례하여 증가합니다. 
    위험 감수율은 감염 인원이 1명 초과인 경우 더 낮게 설정되어야 합니다. 반대로, 공간 내의 기대 감염자 수가 0에 근접한다면, 모델이 추천하는 
    제한 사항이 불필요하다 간주되는 정도로 위험 감수율을 높게 설정해도 됩니다. '''],
             className='faq-answer'),
])

risk_tol_desc = html.Div('''고령자 혹은 기저 질환이 있는 사람 등의 고위험군은 더 낮은 수치의 위험 감수율이 요구됩니다. 높은 위험 감수율은
                            예상 수용 기간 동안 더 많은 전파가 발생함을 의미합니다(자세한 정보는 FAQ (자주 묻는 질문) 란을 참고해 주세요
                            ).''', style={'font-size': '13px', 'margin-left': '20px'})

# Main Panel Text
curr_room_header = "현재 공간: "
main_panel_s1 = "이 모델에 근거하면, 이 공간은 다음과 같은 조건에서 안전*합니다. "
main_panel_six_ft_1 = "6 피트 혹은 2 미터 거리두기 가이드라인에 따르면 이 공간은 "
main_panel_six_ft_2 = "의 인원이 무기한 생활하여도 안전합니다."

main_airb_trans_only_disc = html.Div(["",
                                      html.Span(html.A(href='https://www.nature.com/articles/d41586-020-02058-1',
                                                       children="이 가이드라인은 나열된 누적 시간 동안 한 명의 감염자로부터의 공기 중 전파를 고려한 "
                                                                "것입니다.",
                                                       target='_blank'), ),
                                      html.Span('''''')], className='airborne-text')

# Bottom panels text
n_input_text_1 = "이 공간에 "
n_input_text_2 = " 명이 있으면, "
n_input_text_3 = " 동안 안전할 것입니다."

t_input_text_1 = "사람들이 이 곳에 약 "
t_input_text_2 = " 시간 동안 있는다면, 수용 인원은 "
t_input_text_3 = "으로 제한되어야 합니다."

airb_trans_only_disc = html.Div('''이 가이드라인은 나열된 누적 시간 동안 한 명의 감염자로부터의 공기 중 전파를 고려한 것입니다.''', className='airborne-text')

footer = html.Div([
    html.Div([html.Span('''코로나19 실내 안전 가이드라인은 코로나19의 실내 공기 중 전파의 위험성에 영향을 주는 요인들에 사람들이 친숙해질 
    수 있도록 하며, 다양한 조건에 따른 전파 위험성의 정량적 평가를 보조하기 위해 개발되었습니다. 모델 변수들의 불확실성과 변수들이 갖는 변동성에 
    의해 10배 정도의 오차를 야기할 수 있으나, 이 오차는 위험 감수율을 충분히 작게 설정함으로써 줄일 수 있습니다. 본 가이드라인에서는 호흡기 
    비말을 통한 단거리 전파는 고려하지 않았으며, '''),
              html.A(children="링크된 글",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' (Bazant & Bush, 2020)에 논의된 바와 같이 단거리 비말전파의 위험성은 마스크를 착용하지 않은 경우 상당히 
              증가할 수 있습니다. 코로나19 실내 안전 가이드라인을 사용함에 따른 결과의 책임은 전적으로 사용자에게 있습니다. 
              본 가이드라인은 어떠한 종류의 보장이나 보증을 제공하지 않습니다. 저자들은 본 가이드라인의 사용에 따른 어떠한 법적 책임도 
              지지 않습니다.''')]),
    html.Br(),
    html.Div("에게 감사의 말씀을 드립니다 ")
], className='footer-small-text')
