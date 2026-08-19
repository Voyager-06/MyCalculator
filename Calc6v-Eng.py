from tkinter import *
import time
import tkinter.font as font
import math
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import os
window = Tk()
window.geometry("400x520") #Создаём окно (окно, размеры, имя)
window.resizable(1, 1)
window.title("My Calculator")

in_frame = Frame(window, width=380, height=50) #1 рамка- поле ввода
in_frame.pack(side=TOP)

b_frame = Frame(window, width=380, height=450, bg="Darkgrey") #2- Цифры, операции
b_frame.pack()


count_text = StringVar() #Место, на котором будет отображаться информация на экране
entry = Entry(in_frame, font=("Helvetica", 20, "bold"), textvariable=count_text, width=70, justify=RIGHT)
entry.grid(row=0, column=0)
entry.pack(ipady=24)

llr=[]
sz=""
solution = ""

x=0
def button_click(label): #Функция, которая будет выполняться при нажатии на любую кнопку
    global solution, sz, x
    if label == "C": #Кнопка С очищает поле
        solution = ""
        count_text.set("")
    elif label == "=": #1+1=(2)
        try:
            if solution=="NOTEBOOK OPENED":
                solution="True"
                count_text.set(solution)
            elif solution=="True":
                result = "1"
                count_text.set(result)
                llr.append(solution+"="+result)
                lasres=result
                solution = lasres
                    
            elif solution=="False" or solution=="Error!" or solution=="" or solution=="None":
                result = "0"
                count_text.set(result)
                llr.append(solution+"="+result)
                lasres=result
                solution = lasres
            elif solution=="INPUT":
                count_text.set(x)
                per_string = simpledialog.askstring('Inputing Your Symbols', 'Input:')
                solution=per_string
                count_text.set(solution)
                x=per_string

            else:    
                result = str(eval(solution))
                count_text.set(result)
                llr.append(solution+"="+result)
                lasres=result
                solution = lasres
        except Exception as e:
            count_text.set("Error!")
            solution = ""
    elif label == "D":
        solution = solution[:-1]
        count_text.set(solution)
    elif label == "Date":
        t = time.localtime(time.time())
        localtime = time.asctime(t)
        count_text.set(localtime)
    elif label == "FACTORIAL":
        solution = solution + str("math.factorial(")
        count_text.set(solution)
    elif label == "LOGARIFM":
        solution = solution + str("math.log(")
        count_text.set(solution)
    elif label == "SAVE":
        sz = ""
        sz = solution
    elif label == "PASTE":
        solution = solution+sz
        count_text.set(solution)
    elif label == "NOTEBOOK":
            solution= "NOTEBBOOK OPENED"
            count_text.set(solution)
            #Блокнот
            def chenge_theme(theme):
                    text_fild['bg'] = view_colors[theme]['text_bg']
                    text_fild['fg'] = view_colors[theme]['text_fg']
                    text_fild['insertbackground'] = view_colors[theme]['cursor']
                    text_fild['selectbackground'] = view_colors[theme]['select_bg']


            def chenge_fonts(fontss):
                    text_fild['font'] = fonts[fontss]['font']


            def notepad_exit():
                    answer = messagebox.askokcancel('Quit', 'Is It True?')
                    if answer:
                        root.destroy()


            def chenge_fonts(fontss):
                text_fild['font'] = fonts[fontss]['font']
            # Новая функция для изменения размера шрифта
            def chenge_font_size(size):
                # Получаем текущее семейство шрифта
                current_font = text_fild['font']
                # Если шрифт задан строкой (например, 'Arial 14 bold')
                if isinstance(current_font, str):
                    parts = current_font.split()
                    # Заменяем размер (вторая часть)
                    parts[1] = str(size)
                    new_font = ' '.join(parts)
                # Если шрифт задан кортежем (например, ('Arial', 14, 'bold'))
                else:
                    new_font = (current_font[0], size, current_font[2])
                text_fild['font'] = new_font
            
            def show_stats():
                content = text_fild.get('1.0', END)
                words = len(content.split())
                chars = len(content) - 1  # минус последний символ перевода строки
                lines = int(text_fild.index('end-1c').split('.')[0])
                messagebox.showinfo(
                    'Stats',
                    f'Symbols: {chars}\nWords: {words}\nLines: {lines}'
                )            
                    


            def save_file():
                        file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
                        f = open(file_path, 'w', encoding='utf-8')
                        text = text_fild.get('1.0', END)
                        f.write(text)
                        f.close()
            def find_text():
                find_string = simpledialog.askstring('Find', 'What Will You Find?')
                if find_string:
                    text_fild.tag_remove('found', '1.0', END)
                    idx = '1.0'
                    while True:
                        idx = text_fild.search(find_string, idx, nocase=1, stopindex=END)
                        if not idx: break
                        lastidx = f'{idx}+{len(find_string)}c'
                        text_fild.tag_add('found', idx, lastidx)
                        idx = lastidx
                    text_fild.tag_config('found', foreground='red', background='yellow')
            
            def make_bold():
                try:
                    current_tags = text_fild.tag_names('sel.first')
                    if 'bold' in current_tags:
                        text_fild.tag_remove('bold', 'sel.first', 'sel.last')
                    else:
                        text_fild.tag_add('bold', 'sel.first', 'sel.last')
                        text_fild.tag_config('bold', font=('Arial', 14, 'bold'))                    
                except:
                    messagebox.showwarning('WARNING', 'SELECT TEXT!')
            def make_normal():
                try:
                    current_tags = text_fild.tag_names('sel.first')
                    if 'normal' in current_tags:
                        text_fild.tag_remove('normal', 'sel.first', 'sel.last')
                    else:
                        text_fild.tag_add('normal', 'sel.first', 'sel.last')
                        text_fild.tag_config('normal', font=('Arial', 14, 'normal'))                    
                except:
                    messagebox.showwarning('WARNING', 'SELECT TEXT!')            
            def make_italic():
                try:
                    current_tags = text_fild.tag_names('sel.first')
                    if 'italic' in current_tags:
                        text_fild.tag_remove('italic', 'sel.first', 'sel.last')
                    else:
                        text_fild.tag_add('italic', 'sel.first', 'sel.last')
                        text_fild.tag_config('italic', font=('Arial', 14, 'italic'))                    
                except:
                    messagebox.showwarning('WARNING', 'SELECT TEXT!')
            def make_underline():
                try:
                    current_tags = text_fild.tag_names('sel.first')
                    if 'underline' in current_tags:
                        text_fild.tag_remove('underline', 'sel.first', 'sel.last')
                    else:
                        text_fild.tag_add('underline', 'sel.first', 'sel.last')
                        text_fild.tag_config('underline', font=('Arial', 14, 'underline'))                    
                except:
                    messagebox.showwarning('WARNING', 'SELECT TEXT!')
            def reset_formatting():
                try:
                    # Удаляем все теги форматирования из выделенного текста
                    for tag in ['bold', 'italic', 'underline']:
                        text_fild.tag_remove(tag, 'sel.first', 'sel.last')
                except:
                    messagebox.showwarning('WARNING', 'SELECT TEXT!')
            
            root = Tk()
            root.title('TEXT EDITOR')
            root.geometry('600x700')
            
            
            main_menu = Menu(root)
            
            # Файл
            file_menu = Menu(main_menu, tearoff=0)
            file_menu.add_command(label='OPEN', command=open_file)
            file_menu.add_command(label='SAVE', command=save_file)
            file_menu.add_separator()
            file_menu.add_command(label='FIND', command=find_text)
            file_menu.add_separator()
            file_menu.add_command(label='EXIT', command=notepad_exit)
            root.config(menu=file_menu)
            
            # Вид
            view_menu = Menu(main_menu, tearoff=0)
            view_menu_sub = Menu(view_menu, tearoff=0)
            font_menu_sub = Menu(view_menu, tearoff=0)
            size_menu_sub = Menu(view_menu, tearoff=0)
            format_menu_sub = Menu(view_menu, tearoff=0)
            format_menu_sub.add_command(label='BOLD', command=make_bold)
            format_menu_sub.add_command(label='ITALIC', command=make_italic)
            format_menu_sub.add_command(label='UNDERLINE', command=make_underline)
            format_menu_sub.add_command(label='NORMAL', command=make_normal)
            format_menu_sub.add_separator()
            format_menu_sub.add_command(
                label='RESET',
                command=lambda: reset_formatting())
            view_menu.add_cascade(label='FORMAT', menu=format_menu_sub)
            
            view_menu.add_command(label='STATS', command=show_stats)
            view_menu_sub.add_command(label='DARK', command=lambda: chenge_theme('dark'))
            view_menu_sub.add_command(label='LIGHT', command=lambda: chenge_theme('light'))
            view_menu_sub.add_command(label='OCEAN', command=lambda: chenge_theme('ocean'))
            view_menu_sub.add_command(label='FOREST', command=lambda: chenge_theme('forest'))
            view_menu_sub.add_command(label='MOON', command=lambda: chenge_theme('moon'))
            view_menu_sub.add_command(label='COFFEE', command=lambda: chenge_theme('coffee'))            
            view_menu.add_cascade(label='THEME', menu=view_menu_sub)
            
            font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
            font_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
            font_menu_sub.add_command(label='Times New Roman', command=lambda: chenge_fonts('TNR'))
            font_menu_sub.add_command(label='Calibri', command=lambda: chenge_fonts('Calibri'))
            font_menu_sub.add_command(label='Verdana', command=lambda: chenge_fonts('Verdana'))
            font_menu_sub.add_command(label='Chiller', command=lambda: chenge_fonts('Chiller'))
            font_menu_sub.add_command(label='Kristen ITC', command=lambda: chenge_fonts('Kristen'))
            font_menu_sub.add_command(label='Ink Free', command=lambda: chenge_fonts('InkFree'))
            font_menu_sub.add_command(label='Magneto', command=lambda: chenge_fonts('Magneto'))
            font_menu_sub.add_command(label='Wingdings (symbols)', command=lambda: chenge_fonts('Wingdings'))
            font_menu_sub.add_command(label='Webdings (ikons)', command=lambda: chenge_fonts('Webdings'))
            font_menu_sub.add_command(label='Zapf Dingbats', command=lambda: chenge_fonts('ZapfDingbats'))
            
            view_menu.add_cascade(label='FONT TYPE', menu=font_menu_sub)
            
            
            sizes = [5, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 40, 46, 55, 62, 70]
            for size in sizes:
                size_menu_sub.add_command(
                    label=str(size),
                    command=lambda s=size: chenge_font_size(s)
                )
            view_menu.add_cascade(label='FONT SIZE', menu=size_menu_sub)
            # Добавление списков меню
            main_menu.add_cascade(label='FILE', menu=file_menu)
            main_menu.add_cascade(label='TYPE', menu=view_menu)
            
            root.config(menu=main_menu)
            
            f_text = Frame(root)
            f_text.pack(fill=BOTH, expand=1)
            
            view_colors = {
                'dark': {
                    'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
                },
                'light': {
                    'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
                },
                'ocean': {
                        'text_bg': '#0A2463', 'text_fg': '#00FFFF', 'cursor': '#39FF14', 'select_bg': '#1E90FF'
                },
                'forest': {
                        'text_bg': '#224300', 'text_fg': '#F0FFF0', 'cursor': '#7CFC00', 'select_bg': '#32CD32'
                },
                'moon': {
                        'text_bg': '#191970', 'text_fg': '#E6E6FA', 'cursor': '#B0E0E6', 'select_bg': '#483D8B'
                },
                'coffee': {
                        'text_bg': '#3B2F2F', 'text_fg': '#D2B48C', 'cursor': '#DEB887', 'select_bg': '#A0522D'
                }
            }
            
            fonts = {
                'Arial': {
                    'font':('Arial', 14, 'bold')
                },
                'CSMS': {
                    'font': ('Comic Sans MS', 14, 'bold')
                },
                'TNR': {
                    'font': ('Times New Roman', 14, 'bold')
                },
                'Calibri': {
                    'font': ('Calibri', 14, 'bold')
                },
                'Verdana': {
                        'font': ('Verdana', 14, 'normal')
                },
                'Chiller': {
                    'font': ('Chiller', 16, 'bold')
                },
                'Kristen': {
                    'font': ('Kristen ITC', 14, 'normal')
                },
                'InkFree': {
                    'font': ('Ink Free', 14, 'normal')
                },
                'Magneto': {
                    'font': ('Magneto', 14, 'bold')                
                },
                'Wingdings': {
                    'font': ('Wingdings', 14, 'normal')
                },
                'Webdings': {
                    'font': ('Webdings', 14, 'normal')
                },
                'ZapfDingbats': {
                    'font': ('Zapf Dingbats', 14, 'normal')
                }                
            }
            
            text_fild = Text(f_text,
                             bg='black',
                             fg='lime',
                             padx=10,
                             pady=10,
                             wrap=WORD,
                             insertbackground='brown',
                             selectbackground="#6D7151",
                             spacing3=10,
                             width=30,
                             font='Arial 14 bold'
                             )
            text_fild.pack(expand=1, fill=BOTH, side=LEFT)
            
            scroll = Scrollbar(f_text, command=text_fild.yview)
            scroll.pack(side=LEFT, fill=Y)
            text_fild.config(yscrollcommand=scroll.set)
            root.bind('<Control-n>', lambda e: text_fild.delete('1.0', END))
            root.bind('<Control-o>', lambda e: open_file())
            root.bind('<Control-s>', lambda e: save_file())
            root.bind('<Control-q>', lambda e: notepad_exit())
            root.bind('<Control-f>', lambda e: find_text())            
            root.mainloop()
    elif label == "==":
        solution +='=='
        count_text.set(solution)
            
    else: #А любая другая кнопка просто добавляет число в строку или работает как обычно
        solution = solution + str(label)
        count_text.set(solution)

#Функции к строке создали, что же ещё осталось сделать?
def create_button(parent, text, row, column, command, width=13, columnspan=1):#Верно, создать их!
    btn = Button( #Пока что мы готовимся к этому: создаём отступы (padx, pady), и остальное
        parent,
        text=text,
        width=width,
        height=3,
        bd=0,
        bg="white" if text.isdigit() else "lightgrey",
        command=command
    )
    btn.grid(row=row, column=column, columnspan=columnspan, padx=1, pady=1)
#Создаём кнопки
font.nametofont('TkDefaultFont').configure(size=12)
create_button(b_frame, "C", 0,0, lambda: button_click("C"), width=27, columnspan=2)
create_button(b_frame, "0", 4,0, lambda: button_click(0))
create_button(b_frame, "ТОЧКА", 4,1, lambda: button_click("."))
create_button(b_frame, "1", 1,0, lambda: button_click(1))
create_button(b_frame, "2", 1,1, lambda: button_click(2))
create_button(b_frame, "3", 1,2, lambda: button_click(3))
create_button(b_frame, "4", 2,0, lambda: button_click(4))
create_button(b_frame, "5", 2,1, lambda: button_click(5))
create_button(b_frame, "6", 2,2, lambda: button_click(6))
create_button(b_frame, "7", 3,0, lambda: button_click(7))
create_button(b_frame, "8", 3,1, lambda: button_click(8))
create_button(b_frame, "9", 3,2, lambda: button_click(9))
create_button(b_frame, "%", 7,3, lambda: button_click("%"))
create_button(b_frame, "TOP QSTNS", 6,0, lambda: button_click("3**3=9 3//2=1 . Math.pow(number,pownumber). (<-CLOSE IT!!!!"))
create_button(b_frame, "π", 5,0, lambda: button_click("3.1415"))
create_button(b_frame, "(", 5,2, lambda: button_click("("))
create_button(b_frame, ")", 5,3, lambda: button_click(")"))
create_button(b_frame, "|x-y|", 5,1, lambda: button_click("abs("))
create_button(b_frame, "D", 0,2, lambda: button_click("D"))
create_button(b_frame, "TIME", 6,1, lambda: button_click("Date"))
create_button(b_frame, "LAST RESULTS", 6,2, lambda: button_click(llr))
create_button(b_frame, "FACTORIAL", 1,4, lambda: button_click("FACTORIAL"))
create_button(b_frame, "LOG", 7,0, lambda: button_click("LOGARIFM"))
create_button(b_frame, ",", 4,2, lambda: button_click(","))
create_button(b_frame, "E", 7,2, lambda: button_click("2.7182"))
create_button(b_frame, ";", 7,4, lambda: button_click(";"))
create_button(b_frame, "SQRT", 5,4, lambda: button_click("math.sqrt("))
create_button(b_frame, "CBRT", 6,4, lambda: button_click("math.cbrt("))
create_button(b_frame, "SAVE", 3,4, lambda: button_click("SAVE"))
create_button(b_frame, "PASTE", 4,4, lambda: button_click("PASTE"))
create_button(b_frame, "QUIT", 0,4, lambda: button_click(window.destroy()))
create_button(b_frame, "a-> <-b", 2,4, lambda: button_click(" "))
create_button(b_frame, "POW", 6,3, lambda: button_click("math.pow("))
create_button(b_frame, "NITEBOOK", 7,1, lambda: button_click("NOTEBOOK"))
create_button(b_frame, "/", 0,3, lambda: button_click("/"))
create_button(b_frame, "*", 1,3, lambda: button_click("*"))
create_button(b_frame, "-", 2,3, lambda: button_click("-"))
create_button(b_frame, "+", 3,3, lambda: button_click("+"))
create_button(b_frame, "=", 4,3, lambda: button_click("="))
create_button(b_frame, ">", 1,5, lambda: button_click(">"))
create_button(b_frame, "<", 0,5, lambda: button_click("<"))
create_button(b_frame, "==", 2,5, lambda: button_click("=="))
create_button(b_frame, "<=", 3,5, lambda: button_click("<="))
create_button(b_frame, ">=", 4,5, lambda: button_click(">="))
create_button(b_frame, "!=", 5,5, lambda: button_click("!="))
create_button(b_frame, ":", 7,5, lambda: button_click(":"))
create_button(b_frame, "YOUR SYMBOLS", 6,5, lambda: button_click("INPUT:"))
window.mainloop() #Пуск
