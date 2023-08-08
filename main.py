from fastapi import FastAPI
from Funciones import JPA
from Funciones import genres
from Funciones import specs_years
from Funciones import get_top_5
from Funciones import earlyacces_year
from Funciones import sentiment_years
from Funciones import metascore_year
from collections import Counter
import pandas as pd
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola, Alberto Pernett"}

@app.get("/genero/{years}")
def genero(years: str):
    try:
        resault = genres(years)
        return resault
    except Exception as e:
        return {"error": str(e)}
    

@app.get("/juegos/{years}")
async def juegos(years: str):
    return JPA(years)


@app.get("/specs/{years}")
def specs(years: str):
    try:
        resault = specs_years(years)
        return resault
    except Exception as e:
        return {"error": str(e)}


@app.get("/early_acces/{years}")
def earlyacces(years: str):
    try:
        resault = earlyacces_year(years)
        return resault
    except Exception as e:
        return {"error": str(e)}

@app.get("/sentiment/{years}")
def sentiment(years: str):
    try:
        resault = sentiment_years(years)
        return resault
    except Exception as e:
        return {"error": str(e)}


@app.get("/metascore/{years}")
def metascore(years: str):
    try:
        resault = metascore_year(years)
        return resault
    except Exception as e:
        return {"error": str(e)}