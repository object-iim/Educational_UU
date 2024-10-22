calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    str_1 = (len(string), string.upper(), string.lower())
    count_calls()
    return str_1
string = string_info
print(string_info('Capybara'))
print(string_info('Armageddon'))

def is_contains(string, list_to_search): # string - тип данных __eq__; list_to_search - тип данных __iter__
    string = string.upper() # тут была ошибка 2 знака равно, вместо 1, код не работал, как надо
    list_to_search = list(list_to_search)
    for i in range(len(list_to_search)): # range(len - кол-во повторений цикла, до его окончания
        if list_to_search[i].upper() == string:
            result = True
        else:
            result = False
    count_calls()
    return result
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print(calls)