import random

kuutiot = []

x = int(input('montako arpakuutiota haluat heittää: '))

kuutiot.append(x)

for x in kuutiot:
    print(random.randint(1, 6))
