from fastapi import HTTPException
from curl_cffi import requests

def get_data(search):
    if search.level == "R":
        base = "https://ws-public.interpol.int/notices/v1/red"
    elif search.level == "Y":
        base = "https://ws-public.interpol.int/notices/v1/yellow"
    else:
        raise HTTPException(status_code=400, detail="level must be 'R' or 'Y'")

    params = {
        "resultPerPage": 160,
        "nationality": search.nation,
        "forename": search.forename,
        "name": search.name,
        "ageMax": search.ageMax,
        "ageMin": search.ageMin,
        "sexId": search.sex,
        "warrantCountry": search.warrantCountry,
    }

    response = requests.get(base, params=params, impersonate="chrome")

    if response.status_code != 200:
        return response

    return response.json()
