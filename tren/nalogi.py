from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Налоги")
root.geometry("350x250")
root.option_add("*tearOff", FALSE)
def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")

file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

main_menu = Menu()
main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Редактирование", command=edit_click)
main_menu.add_cascade(label="Просмотр")

root.config(menu=main_menu)
root.mainloop()