data_structure = [[1, 2, 3], {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(*args): # если в этой функции убрать ВСЕ *, то она так же будет работать. Т.е. в целом, символ * не обязателен
    summa_elementov = 0
    for element in args:
        if isinstance(element, int):
            summa_elementov += element
        if isinstance(element, str):
            summa_elementov += len(element)
        if isinstance(element, dict):
            summa_elementov += calculate_structure_sum(*element.keys())
            summa_elementov += calculate_structure_sum(*element.values())
        if isinstance(element, list) or isinstance(element, tuple) or isinstance(element,set):
            summa_elementov += calculate_structure_sum(*element)
    result = summa_elementov
    return result

result = calculate_structure_sum(data_structure)
print(result)

# Такой вариант тоже работает :)
#   "смотрите на меня и не делайте так же" (с) мой учитель

# def calculate_structure_sum(*total_sum):
#     my_list = []
#     for level_1 in total_sum:
#         if isinstance(level_1, list):
#             for level_2 in level_1:
#                 if isinstance(level_2, str):
#                     level_2 = len(level_2)
#                     my_list.append(level_2)
#                 if isinstance(level_2, dict):
#                     values_level_2 = sum(level_2.values())
#                     keys_level_2 = len(level_2.keys())
#                     my_list.append(keys_level_2)
#                     my_list.append(values_level_2)
#                 elif isinstance(level_2, list) or isinstance(level_2, tuple):
#                     for level_3 in level_2:
#                         if isinstance(level_3, int):
#                             my_list.append(level_3)
#                         if isinstance(level_3, str):
#                             level_3 = len(level_3)
#                             my_list.append(level_3)
#                         if isinstance(level_3, dict):
#                             values_level_3 = sum(level_3.values())
#                             my_list.append(values_level_3)
#                             str_values_level_3 = list(dict(level_3))
#                             simvoly = ''.join(str_values_level_3)
#                             kol_vo_simvolov = len(simvoly)
#                             my_list.append(kol_vo_simvolov)
#                         elif isinstance(level_3, list) or isinstance(level_3, set):
#                             for level_4 in level_3:
#                                 if isinstance(level_4, set):
#                                     for level_5 in level_4:
#                                         if isinstance(level_5, tuple):
#                                             for level_6 in level_5:
#                                                 if isinstance(level_6, int):
#                                                     my_list.append(level_6)
#                                                 if isinstance(level_6, str):
#                                                     level_6 = len(level_6)
#                                                     my_list.append(level_6)
#                                                 elif isinstance(level_6, tuple):
#                                                     for level_7 in level_6:
#                                                         if isinstance(level_7, str):
#                                                             level_7 = len(level_7)
#                                                             my_list.append(level_7)
#                                                             for level_7 in level_6:
#                                                                 if isinstance(level_7, int):
#                                                                     my_list.append(level_7)
#                                                             return sum(my_list)
#
# result = calculate_structure_sum(data_structure)
# print(result)

# level_1 == [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])] == data_structure
# level_2 == [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),  добавил "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
# level_3 == добавил 1, 2, 3, 'a': 4, 'b': 5, 6, 'cube': 7, 'drum': 8, и является [{(2, 'Urban', ('Urban2', 35))}]
# level_4 == ничего не добавляет и является {(2, 'Urban', ('Urban2', 35))}
# level_5 == ничего не добавляет и является (2, 'Urban', ('Urban2', 35))
# level_6 == добавил 2, 'Urban' и является ('Urban2', 35)
# level_7 == добавил 'Urban2', 35