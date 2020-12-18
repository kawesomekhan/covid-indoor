import dash_html_components as html

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
    "merv": "त्रुटि: निस्पंदन प्रणाली (MERV) रिक्त नहीं हो सकता ।"
}

# Main Panel Text
curr_room_header = "चालू कक्ष: "
presets = [
    {'label': "अपने अनुसार", 'value': 'custom'},
    {'label': "उपनगरीय आवास", 'value': 'house'},
    {'label': "जलपान गृह", 'value': 'restaurant'},
    {'label': "एकांत कार्यालय", 'value': 'office'},
    {'label': "व्याख्यान कक्ष", 'value': 'classroom'},
    {'label': "न्यूयॉर्क सिटी सबवे कार", 'value': 'subway'},
    {'label': "बोइंग 737", 'value': 'airplane'},
    {'label': "मंदिर (गिरिजाघर)", 'value': 'church'},
]

main_panel_s1 = "इस मॉडल के आधार पर, यह कक्ष निम्न अवधि तथा लोगों की संख्या के लिए सुरक्षित होना चाहिए: "

units_hr = 'घंटों'
units_min = 'मिनट'
units_days = 'दिनों'

units_hr_one = 'घंटों'
units_min_one = 'मिनट'
units_day_one = 'दिनों'
model_output_suffix = ' के लिए '

is_past_recovery_base_string = '>{val:.0f} दिनों के लिए {n_val} लोग'
model_output_base_string = '{n_val} लोग'

main_panel_six_ft_1 = "ध्यान दें कि छह-फुट या दो-मीटर की दूरी के दिशानिर्देशों का संकेत है कि "
main_panel_six_ft_2 = " तक इस कमरे में  अनिश्चित काल के लिए सुरक्षित रहेंगे।"

six_ft_base_string = ' {} लोग'
six_ft_base_string_one = ' {} लोग'

graph_title = "ठहराव (अध्यावास) बनाम एक्सपोज़र (उजागर) समय"
graph_xtitle = "अधिकतम एक्सपोज़र टाइम \u03C4 (घंटे)"
graph_ytitle = "अधिकतम ठहराव (अध्यावास) N"
transient_text = "क्षणिक / अस्थायी"
steady_state_text = "स्थिर अवस्था"

main_airb_trans_only_disc = html.Div(["",
                                      html.Span(html.A(href='https://www.nature.com/articles/d41586-020-02058-1',
                                                       children="यह दिशानिर्देश एक संक्रमित व्यक्ति से हवा द्वारा प्रसारण के कुल एक्सपोज़र समय पर आधारित है।",
                                                       target='_blank'), ),
                                      html.Span('''''')], className='airborne-text')

airb_trans_only_disc = html.Div('''यह दिशानिर्देश एक संक्रमित व्यक्ति से हवा द्वारा प्रसारण के कुल एक्सपोज़र समय पर आधारित है।''', className='airborne-text')

# Bottom panels text
n_input_text_1 = "यदि इस कमरे में "
n_max_base_string = ' {:.0f} लोग'
n_input_text_2 = " लोग हैं, तो इसके रहने वाले "
n_input_text_3 = " तक सुरक्षित रहने चाहिए |"

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
])

# Room Specifications
room_header = "कक्ष विशिष्टियां"

floor_area_text = "कुल तल क्षेत्रफल  (वर्ग फुट): "
floor_area_text_metric = "कुल तल क्षेत्रफल (m²): "
ceiling_height_text = "औसतन छत की ऊंचाई (फुट): "
ceiling_height_text_metric = "औसतन छत की ऊंचाई (m): "

ventilation_text = "वेंटिलेशन प्रणाली: "
vent_type_output_base = "{:.0f} एसीएच"
ventilation_text_adv = "वेंटिलेशन प्रणाल (एसीएच): "
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
    0: {'label': '0%: बहुत सूखी', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: हवाई जहाज', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: सूखा'},
    0.6: {'label': '60%: औसतन'},
    0.99: {'label': '99%: बहुत नम'},
}

need_more_ctrl_text = '''क्या आप अपने निवेश(इनपुट) पर अधिक नियंत्रण करना चाहते हैं? इस पेज के शीर्ष पर ड्रॉपडाउन मेनू 
में एडवांस/अग्रिम मोड पर स्विच करें। '''

human_header = "मानवीय व्यवहार"
# Human Behavior
exertion_text = "तनाव स्तर: "
exertion_types = [
    {'label': "विश्राम स्थिति ", 'value': 0.49},
    {'label': "खड़े रहने कि स्थिति ", 'value': 0.54},
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
    0: {'label': "0% (कोई नहीं, फेस शील्ड)", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (मोटा सूती कपडा)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (रेशमी, फलालैन,शिफॉन)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (शल्यक/सर्जिकल, सूती)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (N95 रेस्पिरेटर /श्वासयंत्र)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "कोई नहीं, फेस शील्ड ", 'value': 0},
    {'label': "मोटा सूती कपडा ", 'value': 0.1},
    {'label': "रेशमी, फलालैन,शिफॉन ", 'value': 0.5},
    {'label': "शल्यक/सर्जिकल, सूती ", 'value': 0.9},
    {'label': "N95 रेस्पिरेटर/ श्वासयंत्र", 'value': 0.95},
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
    0.01: {'label': '0.01: ज्यादा सुरक्षित', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: सुरक्षित', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: असुरक्षित'}
}

# FAQ/Other Inputs & Outputs
faq_header = "प्रायः पूछे जाने वाले प्रश्न"
other_io = "अन्य निवेश (इनपुट) और निर्गम (ऑउटपुट)"

faq_top = html.Div([
    html.H6("प्रायः पूछे जाने वाले प्रश्न"),
    html.H5("6 फीट / 2 मीटर की दूरी पर्याप्त क्यों नहीं है?"),
    html.Div([
        html.Div([html.Span(''''''),
                  # html.A(children="airborne transmission",
                  #        href=link_docs,
                  #        target='_blank'),
                  html.Span('''6 फीट / 2 मीटर दूरी आपको एक संक्रमित व्यक्ति द्वारा खांसते हुए बड़ी बूंदों से बचाती 
                  है, जैसा कि फेस मास्क करते हैं; हालाँकि, यह संक्रामक एरोसोल द्वारा हवा से फैलने वाले संक्रमण के 
                  विरुद्ध रक्षा नहीं करता है और यह पूरे कमरे में फ़ैल सकता है । इस प्रकार घर के अंदर के लोग 60 फीट की 
                  अपेक्षा 6 फीट की दूरी पर हवाई प्रसारण से सुरक्षित नहीं हैं।''')]),
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

values_interest_header = ""
values_interest_desc = html.Div([
    html.H5("वास्तव में ऐप की गणना क्या है?"),
    html.Div([
        html.Div([html.Span('''हवाई प्रसारण के लिए एक जोखिम सहिष्णुता को देखते हुए, ऐप अधिकतम स्वीकार्य कुल उजागर 
        समय, कमरे में ठहराव के उत्पाद और संक्रमित व्यक्ति की उपस्थिति के समय की गणना करता है। एप और भी कई संबंधित 
        मात्राओं की गणना करता है, जोकि पेपर में परिभाषित है, और कुछ लोगों के लिए दिलचस्प हो सकता है।  '''),
                  # html.A(children="paper",
                  #        href=link_paper,
                  #        target='_blank'),
                  html.Span('''''')]),
    ], className='faq-answer'),
])
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
    html.Div(['''नहीं। यह मॉडल एक संक्रमित व्यक्ति से संचरण के जोखिम की गणना करता है। इस प्रकार यह जनसंख्या में 
    संक्रमण की व्यापकता को कम मानता है। इस सीमा में, कमरे में संक्रमित व्यक्तियों की अनुमानित संख्या के साथ संचरण का 
    खतरा बढ़ जाता है, विशेष रूप से ठहराव और आबादी में प्रसार के उत्पाद को । यदि यह मात्रा एक से अधिक हो तो सहिष्णुता 
    को इस संख्या के अनुपात में कम किया जाना चाहिए। इसके विपरीत, जब कमरे में संक्रमित व्यक्तियों की अपेक्षित संख्या 
    शून्य तक पहुंच जाये तो अनुशंसित प्रतिबंधों को अनावश्यक नहीं माने जाने तक सहिष्णुता आनुपातिक रूप से बढ़ायी जा सकती 
    है।'''],
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
