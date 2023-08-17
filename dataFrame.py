import pandas as pd

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
