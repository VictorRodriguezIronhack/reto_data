from flask import Flask, request, render_template
import os
import json
import pandas as pd
import src.modelo as md


app = Flask(__name__)

@app.route("/load")
def upload_file():
 # renderiamos la plantilla "formulario.html"
 return render_template('formulario.html')

@app.route("/upload", methods=['POST'])
def uploader():
    
    distancia = int(request.form['distancia'])
    velocidad = int(request.form['velocidad'])
    temp_int = int(request.form['temp_int'])
    temp_out = int(request.form['temp_out'])
    ac = int(request.form['ac'])
    rain = int(request.form['rain'])
    sun = int(request.form['sun'])
    
    return md.modelo_predictivo(distancia, velocidad, temp_int, temp_out, ac, rain, sun)



app.run(debug=True)