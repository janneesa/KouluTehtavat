import mysql.connector

from flask import Flask, Response
import json

app = Flask(__name__)


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Bumbaz9',
         autocommit=True
         )

@app.route('/kenttä/<icao>')
def hae_kennta(icao):

    sql = 'SELECT airport.ident as ICAO, airport.name, airport.municipality FROM airport'
    sql += " WHERE airport.ident ='" + icao + "'"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
