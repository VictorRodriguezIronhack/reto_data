from flask import Flask, request, render_template
from flask import json
from flask_wtf import FlaskForm
from wtforms import StringField
from flask.json import jsonify, load
from numpy import character
from sqlalchemy.util.langhelpers import method_is_overridden
import tools.sql_tools as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


@app.route("/")
def startup():
    return "Hello World"

@app.route("/collection")
def collection():
    collection = sql.collection()
    return collection

@app.route("/entry")
def gamecomments():
    id_ = request.args['id']
    entry = sql.entry(id_)
    return entry

@app.route("/e10")
def collection():
    collection = sql.e10()
    return collection

@app.route("/sp98")
def collection():
    collection = sql.sp98()
    return collection

app.run(debug=True)