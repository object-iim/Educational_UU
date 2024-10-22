class Vehicle:
    owner: str
    __model: str
    __engine_power: int
    __color: str
    __COLOR_VARIANTS = ['red', 'orange', 'yellow', 'green', 'blue', 'black']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self, __model):
        print(f'Модель: {self.__model}')

    def get_horsepower(self, __engine_power):
        print(f'Мощность: {self.__engine_power}')

    def get_color(self, __color):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model(self)
        self.get_horsepower(self)
        self.get_color(self)
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        new_color = new_color.upper()
        for i in range(len(self.__COLOR_VARIANTS)):
            if new_color == self.__COLOR_VARIANTS[i].upper():
                self.__color = new_color
                break
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()