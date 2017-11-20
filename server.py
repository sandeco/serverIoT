import pandas as pd
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def server():

    action = request.args.get('action')
    device = request.args.get('device')
    value  = request.args.get('value')

    df = pd.read_csv('sensores.csv')

    retorno = ""


    if action=='r':
        value = df.loc[df['device'] == device]['value']
        retorno = str(float(value))
    elif action=='w':
        try:
            df.loc[df['device']==device,'value']=value

            ##df.append([device,value,data])
            df.to_csv('sensores.csv', index=False)
            retorno = "true"
        except ValueError:
            retorno = ValueError

    return retorno
