from dash import html

"""
descriptions.py contains all English text used throughout the app (Basic, Advanced Mode).

Spanish

"""

link_paper = "https://www.medrxiv.org/content/10.1101/2020.08.26.20182824v2"
link_docs = "https://docs.google.com/document/d/1fB5pysccOHvxphpTmCG_TGdytavMmc1cUumn8m0pwzo/edit"

# Header
header = html.Div([
    html.H1(children='COVID-19 Directriz de Seguridad en Espacios Interiores'),
    html.Div([
        html.Div([html.Span(html.A(href="https://www.linkedin.com/in/kasim-k-a92620b1/",
                                   children="Kasim Khan",
                                   target='_blank')),
                  ", ",
                  html.Span(html.A(href="https://math.mit.edu/~bush/",
                                   children="John W. M. Bush",
                                   target='_blank')),
                  ", y ",
                  html.Span(html.A(href="https://www.mit.edu/~bazant/",
                                   children="Martin Z. Bazant",
                                   target='_blank')),
                  ""]),
        html.Div([html.Span(["Más Allá de los Seis Pies (Dos Metros): Una Directriz para Limitar la Transmisión Aérea "
                             "del Covid-19 en Espacios Interiores ("]),
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
language_dd = "Idioma: "

# Unit systems
units_dd = "Unidades: "
unit_settings = [
    {'label': "Inglés (Reino Unido)", 'value': "british"},
    {'label': "Métrico", 'value': "metric"},
]

# Modes
mode_dd = "Modo: "
app_modes = [
    {'label': "Básico", 'value': "basic"},
    {'label': "Avanzado", 'value': "advanced"},
]

error_list = {
    "floor_area": "Error: El área del piso no puede estar vacía.",
    "ceiling_height": "Error: La altura del techo no puede estar vacía.",
    "recirc_rate": "Error: La tasa de recirculación del aire no puede estar vacía.",
    "aerosol_radius": "Error: El radio de aerosoles no puede estar vacía.",
    "viral_deact_rate": "Error: La tasa de desactivación viral no puede estar vacía.",
    "n_max_input": "Error: El número de personas no puede ser menor a 2.",
    "exp_time_input": "Error: El tiempo de exposición debe ser mayor a 0.",
    "air_exchange_rate": "Error: La Tasa de Ventilación (Cambios de Aire por Hora - ACH) debe ser mayor a 0.",
    "merv": "Error: El Sistema de Filtracion no puede estar vacía."
}

# Main Panel Text
curr_room_header = "Espacio actual: "
presets = [
    {'label': "Personalizado", 'value': 'custom'},
    {'label': "Vivienda suburbana", 'value': 'house'},
    {'label': "Restaurante", 'value': 'restaurant'},
    {'label': "Oficina Tranquila", 'value': 'office'},
    {'label': "Salón de Clase [Aula]", 'value': 'classroom'},
    {'label': "Vagón del Metro [Subterráneo] de la Ciudad de Nueva York", 'value': 'subway'},
    {'label': "Boeing 737", 'value': 'airplane'},
    {'label': "Iglesia [Templo]", 'value': 'church'},
]

main_panel_s1 = "Con base en este modelo, debería considerarse seguro* que este espacio tenga: "

units_hr = 'horas'
units_min = 'minutos'
units_days = 'días'

units_hr_one = 'hora'
units_min_one = 'minuto'
units_day_one = 'día'

is_past_recovery_base_string = '{n_val} personas por >{val:.0f} días,'
model_output_base_string = '{n_val} personas por '

main_panel_six_ft_1 = "Nótese que la directriz usual de distanciamiento de seis pies o dos metros indicaría que hasta "
main_panel_six_ft_2 = " estarían seguras en este espacio por un período indefinido."

six_ft_base_string = ' {} personas'
six_ft_base_string_one = ' {} persona'

graph_title = "Ocupación vs. Tiempo de Exposición"
graph_xtitle = "Tiempo de Exposición Máxima \u03C4 (horas)"
graph_ytitle = "Ocupación Máxima N"
transient_text = "Transitorio [Transeúnte]"
steady_state_text = "Estado Estable [Estacionario]"

main_airb_trans_only_disc = html.Div(["*La directriz se basa en la consideración de la ",
                                      html.Span(html.A(href='https://www.nature.com/articles/d41586-020-02058-1',
                                                       children="transmisión aérea",
                                                       target='_blank'), ),
                                      html.Span(''' de una sola persona infectada sobre el tiempo de exposición 
                                      acumulado señalado.''')], className='airborne-text')

airb_trans_only_disc = html.Div('''La directriz se basa en la consideración de la transmisión aérea de una sola 
persona infectada sobre el tiempo de exposición acumulado señalado.''', className='airborne-text')

# Bottom panels text
n_input_text_1 = "Si esta habitación tiene "
n_max_base_string = ' {:.0f} personas'
n_input_text_2 = " personas, sus ocupantes deberían estar seguros por "
n_input_text_3 = "."

t_input_text_1 = "Si las personas permanecen aproximadamente "
t_input_text_2 = " horas en este lugar, la ocupación debería limitarse a "
t_input_text_3 = "."

# About
about_header = "Sobre"
about = html.Div([
    html.H6("Sobre", style={'margin': '0'}),
    html.Div('''Para mitigar la propagación del COVID-19, las directrices de salud pública oficiales han recomendado 
    límites sobre: el distanciamiento entre personas (6 pies/2 metros), tiempo de ocupación (15 minutos), 
    ocupación máxima (25 personas), o ventilación mínima (6 cambios de aire por hora) '''),
    html.Br(),
    html.Div([html.Span('''Existe una creciente '''),
              html.A(children="evidencia científica",
                     href=link_docs,
                     target='_blank'),
              html.Span(''' de la transmisión aérea del COVID-19, la cual ocurre cuando se intercambian pequeñas gotas 
              infecciosas [aerosoles] al respirar el aire compartido en espacios interiores. Aunque las 
              organizaciones de salud pública están comenzando a reconocer la transmisión aérea, aún deben brindar 
              una directriz que incorpore todas las variables relevantes.''')]),
    html.Br(),
    html.Div([html.Span('''Esta aplicación, desarrollada por Kasim Khan en colaboración con Martin Z. Bazant y John 
    W. M. Bush, utiliza un '''),
              html.A(children="modelo teórico",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' para establecer períodos de exposición y niveles de ocupación seguros para espacios 
              interiores. Mediante el ajuste de las especificaciones, las tasas de ventilación y filtración, 
              uso de tapabocas, actividades respiratorias y tolerancia al riesgo (en las demás pestañas), usted puede 
              ver cómo mitigar la transmisión del COVID-19 en diferentes espacios internos.''')]),
])

# Room Specifications
room_header = "Especificaciones Espaciales"

floor_area_text = "Área total (pies cuadrados): "
floor_area_text_metric = "Área total (m²): "
ceiling_height_text = "Altura promedio del techo (pies): "
ceiling_height_text_metric = "Altura promedio del techo (m): "

ventilation_text = "Sistema de Ventilación: "
vent_type_output_base = "{:.0f} ACH"
ventilation_text_adv = "Sistema de Ventilación (ACH): "
ventilation_types = [
    {'label': "Ventanas Cerradas", 'value': 0.3},
    {'label': "Ventanas Abiertas", 'value': 2},
    {'label': "Ventilación Mecánica", 'value': 3},
    {'label': "Ventanas abiertas con ventiladores", 'value': 6},
    {'label': "Mejor Ventilación Mecánica", 'value': 8},
    {'label': "Laboratorio, Restaurante", 'value': 9},
    {'label': "Bar", 'value': 15},
    {'label': "Hospital/Vagón del Metro", 'value': 18},
    {'label': "Laboratorio Toxicológico/Avión", 'value': 24},
]

filtration_text = "Sistema de Filtración: "
filt_type_output_base = "MERV {:.0f} [Valores de Reporte de Eficiencia Mínima]"
filtration_text_adv = "Sistema de Filtración (MERV): "
filter_types = [
    {'label': "Ninguno", 'value': 0},
    {'label': "Aire Acondicionado de Ventana Residencial", 'value': 2},
    {'label': "Residencial/Comercial/Industrial", 'value': 6},
    {'label': "Residencial/Comercial/Hospital", 'value': 10},
    {'label': "Hospital & Cirugía General", 'value': 14},
    {'label': "Filtros HEPA (Alta Eficiencia de Retención de Partículas)", 'value': 17}
]

recirc_text = "Tasa de Recirculación: "
recirc_type_output_base = "{:.1f} recirculación ACH"
recirc_text_adv = "Tasa de Recirculación (recirculación ACH): "
recirc_types = [
    {'label': "Ninguno", 'value': 0},
    {'label': "Lento", 'value': 0.3},
    {'label': "Moderado", 'value': 1},
    {'label': "Rápido", 'value': 10},
    {'label': "Avión", 'value': 24},
    {'label': "Vagón del Metro", 'value': 54},
]

humidity_text = "Humedad Relativa: "
humidity_marks = {
    0: {'label': '0%: Muy Seco', 'style': {'max-width': '25px'}},
    0.2: {'label': '20%: Avión', 'style': {'max-width': '50px'}},
    0.3: {'label': '30%: Seco'},
    0.6: {'label': '60%: Promedio'},
    0.99: {'label': '99%: Muy Húmedo'},
}

need_more_ctrl_text = '''¿Requiere mayor control sobre sus variables? Cámbiese al Modo Avanzado en el menú desplegable 
en la parte superior de la página.'''

human_header = "Comportamiento Humano"
# Human Behavior
exertion_text = "Nivel de Esfuerzo: "
exertion_types = [
    {'label': "Descansando", 'value': 0.49},
    {'label': "De pie", 'value': 0.54},
    {'label': "Ejercicio Leve", 'value': 1.38},
    {'label': "Ejercicio Moderado", 'value': 2.35},
    {'label': "Ejercicio Pesado", 'value': 3.30},
]

breathing_text = "Actividad Respiratoria: "
expiratory_types = [
    {'label': "Respirando (liviano)", 'value': 1.1},
    {'label': "Respirando (normal)", 'value': 4.2},
    {'label': "Respirando (fuerte)", 'value': 8.8},
    # {'label': "Breathing (fast-deep)", 'value': 8.5},
    {'label': "Hablando (susurro)", 'value': 29},
    # {'label': "Speaking (whispered counting)", 'value': 37},
    {'label': "Hablando (normal)", 'value': 72},
    # {'label': "Speaking (voiced counting)", 'value': 72},
    {'label': "Hablando (fuerte)", 'value': 142},
    # {'label': "Singing (whispered 'aah')", 'value': 103},
    {'label': "Cantando", 'value': 970},
]

mask_type_text = "Eficiencia de Filtración de la Máscara (tipo de máscara): "
mask_type_marks = {
    0: {'label': "0% (Ninguna, Protector Facial (Careta))", 'style': {'max-width': '50px'}},
    0.1: {'label': "10% (Algodón Grueso)", 'style': {'max-width': '50px'}},
    0.5: {'label': "50% (Seda, Flánel, Chifón/Raso/Gasa)", 'style': {'max-width': '50px'}},
    0.75: {'label': "75% (Quirúrgica, Algodón)", 'style': {'max-width': '50px'}},
    0.95: {'label': "95% (Respirador N95)", 'style': {'max-width': '50px'}},
}
mask_types = [
    {'label': "Ninguna, Protector Facial (Careta)", 'value': 0},
    {'label': "Algodón Grueso", 'value': 0.1},
    {'label': "Seda, Flánel, Chifón/Raso/Gasa", 'value': 0.5},
    {'label': "Quirúrgica, Algodón", 'value': 0.9},
    {'label': "Respirador N95", 'value': 0.95},
]

mask_fit_text = "Ajuste/Desempeño de la Máscara: "
mask_fit_marks = {
    0: {'label': '0%: Ninguno', 'style': {'max-width': '50px'}},
    0.5: {'label': '50%: Muy bajo'},
    0.95: {'label': '95%: Bueno'}
}

risk_tolerance_text = "Tolerancia al Riesgo: "
risk_tol_desc = html.Div('''Los grupos de mayor vulnerabilidad tales como las de la tercera edad o aquellos con 
condiciones médicas preexistentes precisan una menor tolerancia al riesgo. Una mayor tolerancia al riesgo implica más 
transmisiones esperadas durante el período de ocupación esperado (vea las preguntas frecuentes -FAQ- para mayores 
detalles).''', style={'font-size': '13px', 'margin-left': '20px'})
risk_tol_marks = {
    0.01: {'label': '0.01: Muy seguro', 'style': {'max-width': '50px'}},
    0.1: {'label': '0.10: Seguro', 'style': {'max-width': '50px'}},
    1: {'label': '1.00: Inseguro'}
}

# FAQ/Other Inputs & Outputs
faq_header = "Preguntas Frecuentes"
other_io = "Otras Variables & Resultados"

faq_top = html.Div([
    html.H6("Frequently Asked Questions"),
    html.H5("¿Por qué el distanciamiento de 6 pies/2 metros es insuficiente?"),
    html.Div([
        html.Div([html.Span('''Los 6 pies/2 metros lo protegen de las gotas grandes emitidas por un persona infectada 
        al toser, al igual que el tapabocas; sin embargo, no lo protege contra una '''),
                  html.A(children="transmisión aérea",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' por aerosoles infecciosos que están suspendidos en el aire y pueden difundirse por 
                  todo el espacio. En espacios interiores, las personas no están más seguras de las transmisiones 
                  aéreas por aerosoles a los 6 pies que a los 60 pies. ''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("¿Existen otras formas de transmisión? "),
    html.Div([
        html.Div([html.Span('''Se cree que la '''),
                  html.A(children="transmisión aérea",
                         href=link_docs,
                         target='_blank'),
                  html.Span(''' es la predominante para el COVID-19, pero existen otras posibles formas de 
                  transmisión, tales como los ‘fomes’, mediante el contacto directo con residuos infecciosos sobre 
                  las superficies, las ‘gotas/grandes’ espetadas al toser o estornudar y, los ‘aerosoles de corto 
                  alcance’ provenientes de los residuos respiratorios de una persona infectada por un período 
                  prolongado. Aunque la última de estas formas puede resultar significativa, éstos se eliminan con el 
                  uso de tapabocas o de caretas; sin embargo, el riesgo de la transmisión aérea permanece.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("¿Podemos realmente asumir un espacio con mezclas homogéneas?"),
    html.Div([
        html.Div([html.Span('''Existen muchos factores que contribuyen a la mezcla en los espacios interiores, 
        incluidos los flujos impulsados por la flotabilidad (de calentadores, aires acondicionados y ventanas), 
        la convección forzada por respiraderos y ventiladores, así como el movimiento y la respiración humana. Aunque 
        existen excepciones, tal y como se evalúa en el '''),
                  html.A(children="documento",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', el supuesto de la mezcla homogénea es ampliamente utilizado en el modelaje teórico de 
                  la transmisión aérea de enfermedades.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("¿Se mantendría la validez de la directriz para espacios muy amplios?"),
    html.Div([
        html.Div([html.Span('''En auditorios, estadios, u otros espacios amplios ventilados con gran cantidad de 
        asistentes, el riesgo de transmisión aérea es significativo y expresado adecuadamente por la directriz. Sin 
        embargo, cuando no se emplean tapabocas o caretas se genera un riesgo adicional de transmisión de corto 
        alcance a través de las descargas respiratorias, estimado en el '''),
                  html.A(children="documento",
                         href=link_paper,
                         target='_blank'),
                  html.Span('''.''')]),
    ], className='faq-answer'),
    html.Br(),
    html.H5("¿Por qué es relevante la altura del techo?"),
    html.Div([
        '''La altura del techo afecta el volumen total del espacio, el cual se requiere para calcular la 
        concentración de los aerosoles infecciosos (# de aerosoles por unidad de volumen). Esta concentración es 
        indispensable para estimar el riesgo de transmisión del COVID-19 en este espacio. '''
    ], className='faq-answer'),
    html.Br(),
    html.H5("Conozco los valores ACH/MERV. ¿Dónde los introduzco?"),
    html.Div('''
        Si usted necesita mayor control sobre sus variables, cámbiese al Modo Avanzado usando el menú desplegable en 
        la parte superior de la página web.
    ''', className='faq-answer'),
])

faq_other_params_text = html.Div([
    html.H5("¿Existen parámetros ocultos en el Modo Básico?"),
    html.Div([html.Span('''Todos los parámetros físicos relevantes se describen en detalle en el '''),
              html.A(children="documento",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. En el Modo Básico, la aplicación asume por defecto un radio efectivo de aerosoles de 2 
              μm (a una humedad del 60%) y una tasa máxima de desactivación viral de 0.6/hora (a una humedad ~100%), 
              ambos de los cuales aumentan con la humedad relativa (RH). Las estimaciones de la tasa de desactivación 
              viral erran hacia el lado conservador de una desactivación más lenta. La tasa de desactivación viral 
              puede incrementarse mediante radiación ultravioleta (UV-C) o desinfectantes químicos (p.ej. peróxido de 
              hidrógeno, ozono). La aplicación también estima el parámetro clave de enfermedad, la infecciosidad del 
              aire exhalado, C'''),
              html.Sub("q"),
              html.Span(''' (dosis infectante mínima por unidad de volumen) para una determinada actividad respiratoria,
              usando los valores tabulados en la Figura 2 del '''),
              html.A(children="documento",
                     href=link_paper,
                     target='_blank'),
              html.Span('''. Usted deberá definir estos parámetros por sí mismo en el Modo Avanzado.''')],
             className='faq-answer'),
])

aerosol_radius_text = "Radio Efectivo de Aerosoles (a Humedad Relativa = 60%), r\u0305 (\u03bcm): "
viral_deact_text = html.Span(["Tasa Máxima de Desactivación Viral (a Humedad Relativa = 100%), \u03BB", html.Sub('vmax'), " (/hr): "])

values_interest_header = ""
values_interest_desc = html.Div([
    html.H5("¿Qué es exactamente lo que la aplicación calcula?"),
    html.Div([
        html.Div([html.Span('''Dada una tolerancia al riesgo para una transmisión aérea, la aplicación calcula el 
        tiempo máximo de exposición acumulada permisible, el producto de la ocupación del recinto y el tiempo en 
        presencia de una persona infectada. La aplicación también calcula cantidades relacionadas, definidas en el 
        '''),
                  html.A(children="documento",
                         href=link_paper,
                         target='_blank'),
                  html.Span(''', que puedan resultar de interés:''')]),
    ], className='faq-answer'),
])
outdoor_air_frac_label = html.Span(["Fracción de aire exterior Z", html.Sub('p'), ": "])
aerosol_eff_label = html.Span(["Eficiencia de filtración de aerosoles p", html.Sub('f'), ": "])
breathing_rate_label = html.Span(["Tasa de flujo respiratorio Q", html.Sub('b'), ": "])
cq_label = html.Span(["Aire exhalado infeccioso C", html.Sub('q'), ": "])
mask_pass_prob_label = html.Span(["Probabilidad de filtración del tapabocas p", html.Sub('m'), ": "])
room_vol_label = html.Span(["Volumen del Recinto V: "])
vent_rate_Label = html.Span(["Tasa de flujo de ventilación (externa) Q: "])
recirc_rate_label = html.Span(["Tasa de flujo de retorno (recirculación) de aire Q", html.Sub('f'), ": "])
air_filt_label = html.Span(["Tasa de filtración del aire (\u03BB", html.Sub('f'), "): "])
eff_aerosol_rad_label = html.Span(["Radio de aerosoles ajustado por la humedad r\u0305", html.Sub('eff'), ": "])
viral_deact_label = html.Span(["Tasa de desactivación viral ajustada por la humedad \u03BB", html.Sub('v'), ": "])
sett_speed_label = html.Span(["Velocidad efectiva de sedimentación de aerosoles v\u209B(r\u0305", html.Sub('eff'), "): "])
conc_relax_rate_label = html.Span(["Tasa de relajación de la concentración \u03BB", html.Sub('c'), ": "])
airb_trans_label = html.Span(["Tasa de transmisión aérea \u03B2\u2090: "])

graph_output_header = ""
faq_graphs_text = html.Div([
    html.H5(""),
    # html.Div("Here you go!", className='faq-answer'),
])

faq_infect_rate = html.Div([
    html.H5("¿El modelo explica la prevalencia de la infección en la población local?"),
    html.Div(['''No. El modelo calcula el riesgo de transmisión a partir de una persona infectada. Por ello asume 
    implícitamente que la prevalencia de la infección en la población es relativamente baja. En este límite, 
    el riesgo de transmisión aumenta con el número esperado de personas infectadas en un recinto, específicamente 
    como el producto de la ocupación y de la prevalencia en la población. La tolerancia deberá reducirse en 
    proporción a este número en caso de que sea superior a uno. Por el contrario, cuando el número esperado de 
    personas infectadas en un recinto se aproxime a cero, la tolerancia podrá aumentarse proporcionalmente hasta que 
    las restricciones recomendadas se consideren necesarias. '''],
             className='faq-answer'),
])

assumptions_layout = html.Div([
    html.H5("¿Más Preguntas?"),
    html.Div([html.Span('''Para explicaciones y referencias más detalladas, véase "'''),
              html.A(children="Más Allá de los 6 Pies",
                     href=link_paper,
                     target='_blank'),
              html.Span('''" y otros vínculos publicados en la parte superior de la página web.''')]),
])

footer = html.Div([
    html.Div([html.Span('''La COVID-19 Directriz de Seguridad en Espacios Interiores es una herramienta en evolución 
    que pretende familiarizar al usuario interesado con los factores que influyen sobre el riesgo de una transmisión 
    aérea del COVID-19 en espacios interiores y a contribuir a la evaluación cuantitativa del riesgo en diversos 
    entornos. Debemos anotar que la incertidumbre en y la variabilidad intrínseca de los parámetros del modelo podría 
    conducir a errores tan grandes como de una orden de magnitud, los cuales pueden ser compensados mediante la 
    elección de una tolerancia al riego suficientemente baja. Nuestras directrices no toman en consideración las 
    transmisiones de corto alcance a través de descargas respiratorias, las cuales podrían aumentar sustantivamente 
    el riesgo cuando no se está usando tapabocas, de la manera descrita en el '''),
              html.A(children="documento adjunto",
                     href=link_paper,
                     target='_blank'),
              html.Span(''' (Bazant & Bush, 2020). El uso de La COVID-19 Directriz de Seguridad en Espacios Interiores 
              es responsabilidad absoluta del usuario. Se pone a disponibilidad del usuario sin aseveración o 
              garantía alguna. Los autores no aceptan responsabilidad alguna derivada de su uso.''')]),
    html.Br(),
    html.Div("Agradecimientos especiales a: ")
], className='footer-small-text')
