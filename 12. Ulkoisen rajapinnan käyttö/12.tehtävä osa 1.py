import json
import requests


maara = int(input('Montako vitsiä haluat?: '))

pyyntö = "https://api.chucknorris.io/jokes/random"


for i in range(maara):

    try:
        vastaus = requests.get(pyyntö)
        if vastaus.status_code==200:
            json_vastaus = vastaus.json()

            print(str(i+1) + ".", json_vastaus["value"])

    except requests.exceptions.RequestException as e:
        print ("Hakua ei voitu suorittaa.")