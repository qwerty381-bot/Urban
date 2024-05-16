import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)
def func_add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def func_sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def func_mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def func_div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

window = tk.Tk()

window.title('Calculator')
window.geometry('350x350')
window.resizable(False, False)

button_add = tk.Button(window, text = '+', width = 2, height = 2, command = func_add)
button_add.place(x = 100, y = 200)

button_sub = tk.Button(window, text = '-', width =2, height = 2, command = func_sub)
button_sub.place(x = 150, y = 200)

button_mul = tk.Button(window, text = '*', width = 2, height = 2, command = func_mul)
button_mul.place(x = 200, y = 200)

button_div = tk.Button(window, text = '/', width = 2, height = 2, command = func_div)
button_div.place(x = 250, y = 200)

number1_entry = tk.Entry(window, width = 28)
number1_entry.place(x = 100, y = 75)

number2_entry = tk.Entry(window, width = 28)
number2_entry.place(x = 100, y = 150)

answer_entry = tk.Entry(window, width = 28)
answer_entry.place(x = 100, y = 300)

name_number_1 = tk.Label(text = 'Введите первое число:')
name_number_1.place(x = 100, y = 50)

name_number_2 = tk.Label(text = 'Введите второе число:')
name_number_2.place(x = 100, y = 125)

name_answer = tk.Label(text = 'Ответ:')
name_answer.place(x = 100, y = 275)

window.mainloop()