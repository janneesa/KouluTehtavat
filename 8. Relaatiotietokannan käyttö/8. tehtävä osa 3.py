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
    sql = 'SELECT airport.type FROM airport '
    sql += f"WHERE airport.iso_country = '{maakoodi}' AND TYPE = '{tyyppi}'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        print(f"{tyyppi} kenttiä on {len(tulos)}")
    elif kursori.rowcount == 0:
        print(f'{tyyppi} kenttiä on nolla')

tyyppihakuri("heliport")
tyyppihakuri("small_airport")
tyyppihakuri("medium_airport")
tyyppihakuri('large_airport')
tyyppihakuri('seaplane_base')
tyyppihakuri('closed')