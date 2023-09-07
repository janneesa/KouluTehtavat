import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Bumbaz9',
         autocommit=True
         )

icao = input('Anna kentän ICAO koodi: ')

sql = 'SELECT airport.name, airport.municipality FROM airport'
sql += " WHERE airport.ident ='" + icao + "'"
print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
if kursori.rowcount >0 :
    print(tulos)
