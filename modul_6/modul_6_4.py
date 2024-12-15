from random import randint
from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.filled = False
        if self.__is_valid_color(color):
            self.__color = list(color)
        else:
            print('Некорректные данные. Объект создан с произвольным цветом')
            self.__color = [randint(0, 255) for i in range(3)]
        self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        for rgb_ in color:
            if not isinstance(rgb_, int) or not 0 <= rgb_ <= 255 or len(color) != 3:
                return False
        self.filled = True
        return True

    def set_color(self, *r_g_b):
        if self.__is_valid_color(r_g_b):
            self.__color = list(r_g_b)

    def __is_valid_sides(self, sides):
        if isinstance(self, Cube):
            if len(sides) == 1:
                self.__sides = [sides[0] for i in range(12)]
                return False
        if len(sides) != self.sides_count or 0 in sides:
            return False
        else:
            for side in sides:
                if not isinstance(side, int) or side < 0:
                    return False
            else:
                if isinstance(self, Triangle):
                    if (sides[0] + sides[1] > sides[2]
                            and sides[0] + sides[2] > sides[1]
                            and sides[1] + sides[2] > sides[0]):
                        return True
                    else:
                        print('Такого треугольника не существует')
                        return False
                return True

    def check(self, sides):
        return self.__is_valid_sides(sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if self.check(sides):
            super().__init__(color, *sides)
        else:
            super().__init__(color, 1)
        self.__radius = len(self) / (2 * pi)

    def get_square(self):
        self.__radius = len(self) / (2 * pi)
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if self.check(sides):
            super().__init__(color, *sides)
        else:
            super().__init__(color, 1, 1, 1)

    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2
        return sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1 or 0 in sides:
            sides_ = (1 for i in range(12))
            super().__init__(color, *sides_)
        else:
            sides_ = (sides[0] for i in range(12))
            super().__init__(color, *sides_)

    def get_volume(self):
        a = self.get_sides()
        return a[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
