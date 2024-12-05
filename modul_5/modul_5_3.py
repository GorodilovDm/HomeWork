class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

    def __str__(self) -> str:
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __len__(self) -> int:
        return self.number_of_floors

    def __eq__(self, other) -> bool:
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __le__(self, other) -> bool:
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other

    def __lt__(self, other) -> bool:
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __gt__(self, other) -> bool:
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other

    def __ge__(self, other) -> bool:
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other

    def __ne__(self, other) -> bool:
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other

    def __add__(self, other) -> object:
        if isinstance(other, int):
            self.number_of_floors += other
        elif isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        return self

    def __iadd__(self, other) -> object:
        return self.__add__(other)

    def __radd__(self, other) -> object:
        return self.__add__(other)

    def __mul__(self, other) -> object:
        if isinstance(other, int):
            self.number_of_floors *= other
        elif isinstance(other, House):
            self.number_of_floors *= other.number_of_floors
        return self

    def __imul__(self, other) -> object:
        return self.__mul__(other)

    def __rmul__(self, other) -> object:
        return self.__mul__(other)

    def __truediv__(self, other) -> object:
        if isinstance(other, int):
            self.number_of_floors /= other
        elif isinstance(other, House):
            self.number_of_floors /= other.number_of_floors
        return self

    def __itruediv__(self, other) -> object:
        return self.__truediv__(other)

    def __rtruediv__(self, other) -> object:
        if isinstance(other, int):
            self.number_of_floors = other / self.number_of_floors
        return self

    def __sub__(self, other) -> object:
        if isinstance(other, int):
            self.number_of_floors -= other
        elif isinstance(other, House):
            self.number_of_floors -= other.number_of_floors
        return self

    def __isub__(self, other) -> object:
        return self.__sub__(other)

    def __rsub__(self, other) -> object:
        if isinstance(other, int):
            self.number_of_floors = other - self.number_of_floors
        return self


h1 = House('ЖК Матрешки', 14)
h2 = House('ЖК Адмирал', 17)
# h1.go_to(14)
# h2.go_to(7)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

# __eq__
print(h1 == h2)
h1.number_of_floors = 17
print(h1 == h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)
print(h1 == h2)

h2 = 10 + h2  # __radd__
print(h2)

h1 = h1 * 2  # __mul__
print(h1)

h1 = h1 / 2  # __truediv__
print(h1)

h1 = h1 - 5  # __sub__
print(h1)

h1 /= 10  # __itruediv__
print(h1)

h1 = 15 / h1  # __rtruediv__
print(h1)
