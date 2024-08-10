from flask import Flask, render_template, request, jsonify
from dash import Dash
import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from dash import html
from app_init import app
from app.dashboard.dashboard import dashboard
from llm.solar import Solar

API_KEY = ''
solar = Solar(API_KEY)

@app.route('/')
def home() -> None:
    """Return the landing page."""

    return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login() -> None:
    """Return the login page."""

    return render_template('login.html')

@app.route('/authenticate', methods = ['POST', 'GET'])
def authenticate() -> None:
    """Authenticate the user."""

    username = request.form['username']
    password = request.form['password']

    if (username == 'Company1') and (password == 'password'):
        return flask.redirect('/reports/')

@app.route('/feedback')
def feedback() -> None:
    """Return the Feedback page."""

    return render_template('feedback.html')

@app.route('/reports/', methods = ['GET', 'POST'])
def render_reports() -> None:
    """Return the dashboard page."""

    return flask.redirect('/dashboard')

server = DispatcherMiddleware(app, {'/dashboard': dashboard.server})

@app.route('/plan/')
def plan() -> None:
    """Return the plan template."""

    return render_template('plan.html')

@app.route('/generate', methods=['POST'])

def generate() -> dict:
    """Generate a plan for the current problems."""

    PROMPT = """

    You are a consultant for a medium sized tour company. You are to come up with actionable solutions to address the following complaints from the local community:

        The tour group was very disrespectful to our culture
        The tour group was littering all over.
        The tour company didn't fulfill their end of the bargain. They're promoting their packages at our economic expense.

    What 5 solutions can you suggest to the tour company to resolve these complaints to make their tour packages more sustainable and appease the local community? 
    """

    result = solar.message(PROMPT)

    return jsonify({"response": result})

@app.route("/get_response", methods=["POST"])
def chat() -> dict:
    """Chat with Solar LLM."""

    message = request.form["message"]

    text = f"Solar: {solar.message_chat(message)}"

    return jsonify({"response": text})


if __name__ == '__main__':
    app.run(debug=True)
