#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Mon Nov 28 23:52:06 2016.

@author: lashkov

"""

import random
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('DNA_srg')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.close_win)
        self.menu()
        fra1 = tk.Frame(self)
        fra1.grid(row=0, column=0)
        self.ent = tk.Entry(fra1, width=10, bd=3)
        self.ent.bind('<Return>', self.dna_gen)
        self.var = tk.IntVar()
        sca = tk.Scale(fra1, orient='horizontal', length=300, from_=0, to=100, tickinterval=10, resolution=1,
                       variable=self.var)
        self.ent.grid(row=1, column=0)
        sca.grid(row=1, column=1)
        lab1 = tk.Label(fra1, text='Длина последовательности ДНК:')
        lab2 = tk.Label(fra1, text='AT/GC отношение:')
        lab1.grid(row=0, column=0)
        lab2.grid(row=0, column=1)
        fra2 = tk.Frame(self)
        fra2.grid(row=1, column=0)
        self.tx = tk.Text(fra2, width=80, height=5)
        scr = tk.Scrollbar(fra2, command=self.tx.yview)
        self.tx.configure(yscrollcommand=scr.set)
        self.tx.pack(side=tk.LEFT)
        scr.pack(side=tk.RIGHT, fill=tk.Y)

    def menu(self):
        m = tk.Menu(self)  # создается объект Меню на главном окне
        self.config(menu=m)  # окно конфигурируется с указанием меню для него
        fm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
        # пункту располагается на основном меню (m)
        m.add_cascade(label='Файл', menu=fm)
        # формируется список команд пункта меню
        fm.add_command(label='Сохранить', command=self.save_txt)
        fm.add_command(label='Выход', command=self.close_win)
        m.add_command(label='Запуск', command=self.dna_gen)
        m.add_command(label='Справка', command=self.about)

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.destroy()

    @staticmethod
    def about():
        showinfo('Информация', 'Генерирование случайной последовательности ДНК')

    def dna_gen(self, event=''):
        print(event)
        at_ratio = self.var.get() / 100
        try:
            dna_len = int(self.ent.get())
        except ValueError:
            showerror('Ошибка', 'Некорректная длина цепи!')
            return
        dna_seq = []
        for n in range(dna_len):
            if n < int(at_ratio * dna_len):
                dna_seq.append(random.choice(('A', 'T')))
            else:
                dna_seq.append(random.choice(('G', 'C')))
        random.shuffle(dna_seq)
        txt_dna = ''.join(dna_seq)
        self.tx.delete(1.0, tk.END)
        self.tx.insert(tk.END, txt_dna)

    def save_txt(self):
        opt = {'parent': self, 'filetypes': [('TXT', '.txt'), ], 'initialfile': 'dna.txt', 'title': 'Сохранить как txt'}
        sa = asksaveasfilename(**opt)
        if sa:
            letter = self.tx.get(1.0, tk.END)
            with open(sa, 'w') as f:
                f.write(letter)


def win():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    win()
