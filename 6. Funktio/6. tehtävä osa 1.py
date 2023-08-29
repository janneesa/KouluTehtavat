import random

def noppasimu():
    print('Heitetään noppaa kunnes saadaan 6.')
    heitto = random.randint(1, 6)
    print(heitto)
    while heitto != 6:
        heitto = random.randint(1, 6)
        print(heitto)
    return

noppasimu()