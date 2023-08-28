while True:
    x = float(input('Anna tuumat: '))
    if x < 0:
        print('Et voi antaa negatiivista lukua!')
        break

    y = x * 2.54
    print(str(y) + 'cm')
