import pandas as pd

dados = pd.read_csv('lista_de_sensores.csv')

sensores = dados['id']

print(sensores.to_string)

json = sensores.to_json()

print(json)