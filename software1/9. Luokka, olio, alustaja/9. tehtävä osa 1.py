class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinen_nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = tamanhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

auto = Auto('ABC-123', '142 km/h')

print(auto.rekisteritunnus, auto.huippunopeus, auto.tamanhetkinen_nopeus, auto.kuljettu_matka )