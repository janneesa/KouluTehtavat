import math

def pizza_laskuri(pizzan_halkaisija, pizzan_hinta):
    pizzan_sade = pizzan_halkaisija / 2
    pizzan_neliohinta_m2 = pizzan_hinta / ((math.pi * pizzan_sade**2) / 10000)
    return pizzan_neliohinta_m2

p1h = float(input('Anna ensimmäisen pizzan halkaisijan pituus cm: '))
p1r = float(input('Anna ensimmäisen pizzan hinta e: '))
pizzan_1_neliohinta_m2 = pizza_laskuri(p1h, p1r)
p2h = float(input('Anna toisen pizzan halkaisijan pituus cm: '))
p2r = float(input('Anna toisen pizzan hinta e: '))
pizzan_2_neliohinta_m2 = pizza_laskuri(p2h, p2r)

if pizzan_1_neliohinta_m2 < pizzan_2_neliohinta_m2:
    print(f'Ensimmäinen pizza antaa paremman vastineen rahalle. Sen hinta per m2 on {pizzan_1_neliohinta_m2:.2f}e.')
else:
    print(f'Toinen pizza antaa paremman vastineen rahalle. Sen hinta per m2 on {pizzan_2_neliohinta_m2:.2f}e.')
