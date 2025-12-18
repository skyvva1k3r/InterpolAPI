from curl_cffi import requests
from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.responses import FileResponse  
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel, Field, validator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
async def index():
    return FileResponse('index(AI gen.).html')


@app.get('/search')
async def search(
    level : Optional[str] = Query("", pattern = "^[YR]?$"),
    forename : Optional[str] = Query(""),
    name : Optional[str] = Query(""),
    nation : Optional[str] = Query("", max_length=2),
    ageMax : Optional[int] = Query(120, ge=0, le=120),
    ageMin : Optional[int] = Query(0, ge=0, le=120),
    sex : Optional[str] = Query("", pattern="^[MFU]?$"),
    warrantCountry : Optional[str] = Query("", max_length=2)
):
    return get_data(level, forename, name, nation, ageMax, ageMin, sex, warrantCountry)


def get_data(level, forename, name, nation, ageMax, ageMin, sex, warrantCountry):
    if level == "R":
        url = f"https://ws-public.interpol.int/notices/v1/red?resultPerPage=160&nationality={nation}&forename={forename}&name={name}&ageMax={ageMax}&ageMin={ageMin}&sexId={sex}&warrantCountry={warrantCountry}"
        response = requests.get(url, impersonate="chrome")
    elif level == "Y": 
        url = f"https://ws-public.interpol.int/notices/v1/yellow?resultPerPage=160&nationality={nation}&forename={forename}&name={name}&ageMax={ageMax}&ageMin={ageMin}&sexId={sex}&warrantCountry={warrantCountry}"
        response = requests.get(url, impersonate="chrome")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()