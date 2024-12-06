import tkinter as tk

class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    # wind = tk.Tk()
    # wind.title('Практика')
    # wind.geometry('350x350')
    # frame = tk.Frame(wind, borderwidth=2, relief='ridge', highlightcolor='blue')
    # frame.place(rely=0.1, relx=0.35)
    # log_btn = tk.Button(frame, text='Вход', height=1, font='35')
    # log_btn.pack(fill='x')
    # reg_btn = tk.Button(frame, text='Регистрация', height=1, font='35')
    # reg_btn.pack()
    database = Database()
    while True:
        choice = input('Привет. Выберите действие: \n1 - Вход\n2 - Регистрация\n')
        user = User(input('Введите логин: '), password := input('Введите пароль: '),
                password2 := input('Повторите пароль: '))
        if password.islower() or password.isalpha():
            exit('ff')
        if password != password2:
            exit()
        database.add_user(user.username, user.password)
        print(database.data)
    # wind.mainloop()