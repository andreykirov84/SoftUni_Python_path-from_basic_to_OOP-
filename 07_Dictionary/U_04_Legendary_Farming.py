# def sorted_by_increased_value(dict):
#     return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}


def sorted_by_increased_value(dict):
    return sorted(dict.items(), key=lambda t: t[::-1])


def sorted_by_decreased_value(dict):
    return {k: v for k, v in sorted(dict.items(), reverse=True, key=lambda item: item[1])}


def sorted_by_key(dict):
    return {k: v for k, v in sorted(dict.items(), key=lambda keys: keys[1])}


ll = []
line = input()
while line != '':
    line_ll = line.split(' ')
    ll.extend(line_ll)
    line = input()


key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
legendary_item_obtained = None
for i in range(0, len(ll), 2):
    key = ll[i + 1].lower()
    value = int(ll[i])
    if key == 'shards' or key == 'fragments' or key == 'motes':
        if key in key_materials.keys():
            old_value = key_materials.get(key)
            key_materials.update({key: old_value + value})
        else:
            key_materials.update({key: value})
        if key_materials.get('shards') >= 250 and legendary_item_obtained is None:
            legendary_item_obtained = 'Shadowmourne'
            key_materials.update({'shards': key_materials.get('shards') - 250})
            break
        elif key_materials.get('fragments') >= 250 and legendary_item_obtained is None:
            legendary_item_obtained = 'Valanyr'
            key_materials.update({'fragments': key_materials.get('fragments') - 250})
            break
        elif key_materials.get('motes') >= 250 and legendary_item_obtained is None:
            legendary_item_obtained = 'Dragonwrath'
            key_materials.update({'motes': key_materials.get('motes') - 250})
            break
    else:
        if key in junk.keys():
            old_value = junk.get(key)
            junk.update({key: old_value + value})
        else:
            junk.update({key: value})

print(f'{legendary_item_obtained} obtained!')
key_materials = sorted_by_key(key_materials)
key_materials = sorted_by_decreased_value(key_materials)
junk = sorted_by_key(junk)

[print(f'{key}: {value}') for key, value in key_materials.items()]
[print(f'{key}: {value}') for key, value in junk.items()]

