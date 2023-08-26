import random

maara = int(input('Montako kuutiota haluat heittää: '))
summa = 0

for x in range(maara):
    luku = random.randint(1, 6)
    summa = summa + luku

print('summa on: ' + str(summa))

