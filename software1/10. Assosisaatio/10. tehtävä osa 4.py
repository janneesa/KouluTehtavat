import random
from prettytable import PrettyTable

kilpa_autot = []

tunti = 0


class Auto:
    def __init__(self, rekisteritunnus, ):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = random.randint(100, 200)
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
        if self.uusi_nopeus > self.huippunopeus:
            self.uusi_nopeus = self.huippunopeus
        if self.uusi_nopeus < 0:
            self.uusi_nopeus = 0
        self.tamanhetkinen_nopeus = self.uusi_nopeus

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + tunnit * self.tamanhetkinen_nopeus


class Kilpailu:


    def __init__(self, nimi, pituus, autot):
        self.nimi = str(nimi)
        self.pituus = int(pituus)
        self.autot = autot

    def tunti_kuluu(self):

        global tunti
        tunti += 1

        for auto in self.autot:
            kiihdytys = random.randint(-10, 15)
            auto.kiihdyta(kiihdytys)
            auto.kulje(1)

    def tulosta_tilanne(self):

        taulu = PrettyTable()

        taulu.field_names = ['Rekisterinumero', 'Huippunopeus', 'Hetkellinen nopeus', 'Kuljettu matka']

        for auto in kilpa_autot:
            taulu.add_row([auto.rekisteritunnus, str(auto.huippunopeus) + 'km/h', str(auto.tamanhetkinen_nopeus) + 'km/h', str(auto.kuljettu_matka) + 'km'])

        print(taulu)


    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False




for numero in range(10):
    auto = Auto(f'ABC-{numero + 1}')
    kilpa_autot.append(auto)

kilpailu = Kilpailu('Suuri romuralli', 8000, kilpa_autot)



kisa = True

while kisa == True:

    if kilpailu.kilpailu_ohi() == True:
        break

    kilpailu.tunti_kuluu()

    if tunti % 10 == 0:
        print('Tämänhetkinen tilanne: ')
        kilpailu.tulosta_tilanne()
        if kilpailu.kilpailu_ohi() == True:
            break


print('Lopputulos: ')
kilpailu.tulosta_tilanne()
