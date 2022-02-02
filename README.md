The purpose of Build Week is to empower students to demonstrate mastery of the learning objectives. The Build Weeks experience helps prepare students for the job market.


The Pitch:

Using NLP and / or regression techniques, Kickstarter Success can help predict how successful a 
kickstarter campaign will be based on the monetary goal, description, campaign length, or catagories.

___________________________________________________________________________________________

MVP:

- Train a model that predicts `campaign` success or failure (binary target variable.)
- Deploy a model via Flask API so that predictions can be displayed to the `user.`

___________________________________________________________________________________________

Heroku App: 

https://kickstart-campaign-prediction.herokuapp.com/

___________________________________________________________________________________________

Setup Details:

Required Packages:

numpy, python, dash, requests, pandas, scikit-learn, joblib, gunicorn

____________________________________________________________________________________________

To start locally in command line: 

clone this repository

start venv

command line code: python usd_app.py

____________________________________________________________________________________________

Datasets Used:

The KNN Nearest Neighbors model was trained on Kickstarter campaign data from Kaggle:

https://www.kaggle.com/kemical/kickstarter-projects?select=ks-projects-201801.csv

____________________________________________________________________________________________

API Used:

Currency exhange rate API used to convert all currency inputs to USD (key required):

https://www.exchangerate-api.com/

_____________________________________________________________________________________________

Meet the Team:

Nicholas Papenburg; Github: https://github.com/NPAPENBURG

Celina Walkowicz; Github: https://github.com/CelinaWalkowicz

Matt Grohnke; Github: https://github.com/mgrohnke
