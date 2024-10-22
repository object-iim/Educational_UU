import math

class Figure:
    sides_count = 0
    filled = True

    def __init__(self, __sides, __color):
        self.__sides = __sides
        self.__color = __color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        result = False
        if 0<=r<=255 and 0<=g<=255 and 0<=b<=255:
            result = True
        else:
            result = False
        return result

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if self.__is_valid_color(r, g, b):
            self.__color = r, g, b
        else:
            self.__color = self.__color

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __radius):
        self.__color = __color
        self.__radius = __radius
        super().__init__(__color, __radius)


    def get_square(self, __radius):
        area = math.pi * self.__radius * self.__radius
        return area


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, __sides):
        self.__sides = __sides
        super().__init__([__sides] * self.sides_count, __color)

    def get_square(self):
        area = (math.sqrt(3) / 4) * (self.__sides ** 2)
        result = round(area, 2)
        return result


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, __sides):
        self.__sides = __sides
        super().__init__([__sides] * self.sides_count, __color)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color()) # (55, 66, 77)
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color()) # (222, 35, 130)

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides()) # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15) # Изменится
print(circle1.get_sides()) # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1)) # 15

# Проверка объёма (куба):
print(cube1.get_volume()) # 216

# Другие проверки.
print(" | ______ Другие проверки ______ | ")
triangle1 = Triangle((200, 200, 100), 5)
print(triangle1.get_square())