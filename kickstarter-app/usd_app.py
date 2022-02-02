'''
Kickstarter Campaign Success Prediction
Contains input buttons for use on final prediction app

Local Testing: http://127.0.0.1:8050/

Sections:
1. Imports
2. Variables
    - Predictive Model
    - Styling
3. Initialize App
4. Layout
    - Header
    - Project Category Drop Down
    - Country of Origin Drop Down
    - Campaign Length Slider
    - Monetary Goal Fill-In
5. Callbacks
6. Script Execution
'''

# 1. Imports

# Dash
import dash                                             # Plotly Dash
from dash import dcc                                    # Components
from dash import html                                   # HTML
from dash.dependencies import Input, Output             # Input/Output
# Environment
import requests
# Predictive Model
import pandas as pd
import joblib                                           # Stored Model
from sklearn.neighbors import KNeighborsClassifier      # Model Dependencies
from sklearn import model_selection

# 2. Variables

# Predictive Model
model = joblib.load('model.joblib')

# Styling


# 3. Initialize App
app = dash.Dash(__name__)
server = app.server

# 4. Layout
app.layout = html.Div(
    style={'fontSize':35, 'font-family':'Dongle, sans serif'},
    children=[
        html.Div([

            # Header
            dcc.Markdown('''
            ---
            # Kickstarter Campaign Success Prediction!
            ---
            ''', style={
                'color': '#35ca6e',
                'fontSize': 35,
                'font-family': 'Dongle, sans serif',
                'backgroundColor': '#1a1516',
                'textAlign': 'center',
                'margin': 0,
                'padding-top': '2%',
                'padding-bottom': '2%',
                }
            ),

            # Intro
            dcc.Markdown('''
            Tell us about your project...
            ''',
            style={
                'padding': 5,
                'margin-left': 10,
                'margin-bottom': 10,
                'height': 100,
                }
            ),

            # Project Category Drop Down
            html.Label(
                "1.  Which type of project are you making?",
                style={
                    'margin-left':20,
                    'height':100,
                    'verticalAlign': 'top',
                    },
                ),
            dcc.Dropdown(
                id='main_category',
                options=[
                    {'label': 'Publishing', 'value': 1},
                    {'label': 'Film & Video', 'value': 2},
                    {'label': 'Music', 'value': 3},
                    {'label': 'Food', 'value': 4},
                    {'label': 'Crafts', 'value': 5},
                    {'label': 'Games', 'value': 6},
                    {'label': 'Design', 'value': 7},
                    {'label': 'Comics', 'value': 8},
                    {'label': 'Fashion', 'value': 9},
                    {'label': 'Theater', 'value': 10},
                    {'label': 'Art', 'value': 11},
                    {'label': 'Photography', 'value': 12},
                    {'label': 'Technology', 'value': 13},
                    {'label': 'Dance', 'value': 14},
                    {'label': 'Journalism', 'value': 15},
                ],
                style={
                    'font-size': 35,
                    'backgroundColor': '#718e85',
                    'textAlign': 'left',
                    'padding-right': 10,
                    'padding-bottom': 30,
                    'margin-left': 70,
                    'width': '50%',
                    'height': '30%',
                    'verticalAlign': 'bottom',
                    'display': 'inline-block',
                },
            ),

            html.Br(),
            # Country of Origin Drop Down
            html.Label(
                "2.  In which country is the project being developed?",
                style={
                    'margin-left':20,
                    'height':100,
                    'verticalAlign': 'top',
                    },
                ),
            dcc.Dropdown(
                id='country',
                options=[
                    {'label': 'United States', 'value': 1},
                    {'label': 'Australia', 'value': 4},
                    {'label': 'Austria', 'value': 18},
                    {'label': 'Belgium', 'value': 17},
                    {'label': 'Canada', 'value': 3},
                    {'label': 'Denmark', 'value': 13},
                    {'label': 'France', 'value': 6},
                    {'label': 'Germany', 'value': 5},
                    {'label': 'Hong Kong', 'value': 19},
                    {'label': 'Ireland', 'value': 14},
                    {'label': 'Italy', 'value': 8},
                    {'label': 'Japan', 'value': 22},
                    {'label': 'Luxembourg', 'value': 21},
                    {'label': 'Mexico', 'value': 11},
                    {'label': 'The Netherlands', 'value': 7},
                    {'label': 'New Zealand', 'value': 12},
                    {'label': 'Norway', 'value': 16},
                    {'label': 'Singapore', 'value': 20},
                    {'label': 'Spain', 'value': 9},
                    {'label': 'Sweden', 'value': 10},
                    {'label': 'Switzerland', 'value': 15},
                    {'label': 'The United Kingdom', 'value': 2},
                ],
                style={
                    'font-size': 35,
                    'backgroundColor': '#718e85',
                    'textAlign': 'left',
                    'padding-right': 10,
                    'padding-bottom': 30,
                    'margin-left': 20,
                    'width': '50%',
                    'height': '30%',
                    'verticalAlign': 'bottom',
                    'display': 'inline-block',
                },
            ),

            html.Br(),
            # Numeric (Fill-In)
            html.I(
                "3.  Project Monetary Goal (in USD*):  ",
                style={'margin-left':20, 'verticalAlign': 'top',},
                ),
            dcc.Input(
                id='usd_goal_real',
                type='number',
                min=1, max=25000000000,
                style={
                    'font-family': 'Dongle, sans serif',
                    'font-size': 35,
                    'backgroundColor': '#718e85',
                    'textAlign': 'left',
                    'padding-right': 10,
                    'padding-bottom': 30,
                    'margin-left': 180,
                    'verticalAlign': 'bottom',
                    'display': 'inline-block',
                    'width': 400,
                    },
                ),
            dcc.Markdown('''
            *You can convert your local currency goal to USD [here](https://www.xe.com/currencyconverter/).
            ''',
            style={
                'margin-left': 30,
                'font-size': 25,
                'width': 500,
                'verticalAlign': 'top',
                },
            ),

            html.Br(),
            # Campaign Length (Kickstarter min 1, max 60) Slider
            html.Label(
                "4.  Campaign Length (in days):",
                style={
                    'margin-left':20,
                    'width': 50,
                    'textAlign': 'left',
                    },
                ),
            html.Br(),
            dcc.Slider(
                id='days',
                min=1,
                max=60,
                step=1,
                marks={
                    1: {
                        'label': "1 Day",
                        'style': {
                            'font-size': 20,
                            'margin-left': 20,
                            'verticalAlign': 'middle',
                            'textAlign': 'center',
                            },
                        },
                    15: {
                        'label': "15 Days",
                        'style': {
                            'font-size': 20,
                            'verticalAlign': 'middle',
                            'textAlign': 'left',
                            },
                        },
                    30: {
                        'label': "30 Days*",
                        'style': {
                            'font-size': 20,
                            'verticalAlign': 'middle',
                            'textAlign': 'left',
                            },
                        },
                    45: {
                        'label': "45 Days",
                        'style': {
                            'font-size': 20,
                            'verticalAlign': 'middle',
                            'textAlign': 'left',
                            },
                        },
                    60: {
                        'label': "60 Days",
                        'style': {
                            'font-size': 20,
                            'margin-right': 100,
                            'padding-right': 100,
                            'verticalAlign': 'middle',
                            'textAlign': 'left',
                            },
                        },
                    },
                value=30,
                updatemode='drag',
                tooltip={
                    "placement": "top",
                    "always_visible":True,
                    },
            ),

            html.Br(),
            # Output
            html.Div(id='output-state'),
            html.Br(),
        ]),
])

# 5. Callbacks

@app.callback(
    Output(component_id='output-state', component_property='children'),
    Input(component_id='main_category', component_property='value'),
    Input(component_id='country', component_property='value'),
    Input(component_id='days', component_property='value'),
    Input(component_id='usd_goal_real', component_property='value'),
    )
def predict(main_category, country, days, usd_goal_real):
    '''
    Predicts if a campaign will be successful.
    '''

    # Store data in data frame
    ksdf = pd.DataFrame(
        columns=['main_category', 'country', 'days', 'usd_goal_real'],
        data=[[main_category, country, days, usd_goal_real]]
    )

    # Execute Prediction
    y_pred = model.predict(ksdf)[0]
    if y_pred == 0:
        return "Your campaign won't be successful."
    else:
        return "Your campaign might succeed!"

# 6. Script Execution
# File executes when ran as script in debugging mode (local use)
if __name__ == '__main__':
    app.run_server(debug=True)