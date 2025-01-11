import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__(name=name)
        self.power = power
        self.enemy = 100
        self.day = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            sleep(1)
            self.enemy = self.enemy - self.power if self.enemy > self.power else 0
            self.day += 1
            print(f'{self.name} сражается {self.day} день(дня)..., осталось {self.enemy} воинов.')
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 9)
second_knight = Knight("Sir Galahad", 19)
first_knight.start()
sleep(0.1) # для красоты вывода(иногда строки сливаются)
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
