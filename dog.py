import requests
import json

def SearchBreed(dogBreed):
    url = "https://dogbreeddb.p.rapidapi.com/"

    querystring = {"search": dogBreed}

    headers = {
    "X-RapidAPI-Key": "062c82d7efmsh57637c410f4a7f7p135c0cjsn805dfa823407",
    "X-RapidAPI-Host": "dogbreeddb.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.json())
    return response.json()