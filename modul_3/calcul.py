import tkinter as tk

def get_values():
    num1 = float(number1_entry.get())
    num2 = float(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)




window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False, False)

frm_btn = tk.Frame(window, borderwidth=2, relief='ridge', highlightcolor='blue')
frm_btn.place(x=90, y=200)
button_add = tk.Button(frm_btn, text='+', width=3, height=1, font='35', command=add)
button_add.grid(column=0, row=0, padx=2)
button_sub = tk.Button(frm_btn, text='-', width=3, height=1, font='35', command=sub)
button_sub.grid(column=1, row=0, padx=7)
button_mul = tk.Button(frm_btn, text='*', width=3, height=1, font='35', command=mul)
button_mul.grid(column=2, row=0, padx=7)
button_div = tk.Button(frm_btn, text='/', width=3, height=1, font='35', command=div)
button_div.grid(column=3, row=0, padx=2)


frm_num1 = tk.Frame(window, borderwidth=2, relief='ridge')
frm_num1.place(x=90, y=50)
number1 = tk.Label(frm_num1, text='Введите первое число:', font='20')
number1.pack()
number1_entry = tk.Entry(frm_num1, width=20, font='30')
number1_entry.pack()
frm_num2 = tk.Frame(window, borderwidth=2, relief='ridge')
frm_num2.place(x=90, y=125)
number2 = tk.Label(frm_num2, text='Введите второе число:', font='20')
number2.pack()
number2_entry = tk.Entry(frm_num2, width=20, font='30')
number2_entry.pack()

frm_answ = tk.Frame(window, borderwidth=2, relief='ridge')
frm_answ.place(x=90, y=265)
answer = tk.Label(frm_answ, text='Ответ:', font='20')
answer.pack()
answer_entry = tk.Entry(frm_answ, width=20, font='30')
answer_entry.pack()



window.mainloop()
