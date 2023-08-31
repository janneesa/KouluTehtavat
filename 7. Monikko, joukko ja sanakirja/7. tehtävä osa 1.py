#tammikuu, helmikuu, maaliskuu, huhtikuu, toukokuu, kesäkuu,
#heinäkuu, elokuu, syyskuu, lokakuu, marraskuu, joulukuu

#talvi = ['joulukuu', 'tammikuu', 'helmikuu']
#kevät = ['maaliskuu', 'huhtikuu', 'toukokuu']
#kesa = ['kesäkuu', 'heinäkuu', 'elokuu']
#syksy = ['syyskuu', 'lokakuu', 'marraskuu']

talvi = (12, 1, 2)
kevat = (3, 4, 5)
kesa = (6, 7, 8)
syksy = (9, 10, 11)

kuukausi = int(input('Anna kuukausi numerona 1-12: '))

if kuukausi in talvi:
    print('Talvi')
elif kuukausi in kevat:
    print('Kevät')
elif kuukausi in kesa:
    print('Kesä')
elif kuukausi in syksy:
    print('Syksy')
else:
    print('Virheellinen kuukausi.')


