from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
mongo = app.config["MONGO_URI"]= "mongodb://localhost:27017/reto_data"
mongo = PyMongo(app) 