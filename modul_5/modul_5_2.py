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

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors


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
