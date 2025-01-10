from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def add_():
    tree.insert("", END, values=('06.01.25', 150000))

def new_():
    pass

def open_():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()

def save_():
    pass


root = Tk()
root.title("Налоги")
root.minsize(width=258, height=350)

root.option_add("*tearOff", FALSE)

main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="Новый")
file_menu.add_command(label="Сохранить")
file_menu.add_command(label="Открыть", command=open_)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.destroy)

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Добавить", command=add_, state='disabled')
# main_menu.add_cascade(label="View")
root.config(menu=main_menu)

root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=0, weight=1)


# определяем столбцы
columns = ("date", "summ")

tree = ttk.Treeview(columns=columns, show="headings")
tree.grid(row=0, column=0, sticky="nsew")

# определяем заголовки
tree.heading("date", text="Дата", anchor=W)
tree.heading("summ", text="Сумма", anchor=W)

tree.column("#1", stretch=NO, width=120)
tree.column("#2", stretch=NO, width=120)


# добавляем вертикальную прокрутку
scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")
main_menu.entryconfigure(1, state='normal')
root.mainloop()
