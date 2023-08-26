import random

arpakuutioiden_lukumaara = int(input("Syötä arpakuutioiden lukumäärä: "))
silmalukujen_summa = 0

for _ in range(arpakuutioiden_lukumaara):
    silmaluku = random.randint(1, 6)
    print(f"Heitto: {silmaluku}")
    silmalukujen_summa += silmaluku

print(f"Silmälukujen summa: {silmalukujen_summa}")
