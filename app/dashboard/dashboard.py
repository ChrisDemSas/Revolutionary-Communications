from dash import Dash, html
from flask import Flask
from app_init import app

dashboard = Dash(__name__, server = app, url_base_pathname='/dashboard/')

dashboard.layout = html.Div([html.H1('Hi there, I am Dash1')])