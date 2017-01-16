#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Thu Oct 27 20:17:17 2016.

@author: lashkov

"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror


def open_pdb():
    global s_lines
    lab6.configure(text='')
    opt = {'filetypes': [
        ('Файлы PDB', ('.pdb', '.PDB', '.ent')), ('Все файлы', '.*')]}
    pdb = askopenfilename(**opt)
    try:
        with open(pdb, 'r') as oldfile:
            s_lines = oldfile.readlines()
    except FileNotFoundError:
        return
    except UnicodeDecodeError:
        showerror('Ошибка', 'Некорректный PDB файл!')
        return


def save_pdb():
    opt = {'filetypes': [
        ('Файлы PDB', ('.pdb', '.PDB', '.ent')), ('Все файлы', '.*')]}
    sa = asksaveasfilename(**opt)
    try:
        with open(sa, 'w') as newfile:
            newfile.write(''.join(newlist))
    except FileNotFoundError:
        showinfo('Информация', 'Выберите файл формата PDB')
        return


def close_win():
    if askyesno('Выход', 'Вы точно хотите выйти?'):
        root.destroy()


def about():
    showinfo('Информация', 'Переименоввание цепей в PDB-файле')


def rename_pdb():
    global newlist
    newlist = []
    try:
        if len(lines_pdb) < 10:
            showerror('Ошибка', 'Некорректный PDB файл!')
            return
    except NameError:
        showerror('Ошибка', 'Не загружен PDB файл!')
        return
    try:
        i = int(v1.get())
        j = int(v2.get())
        ink = int(v3.get())
        chain_name_old = str(v4.get())
        chain_name = str(v5.get())
    except ValueError:
        showerror('Ошибка', 'Неверное значение!')
        return
    if chain_name_old == '':
        chain_name = ' '
    if chain_name == '':
        chain_name = ' '
    for s in s_lines:
        if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  ') or (s[0:6] == 'ANISOU'):
            if (int(s[22:26]) in range(i, j + 1)) and (s[21] == chain_name_old):
                s = s[0:21] + chain_name + \
                    '{0:>4d}'.format(int(s[22:26]) + ink) + s[26:]
        newlist.append(s)
    lab6.configure(text='Готово!')


def main():
    global root
    global v1
    global v2
    global v3
    global v4
    global v5
    global lab6
    root = tk.Tk()
    m = tk.Menu(root)  # создается объект Меню на главном окне
    root.config(menu=m)  # окно конфигурируется с указанием меню для него
    fm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
    # пункту располагается на основном меню (m)
    m.add_cascade(label='Файл', menu=fm)
    # формируется список команд пункта меню
    fm.add_command(label='Открыть PDB', command=open_pdb)
    fm.add_command(label='Сохранить PDB', command=save_pdb)
    fm.add_command(label='Выход', command=close_win)
    m.add_command(label='Запуск...', command=rename_pdb)
    m.add_command(label='Справка', command=about)
    v1 = tk.StringVar()
    ent1 = ttk.Entry(root, width=5, textvariable=v1)
    ent1.grid(row=0, column=1, padx=10)
    lab1 = ttk.Label(root, text='Номер первого а.о.: ')
    lab1.grid(row=0, column=0, sticky='W')
    v2 = tk.StringVar()
    ent2 = ttk.Entry(root, width=5, textvariable=v2)
    ent2.grid(row=1, column=1, padx=10)
    lab2 = ttk.Label(root, text='Номер последнего а.о.: ')
    lab2.grid(row=1, column=0, sticky='W')
    v3 = tk.StringVar()
    ent3 = ttk.Entry(root, width=5, textvariable=v3)
    ent3.grid(row=2, column=1, padx=10)
    lab3 = ttk.Label(root, text='Инкремент: ')
    lab3.grid(row=2, column=0, sticky='W')
    v4 = tk.StringVar()
    ent4 = ttk.Entry(root, width=5, textvariable=v4)
    ent4.grid(row=3, column=1, padx=10)
    lab4 = ttk.Label(
        root, text='Старое наименование цепи: ')
    lab4.grid(row=3, column=0, sticky='W')
    v5 = tk.StringVar()
    ent5 = ttk.Entry(root, width=5, textvariable=v5)
    ent5.grid(row=4, column=1, padx=10)
    lab5 = ttk.Label(
        root, text='Новое наименование цепи: ')
    lab5.grid(row=4, column=0, sticky='W')
    lab6 = ttk.Label(root)
    lab6.grid(row=5, column=0)
    root.mainloop()
if __name__ == '__main__':
    main()
