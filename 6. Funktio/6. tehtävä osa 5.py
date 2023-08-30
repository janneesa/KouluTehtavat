kokolista = []

def karsija(karsittava_lista):
    parilliset = []
    for x in karsittava_lista:
        if x % 2 == 0:
            parilliset.append(x)
    return parilliset

while True:
    luku_str = input('Anna kokonais luku. (Tyhjä rivi suorittaa toiminnon): ')
    if luku_str == '':
        break
    luku = int(luku_str)
    kokolista.append(luku)

print(kokolista)
print(karsija(kokolista))
