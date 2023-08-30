import math

def pizza_laskuri(pizza1_halkaisija, pizza1_hinta, pizza2_halkaisija, pizza2_hinta):
    pizza1_sade = pizza1_halkaisija / 2
    pizza2_sade = pizza2_halkaisija / 2
    pizza1_alam2 = ((math.pi * pizza1_sade**2) / 10000)
    pizza2_alam2 = ((math.pi * pizza2_sade**2) / 10000)
    pizza1_neliohinta = pizza1_hinta / pizza1_alam2
    pizza2_neliohinta = pizza2_hinta / pizza2_alam2
    if pizza1_neliohinta < pizza2_neliohinta:
        pizza1_neliohinta = 'Ensimmäisellä pizzalla'
        return pizza1_neliohinta
    else:
        pizza2_neliohinta = 'Toisella pizzalla'
        return pizza2_neliohinta

p1h = float(input('Anna ensimmäisen pizzan halkaisijan pituus cm: '))
p1r = float(input('Anna ensimmäisen pizzan hinta: '))
p2h = float(input('Anna toisen pizzan halkaisijan pituus cm: '))
p2r = float(input('Anna toisen pizzan hinta: '))

print(f'{pizza_laskuri(p1h, p1r, p2h, p2r)} on parempi vastine rahalle')