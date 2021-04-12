import dash_html_components as html

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

Indonesian

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

# Header
header = html.Div([
    html.H1(children='Pedoman Keamanan Dalam Ruangan Untuk COVID-19'),
    html.Div([
        html.Div([html.Span(html.A(href="https://www.linkedin.com/in/kasim-k-a92620b1/",
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href="https://math.mit.edu/~bush/",
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ", dan ",
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
language_dd = "Bahasa: "

# Unit systems
units_dd = "Satuan: "
unit_settings = [
    {'label': "British", 'value': "british"},
    {'label': "Metric", 'value': "metric"},
]

# Modes
mode_dd = "Mode: "
app_modes = [
    {'label': "Dasar", 'value': "basic"},
    {'label': "Lanjut", 'value': "advanced"},
]

error_list = {
    "floor_area": "Error: Area lantai tidak boleh kosong.",
    "ceiling_height": "Error: Tinggi langit-langit tidak boleh kosong.",
    "recirc_rate": "Error: Laju resirkulasi tidak boleh kosong.",
    "aerosol_radius": "Error: Radius aerosol tidak boleh kosong.",
    "viral_deact_rate": "Error: Tingkat deaktivasi virus tidak boleh kosong.",
    "n_max_input": "Error: Jumlah orang tidak boleh kurang dari 2.",
    "exp_time_input": "Error: Waktu pemaparan harus lebih dari 0.",
    "air_exchange_rate": "Error: Tingkat Ventilasi (ACH) harus lebih besar dari 0.",
    "merv": "Error: Sistem Filtrasi (MERV) tidak boleh kosong.",
    "prevalence": "Error: Prevalensi harus lebih besar dari 0 dan kurang dari 100.000."
}

# Main Panel Text
curr_room_header = "Ruangan saat ini: "
presets = [
    {'label': "Custom", 'value': 'custom'},
    {'label': "Ruang kelas", 'value': 'classroom'},
    {'label': "Ruang keluarga", 'value': 'living-room'},
    {'label': "Gereja", 'value': 'church'},
    {'label': "Restoran", 'value': 'restaurant'},
    {'label': "Kantor", 'value': 'office'},
    {'label': "Mobil bawah tanah", 'value': 'subway'},
    {'label': "Pesawat komersial", 'value': 'airplane'},
]

curr_human_header = "Perilaku Manusia: "
presets_human = [
    {'label': "Custom", 'value': 'custom'},
    {'label': "Bermasker, Beristirahat", 'value': 'masks-1'},
    {'label': "Bermasker, Berbicara", 'value': 'masks-2'},
    {'label': "Bermasker, Berolahraga", 'value': 'masks-3'},
    {'label': "Tidak Bermasker, Beristirahat", 'value': 'no-masks-1'},
    {'label': "Tidak Bermasker, Berbicara", 'value': 'no-masks-2'},
    {'label': "Tidak Bermasker, Berolahraga", 'value': 'no-masks-3'},
    {'label': "Tidak Bermasker, Bernyanyi", 'value': 'singing-1'},
]

curr_risk_header = "Toleransi Risiko: "
risk_tol_marks = {
    # 0.01: {'label': '0.01: Lebih Aman', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Lebih Aman', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Tidak Aman'}
}

risk_tolerance_text = "Toleransi Risiko: "
risk_tol_desc = html.Div('''Populasi yang lebih rentan seperti orang tua atau mereka yang memiliki kondisi medis yang 
sudah ada sebelumnya memerlukan toleransi risiko yang lebih rendah. Toleransi risiko yang lebih tinggi berarti lebih 
banyak transmisi yang diharapkan selama waktu tinggal yang diharapkan (lihat FAQ untuk detailnya).''',
                         style={'font-size': '13px', 'margin-left': '20px'})

curr_age_header = "Kelompok Usia: "
presets_age = [
    {'label': "Anak-Anak (<15 tahun)", 'value': 0.23},
    {'label': "Dewasa (15-64 tahun)", 'value': 0.68},
    {'label': "Lanjut Usia (>64 tahun)", 'value': 1}
]
age_group_marks = {
    0.23: {'label': '0.23: Anak-Anak (<15 tahun)', 'style': {'max-width': '75px'}},
    0.68: {'label': '0.68: Dewasa (15-64 tahun)', 'style': {'max-width': '75px'}},
    1: {'label': '1.00: Lanjut Usia (>64 tahun)', 'style': {'width': '75px'}}
}

curr_strain_header = "Strain Virus: "
presets_strain = [
    # {'label': "SARS-CoV-1", 'value': 0.1},
    {'label': "SARS-CoV-2 (Wuhan Strain)", 'value': 1},
    {'label': "SARS-CoV-2 - B.1.1.7 (UK Strain)", 'value': 1.58}
]
viral_strain_marks = {
    1: {'label': '1.0: Wuhan', 'style': {'max-width': '100px'}},
    1.58: {'label': '1.58: B.1.1.7/UK'}
}

pim_header = "Persentase immun: "
# pim_marks = {
#     0: {'label': '0% (mode dasar)'},
#     0.33: {'label': '33% (bawaan)'},
#     1: {'label': '100%'}
# }

risk_conditional_desc = "Jika seseorang yang terinfeksi memasuki..."
risk_prevalence_desc = "Dengan prevalensi infeksi..."
risk_personal_desc = "Untuk membatasi risiko pribadi saya..."

main_panel_s1 = "Berdasarkan model ini, ruangan ini akan aman* jika memiliki: "

main_panel_s1_b = html.Span([
    html.Span('''Untuk membatasi penularan* COVID-19 dalam populasi dengan prevalensi infeksi '''),
    html.Sup('''1'''),
    html.Span(''' of ''')
])
main_panel_s2_b = ''' per 100,000, ruangan ini seharusnya tidak lebih dari:  '''

main_panel_s1_c = html.Span([
    html.Span('''Untuk membatasi peluang saya terinfeksi COVID-19 dalam populasi dengan prevalensi1 infeksi '''),
    html.Sup('''1'''),
    html.Span(''' of ''')
])
main_panel_s2_c = ''' per 100,000, ruangan ini seharusnya tidak lebih dari: '''

units_hr = 'jam'
units_min = 'menit'
units_days = 'hari'
units_months = 'beberapa bulan'

units_hr_one = 'jam'
units_min_one = 'menit'
units_day_one = 'hari'
units_month_one = 'bulan'

is_past_recovery_base_string = '{n_val} orang selama >{val:.0f} jam,'
model_output_base_string = '{n_val} orang selama '

main_panel_six_ft_1 = "Sebaliknya, pedoman jaga jarak enam kaki (atau dua meter) akan membatasi hunian menjadi "
main_panel_six_ft_2 = " yang akan melanggar pedoman* setelah "

six_ft_base_string = ' hingga {} orang'
six_ft_base_string_one = ' hingga {} orang'

graph_title = "Penggunaan Ruang vs. Waktu Paparan"
graph_xtitle = "Waktu paparan maksimum \u03C4 (jam)"
graph_ytitle = "Maximum Occupancy N"
transient_text = "Transien"
steady_state_text = "Kondisi tunak"

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

other_risk_modes_desc = html.Div('''Skenario risiko lain dipertimbangkan dalam Mode Lanjutan. Secara khusus, seseorang dapat 
  mempertimbangkan prevalensi infeksi dalam populasi, kekebalan yang diperoleh melalui vaksinasi atau paparan sebelumnya, dan 
  risiko terhadap individu tertentu.''')

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

airb_trans_only_disc = html.Div('''Panduan ini berdasarkan pertimbangan penularan melalui udara dari satu orang 
yang terinfeksi selama waktu paparan kumulatif tertentu (lihat daftar). ''', className='airborne-text')

incidence_rate_refs = html.Div([html.Sup('''1'''),
                                html.Span('''Untuk memperkirakan prevalensi lokal Anda, berikut beberapa sumber yang dapat digunakan: '''),
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
n_input_text_1 = "Jika ruangan ini memiliki "
n_max_base_string = ' {:.0f} orang'
n_max_overflow_base_string = ' >{:.0f} orang'
n_input_text_2 = " orang, pedoman tersebut* akan dilanggar setelah "
n_input_text_3 = "."

t_input_text_1 = "Jika orang-orang menempati ruang tersebut selama kira-kira "
t_input_text_2 = " jam, jumlah orang yang bisa menempati ruang tersebut seharusnya dibatasi sebanyak "
t_input_text_3 = "."

# About
about_header = "Tentang"
about = html.Div([
    html.H6("Tentang", style={'margin': '0'}),
    html.Div('''Untuk mengurangi penyebaran COVID-19, pedoman kesehatan masyarakat resmi telah merekomendasikan 
    batasan pada: jarak orang-ke-orang (6 kaki / 2 meter), waktu tinggal (15 menit), kapasitas maksimum (25 orang), 
    atau ventilasi minimum (6 perubahan udara per jam).'''),
    html.Br(),
    html.Div([html.Span('''Ada '''),
              html.A(children="bukti ilmiah",
                     href=link_docs,
                     target='_blank'),
              html.Span(''' yang berkembang untuk penularan COVID-19 melalui udara, yang terjadi ketika tetesan 
              aerosol yang menular dipertukarkan dengan menghirup udara dalam ruangan bersama. Sementara organisasi 
              kesehatan masyarakat mulai mengakui penularan melalui udara, mereka belum memberikan pedoman 
              keselamatan yang memasukkan semua variabel yang relevan.''')]),
    html.Br(),
    html.Div([html.Span('''Aplikasi ini, dikembangkan oleh Kasim Khan bekerja sama dengan Martin Z. Bazant dan John 
    W. M. Bush, menggunakan '''),
              html.A(children="model teoritis",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' untuk menghitung waktu paparan yang aman dan kapasitas ruangan. Dengan menyesuaikan 
              spesifikasi ruangan, tingkat ventilasi dan filtrasi, penggunaan masker, aktivitas pernapasan, 
              dan toleransi risiko (di tab lain), Anda dapat melihat cara mengurangi penularan COVID-19 dalam ruangan 
              (indoor), di berbagai ruangan yang berbeda.''')]),
    html.Br(),
    html.Div([html.Span('''Sains dibalik aplikasi ini juga diajarkan secara gratis, mandiri secara massif, kursus daring terbuka (MOOC) pada edX: '''),
              html.A(children="10.S95x Physics of COVID-19 Transmission",
                     href=links.link_mooc,
                     target='_blank')])
])

# Room Specifications
room_header = "Spesifikasi Ruangan - Detail"

floor_area_text = "Total luas lantai (sq. ft.): "
floor_area_text_metric = "Total luas lantai (m²): "
ceiling_height_text = "Tinggi langit-langit rata-rata (ft.): "
ceiling_height_text_metric = "Tinggi langit-langit rata-rata (m): "

ventilation_text = "Sistem Ventilasi: "
vent_type_output_base = "{:.0f} ACH"
vent_type_output_units = html.Span(["hr", html.Sup("-1"), " (ACH Luar ruangan)"])
ventilation_text_adv = html.Span(["Ventilation (hr", html.Sup("-1"), ", ACH Luar ruangan): "])
ventilation_types = [
    {'label': "Jendela-jendela tertutup", 'value': 0.3},
    {'label': "Jendela-jendela terbuka", 'value': 2},
    {'label': "Ventilasi Mekanis", 'value': 3},
    {'label': "Jendela-jendela terbuka dengan kipas angin", 'value': 6},
    {'label': "Ventilasi Mekanis yang Lebih Baik", 'value': 8},
    {'label': "Laboratorium, Restoran", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Rumah Sakit/Kereta Jalur Bawah Tanah", 'value': 18},
    {'label': "Toxic Laboratory/Pesawat", 'value': 24},
]

filtration_text = "Sistem Filtrasi: "
filt_type_output_base = "MERV {:.0f}"
filtration_text_adv = "Sistem Filtrasi (MERV): "
filter_types = [
    {'label': "Tidak Ada", 'value': 0},
    {'label': "Jendela Perumahan AC", 'value': 2},
    {'label': "Perumahan/Komersial/Industri", 'value': 6},
    {'label': "Perumahan/Komersial/Rumah Sakit", 'value': 10},
    {'label': "Rumah Sakit & Bedah Umum", 'value': 14},
    {'label': "HEPA", 'value': 17}
]

recirc_text = "Laju Resirkulasi: "
recirc_type_output_base = "{:.1f} recirculation ACH"
recirc_text_adv = "Laju Resirkulasi (recirculation ACH): "
recirc_types = [
    {'label': "Tidak Ada", 'value': 0},
    {'label': "Lambat", 'value': 0.3},
    {'label': "Sedang", 'value': 1},
    {'label': "Cepat", 'value': 10},
    {'label': "Pesawat Terbang", 'value': 24},
    {'label': "Kereta Jalur Bawah Tanah", 'value': 54},
]

humidity_text = "Humiditas Relatif: "
humidity_marks = {
    0: {'label': '0%: Sangat kering', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: Pesawat terbang', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Kering'},
    0.6: {'label': '60%: Rata-rata'},
    0.99: {'label': '99%: Sangat Lembab'},
}

need_more_ctrl_text = '''Perlu lebih banyak kontrol atas input Anda? Beralih ke Mode Lanjutan menggunakan pilihan di 
bagian atas halaman. '''

human_header = "Perilaku Manusia - Detail"
# Human Behavior
exertion_text = "Tingkat Pernapasan: "
exertion_types = [
    {'label': "Beristirahat", 'value': 0.49},
    {'label': "Berdiri", 'value': 0.54},
    {'label': "Bernyanyi", 'value': 1},
    {'label': "Olahraga Ringan", 'value': 1.38},
    {'label': "Olahraga Sedang", 'value': 2.35},
    {'label': "Olahraga Berat", 'value': 3.30},
]

breathing_text = "Aktivitas Pernafasan: "
expiratory_types = [
    {'label': "Bernafas (ringan)", 'value': 1.1},
    {'label': "Bernafas (normal)", 'value': 4.2},
    {'label': "Bernafas (berat)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Berbicara (berbisik)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Berbicara (normal)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Berbicara (nyaring)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Bernyanyi", 'value': 970},
]

mask_type_text = "Efisiensi Filtrasi Masker (tipe makser): "
mask_type_marks = {
    0: {'label': "0% (tidak ada, pelindung wajah)", 'style': {'max-width': '75px'}},
    0.5: {'label': "50% (katun, flanel)", 'style': {'max-width': '50px'}},
    0.7: {'label': "70% (kapas multilayer, sutra)", 'style': {'max-width': '75px'}},
    0.90: {'label': "90% (masker bedah sekali pakai)", 'style': {'max-width': '75px'}},
    # 0.99: {'label': "99% (N95 Respirator)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Tidak ada, Pelindung Wajah", 'value': 0},
    {'label': "Katun, Flanel", 'value': 0.5},
    {'label': "Kapas Multilayer, Sutra", 'value': 0.7},
    {'label': "Masker bedah sekali pakai", 'value': 0.9},
    {'label': "N95 Respirator", 'value': 0.99},
]

mask_fit_text = "Kesesuaian Masker: "
mask_fit_marks = {
    0: {'label': '0%: Tidak ada', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Buruk'},
    0.95: {'label': '95%: Bagus'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Pertanyaan yang Sering Ditanyakan:"
other_io = "Parameter-parameter Lain"

faq_top = html.Div([
    html.H6("Pertanyaan yang Sering Diajukan"),
    html.H5("Mengapa jarak 6 kaki / 2 meter tidak cukup?"),
    html.Div([
        html.Div([html.Span('''Jarak 6 kaki (atau 2 meter) melindungi Anda dari tetesan besar yang dikeluarkan oleh 
          orang yang terinfeksi ketika batuk, seperti yang dilakukan oleh masker wajah; namun, ini tidak melindungi dari  '''),
                  html.A(children="penularan melalui udara",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' oleh aerosol infeksius yang tersuspensi di udara dan bercampur di seluruh ruangan. Di dalam 
                    ruangan, orang tidak lebih aman dari transmisi udara pada ketinggian 60 kaki daripada 6 kaki. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Apakah ada cara penularan lain?"),
    html.Div([
        html.Div([html.A(children="Penularan melalui udara",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' dianggap dominan untuk COVID-19, tetapi mode lain dimungkinkan, seperti penularan 
                  ‘fomite’ melalui kontak langsung dengan residu infeksi di permukaan, transmisi ‘tetesan besar’ 
                  melalui batuk atau bersin, dan ‘aerosol jarak pendek’ transmisi dari pernapasan orang yang 
                  terinfeksi dalam waktu lama. Meskipun dua mode terakhir mungkin signifikan, mode ini sebagian besar 
                  dihilangkan saat masker wajah atau penutup wajah dikenakan; namun, risiko penularan melalui udara 
                  tetap ada.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Bisakah kita benar-benar menganggap udara di suatu ruangan tercampur dengan baik? "),
    html.Div([
        html.Div([html.Span('''Ada banyak kontributor untuk pencampuran di ruang dalam ruangan, termasuk aliran yang 
        digerakkan oleh daya apung (dari pemanas, AC atau jendela), konveksi paksa dari ventilasi dan kipas angin, 
        serta gerakan dan pernapasan manusia. Meskipun ada pengecualian, seperti yang dibahas di '''),
                  html.A(children="makalah ini",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', asumsi campuran baik digunakan secara luas dalam pemodelan teoretis penularan 
                  penyakit melalui udara.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Apakah pedoman tersebut berlaku untuk ruang yang sangat besar?"),
    html.Div([
        html.Div([html.Span('''Di gedung konser, stadion, atau ruang berventilasi besar lainnya dengan banyak orang, 
        risiko penularan melalui udara menjadi signifikan dan tercakup di dalam pedoman. Namun, jika masker atau 
        pelindung wajah tidak dipakai, ada risiko tambahan penularan jarak pendek melalui jet pernapasan, yang telah 
        diperkirakan di '''),
                  html.A(children="makalah ini",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("Mengapa ketinggian langit-langit menjadi penting?"),
    html.Div([
        '''Ketinggian langit-langit mempengaruhi total volume ruangan, yang diperlukan untuk memperkirakan 
        konsentrasi aerosol infeksius (#aerosol per satuan volume). Konsentrasi ini diperlukan untuk memperkirakan 
        risiko penularan COVID-19 dalam ruangan. '''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Saya tahu angka ACH / MERV saya. Di mana saya bisa memasukkannya?"),
    html.Div('''
        Jika Anda membutuhkan lebih banyak kontrol atas input Anda, alihkan ke Mode Lanjutan menggunakan menu di bagian 
        atas halaman web.
    ''', className='faq-answer'),
    html.Br(),
    html.H5("Mengapa Respirator N95 memiliki efisiensi 99%?"),
    html.Div('''Respirator N95 memiliki efisiensi penyaringan setidaknya 95% pada ukuran partikel 0,3 μm, 10 kali lebih 
      kecil dari ukuran tetesan pada transmisi COVID-19 di udara. Untuk tetesan yang lebih besar, respirator N95 bahkan 
      lebih efisien, mendekati level mendekati 100%. ''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("Apakah ada parameter tersembunyi dalam Mode Dasar?"),
    html.Div([html.Span('''Semua parameter fisik yang relevan secara terperinci di laporkan di '''),
              html.A(children="makalah ini",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. Dalam Mode Dasar, aplikasi mengasumsikan radius aerosol efektif 2 μm (pada kelembapan 
              60%) dan tingkat deaktivasi virus maksimum 0,6 / jam (pada ~ 100% kelembapan), keduanya meningkat 
              dengan kelembapan relatif (RH). Perkiraan tingkat galat deaktivasi virus di sisi konservatif deaktivasi 
              yang lebih lambat. Tingkat deaktivasi virus dapat ditingkatkan dengan radiasi ultraviolet (UV-C) atau 
              disinfektan kimiawi (misalnya hidrogen peroksida, ozon). Aplikasi ini juga memperkirakan parameter 
              utama penyakit, penularan melalui hembusan udara, C'''),
              html.Sub("q"),
              html.Span(''' (kuanta infeksi per unit volume), dari aktivitas pernapasan tertentu, menggunakan nilai 
              tabulasi pada Gambar 2 dari '''),
              html.A(children="makalah ini",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. Anda menentukan sendiri parameter ini dalam Mode Lanjutan.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Radius Aerosol Efektif (pada RH = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Tingkat Deaktivasi Virus Maksimum (pada RH = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

pop_immunity_header = "Imunitas Populasi: "
perc_immune_label = html.Span(["Persentase immun p", html.Sub('im'), " = p", html.Sub('ex'), " + p", html.Sub('v'),
                               " = "])
perc_infectious_label = html.Span(["Persentase infeksi p", html.Sub('i'), " = "])
perc_vaccinated_label = html.Span(["Persentase yang divaksinasi p", html.Sub('v'), " ="])
perc_prev_infected_label = html.Span(["Persentase yang terinfeksi sebelumnya p", html.Sub('ex'), " = "])
perc_susceptible_label = html.Span(["Persentase rentan p", html.Sub('s'), " = 1 - (p", html.Sub('im'), " + p",
                                    html.Sub('i'), ") = "])
pop_immunity_desc = html.Div([html.Div(['''Persentasi infeksi p''', html.Sub('i'), ''' dalam populasi dihitung dari 
  prevalensi infeksius yang dimasukkan dalam tab skenario risiko lainnya (Dengan prevalensi infeksi…, Untuk membatasi 
  risiko pribadi saya…). Persentasi immun  p''', html.Sub('im'), ''' dapat diperkirakan secara konservatif dari persentase 
  vaksinasi populasi ditambah tingkat kasus total dalam populasi, dengan mengabaikan kontribusi dari kasus yang tidak 
  terdeteksi. Kedua nilai ini digunakan untuk menghitung persentase yang rentan p''', html.Sub('s'), '''. Dalam Mode Dasar 
  dan dalam mode risiko pertama (Jika seseorang yang terinfeksi memasuki…), nilai ini diasumsikan 100%.''']),
                              html.Br(),
                              html.Div(['''Berikut ini beberapa tautan yang dapat digunakan untuk menemukan p''', html.Sub('i'), ''' dan p''',
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

values_interest_header = "Nilai-Nilai yang Dihitung: "
values_interest_desc = html.Div([
    html.H5("Apa sebenarnya yang dihitung aplikasi ini?"),
    html.Div([
        html.Div([html.Span('''Aplikasi ini menghitung waktu paparan kumulatif maksimum yang diizinkan, produk dari 
          hunian suatu ruangan dan waktu, di ruang dalam ruangan. Penyebaran COVID-19 dibatasi dengan mensyaratkan 
          bahwa jumlah penularan yang diharapkan per individu yang terinfeksi, "nomor reproduksi dalam ruangan", kurang 
          dari toleransi risiko yang dipilih. Aplikasi ini juga menghitung jumlah terkait, yang dijelaskan di '''),
                  html.A(children="makalah ini",
                         href=links.link_paper,
                         target='_blank'),
                  html.Span(''', yang mungkin menarik untuk dibaca:''')]),
    ], className='faq-answer'),
])
relative_sus_label = html.Span(["Kerentanan relatif s", html.Sub('r'), ": "])
outdoor_air_frac_label = html.Span(["Fraksi udara luar ruangan Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Efisiensi filtrasi aerosol p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Laju aliran pernafasan Q", html.Sub('b'), ": "])
cq_label = html.Span(["Penularan dari hembusan udara C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Kemungkinan lolos melalui masker p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Volume ruangan V: "])
vent_rate_Label = html.Span(["Laju aliran ventilasi (luar ruangan) Q: "])
recirc_rate_label = html.Span(["Laju alir resirkulasi Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Laju alir filtrasi udara (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Jari-jari aerosol yang disesuaikan dengan kelembaban r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Tingkat deaktivasi virus yang disesuaikan dengan kelembaban \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Kecepatan pengendapan aerosol yang v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Laju relaksasi konsentrasi \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Laju penularan melalui udara \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("Apakah model ini memperhitungkan prevalensi infeksi pada populasi lokal?"),
    html.Div(['''Pengaruh prevalensi infeksi pada populasi lokal dapat dipertimbangkan dalam Mode Lanjutan. Di sana, di 
      tab Parameter Lain, seseorang juga dapat menilai pengaruh kekebalan dalam populasi, seperti yang mungkin timbul melalui 
      vaksinasi atau infeksi sebelumnya.'''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("Pertanyaan Lain?"),
    html.Div([html.Span('''Untuk penjelasan lebih detil dan referensi, lihat "'''),
              html.A(children="Beyond 6 Feet",
                     href=link_paper,
                     target='_blank'),
              html.Span('''" dan tautan lain yang dipasang di bagian atas halaman web.''')]),
])

footer = html.Div([
    html.Div([html.Span('''Pedoman Keamanan Dalam Ruangan COVID-19 adalah alat yang berkembang yang dimaksudkan untuk 
    membiasakan pengguna yang tertarik dengan faktor-faktor yang mempengaruhi risiko penularan COVID-19 melalui udara 
    dalam ruangan, dan untuk membantu dalam penilaian kuantitatif risiko di berbagai pengaturan. Kami mencatat bahwa 
    ketidakpastian dan variabilitas intrinsik dari parameter model dapat menyebabkan kesalahan sebesar urutan 
    besarnya, yang dapat dikompensasikan dengan memilih toleransi risiko yang cukup kecil. Pedoman kami tidak 
    memperhitungkan transmisi jarak pendek melalui jet pernapasan, yang secara substansial dapat meningkatkan risiko 
    saat masker tidak dipakai, dengan cara yang dibahas dalam '''),
              html.A(children="manuskrip yang menyertai",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' (Bazant & Bush, 2020). Penggunaan Pedoman Keamanan Dalam Ruangan COVID-19 adalah tanggung 
              jawab pengguna sepenuhnya. Pedoman tersebut tersedia tanpa jaminan atau jaminan apa pun. Penulis tidak 
              bertanggung jawab atas penggunaannya.''')]),
    html.Br(),
    html.Div("Ucapan Terimakasih kepada: ")
], className='footer-small-text')
