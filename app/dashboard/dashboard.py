from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
from flask import Flask
from app_init import app
import pandas as pd
import plotly.express as px
import sqlite3
import plotly.graph_objects as go


conn = sqlite3.connect('app/dashboard/databases/feedback.db')
all = pd.read_sql_query("""SELECT * FROM feedbacks""", conn) # Number of feedback
feedback_category = pd.read_sql_query("""SELECT COUNT(*) AS count, category FROM feedbacks GROUP BY category""", conn)
sentiment = pd.read_sql_query("""SELECT AVG(sentiment) AS average_sentiment, time FROM feedbacks GROUP BY time""", conn)
sentiment_category = pd.read_sql_query("""SELECT AVG(sentiment) AS average_sentiment, category FROM feedbacks GROUP BY category""", conn)
feedback_sentiment = pd.read_sql_query("""SELECT COUNT(sentiment) AS sentiment_counter, sentiment FROM feedbacks GROUP BY sentiment""", conn)
no_communities = pd.read_sql_query("""SELECT DISTINCT(community) AS no_community FROM feedbacks""", conn)

def plot_sentiment():
    """Plot the average sentiment."""

    graph = px.line(sentiment, x = 'time', y = 'average_sentiment', 
            title="Average Sentiment Over Time")

    return graph

def plot_no_feedback_per_category():
    """Plot the number of feedback from each category."""

    graph = px.pie(feedback_category, values = 'count', names = 'category')
    graph.update_layout(margin=dict(t=0, b=0, l=0, r=0))

    return graph

def plot_avg_sentiment_per_category():
    """Plot average sentiment per category."""

    graph = px.bar(sentiment_category, x = 'category', y = 'average_sentiment')

    return graph

def plot_feedback_sentiment():
    """Plot Sentiment distribution."""

    graph = px.bar(feedback_sentiment, x = 'sentiment', y = 'sentiment_counter')

    return graph

def plot_no_feedback():
    """Plot the number of feedback."""

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = all.shape[0],
        title = {'text': "Feedbacks"}
    ))

    return fig

def plot_mean_sentiment():
    """Plot the mean of sentiment."""

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = all['sentiment'].mean(axis = 0),
        title = {'text': "Average Sentiment"}
    ))

    return fig

def plot_no_communities():
    """Plot the number of communities."""

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = no_communities.shape[0],
        title = {"text": "Number of Communities"}
    ))

    return fig

# Use dcc.Dropdown for dropdown menu
dashboard = Dash(__name__, server = app, url_base_pathname='/dashboard/')

dashboard.layout = html.Div(
    [
    html.H1("Welcome!"),
    html.Br(),

    html.Div(children = [dcc.Graph(id = "no-feedback", figure = plot_no_feedback(), style={'display': 'inline-block', 'width': '30%'}),
            dcc.Graph(id = "mean-sentiment", figure = plot_mean_sentiment(), style={'display': 'inline-block', 'width': '30%'}),
            dcc.Graph(id = "no-communities", figure = plot_no_communities(), style={'display': 'inline-block', 'width': '30%'})
            
            ]),

    html.Div(children = [
        dcc.Graph(id="sentiment", figure = plot_sentiment(), style = {'display': 'inline-block', 'width': '70%', 'height': '100%'}),
        dcc.Graph(id = "category-feedback1", figure = plot_no_feedback_per_category(), style={'display': 'inline-block', 'width': '30%', 'height': '100%'})]),

    html.Div(children = [dcc.Graph(id="no-feedback-sentiment", figure = plot_feedback_sentiment(), style={'display': 'inline-block', 'width': '50%', 'height': '100%'}), 
            dcc.Graph(id="no-avg-feedback", figure = plot_avg_sentiment_per_category(), style={'display': 'inline-block', 'width': '50%', 'height': '100%'})])
    ]

    )
