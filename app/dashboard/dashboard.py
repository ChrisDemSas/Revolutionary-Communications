from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output
from flask import Flask
from app_init import app
import pandas as pd
import plotly.express as px
import sqlite3


conn = sqlite3.connect('/databases/feedback.db')
cursor = conn.cursor()

dashboard = Dash(__name__, server = app, url_base_pathname='/dashboard/')

dashboard.layout = html.Div([html.H1('Hi there, I am Dash1')])