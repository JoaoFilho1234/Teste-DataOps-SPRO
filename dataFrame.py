import pandas as pd
from pymongo import MongoClient

#Criando dataframe Carro

data1 = {
    'Carros': ['Onix', 'Polo', 'Sandero', 'Fiesta', 'City'],
    'Cor': ['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'],
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda']
}


df1 = pd.DataFrame(data1)

#Criando dataframe Montadora

data2 = {
    'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
    'País': ['EUA', 'Alemanhã', 'França', 'EUA', 'Japão']
}

df2 = pd.DataFrame(data2)

client = MongoClient('mongodb://localhost', 27017)
db = client['local']
collection1 = db['Carros']
collection2 = db['Montadoras']

data_to_insert1 = df1.to_dict(orient='records')
data_to_insert2 = df2.to_dict(orient='records')

collection1.insert_many(data_to_insert1)
collection2.insert_many(data_to_insert2)

client.close()
