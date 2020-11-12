name_pl = input('Input player name ')
name_en = input('Input name of defender ')

player = {'name': name_pl, 'health': 100, 'damage': 10}
enemy = {'name': name_en, 'health': 100, 'damage': 10}


def attack(person1, person2):
    person2['health'] = person2['health'] - person1['damage']


attack(player, enemy)
print(enemy)
