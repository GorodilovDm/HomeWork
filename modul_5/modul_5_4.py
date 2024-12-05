class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'{self.name} построен')

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

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
print(House.houses_history)
h2 = House('ЖК Адмирал', 17)
print(House.houses_history)
h3 = House('ЖК Апельсин', 17)
print(House.houses_history)
del h1
del h3
print(House.houses_history)
