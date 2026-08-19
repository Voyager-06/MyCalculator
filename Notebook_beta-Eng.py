from tkinter import *
import time
import tkinter.font as font
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
        # ---------- БЛОКНОТ (адаптирован для телефона) ----------
def open_file():
            file_path = filedialog.askopenfilename(filetypes=(('Text Docs (*.txt)', '*.txt'), ('All Files', '*.*')))
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    text_fild.delete('1.0', END)
                    text_fild.insert('1.0', content)

def chenge_theme(theme):
            text_fild['bg'] = view_colors[theme]['text_bg']
            text_fild['fg'] = view_colors[theme]['text_fg']
            text_fild['insertbackground'] = view_colors[theme]['cursor']
            text_fild['selectbackground'] = view_colors[theme]['select_bg']

def chenge_fonts(fontss):
            text_fild['font'] = fonts[fontss]['font']

def notepad_exit():
            if messagebox.askokcancel('QUIT', 'IS IT TRUE?'):
                root.destroy()

def chenge_font_size(size):
            current_font = text_fild['font']
            if isinstance(current_font, str):
                parts = current_font.split()
                parts[1] = str(size)
                new_font = ' '.join(parts)
            else:
                new_font = (current_font[0], size, current_font[2] if len(current_font) > 2 else 'normal')
            text_fild['font'] = new_font

def show_stats():
            content = text_fild.get('1.0', END)
            words = len(content.split())
            chars = len(content) - 1
            lines = int(text_fild.index('end-1c').split('.')[0])
            messagebox.showinfo('STATS', f'SYMBOLS: {chars}\nWORDS: {words}\nLINES: {lines}')

def save_file():
            file_path = filedialog.asksaveasfilename(filetypes=(('Text Docs (*.txt)', '*.txt'), ('All Files', '*.*')))
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(text_fild.get('1.0', END))
def localtimer():
    t = time.localtime(time.time())
    localtime = time.asctime(t)
    messagebox.showinfo('Время:', localtime)

def find_text():
            find_string = simpledialog.askstring('FIND', 'WHAT?')
            if find_string:
                text_fild.tag_remove('found', '1.0', END)
                idx = '1.0'
                while True:
                    idx = text_fild.search(find_string, idx, nocase=1, stopindex=END)
                    if not idx:
                        break
                    lastidx = f'{idx}+{len(find_string)}c'
                    text_fild.tag_add('found', idx, lastidx)
                    idx = lastidx
                text_fild.tag_config('found', foreground='red', background='yellow')

def make_bold():
            try:
                if 'bold' in text_fild.tag_names('sel.first'):
                    text_fild.tag_remove('bold', 'sel.first', 'sel.last')
                else:
                    text_fild.tag_add('bold', 'sel.first', 'sel.last')
                    text_fild.tag_config('bold', font=('Arial', 10, 'bold'))
            except:
                messagebox.showwarning('WARNING', 'SELECT THE TEXT!')

def make_normal():
            try:
                if 'normal' in text_fild.tag_names('sel.first'):
                    text_fild.tag_remove('normal', 'sel.first', 'sel.last')
                else:
                    text_fild.tag_add('normal', 'sel.first', 'sel.last')
                    text_fild.tag_config('normal', font=('Arial', 10, 'normal'))
            except:
                messagebox.showwarning('WARNING', 'SELECT THE TEXT!')

def make_italic():
            try:
                if 'italic' in text_fild.tag_names('sel.first'):
                    text_fild.tag_remove('italic', 'sel.first', 'sel.last')
                else:
                    text_fild.tag_add('italic', 'sel.first', 'sel.last')
                    text_fild.tag_config('italic', font=('Arial', 10, 'italic'))
            except:
                messagebox.showwarning('WARNING', 'SELECT THE TEXT!')

def make_underline():
            try:
                if 'underline' in text_fild.tag_names('sel.first'):
                    text_fild.tag_remove('underline', 'sel.first', 'sel.last')
                else:
                    text_fild.tag_add('underline', 'sel.first', 'sel.last')
                    text_fild.tag_config('underline', font=('Arial', 10, 'underline'))
            except:
                messagebox.showwarning('WARNING', 'SELECT THE TEXT!')

def reset_formatting():
            try:
                for tag in ['bold', 'italic', 'underline', 'normal']:
                    text_fild.tag_remove(tag, 'sel.first', 'sel.last')
            except:
                messagebox.showwarning('WARNING', 'SELECT THE TEXT!')

root = Tk()
root.title('TEXT EDITOR')
root.geometry('340x600')  # Уменьшенное окно для телефона/Изначальное для компьютера
root.resizable(1, 1)

# --- Меню ---
main_menu = Menu(root)
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='OPEN', command=open_file)
file_menu.add_command(label='SAVE', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='FIND', command=find_text)
file_menu.add_separator()
file_menu.add_command(label='QUIT', command=notepad_exit)
file_menu.add_separator()
file_menu.add_command(label='TIME', command=localtimer)
main_menu.add_cascade(label='FILE', menu=file_menu)

view_menu = Menu(main_menu, tearoff=0)
        # Форматирование
format_menu_sub = Menu(view_menu, tearoff=0)
format_menu_sub.add_command(label='STRONG', command=make_bold)
format_menu_sub.add_command(label='ITALIC', command=make_italic)
format_menu_sub.add_command(label='UNDERLINE', command=make_underline)
format_menu_sub.add_command(label='NORMAL', command=make_normal)
format_menu_sub.add_separator()
format_menu_sub.add_command(label='RESET FORMATTING', command=reset_formatting)
view_menu.add_cascade(label='FORMATTING', menu=format_menu_sub)
        # Статистика
view_menu.add_command(label='STATS', command=show_stats)
        # Темы
theme_menu = Menu(view_menu, tearoff=0)
theme_menu.add_command(label='DARK', command=lambda: chenge_theme('dark'))
theme_menu.add_command(label='LIGHT', command=lambda: chenge_theme('light'))
theme_menu.add_command(label='SEA', command=lambda: chenge_theme('ocean'))
theme_menu.add_command(label='FOREST', command=lambda: chenge_theme('forest'))
theme_menu.add_command(label='MOON', command=lambda: chenge_theme('moon'))
theme_menu.add_command(label='COFFEE', command=lambda: chenge_theme('coffee'))
view_menu.add_cascade(label='THEME', menu=theme_menu)
        # Шрифты
font_menu = Menu(view_menu, tearoff=0)
font_menu.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
font_menu.add_command(label='Times New Roman', command=lambda: chenge_fonts('TNR'))
font_menu.add_command(label='Calibri', command=lambda: chenge_fonts('Calibri'))
font_menu.add_command(label='Verdana', command=lambda: chenge_fonts('Verdana'))
font_menu.add_command(label='Chiller', command=lambda: chenge_fonts('Chiller'))
font_menu.add_command(label='Kristen ITC', command=lambda: chenge_fonts('Kristen'))
font_menu.add_command(label='Ink Free', command=lambda: chenge_fonts('InkFree'))
font_menu.add_command(label='Magneto', command=lambda: chenge_fonts('Magneto'))
font_menu.add_command(label='Wingdings (символы)', command=lambda: chenge_fonts('Wingdings'))
font_menu.add_command(label='Webdings (иконки)', command=lambda: chenge_fonts('Webdings'))
font_menu.add_command(label='Zapf Dingbats', command=lambda: chenge_fonts('ZapfDingbats'))
view_menu.add_cascade(label='Вид шрифта', menu=font_menu)
        # Размер шрифта
size_menu = Menu(view_menu, tearoff=0)
for s in [5, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 40, 46, 55, 62, 70]:
            size_menu.add_command(label=str(s), command=lambda sz=s: chenge_font_size(sz))
view_menu.add_cascade(label='FONT SIZE', menu=size_menu)

main_menu.add_cascade(label='VIEW MENU', menu=view_menu)
root.config(menu=main_menu)

        # --- Текстовое поле и скролл ---
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

view_colors = {
            'dark': {'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'},
            'light': {'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'},
            'ocean': {'text_bg': '#0A2463', 'text_fg': '#00FFFF', 'cursor': '#39FF14', 'select_bg': '#1E90FF'},
            'forest': {'text_bg': '#224300', 'text_fg': '#F0FFF0', 'cursor': '#7CFC00', 'select_bg': '#32CD32'},
            'moon': {'text_bg': '#191970', 'text_fg': '#E6E6FA', 'cursor': '#B0E0E6', 'select_bg': '#483D8B'},
            'coffee': {'text_bg': '#3B2F2F', 'text_fg': '#D2B48C', 'cursor': '#DEB887', 'select_bg': '#A0522D'}
        }

fonts = {
            'Arial': {'font': ('Arial', 10, 'bold')},
            'CSMS': {'font': ('Comic Sans MS', 10, 'bold')},
            'TNR': {'font': ('Times New Roman', 10, 'bold')},
            'Calibri': {'font': ('Calibri', 10, 'bold')},
            'Verdana': {'font': ('Verdana', 10, 'normal')},
            'Chiller': {'font': ('Chiller', 12, 'bold')},
            'Kristen': {'font': ('Kristen ITC', 10, 'normal')},
            'InkFree': {'font': ('Ink Free', 10, 'normal')},
            'Magneto': {'font': ('Magneto', 10, 'bold')},
            'Wingdings': {'font': ('Wingdings', 10, 'normal')},
            'Webdings': {'font': ('Webdings', 10, 'normal')},
            'ZapfDingbats': {'font': ('Zapf Dingbats', 10, 'normal')}
        }

text_fild = Text(f_text,
                         bg='black',
                         fg='lime',
                         padx=6,
                         pady=6,
                         wrap=WORD,
                         insertbackground='brown',
                         selectbackground="#6D7151",
                         spacing3=6,
                         width=25,
                         font='Arial 10 bold')  # Уменьшенный шрифт для телефона
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

        # --- Горячие клавиши (оставляем) ---
root.bind('<Control-n>', lambda e: text_fild.delete('1.0', END))
root.bind('<Control-o>', lambda e: open_file())
root.bind('<Control-s>', lambda e: save_file())
root.bind('<Control-q>', lambda e: notepad_exit())
root.bind('<Control-f>', lambda e: find_text())

root.mainloop()
