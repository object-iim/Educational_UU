class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __len__(self):
        return self.number_of_floors

building3 = House('ЖК Эльбрус', 10)
building4 = House('ЖК Акация', 20)

# __str__
print(building3)
print(building4)

# __len__
print(len(building3))
print(len(building4))