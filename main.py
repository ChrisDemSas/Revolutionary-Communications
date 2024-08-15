from flask import Flask, render_template, request, jsonify
from dash import Dash
import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from dash import html
from app_init import app
from app.dashboard.dashboard import dashboard
from llm.solar import Solar
import datetime
from etl import etl
from llm.predibase_sentiment import PredibaseSentiment
import sqlite3
from app.utils.db_operations import read_sql


SOLAR_API_KEY = ''
solar = Solar(SOLAR_API_KEY)

PREDIBASE_API_KEY = ''
ADAPTER = ''
predibase = PredibaseSentiment(PREDIBASE_API_KEY, ADAPTER)

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

@app.route('/submit_feedback', methods = ['POST', 'GET'])
def submit_feedback() -> None:
    """Submit a feedback and load to a database."""

    category = request.form['category']
    community = request.form['community']
    feedback = request.form['feedback']
    todays_date = datetime.datetime.today().strftime('%Y-%m-%d')
    todays_date = datetime.datetime.strptime(todays_date, '%Y-%m-%d')

    data = {
        'category': category,
        'community': community,
        'feedback': feedback,
        'time': todays_date
    }

    etl(data, 'app/databases/feedback.db', predibase)

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

    conn = sqlite3.connect('app/databases/feedback.db')
    df = read_sql('app/dashboard/queries/recent_comments.sql', conn)

    comments = ""

    for item in df.to_dict("records"):
        feedback = item['feedback']
        comments += feedback + '\n'


    PROMPT = f"""

    You are a consultant for a medium sized tour company. You are to come up with actionable solutions to address the following complaints from the local community:

       {comments}

    What are 10 detailed solutions can you suggest to the tour company to resolve these complaints to make their tour packages more sustainable and appease the local community? 
    Make sure the solutions deal primarily with the tour company and tourists, and not the local community. 
    """

    result = solar.message(PROMPT)

    return jsonify({"response": result})

@app.route("/get_response", methods=["POST"])
def chat() -> dict:
    """Chat with Solar LLM."""

    message = request.form["message"]

    text = f"Solar: {solar.message_chat(message)}"

    return jsonify({"response": text})

@app.route('/chatbot')
def chatbot() -> None:
    """Render the chatbot page."""

    return render_template("chat.html")


if __name__ == '__main__':
    app.run(debug=True)
