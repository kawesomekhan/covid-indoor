import dash_html_components as html
import descriptions_links as links

"""

descriptions: Farsi

"""

# Header
header = html.Div([
    html.H1(children='COVID-19 راهنمای ایمنی محیط داخلی برای ویروس'),
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
language_dd = "زبان: "

# Unit systems
units_dd = "واحدها: "
unit_settings = [
    {'label': "انگلیسی", 'value': "british"},
    {'label': "متریک", 'value': "metric"},
]

# Modes
mode_dd = "حالت: "
app_modes = [
    {'label': "ساده", 'value': "basic"},
    {'label': "پیشرفته", 'value': "advanced"},
]

error_list = {
    "floor_area": "خطا: مساحت کف نمی تواند تهی باشد.",
    "ceiling_height": "خطا: ارتفاع سقف نمی تواند تهی باشد.",
    "recirc_rate": "خطا: میزان گردش هوا نمی تواند تهی باشد.",
    "aerosol_radius": "خطا: شعاع آئروسل) ذرات هوایی (نمی تواند تهی باشد.",
    "viral_deact_rate": "خطا: میزان غیرفعال سازی ویروس نمی تواند تهی باشد.",
    "n_max_input": "خطا: تعداد افراد نمی تواند از 2 نفر کمتر باشد.",
    "exp_time_input": "خطا: مدت زمان قرارگیری در معرض ویروس باید بیشتر از 0 باشد.",
    "air_exchange_rate": "خطا: میزان تهویه هوا باید بیشتر از 0 باشد.",
    "merv": "خطا: سیستم تصفیه نمی تواند تهی باشد.",
    "prevalence": "خطا: شیوع باید بیشتر از 0 و کمتر از 100000 باشد"
}

# Main Panel Text
curr_room_header = "مشخصات اتاق:"
presets = [
    {'label': "سفارشی", 'value': 'custom'},
    {'label': "کلاس درس", 'value': 'classroom'},
    {'label': "اتاق نشیمن", 'value': 'living-room'},
    {'label': "کلیسا", 'value': 'church'},
    {'label': "رستوران", 'value': 'restaurant'},
    {'label': "اداره", 'value': 'office'},
    {'label': "واگن مترو", 'value': 'subway'},
    {'label': "هواپیمای تجاری", 'value': 'airplane'},
]

curr_human_header = "رفتار انسانی:"
presets_human = [
    {'label': "سفارشی", 'value': 'custom'},
    {'label': "ماسک ، استراحت", 'value': 'masks-1'},
    {'label': "ماسک ، صحبت کردن", 'value': 'masks-2'},
    {'label': "ماسک ، ورزش", 'value': 'masks-3'},
    {'label': "بدون ماسک ، در حال استراحت", 'value': 'no-masks-1'},
    {'label': "بدون ماسک ، صحبت کردن", 'value': 'no-masks-2'},
    {'label': "بدون ماسک ، ورزش کنید", 'value': 'no-masks-3'},
    {'label': "بدون ماسک ، آواز", 'value': 'singing-1'},
]

curr_risk_header = "ریسک پذیری:"
# presets_risk = [
#     {'label': "Low", 'value': 0.01},
#     {'label': "Medium", 'value': 0.1},
#     {'label': "High", 'value': 1},
# ]
risk_tol_marks = {
    # 0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: امن تر', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: ناامن'}
}

risk_tolerance_text = "ریسک پذیری: "
risk_tol_desc = html.Div('''More vulnerable populations such as the elderly or those with preexisting medical 
conditions require a lower risk tolerance (~0.01). A higher risk tolerance will mean more expected 
transmissions during the expected occupancy period (see FAQ for details).''', style={'font-size': '13px',
                                                                                     'margin-left': '20px'})

curr_age_header = "گروه سنی:"
presets_age = [
    {'label': "کودکان (کمتر از 15 سال)", 'value': 0.23},
    {'label': "بزرگسالان (15-64 سال)", 'value': 0.68},
    {'label': "سالمندان (> 64 سال)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: کودکان (کمتر از 15 سال)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: بزرگسالان (15-64 سال)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: سالمندان (> 64 سال)', 'style': {'width': '75px'}}
}

curr_strain_header = "گونه ویروسی:"
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2 (نژاد ووهان)", 'value': 1},
    {'label': "SARS-CoV-2 (انگلیسی گونه)", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: ووهان', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: انگلستان/B.1.1.7'}
}

pim_header = "درصد ایمنی:"
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "اگر فرد آلوده وارد شود ..."
risk_prevalence_desc = "با توجه به شیوع عفونت"
risk_personal_desc = "برای محدود کردن خطر شخصی من ..."

main_panel_s1 = '''بر اساس این مدل ، برای این اتاق ایمن است که داشته باشد:'''

main_panel_s1_b = html.Span([
    html.Span('''برای محدود کردن انتقال COVID-19 در جمعیتی با شیوع عفونت'''),
    html.Sup('''1'''),
    html.Span(''' ''')
])
main_panel_s2_b = ''' در هر 100000 ، این فضا نباید بیشتر از موارد زیر داشته باشد:'''

main_panel_s1_c = html.Span([
    html.Span('''برای محدود کردن احتمال ابتلای من به COVID-19 در جمعیتی با شیوع عفونت'''),
    html.Sup('''1'''),
    html.Span(''' ''')
])
main_panel_s2_c = '''در 100000 ، این فضا نباید بیشتر از موارد زیر داشته باشد: '''

units_hr = 'ساعت'
units_min = 'دقیقه'
units_days = 'روز'
units_months = 'ماه ها'

units_hr_one = 'ساعت'
units_min_one = 'دقیقه'
units_day_one = 'روز'
units_month_one = 'ماه'

is_past_recovery_base_string = ' {n_val} نفر به مدت >{val:.0f} روز'
model_output_base_string = '{n_val} نفر به مدت '
nt_bridge_string = " نفر به مدت "
tn_bridge_string = " مدت "

main_panel_six_ft_1 = "در مقابل ، دستورالعمل فاصله شش فوت (یا دو متری) تعداد ظرفیت را به "
main_panel_six_ft_2 = " محدود می کند که این دستورالعمل را پس از "
main_panel_six_ft_3 = " نقض می کند "

six_ft_base_string = ' {} نفر'
six_ft_base_string_one = ' {} نفر'

graph_title = "تعداد ظرفیت در مقابل زمان قرار گرفتن در معرض"
graph_xtitle = "حداکثر زمان قرار گرفتن در معرض (ساعت) \u03C4 (hours)"
graph_ytitle = "حداکثر ظرفیت N"
transient_text = "گذرا"
steady_state_text = "حالت پایدار"

main_airb_trans_only_disc = html.Div(["*The guideline restricts the probability of ",
                                      html.Span(html.A(href=links.link_docs,
                                                       children="airborne transmissions",
                                                       target='_blank'), ),
                                      html.Span(''' per infected person to be less than the risk tolerance 
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*The guideline restricts the probability of ",
                                            html.Span(html.A(href=links.link_docs,
                                                             children="airborne transmissions",
                                                             target='_blank'), ),
                                            html.Span(''' per infected person to be less than the risk tolerance (10%)
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')

other_risk_modes_desc = html.Div('''سایر سناریوهای ریسک در حالت پیشرفته در نظر گرفته شده است. به طور خاص ، ممکن است شیوع عفونت در جمعیت ، ایمنی بدست آمده از طریق واکسیناسیون یا قرار گرفتن در معرض قبلی و خطر برای یک فرد خاص در نظر گرفته شود.''')

main_airb_trans_only_desc_b = html.Div(["*The guideline restricts the probability of one ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="airborne transmission",
                                                         target='_blank'), ),
                                        html.Span(''' per infected person to be less than the risk tolerance 
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["*The guideline restricts the probability of ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="airborne transmission",
                                                         target='_blank'), ),
                                        html.Span(''' to a particular individual to be less than the risk tolerance 
                                      over the cumulative exposure time 
                                      listed.''')], className='airborne-text')

airb_trans_only_disc = html.Div('''''', className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''برای تخمین شیوع محلی خود ، منابع مفیدی در اینجا آورده شده است: '''),
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
n_input_text_1 = "اگر این اتاق "
n_max_base_string = ' {:.0f} نفر'
n_max_overflow_base_string = ' >{:.0f} نفر'
n_input_text_2 = " نفر داشته باشد ، دستورالعمل * پس از "
n_input_text_3 = " نقض می شود."

t_input_text_1 = "اگر افراد تقریباً "
t_input_text_2 = " ساعت را در اینجا بگذرانند ، تعداد ساکنان آن باید به "
t_input_text_3 = "محدود شود."

# About
about_header = "درباره"
about = html.Div([
    html.H6("درباره", style={'margin': '0'}),
    html.Div('''برای کاهش شیوع COVID-19 ، دستورالعملهای رسمی بهداشت عمومی محدودیتهایی را در موارد زیر توصیه کرده اند : مسافت فرد به فرد (6 فوت در 2 متر ) ، زمان سکونت (15 دقیقه ) ، حداکثر ساکنان (25 نفر ) یا حداقل تهویه (6 تغییر هوا در ساعت).'''),
    html.Br(),
    html.Div([html.Span('''There is growing '''),
              html.A(children="scientific evidence",
                     href=links.link_docs,
                     target='_blank'),
              html.Span(''' for airborne transmission of COVID-19, which occurs when 
    infectious aerosol droplets are exchanged by breathing shared indoor air. While public health organizations are 
    beginning to acknowledge airborne transmission, they have yet to provide a safety guideline that incorporates all 
    the relevant variables.''')]),
    html.Br(),
    html.Div([html.Span('''This app, developed by Kasim Khan in collaboration with Martin Z. Bazant and John W. M. Bush, 
    uses a '''),
              html.A(children="theoretical model",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' to calculate safe exposure times and occupancy levels for indoor spaces.  By adjusting 
    room specifications, ventilation and filtration rates, face-mask usage, respiratory activities, 
    and risk tolerance (in the other tabs), you can see how to mitigate indoor COVID-19 transmission in different 
    indoor spaces.''')]),
    html.Br(),
    html.Div([html.Span('''علمی که پشت این برنامه نرم افزاری است همچنین در یک دوره آنلاین آزاد و گسترده ، خود گام (MOOC) در edX: 10.S95x'''),
              html.A(children="Physics of COVID-19 Transmission آموزش داده می شود",
                     href=links.link_mooc,
                     target='_blank')])
])

# Room Specifications
room_header = "مشخصات اتاق - جزئیات:"

floor_area_text = "مساحت کل زمین (sq. ft.): "
floor_area_text_metric = "مساحت کل زمین (m²): "
ceiling_height_text = "ارتفاع متوسط سقف (ft.): "
ceiling_height_text_metric = "ارتفاع متوسط سقف (m): "

ventilation_text = "سیستم تهویه: "
vent_type_output_base = "{:.1f} "
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (در فضای باز (ACH) نرخ تهویه )"])
ventilation_text_adv = html.Span(["سیستم تهویه (hr", html.Sup("-1"), ", در فضای باز (ACH) نرخ تهویه ): "])
ventilation_types = [
    {'label': "پنجره های بسته", 'value': 0.3},
    {'label': "پنجره های باز ", 'value': 2},
    {'label': "تهویه مکانیکی", 'value': 3},
    {'label': "پنجره های باز با پنکه", 'value': 6},
    {'label': "تهویه مکانیکی بهتر", 'value': 8},
    {'label': "آزمایشگاه ، رستوران", 'value': 9},
    {'label': "کافه", 'value': 15},
    {'label': "بیمارستان/ واگن  مترو", 'value': 18},
    {'label': "آزمایشگاه سمی / هواپیما", 'value': 24},
]

filtration_text = "سیستم تصفیه: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "سیستم تصفیه (MERV): "
filter_types = [
    {'label': "هیچ کدام", 'value': 0},
    {'label': "کولر پنجره مسکونی", 'value': 2},
    {'label': "مسکونی / تجاری / صنعتی", 'value': 6},
    {'label': "مسکونی / تجاری / بیمارستانی", 'value': 10},
    {'label': "بیمارستان و جراحی عمومی", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_text = "نرخ گردش مجدد: "
recirc_type_output_base = "{:.1f} "
recirc_type_output_units = html.Span(["hr", html.Sup("-1")])
recirc_text_adv = html.Span(["نرخ گردش مجدد (hr", html.Sup("-1"), "): "])
recirc_types = [
    {'label': "هیچ کدام", 'value': 0},
    {'label': "آهسته", 'value': 0.3},
    {'label': "در حد متوسط", 'value': 1},
    {'label': "سریع", 'value': 10},
    {'label': "هواپیما", 'value': 24},
    {'label': "واگن مترو", 'value': 54},
]

humidity_text = "رطوبت نسبی: "
humidity_marks = {
    0.01: {'label': '1%: خیلی خشک', 'style': {'max-width': '25px'}},
    # 0.2: {'label': '20%: Airplane', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: خشک'},
    0.6: {'label': '60%: متوسط'},
    0.99: {'label': '99%: خیلی مرطوب'},
}

need_more_ctrl_text = '''آیا به کنترل بیشتری بر ورودی های خود نیاز دارید؟ با استفاده از کشویی در بالای صفحه به حالت پیشرفته بروید.'''

human_header = "رفتار انسانی - جزئیات"
# Human Behavior
exertion_text = "میزان تنفس: "
exertion_types = [
    {'label': "استراحت  در حال", 'value': 0.49},
    {'label': "ایستاده", 'value': 0.54},
    {'label': "آواز خواندن", 'value': 1},
    {'label': "ورزش سبک", 'value': 1.38},
    {'label': "ورزش متوسط", 'value': 2.35},
    {'label': "ورزش سنگین", 'value': 3.30},
]

breathing_text = "فعالیت تنفسی: "
expiratory_types = [
    {'label': "تنفس (سبک)", 'value': 1.1},
    {'label': "تنفس (طبیعی)", 'value': 4.2},
    {'label': "تنفس (سنگین)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "صحبت کردن (نجوا)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "صحبت کردن (عادی)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "صحبت کردن (بلند)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "آواز خواندن", 'value': 970},
]

mask_type_text = "کارایی تصفیه ماسک (نوع ماسک): "
mask_type_marks = {
    0: {'label': "0% (هیچ ، محافظ صورت)", 'style': {'max-width': '75px'}},
    0.5: {'label': "50% (پارچه نخی )", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (پارچه نخی  چند لایه ، ابریشم)", 'style': {'max-width': '75px'}},
    0.90: {'label': "90% (یکبار مصرف جراحی)", 'style': {'max-width': '75px'}},
    # 0.99: {'label': "99% (N95 resp-irator)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "هیچ ، محافظ صورت", 'value': 0},
    {'label': "پارچه نخی ", 'value': 0.5},
    {'label': "پارچه نخی  چند لایه ، ابریشم", 'value': 0.7},
    {'label': "یکبار مصرف جراحی", 'value': 0.9},
    {'label': "ماسک تنفسی N95", 'value': 0.99},
]

mask_fit_text = "سازگاری ماسک: "
mask_fit_marks = {
    0: {'label': '0%: هیچ یک', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: کم'},
    0.95: {'label': '95%: خوب'}
}

# FAQ/Other Inputs & Outputs
faq_header = "سوالات متداول"
other_io = "سایر پارامترها"

faq_top = html.Div([
    html.H6("سوالات متداول"),
    html.H5("چرا فاصله 6 فوت / 2 متر کافی نیست؟"),
    html.Div([
        html.Div([html.Span('''6 feet (or 2 meter) spacing protects you from large drops ejected by an infected 
        person coughing, as do face masks; however, it doesn’t protect against '''),
                  html.A(children="airborne transmission",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' by infectious aerosols that are suspended in the air and mixed throughout a room. 
                  Indoors, people are no safer from airborne transmission at 60 feet than 6 feet. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("آیا حالت های انتقال دیگری نیز وجود دارد؟"),
    html.Div([
        html.Div([html.A(children="Airborne transmission",
                         href=links.link_docs,
                         target='_blank'),
                  html.Span(''' is thought to be dominant for COVID-19, but other modes are possible, such as `fomite’ 
                  transmission through direct contact with infectious residues on surfaces, `large-droplet' 
                  transmission via coughing or sneezing, and `short-range aerosol' transmission from the respiratory 
                  jet of an infected person over a prolonged period. While the latter two modes may be significant, 
                  they are largely eliminated when face masks or shields are worn; however, the risk of airborne 
                  transmission remains.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("آیا واقعاً می توانیم یک اتاق کاملاً مخلوط شده را تصور کنیم؟"),
    html.Div([
        html.Div([html.Span('''There are many contributors to mixing in indoor spaces, including buoyancy-driven 
        flows (from heaters, air conditioners or windows), forced convection from vents and fans, and human motion 
        and respiration. While there are exceptions, as discussed in the '''),
                  html.A(children="paper",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''', the assumption of well-mixedness is widely used in the theoretical modeling of 
                  airborne disease transmission.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("آیا این راهنما برای فضاهای بسیار بزرگ در نظر گرفته شده است؟"),
    html.Div([
        html.Div([html.Span('''In concert halls, stadiums, or other large, ventilated spaces with large numbers of 
        people, the risk of airborne transmission is significant and properly captured by the guideline.  However, 
        when masks or face shields are not worn, there is an additional risk of short-range transmission through 
        respiratory jets, estimated in the '''),
                  html.A(children="paper",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("چرا ارتفاع سقف اهمیت دارد؟"),
    html.Div([
        '''ارتفاع سقف بر حجم کل اتاق تأثیر می گذارد ، که برای تخمین غلظت ذرات معلق در هوا (تعداد قطرات هوا در واحد حجم) مورد نیاز است. این غلظت برای برآورد خطر انتقال COVID-19 در اتاق مورد نیاز است.'''
    ], className='faq-answer'),
    html.Br(),
    html.H5("من شماره های ACH / MERV خود را می دانم.  کجا می توانم آنها  را وارد کنم ؟"),
    html.Div('''
        اگر به کنترل بیشتری بر ورودی های خود نیاز دارید ، با استفاده از کشویی در بالای صفحه وب به حالت پیشرفته بروید.
    ''', className='faq-answer'),
    html.Br(),
    html.H5("چرا ماسک تنفسی  N95 کارایی99%  دارند؟"),
    html.Div('''دستگاه های تنفس N95 حداقل 95٪ بازده فیلتراسیون در اندازه ذرات 0.3 میکرومتر دارند ، 10 برابر کوچکتر از اندازه قطرات در انتقال COVID-19 موجود در هوا. برای قطره های بزرگ تر ، دستگاه های تنفس N95 حتی کارآیی بیشتری دارند نزدیک به 100٪.''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("آیا پارامترهای مخفی در حالت ساده وجود دارد ؟"),
    html.Div([html.Span('''All of the relevant physical parameters are detailed in the '''),
              html.A(children="paper",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''. In Basic Mode, the app assumes a default effective aerosol radius of 2 μm (at 60% 
              humidity) and a maximum viral deactivation rate of 0.6 /hr (at ~100% humidity), both of which increase 
              with relative humidity (RH). Estimates for the viral deactivation rate err on the conservative side of 
              slower deactivation.  The viral deactivation rate can be increased by ultraviolet radiation (UV-C) or 
              chemical disinfectants (e.g. hydrogen peroxide, ozone). The app also estimates the key disease 
              parameter, the infectiousness of exhaled air, C'''),
              html.Sub("q"),
              html.Span(''' (infection quanta per unit volume), from the specified 
              respiratory activity, using tabulated values in Figure 2 of the '''),
              html.A(children="paper",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''. You define these parameters yourself in Advanced Mode.''')],
             className='faq-answer'),
])

aerosol_radius_text = "شعاع موثر آئروسل با (با RH = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["حداکثر میزان غیرفعال سازی ویروسی (با RH = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

pop_immunity_header = "مصونیت جمعیت: "
perc_immune_label = html.Span(["درصد ایمنی p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["درصد عفونی p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["درصد واکسینه شده p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["درصد قبلا آلوده شده p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["درصد حساس p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''درصد آلودگی  p''', html.Sub('i'), '''در جمعیت از شیوع عفونی وارد شده در برگه های سناریوی خطر دیگر محاسبه می شود (با توجه به شیوع عفونت… ، برای محدود کردن خطر شخصی من…). درصد p''',
                                        html.Sub('im'), '''ایمنی را می توان از طریق درصد واکسیناسیون جمعیت به علاوه میزان کل موارد در جمعیت ، با غفلت از سهم موارد کشف نشده ، تخمین زد. از این دو مقدار برای محاسبه درصد حساس p'''
                                           , html.Sub('s'), ''' استفاده می شود. در حالت Basic و در حالت خطر اول (اگر فرد آلوده وارد شود ...) ، این مقدار 100٪ فرض می شود.''']),
                              html.Br(),
                              html.Div(['''در اینجا چند لینک مفید برای پیدا کردن p''', html.Sub('i'), ''' و p''',
                                        html.Sub('im'), '''آورده شده است: ''',
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

values_interest_header = "مقادیر محاسبه شده مورد علاقه: "
values_interest_desc = html.Div([
    html.H5("برنامه دقیقاً چه محاسبه ای می‌کند؟"),
    html.Div([
        html.Div([html.Span('''The app calculates the maximum allowable cumulative exposure time, the product of room 
        occupancy and time, in an indoor space. The spread of COVID-19 is limited by requiring that the expected 
        number of transmissions per infected individual, the “indoor reproductive number", be less than the chosen 
        risk tolerance. The app also calculates related quantities, defined in the '''),
                  html.A(children="paper",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''', that may be of interest:''')]),
    ], className='faq-answer'),
])
relative_sus_label = html.Span(["حساسیت نسبی s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["کسر هوای بیرونی Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["بازده تصفیه آئروسل p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["سرعت جریان تنفس Q", html.Sub('b'), ": "])
cq_label = html.Span(["عفونت هوای بازدم C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["احتمال عبور از ماسک p", html.Sub('m'), ": "])
room_vol_label = html.Span(["حجم اتاق  V: "])
vent_rate_Label = html.Span(["سرعت جریان تهویه (در فضای باز) Q: "])
recirc_rate_label = html.Span(["سرعت جریان بازگشت (گردش مجدد) Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["میزان تصفیه هوا (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["شعاع آئروسل با رطوبت تنظیم شده r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["میزان غیرفعال سازی ویروسی تنظیم شده با رطوبت \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["سرعت ته نشینی موثر آئروسل v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["سرعت سست سازی غلظت \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["میزان انتقال از طریق هوا \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("آیا این مدل شیوع عفونت در جمعیت محلی را در بر می گیرد؟"),
    html.Div(['''تأثیر شیوع عفونت در جمعیت محلی را می توان در حالت پیشرفته در نظر گرفت. در آنجا ، در برگه سایر پارامترها ، ممکن است تأثیر ایمنی در جمعیت را ارزیابی کنید  که ممکن است از طریق واکسیناسیون یا عفونت قبلی ایجاد شود.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("سوالات بیشتر؟"),
    html.Div([html.Span('''برای توضیحات و ارجاعات بیشتر ، به "'''),
              html.A(children="فراتر از 6 فوت",
                     href=links.link_paper,
                     target='_blank'),
              html.Span('''" و سایر پیوندهای در بالای صفحه وب مراجعه کنید.''')]),
])

footer = html.Div([
    html.Div([html.Span('''The COVID-19 Indoor Safety Guideline is an evolving tool intended to familiarize the 
    interested user with the factors influencing the risk of indoor airborne transmission of COVID-19, and to assist 
    in the quantitative assessment of risk in various settings. We note that uncertainty in and intrinsic variability 
    of model parameters may lead to errors as large as an order of magnitude, which may be compensated for by 
    choosing a sufficiently small risk tolerance. Our guideline does not take into account short-range transmission 
    through respiratory jets, which may substantially elevate risk when face masks are not being worn, in a manner 
    discussed in the '''),
              html.A(children="accompanying manuscript",
                     href=links.link_paper,
                     target='_blank'),
              html.Span(''' (Bazant & Bush, 2020). Use of the COVID-19 Indoor Safety Guideline is the sole 
              responsibility of the user. It is being made available without guarantee or warranty of any kind. The 
              authors do not accept any liability from its use.''')]),
    html.Br(),
    html.Div("با تشکر ویژه از: ")
], className='footer-small-text')
