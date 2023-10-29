import json
import requests


api_key = 'f3d14acd879ccda1cb4703f95ba9bcfa'

hakusana = input("Anna kaupunki: ")

pyyntö = f"http://api.openweathermap.org/geo/1.0/direct?q={hakusana}&limit=1&appid={api_key}"


def hae_koordinaatit():
    try:
        vastaus = requests.get(pyyntö)
        if vastaus.status_code == 200:
            json_vastaus = vastaus.json()
            for a in json_vastaus:
                lat = (str(a["lat"]))
                lon = (str(a["lon"]))

            return lat, lon

    except requests.exceptions.RequestException as e:
        print ("Hakua ei voitu suorittaa.")


def hae_saa(koordinaatit):

    lat, lon = koordinaatit

    saa = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}'

    try:
        vastaus = requests.get(saa)
        if vastaus.status_code == 200:
            json_vastaus = vastaus.json()

            for i in json_vastaus["weather"]:
                print(f'Sää kohteessa {hakusana}: {i["description"]}.')

            print(f'Lämpötilan on {json_vastaus["main"]["temp"]} Celsius.')

    except requests.exceptions.RequestException as e:
        print("Hakua ei voitu suorittaa.")


hae_saa(hae_koordinaatit())
