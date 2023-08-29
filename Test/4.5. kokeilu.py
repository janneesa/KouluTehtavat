tunnus = 'python'
salis = 'rules'

anna_tunnus = input('Anna käyttäjä tunnus: ')
anna_salis = input('Anna salasana:')

yritykset = 1

while anna_tunnus != tunnus and anna_salis != salis:
    print(yritykset)
    if yritykset > 4:
        print('Pääsy evätty.')
        break

    if anna_tunnus != tunnus or anna_salis != salis:
        print('Väärin.')
        yritykset += 1
        anna_tunnus = input('Anna käyttäjä tunnus: ')
        anna_salis = input('Anna salasana: ')

    else:
        print('Tervetuloa!')

if anna_tunnus == tunnus and anna_salis == salis:
    print('Tervetuloa!')

