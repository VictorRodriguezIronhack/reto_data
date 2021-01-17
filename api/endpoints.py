from api.app import app 
from api.app import mongo
from flask import request,Response,jsonify
from bson.json_util import loads, dumps, ObjectId
import json

@app.route('/') #doy la bienvenida solo con la url original
def hola_mundo():
    return "<h1>BIENVENIDO A COBIFY!!!!<h1>"


@app.route("/gas/<tipo>")
def gas_caracteristicas(tipo):
    #SACA LAS CARACTERISTICAS DE CADA TRAYECTO EN TORNO A ESE TIPO DE GAS
    tipo = mongo.db.combustibles.find({"gas_type":tipo})
    r = dumps(tipo)
    rjson = Response(r, mimetype="application/json")
    return rjson

#media de consumo de cada tipo de gas y el gasto

@app.route("/consumo/<gas>")
def consumo_medio(gas):
    consumo = mongo.db.combustibles.find({"gas_type":gas})
    
    l = list(consumo)
    lista = [i["consume"]for i in l]
    consumo_medio = sum(lista)/len(lista)
    
    return {"consumo_medio": round(consumo_medio,2),"gasto": round(consumo_medio*l[1]["price"],2)}

#consumo con lluvia o sin lluvia y gasto 
@app.route("/lluvia/<gas>/<int:numero>")
def lluvia(gas,numero):
    rain = mongo.db.combustibles.find({"gas_type":gas,"rain":numero})
    t = list(rain)
    lista_nueva = [i["consume"] for i in t]
    

    
    med = sum(lista_nueva)/len(lista_nueva)
    return {"consumo medio": round(med,2), "gasto": round(med*t[1]["price"],2) }
    
#lo mismo pero con el sol   
@app.route("/sol/<gas>/<int:numero>")
def sol(gas,numero):
    sol = mongo.db.combustibles.find({"gas_type":gas,"sun":numero})
    t = list(sol)
    lista_nueva = [i["consume"] for i in t]
    med = sum(lista_nueva)/len(lista_nueva)
    return {"consumo medio": round(med,2), "gasto": round(med*t[1]["price"],2) }
    
#Con AC o sin aire

@app.route("/aire/<gas>/<int:numero>")
def aire(gas,numero):
    aire = mongo.db.combustibles.find({"gas_type":gas,"AC":numero})
    t = list(aire)
    lista_nueva = [i["consume"] for i in t]
    med = sum(lista_nueva)/len(lista_nueva)
    return {"consumo medio": round(med,2), "gasto": round(med*t[1]["price"],2) }


    