import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import dash._callback_context
from flask_talisman import Talisman

import descriptions as desc
import essentials as ess

"""
app.py handles the general app functionality related to the HTML header, switching between modes (Basic Mode,
Advanced Mode), Unit Systems, Languages, and running the app.
"""

# Dash App Setup
app = dash.Dash(__name__, suppress_callback_exceptions=True, use_pages=True)

csp = {
    'default-src': ['\'self\'',
                    'https://www.google-analytics.com'],
    'script-src': ['\'self\'',
                   'https://www.googletagmanager.com',
                   'https://www.google-analytics.com',
                   '\'unsafe-inline\'',
                   '\'unsafe-eval\''],
    'style-src': ['\'self\'',
                  'https://fonts.googleapis.com',
                  '\'unsafe-inline\''],
    'font-src': ['\'self\'',
                 'https://fonts.googleapis.com',
                 'https://fonts.gstatic.com']
}

Talisman(app.server, content_security_policy=csp)

curr_units = 'british'

# Languages
languages = [
    # {'label': "العربية", 'value': "ar"},
    {'label': "Čeština", 'value': "cs"},
    # {'label': "Dansk", 'value': "da", 'disabled': True},
    {'label': "Deutsch", 'value': "de"},
    {'label': "Ελληνικά", 'value': "el"},
    {'label': "English", 'value': "en"},
    # {'label': "Espa\u00f1ol", 'value': "es", 'disabled': True},
    {'label': "Euskara", 'value': "eu"},
    {'label': "Fran\u00e7ais", 'value': "fr"},
    {'label': "हिन्दी", 'value': "hi"},
    {'label': "Magyar", 'value': "hu"},
    {'label': "Bahasa Indonesia", 'value': "id"},
    # {'label': "Italiano", 'value': "it", 'disabled': True},
    {'label': "한국어", 'value': "ko"},
    # {'label': "Nederlands", 'value': "nl"},
    {'label': "Português do Brasil", 'value': "pt-br"},
    {'label': "Pусский", 'value': "ru"},
    {'label': "Svenska", 'value': "sv"},
    {'label': "简体中文", 'value': "zh"},
    {'label': "繁體中文", 'value': "zh_tw"},
]

# Used for Heroku deployment
server = app.server

# Custom HTML Header
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <!-- Socials meta -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta property="og:url" content="https://indoor-covid-safety.herokuapp.com/"/>
        <meta property="og:title" content="COVID-19 Indoor Safety Guideline"/>
        <meta property="og:description" content="See how to mitigate indoor COVID-19 transmission in different indoor spaces."/>
        <meta property="og:image" content="https://indoor-covid-safety.herokuapp.com/assets/COVID_graph.png"/>
        <meta property="og:type" content="website"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>COVID-19 Indoor Safety Guideline</title>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-143756813-2"></script>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>'''

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Location(id='url-read'),

    html.Div(className='grid-header', children=[
        html.Div(className='app-card-header', children=[
            html.Span(desc.header, id='header-text')
        ]),
        html.Div(className='app-card-header', children=[

            html.Div(id='header-left', children=[
                dbc.NavbarSimple(
                    children=[
                        dbc.DropdownMenu(
                            children=[
                                dbc.DropdownMenuItem(desc.app_modes[0]['label'], href="/", style={"font-size": "13px"},
                                                     id='basic-dd-item'),
                                dbc.DropdownMenuItem(desc.app_modes[1]['label'], href="/advanced", style={"font-size": "13px"},
                                                     id='adv-dd-item'),
                            ],
                            nav=True,
                            in_navbar=True,
                            label=desc.mode_dd,
                            id='navbar-dropdown-menu',
                            size="lg",
                        ),
                    ],
                    links_left=False,
                    color="#fff",
                    dark=False,
                    brand="Switch App Mode",
                    brand_style={
                        "color": "#de1616",
                    },
                    id='navbar',
                ),
                html.Div(className='grid-settings', children=[
                    html.Div(className='card-settings', children=[
                        html.Div(html.Span(desc.language_dd, id='language-dd'), className='settings-header'),
                        dcc.Dropdown(id='lang-setting',
                                     options=languages,
                                     value="",
                                     searchable=False,
                                     clearable=False)
                    ]),
                    html.Div(className='card-settings', children=[
                        html.Div(html.Span(desc.units_dd, id='units-dd'), className='settings-header'),
                        dcc.Dropdown(id='units-setting',
                                     options=desc.unit_settings,
                                     value="",
                                     searchable=False,
                                     clearable=False)
                    ]),
                    # html.Div(className='card-settings', children=[
                    #     html.Div(html.Span(desc.mode_dd, id='mode-dd'), className='settings-header'),
                    #     dcc.Dropdown(id='app-mode',
                    #                  options=desc.app_modes,
                    #                  value="",
                    #                  searchable=False,
                    #                  clearable=False)
                    # ]),
                ]),

            ])
        ]),
    ]),
    html.Br(),
    # html.Div(id='page-content'),
    dash.page_container,
    html.Br(),
    html.Div(desc.footer, id='footer-text'),

    html.Div(id='window-width'),
    html.Div(id='window-height'),
])


# Updates window width div on page update
app.clientside_callback(
    """
    function() {
        return window.innerWidth;
    }
    """,
    Output('window-width', 'children'),
    Input('url', 'search'),
)

# Updates window height div on page update
app.clientside_callback(
    """
    function() {
        return window.innerHeight;
    }
    """,
    Output('window-height', 'children'),
    Input('url', 'search'),
)


# Updates header based on language
@app.callback(
    [Output('header-text', 'children'),
     Output('language-dd', 'children'),
     Output('units-dd', 'children'),
     Output('navbar-dropdown-menu', 'label'),
     Output('units-setting', 'options'),
     Output('basic-dd-item', 'children'),
     Output('adv-dd-item', 'children'),
     Output('footer-text', 'children')],
    [Input('url', 'search')]
)
def update_header_and_footer(search):
    params = ess.search_to_params(search)
    if "lang" in params:
        language = params["lang"]
    else:
        language = "en"

    return ess.get_header_and_footer_text(language)


# Updates URL based on menu dropdowns (language, units, mode)
@app.callback(
    Output('url', 'search'),
    [Input('units-setting', 'value'),
     Input('lang-setting', 'value'),
     Input('url-read', 'search')]
)
def update_units_search(units, lang, search):
    # if nothing is selected in our dropdown, that means we just loaded the page
    if units == "":
        return search

    units_str = ""
    if units == 'metric':
        units_str = "units=metric"
    elif units == 'british':
        units_str = ""

    lang_str = ""
    if lang == 'en':
        lang_str = ""
    else:
        lang_str = "lang=" + lang

    search_terms = [units_str, lang_str]
    search_str = ""
    for term in search_terms:
        if term != "":
            if search_str == "":
                search_str = "?" + term
            else:
                search_str = search_str + "&" + term

    return search_str


# Updates menu dropdowns language and units based on URL search terms.
@app.callback(
    [Output('units-setting', 'value'),
     Output('lang-setting', 'value')],
    [Input('url', 'search')]
)
def update_dropdowns(search):
    params = ess.search_to_params(search)
    my_units = "british"
    if "units" in params:
        my_units = params["units"]

    my_lang = "en"
    if "lang" in params:
        my_lang = params["lang"]

    return [my_units, my_lang]


if __name__ == "__main__":
    app.run_server(debug=False)
