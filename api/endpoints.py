from flask import Flask, request
from pymongo import MongoClient
from flask_pymongo import PyMongo
import os
from helpers.mongoConnection import insert_data, getConsumeDist, getConsumeSpeed, getConsumeTemp, getConsumeFuel
from bson import json_util

from api.app import app

client = MongoClient("mongodb://127.0.0.1:27017")  
db = client["car_fuel_api"] #Seleción de database

# Endpoints API 
@app.route("/", methods=["GET"])
def welcome():
    return {"welcome": "Welcome to the car fuel API"}

# Endpoints extraer datos

# Obtener el consumo dependiendo de la distancia
@app.route("/getconsumed/<distance>")
def getConsumeD(distance):
    return json_util.dumps(getConsumeDist(distance, dict(request.args)))

# Obtener el consumo dependiendo de la velocidad
@app.route("/getconsumes/<speed>")
def getConsumeS(speed):
    return json_util.dumps(getConsumeSpeed(speed, dict(request.args)))

# Obtener el consumo dependiendo de la temperatura exterior
@app.route("/getconsumet/<temp_outside>")
def getConsumeT(temp_outside):
    return json_util.dumps(getConsumeTemp(temp_outside, dict(request.args)))

# Obtener el consumo dependiendo del combustible
@app.route("/getconsumef/<gas_type>")
def getConsumeF(gas_type):
    return json_util.dumps(getConsumeFuel(gas_type, dict(request.args)))
