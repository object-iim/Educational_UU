import random

def field():
    numbers_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = random.choice(numbers_1)
    return n
n = field() # можно заменить на n = int(input('Введите число от 3 до 20: '))
print(f'Вам выпало число {n}')

# if n < 3 or n > 20:
#     n = int(input('БЫЛО СКАЗАНО ОТ 3 ДО 20: '))

numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers_2.remove(n)

result = ''

for i in numbers_2:
    for j in numbers_2:
        pair = (i, j)
        if n % sum(pair) == 0 and i < j:
            result = result + str(i) + str(j)

print("Пароль к данному числу -", result)