import random

kilpa_autot = []

class Auto:
    def __init__(self, rekisteritunnus,):
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
        #print(self.tamanhetkinen_nopeus)

    def kulje(self, tunnit):
        #print(f'Ajetaan {tunnit} tuntia.')
        self.kuljettu_matka = self.kuljettu_matka + tunnit * self.tamanhetkinen_nopeus


for numero in range(10):
    auto = Auto(f'ABC-{numero+1}')
    kilpa_autot.append(auto)

kilpailu = True
aika = 0

while kilpailu:
    aika += 1
    for auto in kilpa_autot:
        kiihdytys = random.randint(-10, 15)
        auto.kiihdyta(kiihdytys)
        auto.kulje(1)
        print(f"{auto.rekisteritunnus}: Nopeus: {auto.tamanhetkinen_nopeus}km/h, Kuljettu matka {auto.kuljettu_matka} km.")

    for auto in kilpa_autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu = False
            #print(f"{auto.rekisteritunnus}: Nopeus: {auto.tamanhetkinen_nopeus}km/h, Kuljettu matka {auto.kuljettu_matka} km.")

for auto in kilpa_autot:
    print(f'Rekisterinumero: {auto.rekisteritunnus}, Huippunopeus: {auto.huippunopeus}km/h, Hetkellinen nopeus: {auto.tamanhetkinen_nopeus}km/h, Kuljettu matka: {auto. kuljettu_matka}km')

