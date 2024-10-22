# 1. Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params() # вызов без агрументов
print_params(b = 25) # вызов работает :) выводит все аргументы, мы просто перезаписали b
print_params(c = [1,2,3]) # вызов работает :) выводит все аргументы, теперь мы просто перезаписали c
# 2. Распаковка параметров
values_list = [2025, 'New Year', True]
values_dict = {'1': 1, 'b': 'строка', 'c': True}
print_params(*values_list)
print_params(*values_dict) # исли ставить ** пишет ошибку got an unexpected keyword argument
# 3. Распаковка + отдельные параметры
values_list_2 = [2023, "it was a year ago"]
print_params(*values_list_2, 42)

# Исходный код
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)