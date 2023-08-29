def muuntaja(gallonat):
    litrat = gallonat * 3.785
    print(f'{litrat:.2f} litraa')
    return

while True:

    maara = float(input('Muunnetaan gallonat litroiksi. Monta gallonaa?: '))
    if maara < 0:
        break
    muuntaja(maara)

