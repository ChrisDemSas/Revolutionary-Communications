from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
from flask import Flask
from app_init import app
import pandas as pd
import plotly.express as px
import sqlite3
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

conn = sqlite3.connect('app/databases/feedback.db')
all = pd.read_sql_query("""SELECT * FROM feedbacks""", conn) # Number of feedback
feedback_category = pd.read_sql_query("""SELECT COUNT(*) AS count, category FROM feedbacks GROUP BY category""", conn)
sentiment = pd.read_sql_query("""SELECT AVG(sentiment) AS average_sentiment, time FROM feedbacks GROUP BY time""", conn)
sentiment_category = pd.read_sql_query("""SELECT AVG(sentiment) AS average_sentiment, category FROM feedbacks GROUP BY category""", conn)
feedback_sentiment = pd.read_sql_query("""SELECT COUNT(sentiment) AS sentiment_counter, sentiment FROM feedbacks GROUP BY sentiment""", conn)
no_communities = pd.read_sql_query("""SELECT DISTINCT(community) AS no_community FROM feedbacks""", conn)

def plot_sentiment():
    """Plot the average sentiment over time."""

    graph = px.line(sentiment, x = 'time', y = 'average_sentiment', 
            title="Average Sentiment Rating Over Time")
    graph.update_layout(margin=dict(t=50, b=0, l=0, r=0), height = 500, template='simple_white')

    return graph

def plot_no_feedback_per_category():
    """Plot the number of feedback from each category."""

    graph = px.pie(feedback_category, values = 'count', names = 'category',
                   title = "Feedback Proportions")
    graph.update_layout(margin=dict(t=75, b=75, l=50, r=0), template='simple_white')

    return graph

def plot_avg_sentiment_per_category():
    """Plot average sentiment per category."""

    graph = px.bar(sentiment_category, x = 'category', y = 'average_sentiment',
                   title = "Average Sentiment Rating Per Category")
    graph.update_layout(margin=dict(t=75, b=70, l=10, r=10), template='simple_white')

    return graph

def plot_feedback_sentiment():
    """Plot Sentiment distribution."""

    graph = px.bar(feedback_sentiment, x = 'sentiment', y = 'sentiment_counter',
                   title = "Number of Feedback Per Sentiment Rating")
    graph.update_layout(margin=dict(t=75, b=70, l=10, r=10), template='simple_white')

    return graph

def plot_no_feedback():
    """Plot the number of feedback."""

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = all.shape[0],
        title = {'text': "Feedbacks"}
    ))
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=200)

    return fig

def plot_mean_sentiment():
    """Plot the mean of sentiment."""

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = all['sentiment'].mean(axis = 0),
        title = {'text': "Average Sentiment Rating"}
    ))
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=200)

    return fig

def plot_no_communities():
    """Plot the number of communities."""

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = no_communities.shape[0],
        title = {"text": "Number of Communities Served"}
    ))
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=200)

    return fig

# Use dcc.Dropdown for dropdown menu
dashboard = Dash(__name__, server = app, routes_pathname_prefix = '/dashboard/')

dashboard.layout = html.Div(
    [
    html.Div(children = [html.H1("Welcome!", style={'textAlign': 'center'}), 
                        html.A(html.Button("Dashboard", id="dashboard-button-d"), href="/dashboard/", target="_blank"),
                        html.A(html.Button("Brainstorm", id="brainstorm-button-d"), href="/plan", target="_blank"),
                        html.A(html.Button("Chat", id="chat-button-d"), href="/chatbot", target="_blank")], id="container")
             ,
    html.Br(),

    html.Div(children = [dcc.Graph(id = "no-feedback", figure = plot_no_feedback()),
            dcc.Graph(id = "mean-sentiment", figure = plot_mean_sentiment()),
            dcc.Graph(id = "no-communities", figure = plot_no_communities())            
            ], style={'textAlign': 'center'}),

    html.Div(children = [dcc.Graph(id="no-feedback-sentiment", figure = plot_feedback_sentiment()), 
            dcc.Graph(id="no-avg-feedback", figure = plot_avg_sentiment_per_category()),
            dcc.Graph(id = "category-feedback", figure = plot_no_feedback_per_category())
            ], style={'textAlign': 'center'}),

    html.Div(children = [dcc.Graph(id="sentiment", figure = plot_sentiment())], 
             style={'textAlign': 'center'})
    ]

    )