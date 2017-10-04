#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Thu Oct 27 20:17:17 2016.

@author: lashkov

"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Set B')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.close_win)
        self.menu()
        self.v1 = tk.StringVar()
        ent1 = ttk.Entry(self, textvariable=self.v1, width=5)
        ent1.grid(row=1, column=1, padx=10, pady=5)
        lab1 = ttk.Label(self, text='Номер первого а.о.: ')
        lab1.grid(row=1, column=0, sticky='W', padx=10, pady=5)
        self.v2 = tk.StringVar()
        ent2 = ttk.Entry(self, textvariable=self.v2, width=5)
        ent2.grid(row=2, column=1, padx=10, pady=5)
        lab2 = ttk.Label(self, text='Номер последнего а.о.: ')
        lab2.grid(row=2, column=0, sticky='W', padx=10, pady=5)
        self.v3 = tk.StringVar()
        ent3 = ttk.Entry(self, textvariable=self.v3, width=5)
        ent3.grid(row=3, column=1, padx=10, pady=5)
        lab3 = ttk.Label(self, text='Температурный фактор: ')
        lab3.grid(row=3, column=0, sticky='W', padx=10, pady=5)
        self.v4 = tk.StringVar()
        ent4 = ttk.Entry(self, textvariable=self.v4, width=5)
        ent4.grid(row=0, column=1, padx=10, pady=5)
        lab4 = ttk.Label(self, text='Наименование цепи: ')
        lab4.grid(row=0, column=0, sticky='W', padx=10, pady=5)
        self.lab6 = ttk.Label(self)
        self.lab6.grid(row=4, column=0, pady=5)

    def menu(self):
        m = tk.Menu(self)  # создается объект Меню на главном окне
        self.config(menu=m)  # окно конфигурируется с указанием меню для него
        fm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
        # пункту располагается на основном меню (m)
        m.add_cascade(label='Файл', menu=fm)
        # формируется список команд пункта меню
        fm.add_command(label='Открыть PDB', command=self.open_pdb)
        fm.add_command(label='Сохранить PDB', command=self.save_pdb)
        fm.add_command(label='Выход', command=self.close_win)
        m.add_command(label='Запуск...', command=self.set_b)
        m.add_command(label='Справка', command=self.about)

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.destroy()

    @staticmethod
    def about():
        showinfo('Информация', 'Переименоввание цепей в PDB-файле')


class App(Gui):
    def __init__(self):
        super().__init__()
        self.s_lines = []
        self.newlist = []
        self.run_flag = False

    def open_pdb(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчёт не закончен!')
            return
        self.lab6.configure(text='')
        opt = {'filetypes': [
            ('Файлы PDB', ('.pdb', '.PDB', '.ent')), ('Все файлы', '.*')]}
        pdb = askopenfilename(**opt)
        try:
            with open(pdb) as oldfile:
                self.s_lines = oldfile.readlines()
        except FileNotFoundError:
            return
        except UnicodeDecodeError:
            showerror('Ошибка', 'Некорректный PDB файл!')
            return
        else:
            self.newlist = []

    def save_pdb(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчёт не закончен!')
            return
        if not self.newlist:
            showerror('Ошибка!', 'Данные не получены!')
            return
        opt = {'filetypes': [
            ('Файлы PDB', ('.pdb', '.PDB', '.ent')), ('Все файлы', '.*')]}
        sa = asksaveasfilename(**opt)
        if sa:
            try:
                with open(sa, 'w') as newfile:
                    newfile.write(''.join(self.newlist))
            except FileNotFoundError:
                showinfo('Информация', 'Выберите файл формата PDB')
                return

    def set_b(self):
        if self.run_flag:
            showerror('Ошибка!', 'Расчёт не закончен!')
            return
        if self.s_lines == {}:
            showerror('Ошибка', 'Не загружен PDB файл!')
            return
        if len(self.s_lines) < 10:
            showerror('Ошибка', 'Некорректный PDB файл!')
            return
        try:
            chain_name = str(self.v4.get())
            i = int(self.v1.get())
            j = int(self.v2.get())
            adp = float(self.v3.get())
        except ValueError:
            showerror('Ошибка', 'Неверное значение!')
            return
        if chain_name == '':
            chain_name = ' '
        b_factor = str('{0:6.2f}'.format(adp))
        self.newlist = []
        self.run_flag = True
        for s in self.s_lines:
            if ((s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  ')) and s[21] == chain_name:
                if int(s[22:26]) in range(i, j + 1):
                    s = s[0:60] + b_factor + s[66:]
            self.newlist.append(s)
        self.lab6.configure(text='Готово!')
        self.run_flag = False


def win():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    win()
