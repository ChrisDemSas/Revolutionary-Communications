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

def read_sql(fname: str, conn: sqlite3) -> pd.DataFrame:
    """ Returns a pandas dataframe from external file. """

    with open(fname, 'r') as f:
        return pd.read_sql_query(f.read(), conn)
     
def plot_sentiment():
    """Plot the average sentiment over time."""

    sentiment = read_sql('app/dashboard/queries/sentiment.sql', conn)

    graph = px.line(sentiment, x = 'time', y = 'average_sentiment', labels = {'time': 'Time', 'average_sentiment': 'Average Sentiment Rating'},
            title="Average Sentiment Rating Over Time")
    graph.update_layout(margin=dict(t=50, b=0, l=0, r=0), height = 500, template='simple_white')

    return graph

def plot_no_feedback_per_category():
    """Plot the number of feedback from each category."""

    feedback_category = read_sql('app/dashboard/queries/feedback_category.sql', conn)

    graph = px.pie(feedback_category, values = 'count', names = 'category', 
                   title = "Feedback Proportions")
    graph.update_layout(margin=dict(t=75, b=75, l=50, r=0), template='simple_white')

    return graph

def plot_avg_sentiment_per_category():
    """Plot average sentiment per category."""

    sentiment_category = read_sql('app/dashboard/queries/sentiment_category.sql', conn)

    graph = px.bar(sentiment_category, x = 'category', y = 'average_sentiment', labels = {'category': 'Category', 'average_sentiment': 'Average Sentiment Rating'},
                   title = "Average Sentiment Rating Per Category")
    graph.update_layout(margin=dict(t=75, b=70, l=10, r=10), template='simple_white')

    return graph

def plot_feedback_sentiment():
    """Plot Sentiment distribution."""

    feedback_sentiment = read_sql('app/dashboard/queries/feedback_sentiment.sql', conn)

    graph = px.bar(feedback_sentiment, x = 'sentiment', y = 'sentiment_counter', labels = {'sentiment': 'Sentiment Rating', 'sentiment_counter': 'Number of Sentiment Rating'},
                   title = "Number of Feedback Per Sentiment Rating")
    graph.update_layout(margin=dict(t=75, b=70, l=10, r=10), template='simple_white')

    return graph

def plot_no_feedback():
    """Plot the number of feedback."""

    all = read_sql('app/dashboard/queries/all.sql', conn)

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = all.shape[0],
        title = {'text': "Feedbacks"}
    ))
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=200)

    return fig

def plot_mean_sentiment():
    """Plot the mean of sentiment."""

    all = read_sql('app/dashboard/queries/all.sql', conn)

    fig = go.Figure(go.Indicator(
        mode = "number",
        value = all['sentiment'].mean(axis = 0),
        title = {'text': "Average Sentiment Rating"}
    ))
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=200)

    return fig

def plot_no_communities():
    """Plot the number of communities."""

    no_communities = read_sql('app/dashboard/queries/no_communities.sql', conn)

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