kaupungit = []

for _ in range(5):
    kysy = input('Nimeä kaupunki: ')
    kaupungit.append(kysy)

for _ in kaupungit:
    print(_.capitalize())
