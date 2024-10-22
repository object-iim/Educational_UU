class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if not isinstance(other, House):
            return 'Невозможно выполнить операцию. Возможно, один из членов операции не является объектом класса House'
        else:
            return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        if not isinstance(other, House):
            return 'Невозможно выполнить операцию. Возможно, один из членов операции не является объектом класса House'
        else:
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if not isinstance(other, House):
            return 'Невозможно выполнить операцию. Возможно, один из членов операции не является объектом класса House'
        else:
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if not isinstance(other, House):
            return 'Невозможно выполнить операцию. Возможно, один из членов операции не является объектом класса House'
        else:
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if not isinstance(other, House):
            return 'Невозможно выполнить операцию. Возможно, один из членов операции не является объектом класса House'
        else:
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        if not isinstance(other, House):
            return 'Невозможно выполнить операцию. Возможно, один из членов операции не является объектом класса House'
        else:
            return self.number_of_floors != other.number_of_floors


    def __add__(self, value):
        if not isinstance(value, int):
            return 'Невозможно выполнить операцию. Возможно, в данной операции нет чисел'
        else:
            self.number_of_floors = self.number_of_floors + value
            return self
    def __radd__(self, value):
        if not isinstance(value, int):
            return 'Невозможно выполнить операцию. Возможно, в данной операции нет чисел'
        else:
            self.number_of_floors = value + self.number_of_floors
            return self
    def __iadd__(self, value):
        if not isinstance(value, int):
            return 'Невозможно выполнить операцию. Возможно, в данной операции нет чисел'
        else:
            self.number_of_floors += value
            return self

building3 = House('ЖК Эльбрус', 10)
building4 = House('ЖК Акация', 20)

print(building3)
print(building4)

print(building3 == building4) # __eq__

building3 = building3 + 10 # __add__
print(building3)
print(building3 == building4)

building3 += 10 # __iadd__
print(building3)

building4 = 10 + building4 # __radd__
print(building4)

print(building3 > building4) # __gt__
print(building3 >= building4) # __ge__
print(building3 < building4) # __lt__
print(building3 <= building4) # __le__
print(building3 != building4) # __ne__