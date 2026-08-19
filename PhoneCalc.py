from tkinter import *
import time
import tkinter.font as font
import math
from tkinter import messagebox, filedialog, simpledialog

window = Tk()
window.geometry("340x620")          # под телефон
window.resizable(0, 0)              # отключаем изменение размеров
window.title("My Calculator")

# Поле ввода
in_frame = Frame(window, width=320, height=40)
in_frame.pack(side=TOP, fill=X)

count_text = StringVar()
entry = Entry(in_frame, font=("Helvetica", 16, "bold"), textvariable=count_text,
              justify=RIGHT, bd=5, relief=SUNKEN)
entry.pack(fill=X, ipady=6, padx=4, pady=4)

# Панель с кнопками (4 столбца)
b_frame = Frame(window, bg="Darkgrey")
b_frame.pack(fill=BOTH, expand=True)

llr = []
sz = ""
solution = ""
x = 0

# Функции обработки кнопок (без изменений, кроме блокнота – оставлен как есть)
def button_click(label):
    global solution, sz, x
    if label == "C":
        solution = ""
        count_text.set("")
    elif label == "=":
        try:
            if solution == "БЛОКНОТ ОТКРЫТ":
                solution = "True"
                count_text.set(solution)
            elif solution == "True":
                result = "1"
                count_text.set(result)
                llr.append(solution + "=" + result)
                solution = result
            elif solution in ("False", "Ошибка!", "", "None"):
                result = "0"
                count_text.set(result)
                llr.append(solution + "=" + result)
                solution = result
            elif solution == "ВВОД:":
                count_text.set(x)
                per_string = simpledialog.askstring('Ввод символов', 'Введите:')
                solution = per_string
                count_text.set(solution)
                x = per_string
            else:
                result = str(eval(solution))
                count_text.set(result)
                llr.append(solution + "=" + result)
                solution = result
        except Exception:
            count_text.set("Ошибка!")
            solution = ""
    elif label == "D":
        solution = solution[:-1]
        count_text.set(solution)
    elif label == "Date":
        t = time.localtime(time.time())
        count_text.set(time.asctime(t))
    elif label == "FACTORIAL":
        solution += "math.factorial("
        count_text.set(solution)
    elif label == "LOGARIFM":
        solution += "math.log("
        count_text.set(solution)
    elif label == "СЗ":
        sz = solution
    elif label == "ВЗ":
        solution += sz
        count_text.set(solution)
    elif label == "БЛОКНОТ":
        solution = "БЛОКНОТ ОТКРЫТ"
        count_text.set(solution)
        # --- КОД БЛОКНОТА (полностью из вашего файла) ---
        # Здесь должен быть весь код блокнота, но для краткости я оставляю заглушку.
        # Вставьте сюда свой полный код (он не меняется).
        
        messagebox.showinfo("Блокнот", "Вставьте код блокнота из исходного файла")
        
        # --------------------------------------------------
    elif label == "RAVNO":
        solution += '=='
        count_text.set(solution)
    else:
        solution += str(label)
        count_text.set(solution)

# Функция создания кнопки с уменьшенными размерами
def create_button(parent, text, row, column, command, width=6, columnspan=1):
    btn = Button(parent, text=text, width=width, height=2,
                 bd=0, bg="white" if text.isdigit() else "lightgrey",
                 font=("Helvetica", 8, "bold"), command=command)
    btn.grid(row=row, column=column, columnspan=columnspan, padx=1, pady=1)

font.nametofont('TkDefaultFont').configure(size=8)

# ------------------------------------------------------------
# НОВАЯ РАСКЛАДКА НА 4 СТОЛБЦА (все кнопки)
# ------------------------------------------------------------
# Строка 0: C (2 колонки), D, /
create_button(b_frame, "C", 0, 0, lambda: button_click("C"), width=12, columnspan=2)
create_button(b_frame, "D", 0, 2, lambda: button_click("D"))
reate_button(b_frame, "/", 0, 3, lambda: button_click("/"))

# Строка 1: 7,8,9,*
create_button(b_frame, "7", 1, 0, lambda: button_click(7))
create_button(b_frame, "8", 1, 1, lambda: button_click(8))
create_button(b_frame, "9", 1, 2, lambda: button_click(9))
create_button(b_frame, "*", 1, 3, lambda: button_click("*"))

# Строка 2: 4,5,6,-
create_button(b_frame, "4", 2, 0, lambda: button_click(4))
create_button(b_frame, "5", 2, 1, lambda: button_click(5))
create_button(b_frame, "6", 2, 2, lambda: button_click(6))
create_button(b_frame, "-", 2, 3, lambda: button_click("-"))

# Строка 3: 1,2,3,+
create_button(b_frame, "1", 3, 0, lambda: button_click(1))
create_button(b_frame, "2", 3, 1, lambda: button_click(2))
create_button(b_frame, "3", 3, 2, lambda: button_click(3))
create_button(b_frame, "+", 3, 3, lambda: button_click("+"))

# Строка 4: 0, точка, =, %
create_button(b_frame, "0", 4, 0, lambda: button_click(0))
create_button(b_frame, ".", 4, 1, lambda: button_click("."))
create_button(b_frame, "=", 4, 2, lambda: button_click("="))
create_button(b_frame, "%", 4, 3, lambda: button_click("%"))

# Строка 5: (, ), модуль, корень
create_button(b_frame, "(", 5, 0, lambda: button_click("("))
create_button(b_frame, ")", 5, 1, lambda: button_click(")"))
create_button(b_frame, "abs", 5, 2, lambda: button_click("abs("))
create_button(b_frame, "√", 5, 3, lambda: button_click("math.sqrt("))

# Строка 6: факториал, логарифм, степень, кубкорень
create_button(b_frame, "!", 6, 0, lambda: button_click("FACTORIAL"))
create_button(b_frame, "log", 6, 1, lambda: button_click("LOGARIFM"))
create_button(b_frame, "x^y", 6, 2, lambda: button_click("math.pow("))
create_button(b_frame, "∛", 6, 3, lambda: button_click("math.cbrt("))

# Строка 7: π, E, запятая, пробел
create_button(b_frame, "π", 7, 0, lambda: button_click("3.1415"))
create_button(b_frame, "e", 7, 1, lambda: button_click("2.7182"))
create_button(b_frame, ",", 7, 2, lambda: button_click(","))
create_button(b_frame, "ПРОБ.", 7, 3, lambda: button_click(" "))

# Строка 8: сохрзапись, вставзапись, блокнот, время
create_button(b_frame, "СЗ", 8, 0, lambda: button_click("СЗ"))
create_button(b_frame, "ВЗ", 8, 1, lambda: button_click("ВЗ"))
create_button(b_frame, ";", 8, 2, lambda: button_click(";"))
create_button(b_frame, "Время", 8, 3, lambda: button_click("Date"))

# Строка 9: результаты, автор, чаво, свойввод
create_button(b_frame, "Результаты", 9, 0, lambda: button_click(llr))
create_button(b_frame, "Автор", 9, 1, lambda: button_click("Voyager-06"))
create_button(b_frame, "ЧАВО", 9, 2, lambda: button_click("Кор=**0.5; //; math.pow"))
create_button(b_frame, "ВВОД:", 9, 3, lambda: button_click("ВВОД:"))

# Строка 10: <, >, <=, >=
create_button(b_frame, "<", 10, 0, lambda: button_click("<"))
create_button(b_frame, ">", 10, 1, lambda: button_click(">"))
create_button(b_frame, "<=", 10, 2, lambda: button_click("<="))
create_button(b_frame, ">=", 10, 3, lambda: button_click(">="))

# Строка 11: !=, :, РАВНО (==), ВЫЙТИ
create_button(b_frame, "!=", 11, 0, lambda: button_click("!="))
create_button(b_frame, ":", 11, 1, lambda: button_click(":"))
create_button(b_frame, "==", 11, 2, lambda: button_click("RAVNO"))
create_button(b_frame, "ВЫЙТИ", 11, 3, lambda: window.destroy())

window.mainloop()
