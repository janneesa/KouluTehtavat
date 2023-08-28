sex = input('Ilmoita biologinen sukupuoli M/F: ')
hemo = int(input('ilmoita hemoglobiiniarvosi g/l: '))

if sex.upper() == 'M' and hemo < 134:
    print('hemoglobiiniarvosi on alhainen')
elif sex.upper() == 'M' and hemo <= 195:
    print('hemoglobiiniarvosi on normaali')
elif sex.upper() == 'M' and hemo > 195:
    print('hemoglobiiniarvosi on korkea')
elif sex.upper() == 'F' and hemo < 117:
    print('hemoglobiiniarvosi on alhainen')
elif sex.upper() == 'F' and hemo <= 175:
    print('hemoglobiiniarvosi on normaali')
elif sex.upper() == 'F' and hemo > 175:
    print('hemoglobiiniarvosi on korkea')
else:
    print('virheelliset arvot')
