import dash
from flask_talisman import Talisman

"""
app.py is to be imported by other files (default.py, advanced.py, index.py) to be referenced in setup.

"""

# Dash App Setup
app = dash.Dash(__name__, suppress_callback_exceptions=True)

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
                 'https://fonts.gstatic.com',]
}

# Talisman(app.server, content_security_policy=csp)

curr_units = 'british'
