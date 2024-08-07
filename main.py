from flask import Flask, render_template
import flask
from dash import Dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from dash import html
from app_init import app
from app.dashboard.dashboard import dashboard

#app = Flask(__name__, static_folder = 'app/style', template_folder='app')
#dashboard = Dash(__name__, server = app, url_base_pathname='/dashboard/')
#dashboard.layout = html.Div([html.H1('Hi there, I am Dash1')])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/reports/')
def render_reports():
    return flask.redirect('/dashboard')

server = DispatcherMiddleware(app, {'/dashboard': dashboard.server})

if __name__ == '__main__':
    app.run(debug=True)
