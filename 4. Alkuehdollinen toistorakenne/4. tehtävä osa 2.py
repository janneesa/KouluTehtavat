while True:
    x = float(input('Anna tuumat: (negatiivinen luku lopettaa) '))
    if x < 0:
        print('Toiminta lopetettu.')
        break

    y = x * 2.54
    print(str(y) + 'cm')
