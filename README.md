<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

<h1 align=center>PROYECTO STEAM</h1>

En este proyecto se desarrollo una API con el fin de que nos lanze unos datos determinantes al momento de buscarlos, filtrando cada uno de ellos con unas funciones que cumplen la tarea de lanzar los resultados directamente conetados a la API.

Empezamos mostrando las librerias con las cuales se importaron los elementos junto con la importacion del Json:

import pandas as pd

import numpy as np

import ast


rows = []
with open('steam_games (1).json', 'r') as f:
    for line in f.readlines():
        rows.append(ast.literal_eval(line))

df = pd.DataFrame(rows)

- con estos codigos arriba pudimos importar los elementos de las librerias y poder ver tambien los datos que nos lanzaran nuestro DataFrame.
a continuacion las funciones realizadas:

from collections import Counter

df.dropna(subset='genres', inplace= True)

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

  - con la funcion anezxada arriba podemos filtrar los 5 valores que nos piden de cada una:
    from collections import Counter
    
<h1 align=center>GENEROS</h1>

df.dropna(subset='genres', inplace= True)

def genero(year: str):
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

<h1 align=center>JUEGOS</h1>

def JPA(year: str):

    if type(year) != str:
        year = str(year)
    data =  df.loc[df["release_date"].str.contains(year) == True]
    data["app_name"].apply(lambda x: str (x))
    data["release_date"].apply(lambda x: str(x))
    data = data.dropna(subset=["app_name"])
    names_list = [i for i in data["app_name"]]
    return {year: names_list}

<h1 align=center>SPECS</h1>

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

<h1 align=center>SENTIMENT</h1>

def sentiment_years(year: str):

    sentiments_list = ['Mixed', 'Mostly Positive', 'Very Positive', 'Overwhelmingly Positive', 'Very Negative', 'Positive', 'Mostly Negative', 'Negative', 'Overwhelmingly Negative']
    data = df.loc[df['release_date'].str.contains(year) == True]
    data_filt = data.loc[data['sentiment'].isin(sentiments_list)]
    result = []
    for i in sentiments_list:
        result.append((i, len(data_filt.loc[data_filt['sentiment'] == i])))
    result = dict(result)
    return {year: result}

  <h1 align=center>METASCORE</h1>

  def metascore_year(year: str):
  
    data = df.loc[df['release_date'].str.contains(year) == True]
    data = data.dropna(subset=['app_name'])
    data_sorted = data.sort_values(by='metascore', ascending=False)
    top_5 = data_sorted.head(5)
    result = {}
    for idx, row in top_5.iterrows():
        result[row['app_name']] = row['metascore']
    return {year: result}

   <h1 align=center>ANALISIS EXPLORATORIO</h1>

   - Empezamos nuestra limpieza de datos filtrando

Cuando filtramos la etapa de exploración y transformación de los datos. Aquí nos encargaremos de limpiar y explorar los datos, preparándolos para futuras predicciones. El Análisis Exploratorio de Datos (AED) resultará esencial para comprender las relaciones entre distintas variables y detectar posibles patrones e irregularidades.

 <h1 align=center>FINAL DEL ESTUDIO</h1>
 
 Este proyecto es de código abierto y está abierto a contribuciones y sugerencias. Si desea contribuir, siga las siguientes instrucciones:

Haga un fork del repositorio: Haga una copia del repositorio en su propia cuenta de GitHub.

Cree una nueva rama: Cree una nueva rama en su fork para trabajar en su característica o corrección específica.

Realice sus cambios: Realice los cambios necesarios en la nueva rama, asegurándose de seguir las mejores prácticas de codificación y documentación.

Realice un pull request: Una vez que haya completado sus cambios, envíe un pull request a la rama principal del repositorio original. Espere la revisión y aprobación del equipo.
