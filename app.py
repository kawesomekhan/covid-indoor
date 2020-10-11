import dash

"""
app.py is to be imported by other files (default.py, advanced.py, index.py) to be referenced in setup.

"""

# Dash App Setup
app = dash.Dash(__name__, suppress_callback_exceptions=True)

