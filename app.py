import dash
from flask_talisman import Talisman

"""
app.py is to be imported by other files (default.py, advanced.py, index.py) to be referenced in setup.

"""

# Dash App Setup
app = dash.Dash(__name__, suppress_callback_exceptions=True)

csp = {
    'default-src': '\'self\'',
    'script-src': ['\'self\'',
                   'https://www.googletagmanager.com/gtag/js?id=UA-143756813-2'],
}

Talisman(app.server, content_security_policy=csp)

curr_units = 'british'
