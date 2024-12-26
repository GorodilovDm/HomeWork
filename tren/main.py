class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'ФИО: {self.name}, Должность: {self.position}, Оклад: {self.salary}'


class Manager(Employee):
    def __init__(self, name, position, salary, team_size):
        super().__init__(name, position, salary)
        self.team_size = team_size

    def __str__(self):
        return f'{super().__str__()}, Размер команды: {self.team_size}'


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        for emp in self.employees:
            print(emp)
        print('-' * 30)

    def save_to_file(self, filename):
        self.filename = filename
        with open(filename, 'a+', encoding='utf-8') as file:
            file.seek(0)
            temp = file.read()
            for emp in self.employees:
                if emp.name in temp:
                    continue
                elif isinstance(emp, Manager):
                    file.write(f'{emp.name}, {emp.position}, {emp.salary}, {emp.team_size}\n')
                else:
                    file.write(f'{emp.name}, {emp.position}, {emp.salary}\n')
            print(f'Сохранено в файл {filename}')

    def read_from_file(self, filename):
        self.filename = filename
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    if line == '\n':
                        continue
                    else:
                        line = line.rstrip('\n')
                        line = line.split(', ')
                        if len(line) == 4:
                            self.add_employee(Manager(line[0], line[1], line[2], line[3]))
                        else:
                            self.add_employee(Employee(line[0], line[1], line[2]))
            self.list_employees()
            # print(file.read())

        except FileNotFoundError:
            print(f'Файл {filename} не существует')

    def dismiss(self, name):
        for emp in self.employees:
            if name == emp.name:
                self.employees.remove(emp)
                print(f'Сотрудник {name}  уволен')
                with open(self.filename, 'w', encoding='utf-8') as file:
                    for emp in self.employees:
                        if isinstance(emp, Manager):
                            file.write(f'{emp.name}, {emp.position}, {emp.salary}, {emp.team_size}\n')
                        else:
                            file.write(f'{emp.name}, {emp.position}, {emp.salary}\n')



company = Company()

while True:
    print('Добро пожаловать в программу Сотрудник 2.0')
    print('В этой программе доступны команды: \n'
          'add - добавление сотрудника\n'
          'list - вывод списка всех сотрудников\n'
          'save - сохранение списка сотрудников в отдельный файл\n'
          'read - чтение списка сотрудников из файла\n'
          'del - уволить сотрудника\n'
          'exit - выход из программы')
    print('-' * 30)
    if not company.employees:
        print('Сотрудников в списке нет')

    action = input('Выберите действие (add/list/save/read/del/exit): ')
    if action == 'add':
        emp_type = input('Введите тип сотрудника (разработчик / тимлид): ')
        name = input('Введите ФИО сотрудника: ')
        position = input('Введите должность сотрудника: ')
        salary = input('Укажите оклад сотрудника: ')

        if emp_type == 'тимлид':
            team_size = int(input('Введите кол-во команды: '))
            company.add_employee(Manager(name, position, salary, team_size))
        else:
            company.add_employee(Employee(name, position, salary))
        print('Сотрудник добавлен')

    elif action == 'list':
        company.list_employees()

    elif action == 'save':
        filename = input('Введите имя файла для сохранения: ')
        company.save_to_file(filename)

    elif action == 'read':
        filename = input('Введите имя файла для чтения: ')
        company.read_from_file(filename)

    elif action == 'del':
        if not company.employees:
            print('Загрузите список сотрудников (read)')
        else:
            name = input('Введите ФИО сотрудника для увольнения: ')
            company.dismiss(name)

    elif action == 'exit':
        print('Сеанс завершен!')
        break

    else:
        print('Некорректное действие! Пожалуйста, попробуйте снова.')

"""
  # Добавить сообщение после добавления сотрудника
  # Добавить сообщение после сохранения

  # Вывести сообщение, если список сотрудников на начало программы пустой
  ** Вывести список сотрудников из другого файла, если сотрудники там есть

  # Добавить возможность увольнения (удаления) сотрудника из общего файла

  # Добавить возможность дополнять список сотрудников добавляя новых (чтобы список каждый раз не обнулялся)
"""
