
class Julkaisu:
    def __init__(self, julkaiun_nimi):
        self.nimi = julkaiun_nimi



class Kirja(Julkaisu):
    def __init__(self, julkaisun_nimi, kirjoittaja, sivumaara):
        super().__init__(julkaisun_nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f'Kirjan nimi: {self.nimi}, Kirjoittaja: {self.kirjoittaja}, Sivuja: {self.sivumaara}')


class Lehti(Julkaisu):
    def __init__(self, julkaisun_nimi, paatoimittaja):
        super().__init__(julkaisun_nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f'Lehden nimi: {self.nimi}, Päätoimittaja: {self.paatoimittaja}')


lehti = Lehti('Aku Ankka', 'Aki Hyyppä')
kirja = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)

lehti.tulosta_tiedot()

kirja.tulosta_tiedot()
