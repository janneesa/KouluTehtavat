import random


class Hissi:
    def __init__(self,hissin_numero, alin_kerros, ylin_kerros):
        self.hissin_numero = hissin_numero
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros


    def kerros_ylos(self):
        self.nykyinen_kerros += 1
        return


    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        return


    def siirry_kerrokseen(self, kerrostalo):

        haluttu_kerros = input(f'Mihin kerrokseen haluat siirtyä 1-{kerrostalo.ylin_kerros}: ')

        print(f'Hissi aloittaa kerroksesta {self.nykyinen_kerros}.')

        while self.nykyinen_kerros != int(haluttu_kerros):

            if self.nykyinen_kerros < int(haluttu_kerros):
                self.kerros_ylos()
                print(f'Nykyinen kerros on {self.nykyinen_kerros}')

            elif self.nykyinen_kerros > int(haluttu_kerros):
                self.kerros_alas()
                print(f'Nykyinen kerros on {self.nykyinen_kerros}')

        print(f'Saavuttu kerrokseen {self.nykyinen_kerros}!')



class Talo:


    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = int(alin_kerros)
        self.ylin_kerros = int(ylin_kerros)
        self.hissien_lkm = int(hissien_lkm)
        self.hissit = []

        for numero in range(self.hissien_lkm):
            hissi = Hissi((numero+1), self.alin_kerros, self.ylin_kerros)
            self.hissit.append(hissi)


    def aja_hissia(self):
        haluttu_hissi = int(input(f'Mitä hissiä haluat käyttää 1-{len(kerrostalo.hissit)}: '))
        for hissi in kerrostalo.hissit:
            if hissi.hissin_numero == haluttu_hissi:
                hissi.siirry_kerrokseen(kerrostalo)


    def palohalytys(self):
        print(f'Talossa on palohälytys! kaikki hissit siirtyvät pohjakerrokseen!')
        for hissi in kerrostalo.hissit:
            hissi.nykyinen_kerros = kerrostalo.alin_kerros
            print(f'Hissi numero {hissi.hissin_numero} on kerroksessa {hissi.nykyinen_kerros}')








kerrostalo = Talo(1, 20, 3)

tulipalo = 5

while True:
    kerrostalo.aja_hissia()
    if tulipalo > random.randint(1, 15):
        kerrostalo.palohalytys()
