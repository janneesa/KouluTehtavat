class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka
    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus += nopeuden_muutos
        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        if self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, tunnit):
        print(f'Ajetaan {tunnit} tuntia.')
        self.kuljettu_matka += tunnit * self.tamanhetkinen_nopeus

auto = Auto('ABC-123', 142)

print(f'Rekisterinumero: {auto.rekisteritunnus}')
print(f'Huippunopeus: {auto.huippunopeus}km/h')
print(f'Nykyinen nopeus: {auto.tamanhetkinen_nopeus}km/h')
print(f'Kuljettu matka: {auto.kuljettu_matka}')

auto.kiihdyta(60)
print(f'Nykyinen nopeus: {auto.tamanhetkinen_nopeus}km/h')
auto.kulje(1.5)
print(f'Kuljettu matka: {auto.kuljettu_matka}km')
