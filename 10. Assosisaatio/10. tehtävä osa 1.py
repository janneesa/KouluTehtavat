class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros


    def kerros_ylos(self):
        self.nykyinen_kerros += 1
        return


    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        return


    def siirry_kerrokseen(self, haluttu_kerros):

        print(f'Hissi aloittaa kerroksesta {self.nykyinen_kerros}.')

        while self.nykyinen_kerros != int(haluttu_kerros):

            if self.nykyinen_kerros < int(haluttu_kerros):
                self.kerros_ylos()
                print(f'Nykyinen kerros on {self.nykyinen_kerros}')

            elif self.nykyinen_kerros > int(haluttu_kerros):
                self.kerros_alas()
                print(f'Nykyinen kerros on {self.nykyinen_kerros}')

        print(f'Saavuttu kerrokseen {self.nykyinen_kerros}!')






max_kerros = int(input('Anna hissiille ylin kerros: '))
min_kerros = int(input('Anna hissille alin kerros: '))

h = Hissi(min_kerros, max_kerros)

print(f'Alin kerros: {h.alin_kerros}. Ylin kerros: {h.ylin_kerros}')
haluttu_kerros = int(input(f'mihin kerrokseen haluat mennä: '))

while haluttu_kerros > h.ylin_kerros or haluttu_kerros < h.alin_kerros:
    haluttu_kerros = int(input(f'Virheellinen kerros. Anna uusi: '))

while haluttu_kerros != '':

    h.siirry_kerrokseen(haluttu_kerros)

    haluttu_kerros = int(input(f'Valitse uusi kerros: '))

    while haluttu_kerros > h.ylin_kerros or haluttu_kerros < h.alin_kerros:
        haluttu_kerros = int(input(f'Virheellinen kerros. Anna uusi: '))
