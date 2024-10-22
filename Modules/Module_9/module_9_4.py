first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x==y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        for elem in data_set:
            file = open(file_name, 'a', encoding='utf-8')
            elem_str = str(elem)
            file.write(elem_str + '\n')
            file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


import random

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *words):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())



