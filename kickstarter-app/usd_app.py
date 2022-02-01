'''
Kickstarter Campaign Success Prediction
Contains input buttons for use on final prediction app

Local Testing: http://127.0.0.1:8050/

Sections:
1. Imports
2. Variables
    - Predictive Model
3. Initialize App
4. Layout (Buttons)
    - Project Category Drop Down
    - Country of Origin Drop Down
    - Campaign Length Fill-in
    - Submit Button
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

# Model
model = joblib.load('model.joblib')

# 3. Initialize App
app = dash.Dash(__name__)

# 4. Layout (Buttons)
app.layout = html.Div([
    html.Div([

    # Project Category Drop Down
        html.Label("Which type of project are you making?"),
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
        ),

        html.Br(),
        # Country of Origin Drop Down
        html.Label("In which country is the project being developed?"),
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
        ),

        html.Br(),
        # Campaign Length (Kickstarter min 1, max 60) Slider
        html.Label("Campaign Length (in days):"),
        html.Br(),
        dcc.Slider(
            id='days',
            min=1,
            max=60,
            step=1,
            marks={
                1: "1 Day(Required Minimum)",
                15: "15 Days",
                30: "30 Days (Recommended)",
                45: "45 Days",
                60: "60 Days (Required Maximum",
                },
            value=30,
            updatemode='drag',
            tooltip={"placement": "bottom", "always_visible":False},
        ),

        # Numeric (Fill-In)
        html.I("Project Monetary Goal (in USD):  "),
        dcc.Input(id='usd_goal_real', type='number', min=1, max=25000000000),
        html.Br(),
        dcc.Markdown('''
        You can convert your local currency goal to USD [here](https://www.xe.com/currencyconverter/).
        '''),

        # Output
        html.Div(id='output-state')
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