numerot = []

def summaaja(lista):
    summa = sum(lista)
    return summa

while True:
    x = input('Anna kokonaisluku: ')
    if x == '':
        break

    x = float(x)
    numerot.append(x)

yhteistulos = summaaja(numerot)
print(f'lukujen summan on: {yhteistulos}')

