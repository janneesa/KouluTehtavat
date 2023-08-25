lista = []  # Alustetaan tyhjä lista, johon tallennetaan luvut

while True:
    luvut = input("Syötä luku. Tyhjä merkkijono suorittaa toiminnan: ")

    if luvut == "":
        break  # Lopetetaan silmukka, kun käyttäjä syöttää tyhjän merkkijonon

    numero = float(luvut)
    lista.append(numero)  # Lisätään luku listaan

if lista:
    pienin = min(lista)
    suurin = max(lista)

    print(f"Pienin syötetty luku oli {pienin:.2f}")
    print(f"Suurin syötetty luku oli {suurin:.2f}")
else:
    print("Et syöttänyt yhtään lukua.")


