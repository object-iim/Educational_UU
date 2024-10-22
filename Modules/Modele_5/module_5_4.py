class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

building3 = House('ЖК Эльбрус', 10)
print(House.houses_history)
building4 = House('ЖК Акация', 20)
print(House.houses_history)
building5 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# print(House.houses_history[1]) # тест возможности взять Название строения по индексу

# Удаление объектов
del building4
del building5

print(House.houses_history)