import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from datetime import datetime as dt
import seaborn as sns
from scipy import stats
import json
import requests
import string
import scipy.stats as st
from bs4 import BeautifulSoup
import statsmodels.formula.api as smf
import statsmodels.api as sm
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Function to calculate coefficients
def calculate_coefficients(group):
    max_repetitions = group['Repetitions'].max()
    num_characters = len(group)

    if max_repetitions == 0:
        # If no character names appeared in the plot summary
        group['Importance Coefficient'] = 1 / num_characters
    else:
        # Divide the number of repetitions for each character by the total sum of repetitions
        group['Importance Coefficient'] = group['Repetitions'] / max_repetitions

    return group

def get_path(file_url):
    # Extract file ID from the Google Drive URL
    file_id = file_url.split('/')[-2]

    # Construct the download link
    download_link = f"https://drive.google.com/uc?id={file_id}"

    # Return the download link
    return download_link

# Method to extract lists of actor names
def wiki_actors_from_ethnicity(url, first_actor, last_actor, json_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    extract = False
    actors = []
    for ul in soup.find_all("ul"):
        for li in ul.find_all("li"):
            if li.a:
                # Start the scan when detecting the first actor
                if li.a.text == first_actor:
                    extract = True

                if extract:
                    actors.append(li.a.text)

                # End the scan when detecting the last actor
                if li.a.text == last_actor:
                    extract = False
                    break

    # Save the list
    with open(json_name, mode="w") as f:
        json.dump(actors, f)

def count_words_in_text(word_list, text):
    # The function now counts each occurrence of any part of the character's name
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words_in_text = text.split()
    word_count = {word: 0 for word in word_list}

    for word in word_list:
        # Splitting the character name into individual words
        parts = word.lower().split()
        # Counting each occurrence of any part of the name
        for part in parts:
            word_count[word] += words_in_text.count(part)

    return word_count

# Define function to plot regression line and return p-value
def plot_regression_and_pvalue_1(df, color, name):
    X = sm.add_constant(df['Year'])
    model = sm.OLS(df['Proportion'], X).fit()
    p_value = model.pvalues['Year']

    fig.add_trace(go.Scatter(x=df['Year'], y=model.fittedvalues, mode='lines', line=dict(color=color), name=f'{name}'))


def plot_regression_and_pvalue_3(df, color, name):
    X = sm.add_constant(df['Year'])
    model = sm.OLS(df['Proportion'], X).fit()
    p_value = model.pvalues['Year']

    # Print regression summary
    print(f"Regression Results for {name}:")
    print(model.summary(), "\n")

    # Plot regression line
    fig.add_trace(go.Scatter(x=df['Year'], y=model.fittedvalues, mode='lines', line=dict(color=color), name=f'{name}'))
