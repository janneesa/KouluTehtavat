import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = random.randint(0, self.huippunopeus)
        self.kuljettu_matka = 0


    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + tunnit * self.tamanhetkinen_nopeus


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasitetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasitetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankki = tankin_koko


tesla = Sahkoauto('ABC-15', 180, 52.5)
lada = Polttomoottoriauto('ACD-123', 165, 32.3)



lada.kulje(3)
tesla.kulje(3)

print(f'Tesla kulki: {tesla.kuljettu_matka}km, nopeus oli: {tesla.tamanhetkinen_nopeus}km/h')
print(f'Lada kulki: {lada.kuljettu_matka}km, nopeus oli: {lada.tamanhetkinen_nopeus}km/h')