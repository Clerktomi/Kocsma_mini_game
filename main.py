import random

adat = {}

with open('data.txt','r',encoding='utf-8') as file_rd:
    for sor in file_rd:
        data = sor.strip().split(',')
        adat['penz'] = int(data[0])
        adat['szint'] = int(data[1])
        adat['nap'] = int(data[2])

def uj_nap():
    adat['nap'] += 1
    with open('data.txt','w',encoding='utf-8') as file_wr:
        print(f'{adat['penz']},{adat['szint']},{adat['nap']}',file=file_wr)

nevek = [
    'B. Sanyi', 'D. Peti', 'F. Jani', 'G. Laci', 'H. Zoli',
    'J. Pisti', 'K. Robi', 'L. Marci', 'M. Zsolti', 'N. Tomi',
    'P. Ricsi', 'R. Ádám', 'S. Dani', 'T. Geri', 'V. Bence',
    'Z. Levi', 'B. Misi', 'D. Norbi', 'F. Balázs', 'G. Gábor',
    'H. Dénes', 'J. Soma', 'K. Máté', 'L. Csabi', 'M. Bálint',
    'N. Milán', 'P. Kevin', 'R. Attila', 'S. Zétény', 'T. Olivér',
    'V. Krisztián', 'Z. Patrik', 'B. Lóránt', 'D. Tibi', 'F. Gellért',
    'G. Tamás', 'H. Zalán', 'J. Márk', 'K. Alex', 'L. Andris',
    'M. Noel', 'N. Erik', 'P. Dominik', 'R. Roland', 'S. Benő',
    'T. Nimród', 'V. Zsolt', 'Z. Antal', 'B. Lajos', 'D. Imre'
]

koszonesek = {
    'udvarias': [
        'Üdvözlöm',
        'Jó napot',
        'Szervusz',
        'Tiszteletem',
        'Helló'
    ],
    'lazasabb': [
        'Szia',
        'Csá',
        'Hali',
        'Na',
        'Hé'
    ],
    'parasztos_ittas': [
        'heee adjad má',
        'Hé hallod',
        'szevasz'
    ]
}


italok = ['Dreher Világos', 'Borsodi', 'Soproni Klasszikus', 'Heineken', 'Becherovka', 'Unicum', 'Jägermeister', 'Baileys', 'Vodka (Finlandia)', 'Johnnie Walker Red Label', 'Jim Beam', 'Jack Daniel’s', 'Tokaji Aszú', 'Egri Bikavér', 'Martini Bianco', 'Gin Tonic (Bombay)', 'Tequila (Olmeca)', 'Rum (Bacardi)', 'Cider (Strongbow)', 'Rozé Fröccs']
arak = [450, 400, 420, 550, 1200, 1300, 1400, 1600, 1500, 1800, 1700, 1900, 2000, 1500, 1000, 1800, 1600, 1500, 900, 700]

print()
print(f'Üdv, Játékunban, Ön egy kocsmáros italokat kell adnia a vásárlóknak, kezelnie kell a balhékat, el kell számolni a pénzel. (Készítette: Szabó Tamás)')
print()

while True:
    nyitas = input('A kocsma megnyitásához: (start) (kilpés: exit): ').lower().strip()

    while nyitas not in ['start','exit']:
        print()
        print(f'Nem megfelelő művelet!')
        print()
        nyitas = input('A kocsma megnyitásához: (start) (kilpés: exit): ').lower().strip()
        print()

    if nyitas == 'exit':
        print()
        print(f'Sikeres kilépés!')
        print()
        break
    else:
        uj_nap()
        print()
        print(f'Kezdődik a munka! {adat['nap']}. nap')
        print()
        ember = random.choice(nevek)
        ital = random.choice(italok)
        index = italok.index(ital)
        print(f'')