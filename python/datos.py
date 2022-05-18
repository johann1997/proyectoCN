# importamos lo necesario
from optparse import Values
from tokenize import Double
from flask import Flask, redirect, render_template, request
import urllib.request as urllib2
import json 
# Instancia de Flask Aplicacion
app = Flask (__name__)

@app.route('/')
def template():
    return render_template("home.html")

@app.route('/home')
def template_2():
    return redirect("home.html")

@app.route('/register',methods=['POST'])
def registro():
    Edad = request.form['edad']
    Sexo = request.form['sexo']
    Chest = request.form['chest']
    Pa = request.form['pa']
    Col = request.form['colesterol']
    Bs = request.form['bs']
    Ecg = request.form['ecg']
    Maxhr = request.form['maxhr']
    Exer = request.form['ExerciseAngina']
    Old = request.form['oldpeak']
    Slope = request.form['slope']


    #Conversiones de tipos de variables
    Ed = int(Edad)
    Res = int(Pa)
    Coles = int(Col)
    BS = int(Bs)
    Max = int(Maxhr)
    Ex = bool(Exer)
    Ol = float(Old)

    datos = {
    "Inputs": {
        "data":
        [
            {
                "Age": Ed,
                "Sex": Sexo,
                "ChestPainType": Chest,
                "RestingBP": Res,
                "Cholesterol": Coles,
                "FastingBS": BS,
                "RestingECG": Ecg,
                "MaxHR": Max,
                "ExerciseAngina": Ex,
                "Oldpeak": Ol,
                "ST_Slope": Slope
            },
        ]
    },
    "GlobalParameters": {
        "method": "predict"
    }
}

    

    body = str.encode(json.dumps(datos))

    url = 'http://0dad529f-a1d7-4239-b0ab-0c8876a9d5ec.australiaeast.azurecontainer.io/score'
    headers = {'Content-Type':'application/json', }

    req = urllib2.Request(url, body, headers) 

    try:
        response = urllib2.urlopen(req)
        result = response.read()
        print(result) 
    except urllib2.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))
    res = result
    new_res = res.decode('utf-8')
    d = json.loads(new_res)
    resultado = str(d["Results"])
    if resultado=="[0]":
        return render_template("true.html")
    else :
        return render_template("false.html")

if __name__ == '__main__':
    app.run(debug=True)