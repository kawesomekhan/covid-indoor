from dash import html
import descriptions_links as links

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

Hindi

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

# Header
header = html.Div([
    html.H1(children='कोविड-19 से आतंरिक बचाव हेतु दिशानिर्देश'),
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
language_dd = "भाषा: "

# Unit systems
units_dd = "इकाई: "
unit_settings = [
    {'label': "हिंदी", 'value': "british"},
    {'label': "मीट्रिक", 'value': "metric"},
]

# Modes
mode_dd = "विधि: "
app_modes = [
    {'label': "आधार", 'value': "basic"},
    {'label': "एडवांस/अग्रिम", 'value': "advanced"},
]

error_list = {
    "floor_area": "त्रुटि: फर्श का क्षेत्रफल रिक्त नहीं हो सकता।",
    "ceiling_height": "त्रुटि: छत की ऊंचाई रिक्त नहीं हो सकती।",
    "recirc_rate": "त्रुटि: पुनर्संचार दर रिक्त नहीं हो सकती। ",
    "aerosol_radius": "त्रुटि: एरोसोल/हवाई त्रिज्या रिक्त नहीं हो सकती। ",
    "viral_deact_rate": "त्रुटि: वायरल निष्क्रियकरण दर रिक्त नहीं हो सकती। ",
    "n_max_input": "त्रुटि: लोगों की संख्या 2 से कम नहीं हो सकती। ",
    "exp_time_input": "त्रुटि: एक्सपोज़र (उजागर) का समय 0 से अधिक होना चाहिए।",
    "air_exchange_rate": "त्रुटि: वेंटिलेशन दर (ACH) 0 से अधिक होनी चाहिए।",
    "merv": "त्रुटि: निस्पंदन प्रणाली (MERV) रिक्त नहीं हो सकता ।",
    "prevalence": "त्रुटि: व्यापकता 0 से अधिक और 100,000 से कम होनी चाहिए।"
}

# Main Panel Text
curr_room_header = "कक्ष विशिष्टियां: "
presets = [
    {'label': "अपने अनुसार", 'value': 'custom'},
    {'label': "उपनगरीय आवास", 'value': 'house'},
    {'label': "बैठक कक्ष", 'value': 'living-room'},
    {'label': "जलपान गृह", 'value': 'restaurant'},
    {'label': "कार्यालय", 'value': 'office'},
    {'label': "कक्षा", 'value': 'classroom'},
    {'label': "मेट्रो कार", 'value': 'subway'},
    {'label': "वाणिज्यिक हवाई विमान", 'value': 'airplane'},
    {'label': "मंदिर (गिरिजाघर)", 'value': 'church'},
]

curr_human_header = "मानवीय व्यवहार: "
presets_human = [
    {'label': "अपने अनुसार", 'value': 'custom'},
    {'label': "मास्क, आराम करते समय", 'value': 'masks-1'},
    {'label': "मास्क, बोलते समय", 'value': 'masks-2'},
    {'label': "मास्क, व्यायाम करते समय", 'value': 'masks-3'},
    {'label': "बिना मास्क, आराम करते समय", 'value': 'no-masks-1'},
    {'label': "बिना मास्क, बोलते समय", 'value': 'no-masks-2'},
    {'label': "बिना मास्क, व्यायाम करते समय", 'value': 'no-masks-3'},
    {'label': "बिना मास्क, गायन करते समय", 'value': 'singing-1'},
]

curr_risk_header = "जोखिम सहिष्णुता: "
# presets_risk = [
#     {'label': "Low", 'value': 0.01},
#     {'label': "Medium", 'value': 0.1},
#     {'label': "High", 'value': 1},
# ]
risk_tol_marks = {
    # 0.01: {'label': '0.01: Safer', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: सुरक्षित', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: असुरक्षित'}
}

curr_age_header = "आयु वर्ग: "
presets_age = [
    {'label': "बच्चे (<15 वर्ष)", 'value': 0.23},
    {'label': "वयस्क (15-64 वर्ष)", 'value': 0.68},
    {'label': "बुजुर्ग (> 64 वर्ष)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: बच्चे (<15 वर्ष)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: वयस्क (15-64 वर्ष)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: बुजुर्ग (> 64 वर्ष)', 'style': {'width': '75px'}}
}

curr_strain_header = "वायरल रूप/स्ट्रेन: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "सार्स-कोवि-2 (वुहान स्ट्रेन)", 'value': 1},
    {'label': "सार्स-कोवि-२-बी-१-१-७-(यूके स्ट्रेन)", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: वुहान', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: बी-१-१-७-/ यूके', 'style': {'width': '75px'}}
}

pim_header = "प्रतिरक्षा प्रतिशत: "
# pim_marks = {
#     0: {'label': '0% (basic mode)'},
#     0.33: {'label': '33% (default)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "यदि एक संक्रमित व्यक्ति…"
risk_prevalence_desc = "संक्रमण की व्यापकता को देखते हुए…"
risk_personal_desc = "मेरे व्यक्तिगत जोखिम को सीमित करने के लिए ..."
risk_options = [
    {'label': risk_conditional_desc, 'value': 'conditional'},
    {'label': risk_prevalence_desc, 'value': 'prevalence'},
    {'label': risk_personal_desc, 'value': 'personal'},
]

main_panel_s1 = "इस मॉडल के आधार पर, यह कक्ष निम्न अवधि तथा लोगों की संख्या के लिए सुरक्षित होना चाहिए: "

main_panel_s1_b = html.Span([
    html.Span('''यह जनसंख्या जहाँ कि'''),
    html.Sup('''1'''),
    html.Span(''' ''')
])
main_panel_s2_b = ''' प्रति 100,000 का संक्रमण प्रचलित है, कोविड -19 के संचरण को सीमित करने के लिए, इस स्थान में: '''

main_panel_s1_c = html.Span([
    html.Span('''कोविड-19 से संक्रमित होने की मेरी संभावना को सीमित करने के लिए'''),
    html.Sup('''1'''),
    html.Span(''',''')
])
main_panel_s2_c = ''' प्रति 100,000 के संक्रमण प्रचलन के साथ, इस स्थान में: '''

units_hr = 'घंटों'
units_min = 'मिनट'
units_days = 'दिनों'
units_months = 'महीने'

units_hr_one = 'घंटे'
units_min_one = 'मिनट'
units_day_one = 'दिन'
model_output_suffix = ' के लिए '
units_month_one = 'महीना'

is_past_recovery_base_string = '>{val:.0f} दिनों के लिए {n_val} लोग'
model_output_base_string = '{n_val} लोग'
people_string = ' लोग'
nt_bridge_string = " के लिए "
tn_bridge_string = " के लिए "

main_panel_six_ft_1 = "इसके विपरीत, छह-फुट (या दो-मीटर) दूर दिशा-निर्देश अध्यावास को "
main_panel_six_ft_2 = " तक सीमित कर देगा, जोकि "
main_panel_six_ft_3 = " के बाद दिशानिर्देशों* का उल्लंघन करेगा"

six_ft_base_string = ' {} लोग'
six_ft_base_string_one = ' {} लोग'

graph_title = "ठहराव (अध्यावास) बनाम एक्सपोज़र (उजागर) समय"
graph_xtitle = "अधिकतम एक्सपोज़र टाइम \u03C4 (घंटे)"
graph_ytitle = "अधिकतम ठहराव (अध्यावास) N"
transient_text = "क्षणिक / अस्थायी"
steady_state_text = "स्थिर अवस्था"

main_airb_trans_only_disc = html.Div(["यह दिशानिर्देश प्रति व्यक्ति ",
                                      html.Span(html.A(href=links.link_docs,
                                                       children='''हवाई संचरण''',
                                                       target='_blank'), ),
                                      html.Span(''' की संभावना को सूचीबद्ध संचयी अनावरण समय में जोखिम सहिष्णुता से कम 
                                      होने के लिए प्रतिबंधित करता है।''')], className='airborne-text')
main_airb_trans_only_disc_basic = html.Div(["*दिशानिर्देश प्रति संक्रमित व्यक्ति ",
                                            html.Span(html.A(href=links.link_docs,
                                                             children="हवाई संचरण",
                                                             target='_blank'), ),
                                            html.Span(''' दिकी संभावना को सूचीबद्ध जोखिम सहिष्णुता (10%) से कम होने के 
                                            लिए प्रतिबंधित करता है।''')], className='airborne-text')

other_risk_modes_desc = html.Div('''अन्य जोखिम परिदृश्यों को उन्नत मोड में माना जाता है। विशेष रूप से, किसी आबादी में 
संक्रमण की व्यापकता, टीकाकरण या पूर्व अनावरण के माध्यम से प्राप्त प्रतिरक्षा, और एक विशिष्ट व्यक्ति के लिए जोखिम पर 
विचार किया जा सकता है।''')

main_airb_trans_only_desc_b = html.Div(["*दिशानिर्देश एक ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="हवाई संचरण",
                                                         target='_blank'), ),
                                        html.Span(''' प्रति संक्रमित व्यक्ति की संभावना को संचयित अनावरण समय की जोखिम 
                                        सहिष्णुता से कम होने के लिए प्रतिबंधित करता है।''')],
                                       className='airborne-text')
main_airb_trans_only_desc_c = html.Div(["*दिशानिर्देश किसी विशेष व्यक्ति पर ",
                                        html.Span(html.A(href=links.link_docs,
                                                         children="हवाई संचरण",
                                                         target='_blank'), ),
                                        html.Span(''' की संभावना को संचयित अनावरण समय की जोखिम सहिष्णुता से कम होने के 
                                        लिए प्रतिबंधित करता है।''')], className='airborne-text')

airb_trans_only_disc = html.Div('''यह दिशानिर्देश एक संक्रमित व्यक्ति से हवा द्वारा प्रसारण के कुल एक्सपोज़र समय पर 
आधारित है।''', className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''अपने स्थानीय प्रसार का अनुमान लगाने के लिए, यहाँ कुछ सहायक संसाधन हैं: '''),
                                # html.Span(html.A(href=links.link_jhu_dashboard,
                                #                  children="JHU COVID-19 Dashboard",
                                #                  target='_blank')),
                                # html.Span(''', '''),
                                html.Span(html.A(href=links.link_cdc_dashboard,
                                                 children="सी डी सी कोविड -19 डेटा ट्रैकर",
                                                 target='_blank')),
                                html.Span(", "),
                                html.Span(html.A(href=links.link_jhu_data,
                                                 children="जे एच यू कोरोनावायरस रिसोर्स सेंटर",
                                                 target='_blank')),
                                html.Span(", "),
                                html.A(children="यूएस इम्युनिटी एस्टिमेट्स",
                                       href=links.link_cdc_immunity,
                                       target='_blank'),
                                html.Span(", "),
                                html.A(children="इंटरनेशनल इम्युनिटी एस्टिमेट्स",
                                       href=links.link_jhu_vaccine,
                                       target='_blank'),
                                ], className='airborne-text')

# Bottom panels text
n_input_text_1 = "यदि इस कमरे में "
n_max_base_string = ' {:.0f} लोग'
n_max_overflow_base_string = ' >{:.0f} लोग'
n_input_text_2 = " लोग हैं, तो इसके रहने वाले "
n_input_text_3 = " के बाद दिशानिर्देशों * का उल्लंघन हो  जाएगा।"

t_input_text_1 = "यदि लोग यहां लगभग "
t_input_text_2 = " घंटे बिताते हैं, तो अधिकतम "
t_input_text_3 = " होने चाहिए।"

# About
about_header = "विषय में"
about = html.Div([
    html.H6("विषय में", style={'margin': '0'}),
    html.Div('''कोविड -19 के प्रसार को कम करने के लिए, आधिकारिक सार्वजनिक स्वास्थ्य दिशानिर्देशों द्वारा: 
    व्यक्ति-से-व्यक्ति की दूरी (6 फीट / 2 मीटर), ठहराव के समय (15 मिनट), अधिकतम ठहराव (25 लोग), या न्यूनतम वेंटिलेशन 
    ( प्रति घंटे 6 वायु परिवर्तन), की सीमा तय की संस्तुति की गयी है।'''),
    html.Br(),
    html.Div([html.Span(''''''),
              # html.A(children="scientific evidence",
              #        href=link_docs,
              #        target='_blank'),
              html.Span('''कोविड -19 के हवाई प्रसारण के लिए वैज्ञानिक प्रमाण बढ़ रहे हैं । यह हवाई प्रसारण संक्रामक 
              हवा के बंद स्थानों के आदान प्रदान की वजह से होता है। जबकि सार्वजनिक स्वास्थ्य संगठन हवाई प्रसारण को 
              स्वीकार करने लगे हैं, उन्हें अभी भी सभी प्रासंगिक चर को शामिल करते हुए सुरक्षा दिशानिर्देश को प्रदान 
              करना शेष है ।''')]),
    html.Br(),
    html.Div([html.Span(''''''),
              # html.A(children="theoretical model",
              #        href=link_paper,
              #        target='_blank'),
              html.Span('''मार्टिन बजांत और जॉन डब्लू. ऍम. बुश  के सहयोग से कासिम खान द्वारा विकसित यह ऐप, 
              आतंरिक स्थानों के लिए सुरक्षित एक्सपोज़र समय और ठहराव स्तर की गणना करने के लिए एक सैद्धांतिक मॉडल का 
              उपयोग करती है। कमरे के विनिर्देशों, वेंटिलेशन और निस्पंदन दरों, चेहरे के मुखोटे का उपयोग, 
              श्वसन गतिविधियों और जोखिम सहिष्णुता (अन्य टैब में) को समायोजित करके, आप देख सकते हैं कि विभिन्न आतंरिक 
              स्थानों में आतंरिक कॉवेड -19 ट्रांसमिशन को कैसे कम किया जाए।''')]),
    html.Br(),
    html.Div([html.Span('''एप्लिकेशन के पीछे के विज्ञान को भी मुफ्त में बड़े पैमाने पर ऑनलाइन पाठ्यक्रम (ऍमओओसी) 
    एडेक्स पर: '''),
              html.A(children="10.S95x कोविड -19 के संचरण का विज्ञान' के नाम से पढ़ाया जाता है।",
                     href=links.link_mooc,
                     target='_blank')])

])

# Room Specifications
room_header = "कमरे के विनिर्देश - विवरण"

floor_area_text = "कुल तल क्षेत्रफल  (वर्ग फुट): "
floor_area_text_metric = "कुल तल क्षेत्रफल (m²): "
ceiling_height_text = "औसतन छत की ऊंचाई (फुट): "
ceiling_height_text_metric = "औसतन छत की ऊंचाई (m): "

ventilation_text = "वेंटिलेशन प्रणाली: "
vent_type_output_base = "{:.1f} "
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (बाहरी ACH)"])
ventilation_text_adv = html.Span(["वेंटिलेशन प्रणाल (hr", html.Sup("-1"), ", बाहरी ACH): "])
ventilation_types = [
    {'label': "बंद खिड़कियां", 'value': 0.3},
    {'label': "खुली खिड़कियां", 'value': 2},
    {'label': "यांत्रिक वेंटिलेशन", 'value': 3},
    {'label': "पंखो सहित खुली खिड़कियां", 'value': 6},
    {'label': "बेहतर यांत्रिक वेंटिलेशन ", 'value': 8},
    {'label': "प्रयोगशाला, जलपानगृह ", 'value': 9},
    {'label': "बार (मधुशाला)", 'value': 15},
    {'label': "अस्पताल / मेट्रो कार", 'value': 18},
    {'label': "विषाक्त प्रयोगशाला / हवाई जहाज", 'value': 24},
]

filtration_text = "निस्पंदन प्रणाली: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "निस्पंदन प्रणाली (MERV): "
filter_types = [
    {'label': "कोई नहीं", 'value': 0},
    {'label': "आवासीय खिड़की ए.सी.", 'value': 2},
    {'label': "आवासीय / वाणिज्यिक / औद्योगिक", 'value': 6},
    {'label': "आवासीय / वाणिज्यिक / अस्पताल", 'value': 10},
    {'label': "अस्पताल और सामान्य शल्य चिकित्सा ", 'value': 14},
    {'label': "HEPA - उच्च क्षमतायुक्त एयर फ़िल्टर", 'value': 17}
]

recirc_text = "पुनर्संचरण दर: "
recirc_type_output_base = "{:.1f} पुनर्संचरण ACH"
recirc_text_adv = "पुनर्संचरण दर (पुनर्संचरण ACH): "
recirc_types = [
    {'label': "कोई नहीं ", 'value': 0},
    {'label': "धीरे ", 'value': 0.3},
    {'label': "मध्यम ", 'value': 1},
    {'label': "तेज ", 'value': 10},
    {'label': "विमान ", 'value': 24},
    {'label': "मेट्रो कार", 'value': 54},
]

humidity_text = "सापेक्ष आर्द्रता: "
humidity_marks = {
    0.01: {'label': '1%: बहुत सूखी', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: हवाई जहाज', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: सूखा'},
    0.6: {'label': '60%: औसतन'},
    0.99: {'label': '99%: बहुत नम'},
}

need_more_ctrl_text = '''क्या आप अपने निवेश(इनपुट) पर अधिक नियंत्रण करना चाहते हैं? इस पेज के शीर्ष पर ड्रॉपडाउन मेनू 
में एडवांस/अग्रिम मोड पर स्विच करें। '''

human_header = "मानव व्यवहार - विवरण"
# Human Behavior
exertion_text = "स्वांस - दर: "
exertion_types = [
    {'label': "विश्राम स्थिति ", 'value': 0.49},
    {'label': "खड़े रहने कि स्थिति ", 'value': 0.54},
    {'label': "गायन", 'value': 1},
    {'label': "हल्का व्यायाम", 'value': 1.38},
    {'label': "मध्यम व्यायाम", 'value': 2.35},
    {'label': "भारी व्यायाम", 'value': 3.30},
]

breathing_text = "श्वसन क्रिया: "
expiratory_types = [
    {'label': "श्वसन (हल्का)", 'value': 1.1},
    {'label': "श्वसन (सामान्य)", 'value': 4.2},
    {'label': "श्वसन (भारी)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "बात करना (कानाफूसी)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "बात करना (सामान्य)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "बात करना (जोर से)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "गायन", 'value': 970},
]

mask_type_text = "मास्क निस्पंदन क्षमता (मास्क प्रकार): "
mask_type_marks = {
    0: {'label': "0% (कुछ नहीं, फेस शील्ड)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (सूती, फलालैन)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (बहुपरत सूती, रेशम)", 'style': {'max-width': '75px'}},
    0.90: {'label': "90% (डिस्पोजेबल सर्जिक/शल्यक)", 'style': {'max-width': '50px'}},
    # 0.99: {'label': "99% (N95 रेस्पिरेटर/श्वासयंत)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "कुछ नहीं, फेस शील्ड", 'value': 0},
    {'label': "सूती, फलालैन", 'value': 0.5},
    {'label': "बहुपरत सूती, रेशम", 'value': 0.7},
    {'label': "डिस्पोजेबल सर्जिक/शल्यक", 'value': 0.9},
    {'label': "N95 रेस्पिरेटर/श्वासयंतर", 'value': 0.99},
]

mask_fit_text = "मास्क फिट / अनुपालन: "
mask_fit_marks = {
    0: {'label': '0%: कोई नहीं', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: निम्न स्तर'},
    0.95: {'label': '95%: अच्छा'}
}

risk_tolerance_text = "जोखिम सहिष्णुता: "
risk_tol_desc = html.Div('''अधिक कमजोर आबादी जैसे कि बुजुर्गों या लम्बे समय से बीमार लोगों को कम जोखिम सहिष्णुता की 
आवश्यकता होती है। एक उच्च जोखिम सहिष्णुता का मतलब अपेक्षित ठहराव अवधि के दौरान अधिक प्रसारण होने की आशंका है (विवरण 
के लिए FAQ देखें)। ''', style={'font-size': '13px', 'margin-left': '20px'})
risk_tol_marks = {
    # 0.01: {'label': '0.01: ज्यादा सुरक्षित', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: सुरक्षित', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: असुरक्षित'}
}

# FAQ/Other Inputs & Outputs
faq_header = "प्रायः पूछे जाने वाले प्रश्न"
other_io = "अन्य मापदंड"

faq_top = html.Div([
    html.H6("प्रायः पूछे जाने वाले प्रश्न"),
    html.H5("6 फीट / 2 मीटर की दूरी पर्याप्त क्यों नहीं है?"),
    html.Div([
        html.Div([html.Span(''''''),
                  # html.A(children="airborne transmission",
                  #        href=link_docs,
                  #        target='_blank'),
                  html.Span('''6 फीट (या 2 मीटर) की दूरी आपको, फेस मास्क (मुखौटे) की तरह ही संक्रमित व्यक्ति द्वारा 
                  खांसने वाले बड़े बूंदों से बचाती है; हालाँकि, यह हवा में फैली और पूरे कमरे में मिश्रित संक्रामक हवा 
                  के संचरण से रक्षा नहीं करती है। घर के अंदर, लोग 6 फीट की तुलना में 60 फीट की दूरी पर हवाई संचरण 
                  द्वारा संक्रमड से ज्यादा सुरक्षित नहीं हैं।''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("क्या प्रसारण के अन्य तरीके हैं?"),
    html.Div([
        html.Div([html.A(children="",
                         href=link_docs,
                         target='_blank'),
                  html.Span('''हवा द्वारा फैलने को कोविड-19 के फैलने का मुख्य काराण माना जाता है, लेकिन अन्य तरीके भी 
                  संभव हैं | जैसे `संक्रमणीय पदार्थ': सतहों पर सीधे संपर्क के माध्यम से, 'बड़ी-बूंदो का ट्रांसमिशन': 
                  खाँसी या छींकने के माध्यम से , और `छोटी-दूरी के हवाई संचरण': एक लंबे समय से अधिक संक्रमित व्यक्ति 
                  के सांसों के संचरण से। हालाँकि बाद के दो तरीके महत्वपूर्ण हो सकते हैं, वे फेस मास्क या ढाल पहनने पर 
                  काफी हद तक समाप्त हो जाते हैं; फिर भी हवाई प्रसारण का जोखिम बना रहता है।''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("क्या हम वास्तव में एक अच्छी तरह से मिश्रित कमरा मान सकते हैं?"),
    html.Div([
        html.Div([html.Span(''''''),
                  # html.A(children="paper",
                  #        href=link_paper,
                  #        target='_blank'),
                  html.Span('''आतंरिक खली स्थान में हवा को मिश्रित करने के लिए कई योगदानकर्ता हैं, जिसमें उछाल-चालित 
                  प्रवाह (हीटर, एयर कंडीशनर या खिड़कियों से), पंखो और छिद्रों से दबाबदार हवाई संवहन, और मानव गतिविधि 
                  और श्वसन शामिल हैं। जबकि इसके कुछ अपवाद भी हैं, जैसा कि पेपर में चर्चा की गई है, कमरों के अच्छी तरह 
                  से मिश्रित होने की धारणा को व्यापक रूप से हवाई रोग संचरण के सैद्धांतिक मॉडलिंग में उपयोग किया जाता 
                  है।''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("क्या ये दिशानिर्देश बहुत बड़ी जगहों पर लागू होते हैं ?"),
    html.Div([
        html.Div([html.Span('''कॉन्सर्ट हॉल, स्टेडियम या अन्य बड़े हवादार स्थानों में जहाँ कि बड़ी संख्या में लोग 
        होते हैं, हवाई प्रसारण का जोखिम ज्यादा है और इसको दिशानिर्देश उचित रूप से कवर करते हैं। हालांकि, जब मास्क या 
        फेस शील्ड नहीं पहने जाते हैं, तो साँस के माध्यम से छोटी दूरी के प्रसारण का एक अतिरिक्त खतरा होता है, 
        पेपर में इसका अनुमान लगाया गया है।'''),
                  # html.A(children="paper",
                  #        href=link_paper,
                  #        target='_blank'),
                  html.Span('''''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("छत की ऊंचाई क्यों मायने रखती है?"),
    html.Div([
        '''छत की ऊंचाई कमरे की कुल मात्रा को प्रभावित करती है, जो हवाई संक्रमण (# हवाई संक्रमण प्रति यूनिट मात्रा) की 
        एकाग्रता का अनुमान लगाने के लिए आवश्यक है। कमरे की  कोविड -19 संचरण जोखिम का अनुमान लगाने के लिए इस एकाग्रता 
        की आवश्यकता होती है। '''
    ], className='faq-answer'),
    html.Br(),
    html.H5("मुझे अपने ACH / MERV नंबर पता हैं। मैं उन्हें कहां दर्ज कर सकता हूं?"),
    html.Div('''
        यदि आपको अपने निवेश (इनपुट) पर अधिक नियंत्रण की आवश्यकता है, तो वेबपेज के शीर्ष पर ड्रॉपडाउन का उपयोग करते हुए एडवांस मोड पर स्विच करें।
    ''', className='faq-answer'),
    html.Br(),
    html.H5("N95 श्वासयंत्र में 99% दक्षता क्यों है?"),
    html.Div('''N95 श्वासयंत्र 0.3 माइक्रोन के कणों के लिए कम से कम 95% निस्पंदन दक्षता रखते हैं, जोकि कोविड -19 के 
    हवाई संचरण की बूदों आकार से 10 गुना छोटा माप है। अत: बड़ी बूंदों के लिए, N95 श्वासयंत्र और भी अधिक कुशल हैं, 
    लगभग 100% कुशलता स्तर तक पहुंचते हैं।''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("क्या आधार मोड में कोई छिपे हुए मापदंड हैं?"),
    html.Div([html.Span(''''''),
              # html.A(children="paper",
              #        href=link_paper,
              #        target='_blank'),
              html.Span('''सभी प्रासंगिक भौतिक मापदंड पेपर में विस्तृत हैं। आधार मोड में, ऐप 2 माइक्रोन (60% आर्द्रता 
              पर) की एक डिफ़ॉल्ट प्रभावी एरोसोल त्रिज्या और 0.6 / घंटा (~ 100% आर्द्रता पर) की अधिकतम वायरल 
              निष्क्रियता दर मानती है, जोकि दोनों सापेक्ष आर्द्रता (आरएच) के साथ बढ़ते हैं। धीमी निष्क्रियता के कम से 
              कम पक्ष पर वायरल निष्क्रियकरण दर के लिए अनुमान लगाती है। वायरल निष्क्रियता दर पराबैंगनी विकिरण (
              यूवी-सी) या रासायनिक कीटाणुनाशक (जैसे हाइड्रोजन पेरोक्साइड, ओजोन) द्वारा बढ़ाई जा सकती है। ऐप में पेपर 
              के चित्र 2 में सारणीबद्ध मूल्यों का उपयोग करते हुए, निर्दिष्ट श्वसन गतिविधि से, प्रमुख रोग पैरामीटर, 
              एक्सहेल्ड एयर की संक्रामकता, सीक्यू (संक्रमण मात्रा प्रति यूनिट मात्रा) का अनुमान लगाया गया है। आप इन 
              मापदंडों को अपने आप उन्नत मोड में परिभाषित कर सकते हैं।'''),
              # html.Sub("q"),
              # html.Span(''' (infection quanta per unit volume), from the specified
              # respiratory activity, using tabulated values in Figure 2 of the '''),
              # html.A(children="paper",
              #        href=link_paper,
              #        target='_blank'),
              html.Span('''''')],
             className='faq-answer'),
])

aerosol_radius_text = "प्रभावी एरोसोल त्रिज्या (आरएच = 60% पर), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["अधिकतम वायरल निष्क्रियता दर (आरएच = 100% पर), \u03BB", html.Sub('vmax'), " (/hr): "])

pop_immunity_header = "जनसंख्या प्रतिरक्षा: "
perc_immune_label = html.Span(["प्रतिरक्षा प्रतिशत p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["संक्रामक प्रतिशत p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["टीकाकरण प्रतिशत p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["पूर्व में संक्रमित प्रतिशत p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["अतिसंवेदनशील प्रतिशत p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''जनसंख्या में संक्रामक प्रतिशत p''', html.Sub('i'), '''की गणना अन्य जोखिम 
परिदृश्य टैब में दर्ज संक्रामक प्रसार से की जाती है (संक्रमण की व्यापकता को देखते हुए…… मेरे व्यक्तिगत जोखिम को सीमित 
करने के लिए…… ) । प्रतिशत प्रतिरक्षा p''', html.Sub('im'), ''' का अनुमान जनसंख्या के टीकाकरण प्रतिशत और जनसंख्या में 
कुल मामलों की दर, और पूर्व निर्धारित 'बिना पता चले मामलों' के योगदान की उपेक्षा करके से लगाया जा सकता है। इन दो 
मूल्यों का उपयोग अतिसंवेदनशील प्रतिशत p''', html.Sub('s'), ''' की गणना के लिए किया जाता है। बेसिक और पहले रिस्क मोड 
में (यदि कोई संक्रमित व्यक्ति प्रवेश करता है ...), यह मान 100% माना जाता है।''']),
                              html.Br(),
                              html.Div(['''यहाँ p''', html.Sub('i'), ''' और p''',
                                        html.Sub('im'), '''का अनुमान लगाने के लिए कुछ उपयोगी लिंक दिए गए हैं: ''',
                                        html.Span(html.A(href=links.link_cdc_dashboard,
                                                         children="सी डी सी कोविड -19 डेटा ट्रैकर",
                                                         target='_blank')),
                                        html.Span(", "),
                                        html.Span(html.A(href=links.link_jhu_data,
                                                         children="जे एच यू कोरोनावायरस रिसोर्स सेंटर",
                                                         target='_blank')),
                                        html.Span(", "),
                                        html.A(children="यूएस इम्युनिटी एस्टिमेट्स",
                                               href=links.link_cdc_immunity,
                                               target='_blank'),
                                        html.Span(", "),
                                        html.A(children="इंटरनेशनल इम्युनिटी एस्टिमेट्स",
                                               href=links.link_jhu_vaccine,
                                               target='_blank'),
                                        ])
                              ])

values_interest_header = "आंकलित रोचक मापदंड"
values_interest_desc = html.Div([
    html.H5("वास्तव में ऐप की गणना क्या है?"),
    html.Div([
        html.Div([html.Span('''एप्लिकेशन एक आतंरिक स्थान में अधिकतम स्वीकार्य संचयी जोखिम समय, जोकि कमरे के अधिभोग और 
        समय का गुडन है, की गणना करता है। प्रति संक्रमित व्यक्ति संचरण की अपेक्षित संख्या ("इनडोर प्रजनन संख्या") को 
        चुने हुए जोखिम सहिष्णुता से कम करके कोविड -19 के प्रसार को सीमित किया जाता है। ऐप पेपर में लिखित अन्य संबंधित 
        मापदंडों की भी गणना करती है, जोकि कुछ पाठकों के लिए रोचक हो सकते हैं।'''),
                  # html.A(children="paper",
                  #        href=link_paper,
                  #        target='_blank'),
                  html.Span('''''')]),
    ], className='faq-answer'),
])
relative_sus_label = html.Span(["सापेक्ष संवेदनशीलता s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["बाहरी वायु अंश Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["एरोसोल निस्पंदन दक्षता p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["श्वास प्रवाह दर Q", html.Sub('b'), ": "])
cq_label = html.Span(["छोड़ी गई हवा C", html.Sub('q'), " की संक्रामकता: "])
mask_pass_prob_label = html.Span(["मास्क द्वारा पास होने की संभावना p", html.Sub('m'), ": "])
room_vol_label = html.Span(["कमरे का आयतन V: "])
vent_rate_Label = html.Span(["वेंटिलेशन (बाह्य) प्रवाह दर Q: "])
recirc_rate_label = html.Span(["वापसी (पुनर्संचरण) प्रवाह दर Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["वायु निस्पंदन दर (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["आर्द्रता-समायोजित एरोसोल त्रिज्या रूफ r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["आर्द्रता-समायोजित वायरल निष्क्रियकरण दर \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["प्रभावी एयरोसोल  (हवाई संक्रमण) जमाव की गति v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["एकाग्रता छूट दर \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["एयरबोर्न ट्रांसमिशन (हवाई संक्रमण) दर \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("क्या यह मॉडल स्थानीय आबादी में संक्रमण की व्यापकता पर विचार करता है? "),
    html.Div(['''स्थानीय आबादी में संक्रमण के प्रसार के प्रभाव को उन्नत मोड में देखा जा सकता है। वहां, 
    अन्य पैरामीटर्स टैब में, कोई भी आबादी में प्रतिरक्षा के प्रभाव का भी आकलन कर सकता है, जोकि टीकाकरण या पिछले 
    संक्रमण से उत्पन्न हो सकती है।'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("क्या आपके अन्य प्रश्न हैं ? "),
    html.Div([html.Span(''''''),
              # html.A(children="Beyond 6 Feet",
              #        href=link_paper,
              #        target='_blank'),
              html.Span('''अधिक विस्तृत स्पष्टीकरण और संदर्भों के लिए, "6 फीट से आगे" और अन्य लिंक वेबपेज के शीर्ष पर देखें।''')]),
])

footer = html.Div([
    html.Div([html.Span('''कोविड-19 से आतंरिक बचाव हेतु दिशानिर्देश कोविड-19 के इंडोर हवाई संक्रमण के जोखिम को 
    प्रभावित करने वाले कारकों के साथ और विभिन्न समायोजनों में जोखिम के मात्रात्मक मूल्यांकन में सहायता करने के लिए 
    इच्छुक उपयोगकर्ता को परिचित कराने के उद्देश्य से एक विकसित उपकरण है। ध्यान दें कि मॉडल मापदंडों की अनिश्चितता और 
    आंतरिक परिवर्तनशीलता परिमाण के एक आदेश के रूप में त्रुटियों को जन्म दे सकती है, जिसे पर्याप्त रूप से छोटे जोखिम 
    सहिष्णुता का चयन करके मुआवजा दिया जा सकता है। हमारे दिशानिर्देश श्वसन जेट के माध्यम से छोटी दूरी के प्रस्तारण को 
    ध्यान में नहीं रखते हैं, जो कि चेहरे के मुखौटे के रूप में नहीं पहने जा रहे है।  जैसा की पाण्डुलिपि (बेज़ान्ट और 
    बुश, २०२०) में चर्चित है।  कोविड-19 आतंरिक बचाव दिशानिर्देशों का उपयोग उपयोगकर्ता की एकमात्र जिम्मेदारी है। इसे 
    बिना किसी प्रकार की गारंटी या वारंटी के उपलब्ध कराया जा रहा है। लेखक इसके उपयोग से किसी भी दायित्व को स्वीकार 
    नहीं करते हैं।'''),
              # html.A(children="accompanying manuscript",
              #        href=link_paper,
              #        target='_blank'),
              html.Span('''''')]),
    html.Br(),
    html.Div("विशेष धन्यवाद: ")
], className='footer-small-text')
