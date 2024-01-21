vuodenajat = ('talvi', 'talvi', 'kevät', 'kevät', 'kevät', 'kesä', 'kesä', 'kesä', 'syksy', 'syksy', 'syksy', 'talvi')
kuukausi = int(input('Anna kuukausi numerona: '))
if kuukausi - 1 not in range(len(vuodenajat)):
    print('virheellinen kuukausi.')
else:
    print(vuodenajat[kuukausi - 1])
