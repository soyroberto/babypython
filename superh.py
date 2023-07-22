adjectives = {
    'A': 'Austere',
    'B': 'Brilliant',
    'C': 'Captain',
    'D': 'Dark',
    'E': 'Elegant',
    'F': 'Fantastic',
    'G': 'Gargantuan',
    'H': 'Hulking',
    'I': 'Incredible',
    'J': 'Jovial',
    'K': 'Killing',
    'L': 'Local',
    'M': 'Majestic',
    'N': 'Noble',
    'O': 'Officer',
    'P': 'Proud',
    'Q': 'Quirky',
    'R': 'Radiant',
    'S': 'Swift',
    'T': 'Twin',
    'U': 'Undying',
    'V': 'Venerated',
    'W': 'Wild',
    'X': 'Xeric',
    'Y': 'Yellow',
    'Z': 'Zesty',
}

nouns = {
    1: 'Avenger',
    2: 'Muffin',
    3: 'Crusher',
    4: 'Angel',
    5: 'Striker',
    6: 'Arrow',
    7: 'Judgement',
    8: 'Arbiter',
    9: 'Flash',
    10: 'Blobfish',
    11: 'Vigilante',
    12: 'Lightning',
}

name = input('Please enter your name: ')
month = input('Please enter the number of your birth month (1--12): ')

adjective_key = name[0].upper()
noun_key = int(month)
superhero_name = adjectives[adjective_key] + ' ' + nouns[noun_key]

print('Your superhero name is "' + superhero_name + '".')