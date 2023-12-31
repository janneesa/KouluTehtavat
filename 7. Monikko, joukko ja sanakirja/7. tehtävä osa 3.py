lentokentat = {'EFHK': 'Helsinki'}
lopetus = 0

def haku(icao):  #funktio joka hakee kentän icao koodilla
    print(f'{icao} on {lentokentat[icao]} airport.')
    return

def add(icao, kentta):  #funktio joka lisää icaon ja kentän
    lentokentat[icao] = kentta
    print(f'{icao} : {kentta} lisätty.')
    return

print('Tällä ohjelmalla voit: hakea ja lisätä tietoja lentokentistä järjestelmään.\nAlla on lueteltu käytettävät toiminnot')
toiminto = input('Haku, Lisäys, Lopeta: ')  #määrätään toiminto

while lopetus < 1:
    if toiminto.lower() == 'lopeta' or toiminto == '':  #lopetetaan tehtävä
        lopetus = 1
        print('Ohjelma sammutettu')

    elif toiminto.lower() == 'haku':  #haetaan kenttää icao koodilla
        ICAO = input('Palaa syöttämällä tyhjä rivi.\nAnna ICAO: ')
        if ICAO == '':
            toiminto = 'paluu'
        elif ICAO.upper() not in lentokentat:
            print('ICAO koodia ei löydy')
        else:
            haku(ICAO.upper())

    elif toiminto.lower() == 'lisäys':  #lisätään icao ja kenttä
        ICAO = input('Palaa syöttämällä tyhjä rivi.\nSyötä ICAO: ')
        if ICAO == '':
            toiminto = 'paluu'
        if toiminto == 'paluu':
            continue
        KENTTA = input('Palaa syöttämällä tyhjä rivi.\nSyötä lentokentän nimi: ')
        if KENTTA == '':
            toiminto = 'paluu'
        else:
            add(ICAO.upper(), KENTTA.capitalize())
            toiminto = 'paluu'


    elif toiminto.lower() == 'paluu':
        toiminto = input('Haku, Lisäys, Lopeta: ')  # määrätään toiminto

    else:
        print('Virheellinen toiminto. ')
        toiminto = input('Haku, Lisäys, Lopeta: ')  # määrätään toiminto
