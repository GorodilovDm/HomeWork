import threading
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    table.guest.start()
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while threading.active_count() - 1:
            for table in self.tables:
                if not table.guest is None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        print('-' * 30)
                        table.guest = None
                        if not self.queue.empty():
                            table.guest = self.queue.get()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            table.guest.start()


tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
                ]

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)
cafe.discuss_guests()
