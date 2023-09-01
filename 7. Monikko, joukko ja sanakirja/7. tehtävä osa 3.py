lentokentat = {'EFHK':'Helsinki'}
lopetus = 0

def haku(icao): #funktio joka hakee kentän icao koodilla
    print(f'{icao} on {lentokentat[icao]} airport.')
    return

def add(icao, kentta): #funktio joka lisää icaon ja kentän
    lentokentat[icao] = kentta
    print(f'{icao} : {kentta} lisätty.')
    return

toiminto = input('Haku, Lisäys, Lopeta: ') #määrätään toiminto

while lopetus < 1:
    if toiminto.lower() == 'lopeta': #lopetetaan tehtävä
        lopetus = 1
        print('Ohjelma sammutettu')

    if toiminto.lower() == 'haku': #haetaan kenttää icao koodilla
        ICAO = input('Palaa syöttämällä tyhjä rivi. Anna ICAO: ')
        if ICAO == '':
            toiminto = 'paluu'
        elif ICAO not in lentokentat:
            print('ICAO koodia ei löydy')
        else:
            haku(ICAO.upper())

    if toiminto.lower() == 'lisäys': #lisätään icao ja kenttä
        ICAO = input('Palaa syöttämällä tyhjä rivi. Syötä ICAO: ')
        if ICAO == '':
            toiminto = 'paluu'
        KENTTA = input('Palaa syöttämällä tyhjä rivi. Syötä lentokentän nimi: ')
        if KENTTA == '':
            toiminto = 'paluu'
        else:
            add(ICAO.upper(), KENTTA.capitalize())
            toiminto = 'paluu'


    if toiminto.lower() == 'paluu':
        toiminto = input('Haku, Lisäys, Lopeta: ')  # määrätään toiminto
