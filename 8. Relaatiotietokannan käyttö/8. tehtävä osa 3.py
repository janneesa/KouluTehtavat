import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='Bumbaz9',
         autocommit=True
         )

def koordinaattori(icao):
    while True:
        sql = 'SELECT latitude_deg, longitude_deg FROM airport '
        sql += f"WHERE airport.ident = '{icao}'"
        #print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        koordinaatit = kursori.fetchall()
        print(koordinaatit)
        if kursori.rowcount > 0:
            return koordinaatit
        elif kursori.rowcount == 0:
            icao = input('Virheelline ICAO. Anna uusi: ')


icao1 = input('Anna ICAO: ')
kentta1 = koordinaattori(icao1)
icao2 = input('Anna toinen ICAO: ')
kentta2 = koordinaattori(icao2)

from geopy import distance
print(f'Kenttien etäisyys on {distance.distance(kentta1, kentta2).km:.2f}km')
