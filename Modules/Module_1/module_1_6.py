# Работа со словарем.
my_dict = {"Артем": 1987, "Василий Петрович": 1971, "Аллочка": 2015}
print(my_dict)
print("Existing value: ", my_dict['Артем'])
print('Not existing value: ', my_dict.get('Алина'))
my_dict.update({'Зинаида Михаиловна': 1964,
                'Михаил Михаилович': 1964})
v = my_dict.pop('Михаил Михаилович')
print("Deleted value: ", v)
print('Modified dictionary: ', my_dict)

# Работа со множеством.
my_set = {2, 3, 3, 3.14, True, False, ("Миша", "Саша", "Даша"), 3.14}
print('Set: ', my_set)
my_set.update({70, 60})
my_set.discard(3)
print('Modified set: ', my_set)