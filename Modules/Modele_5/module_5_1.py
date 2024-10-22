class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for new_floor in range(1, new_floor+1):
                print(new_floor)

building1 = House('ЖК Горский', 18)
building2 = House('Домик в деревне', 2)
building1.go_to(5)
building2.go_to(10)