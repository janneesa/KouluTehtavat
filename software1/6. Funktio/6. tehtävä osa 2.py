import random

def noppasimu(maximi):
    print(f'Heitetään noppaa kunnes saadaan {maximi} luku.')
    heitto = random.randint(1, maximi)
    print(heitto)
    while heitto != maximi:
        heitto = random.randint(1, maximi)
        print(heitto)
    return

noppa = int(input('Kuinka suurta noppaa haluat heittää: '))
noppasimu(noppa)
