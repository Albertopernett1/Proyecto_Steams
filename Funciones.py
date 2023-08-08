import pandas as pd
import numpy as np
import ast

rows = []
with open('steam_games (2).json', 'r') as f:
    for line in f.readlines():
        rows.append(ast.literal_eval(line))

df = pd.DataFrame(rows)

def get_top_5(diccionario):
    diccionario = dict(sorted(diccionario.items(), key=lambda x: x[1], reverse=True))
    primeros_5_valores = {}
    contador = 0
    for clave, valor in diccionario.items():
        primeros_5_valores[clave] = valor
        contador += 1
        if contador == 5:
            break
    return primeros_5_valores

#def genero( Año: str ): Se ingresa un año y devuelve una lista con los 5 géneros más vendidos en el orden correspondiente.

from collections import Counter

def genres(year: str):
    df.dropna(subset='genres', inplace= True)
    ventas = df.loc[df["release_date"].str.contains(year) == True]
    lista0 = ventas['genres'].tolist()
    B=[]
    for lista1 in lista0:
        for numero in lista1:
            B.append(numero)

    a = dict(Counter(B))
    sorteddict=sorted(a)
    sorteddict=sorteddict[0:4]
    return sorteddict

#def juegos( Año: str ): Se ingresa un año y devuelve una lista con los juegos lanzados en el año.

def JPA(year: str):
    if type(year) != str:
        year = str(year)
    data =  df.loc[df["release_date"].str.contains(year) == True]
    data["app_name"].apply(lambda x: str (x))
    data["release_date"].apply(lambda x: str(x))
    data = data.dropna(subset=["app_name"])
    names_list = [i for i in data["app_name"]]
    return {year: names_list}

#def specs( Año: str ): Se ingresa un año y devuelve una lista con los 5 specs que más se repiten en el mismo en el orden correspondiente.

from collections import Counter

def specs_years(year: str):
    df.dropna(subset='specs', inplace= True)
    repetidos = df.loc[df["release_date"].str.contains(year) == True]
    lista0 = repetidos['specs'].tolist()
    B=[]
    for lista1 in lista0:
        for numero in lista1:
            B.append(numero)
    
    a = dict(Counter(B))
    specs_1 = get_top_5(a)
    return specs_1


#def earlyacces( Año: str ): Cantidad de juegos lanzados en un año con early access.

def earlyacces_year(year: str):
    df.dropna(subset='early_access', inplace= True)
    cantidad_juegos = df.loc[df["release_date"].str.contains(year) == True]
    lista = cantidad_juegos['early_access'].tolist()
    diccionario = {year: len(lista)}
    return diccionario

#def sentiment( Año: str ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.

def sentiment_years(year: str):
    sentiments_list = ['Mixed', 'Mostly Positive', 'Very Positive', 'Overwhelmingly Positive', 'Very Negative', 'Positive', 'Mostly Negative', 'Negative', 'Overwhelmingly Negative']
    data = df.loc[df['release_date'].str.contains(year) == True]
    data_filt = data.loc[data['sentiment'].isin(sentiments_list)]
    result = []
    for i in sentiments_list:
        result.append((i, len(data_filt.loc[data_filt['sentiment'] == i])))
    result = dict(result)
    return {year: result}

#def metascore( Año: str ): Top 5 juegos según año con mayor metascore.

def metascore_year(year: str):
    data = df.loc[df['release_date'].str.contains(year) == True]
    data = data.dropna(subset=['app_name'])
    data_sorted = data.sort_values(by='metascore', ascending=False)
    top_5 = data_sorted.head(5)
    result = {}
    for idx, row in top_5.iterrows():
        result[row['app_name']] = row['metascore']
    return {year: result}





