import pandas as pd
import csv
from datetime import datetime
from flask import Flask


app = Flask(__name__)

nomeArquivo = "sensores.csv"

def gravarDados(device, valor): # função para gravar o valor de um sensor (device)
    
     # nome do arquivo em que o valor será salvo
    try:
        with open(nomeArquivo, 'a', newline='') as arquivo: 
            writer = csv.DictWriter(arquivo, fieldnames=['horario', 'sensor', 'valor'], delimiter=';')        
            if arquivo.tell() == 0:
                writer.writeheader()
            writer.writerow({'horario': str(datetime.now()),'sensor': device, 'valor': valor}) # salvando horario atual e os dados
        return 'Ok'
    except Exception as e: # caso de algum erro
        return 'Falha ao gravar o valor do device: ' + device
    
def lerDados(device): # função que recebe qual o dispositivo para ser buscado, e retorna o ultimo valor que foi gravado
    try:
        dados = pd.read_csv(nomeArquivo, sep=';') # abre o arquivo contendo os dados
        ultimo_valor = int(dados.loc[dados['sensor']==device, 'valor'].tail(1)) # procura o ultimo valor do sensor informado
        return str(ultimo_valor)
    except Exception as e:
        return 'Falha ao buscar o valor do device: ' + device

@app.route("/gravar/<device>/<valor>") # para gravar um valor chamar assim: 127.0.0.1:5000/gravar/sensor-temp5/32   ...sendo o 32 o valor do sensor
def flaskGravar(device, valor): # funcao vai receber os dados, repassar para a função responsável por gravar, e retornar a mensagem de sucesso ou falha
    return gravarDados(device, valor)

@app.route("/ler/<device>")
def flaskLer(device): # para ler o ultimo valor de um sensor chamar assim: 127.0.0.1:5000/ler/sensor-temp3    ...sendo o 'sensor-temp3' o nome do sensor
    return lerDados(device) # funcao vai receber os dados, repassar para a função responsável por ler, e retornar o ultimo valor ou mensagem de falha

app.run(port=5000)