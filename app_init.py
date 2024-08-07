from flask import Flask, render_template
import flask
from dash import Dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from dash import html

app = Flask(__name__, static_folder = 'app/style', template_folder='app')
