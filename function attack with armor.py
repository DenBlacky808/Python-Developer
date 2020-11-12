name_attacker = input('Input attacker name ')
name_defender = input('Input name of defender ')
attacker = {'name': name_attacker, 'health': 100, 'damage': 10, 'armor': 1.2}
defender = {'name': name_defender, 'health': 100, 'damage': 10, 'armor': 1.2}


def damage(attack_1, defender_1):
    return attack_1['damage'] / defender_1['armor']


def health_after_attack(plr):
    plr['health'] = plr['health'] - damage(attacker, defender)


health_after_attack(defender)
print(round(defender['health'], 2))
print(defender)
