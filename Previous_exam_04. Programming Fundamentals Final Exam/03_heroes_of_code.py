def sorted_by_value_descending_key_ascending(dd):
    return dict(sorted(dd.items(), key=lambda x: (-x[1][0], x[0])))


MAX_HEALTH = 100
MAX_MANA = 200

heroes_number = int(input())
heroes = {}

for _ in range(heroes_number):
    heroes_input = input().split(' ')
    name = heroes_input[0]
    health = int(heroes_input[1])
    mana = int(heroes_input[2])
    heroes.update({name: [health, mana]})

command = input().split(' - ')
while command[0] != 'End':
    if command[0] == 'CastSpell':
        name = command[1]
        mana_needed = int(command[2])
        spell_name = command[3]
        old_health = heroes[name][0]
        old_mana = heroes[name][1]
        if old_mana >= mana_needed:
            heroes.update({name: [old_health, old_mana - mana_needed]})
            print(f"{name} has successfully cast {spell_name} and now has {old_mana - mana_needed} MP!")
            command = input().split(' - ')
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")
            command = input().split(' - ')

    elif command[0] == 'TakeDamage':
        name = command[1]
        damage = int(command[2])
        attacker = command[3]
        old_health = heroes[name][0]
        old_mana = heroes[name][1]
        if old_health - damage > 0:
            heroes.update({name: [old_health - damage, old_mana]})
            print(f"{name} was hit for {damage} HP by {attacker} and now has {old_health - damage} HP left!")
            command = input().split(' - ')
        else:
            heroes.pop(name)
            print(f"{name} has been killed by {attacker}!")
            command = input().split(' - ')

    elif command[0] == 'Recharge':
        name = command[1]
        mana_amount = int(command[2])
        old_health = heroes[name][0]
        old_mana = heroes[name][1]
        new_mana = old_mana + mana_amount
        if new_mana > MAX_MANA:
            new_mana = MAX_MANA
            mana_amount = MAX_MANA - old_mana
        heroes.update({name: [old_health, new_mana]})
        print(f"{name} recharged for {mana_amount} MP!")
        command = input().split(' - ')

    elif command[0] == 'Heal':
        name = command[1]
        health_amount = int(command[2])
        old_health = heroes[name][0]
        old_mana = heroes[name][1]
        new_health = old_health + health_amount
        if new_health > MAX_HEALTH:
            new_health = MAX_HEALTH
            health_amount = MAX_HEALTH - old_health
        heroes.update({name: [new_health, old_mana]})
        print(f"{name} healed for {health_amount} HP!")
        command = input().split(' - ')

heroes = sorted_by_value_descending_key_ascending(heroes)

for hero in heroes:
    hp = heroes[hero][0]
    mp = heroes[hero][1]
    print(f'{hero}\n  HP: {hp}\n  MP: {mp}')
