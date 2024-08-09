from flask import Flask, render_template
import flask
from dash import Dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from dash import html
from app_init import app
from app.dashboard.dashboard import dashboard

@app.route('/')
def home() -> None:
    """Return the landing page."""
    return render_template('index.html')

@app.route('/login')
def login() -> None:
    """Return the login page."""
    return render_template('login.html')

@app.route('/feedback')
def feedback() -> None:
    """Return the Feedback page."""
    return render_template('feedback.html')

@app.route('/reports/')
def render_reports() -> None:
    """Return the dashboard page."""
    return flask.redirect('/dashboard')

server = DispatcherMiddleware(app, {'/dashboard': dashboard.server})

@app.route('/get', methods=['GET', 'POST'])
def plan() -> str:
    """Return one chat with the Solar LLM."""
    msg = request.form["msg"]
    input = """Insert Prompt Here."""
    return get_Chat_response(input) # Chat Response here

def get_Chat_response(text: str) -> str:
    """Take in an input and return the response.
    
    Attributes:
        text: The text that is transmitted to Solar LLM.
    """


if __name__ == '__main__':
    app.run(debug=True)
