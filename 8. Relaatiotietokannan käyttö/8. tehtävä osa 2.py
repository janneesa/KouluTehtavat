import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='Bumbaz9',
         autocommit=True
         )

maakoodi = input('Anna maakoodi: ')

def tyyppihakuri(tyyppi):
    sql = 'SELECT airport.type FROM airport'
    sql += f" WHERE airport.type = '{tyyppi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print(f"{tyyppi} kenttiä on {len(tulos)}")

tyyppihakuri("heliport")
tyyppihakuri("small_airport")

