#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Tue Oct 18 14:38:07 2016.

@author: lashkov

"""

import os.path
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

matplotlib.use('TkAgg')


class Graph:
    def __init__(self, root):
        self.fra = root
        self.legend = True
        self.grid = False
        self.xvg_file = None
        self.fig = None
        self.nparrays = []
        self.files = []

    def xvg_open(self):
        opt = {'filetypes': [
            ('Файлы XVG', ('.xvg', '.XVG')), ('Все файлы', '.*')]}
        xvg_file = askopenfilename(**opt)
        try:
            fname = open(xvg_file, 'r')
            n = 0
            while True:
                subtitle = str(open(xvg_file, 'r').readlines()[n])
                if (subtitle[0] == '@') or (subtitle[0] == '#'):
                    n += 1
                else:
                    nparray = np.loadtxt(fname, skiprows=n)
                    fname.close()
                    break
            self.nparrays.append(nparray)
            self.xvg_file = xvg_file
            self.files.append(xvg_file)
            showinfo('Информация', 'Столбцов данных: {0:d}\nCтрок данных: {1:d}\nНомер графика: {2:d}'.format(
                nparray.shape[1], nparray.shape[0], len(self.nparrays)))
        except FileNotFoundError:
            pass
        except UnicodeDecodeError:
            showerror('Ошибка!', 'Неверный формат файла!')
            fname.close()
        except ValueError:
            showerror('Ошибка!', 'Неверный формат файла!')
            fname.close()
        try:
            self.print_graph()
        except AttributeError:
            pass

    def name_label(self):
        str_label = str(open(self.xvg_file).readlines()[13])
        open(self.xvg_file).close()
        i = str_label.index('"')
        j = str_label.rindex('"')
        label = str_label[i + 1:j]
        return label

    def name_x(self):
        str_label = str(open(self.xvg_file).readlines()[14])
        open(self.xvg_file).close()
        i = str_label.index('"')
        j = str_label.rindex('"')
        name_x = str_label[i + 1:j]
        return name_x

    def name_y(self):
        str_label = str(open(self.xvg_file).readlines()[15])
        open(self.xvg_file).close()
        i = str_label.index('"')
        j = str_label.rindex('"')
        name_y = str_label[i + 1:j]
        return name_y

    def legend_set(self):
        self.legend = bool(askyesno('Техническая легенда', 'Отобразить?'))
        try:
            self.print_graph()
        except AttributeError:
            pass

    def grid_set(self):
        self.grid = bool(askyesno('Cетка', 'Отобразить?'))
        try:
            self.print_graph()
        except AttributeError:
            pass

    def print_graph(self):
        if self.xvg_file is None:
            return
        try:
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
        except AttributeError:
            pass
        self.fig = Figure()
        ax = self.fig.add_subplot(111)
        try:
            ax.set_title(self.name_label())
        except AttributeError:
            return
        ax.set_ylabel(self.name_y())
        ax.set_xlabel(self.name_x())
        ax.grid(self.grid)
        i = 0
        for nparray in self.nparrays:
            x = nparray[:, 0]
            y = nparray[:, 1]
            ax.plot(x, y, label=os.path.basename(self.files[i]))
            i += 1
        if self.legend:
            ax.legend(loc='best', frameon=False)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fra)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.fra)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(fill=tk.BOTH, side=tk.TOP, expand=1)

    def sbros(self):
        try:
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
        except AttributeError:
            return
        self.legend = True
        self.grid = False
        self.nparrays = []
        self.files = []

    def save_graph(self):
        sa = asksaveasfilename()
        if sa:
            try:
                self.fig.savefig(sa, dpi=600)
            except FileNotFoundError:
                pass
            except AttributeError:
                showerror('Ошибка!', 'График недоступен!')


def about():
    showinfo('Информация',
             'Отображение графика по данным xvg-файлов')


def win():
    root = tk.Tk()
    root.title('Multigraph')
    root.minsize(width=640, height=515)
    root.maxsize(width=640, height=515)
    fra = tk.Frame(root)
    fra.grid(row=0, column=0)
    graph = Graph(fra)
    m = tk.Menu(root)  # создается объект Меню на главном окне
    root.config(menu=m)  # окно конфигурируется с указанием меню для него
    fm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
    # пункту располагается на основном меню (m)
    m.add_cascade(label='Файл', menu=fm)
    # формируется список команд пункта меню
    fm.add_command(label='Открыть XVG', command=graph.xvg_open)
    fm.add_command(label='Сохранить график', command=graph.save_graph)
    fm.add_command(label='Выход', command=root.destroy)
    rm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
    # пункту располагается на основном меню (m)
    m.add_cascade(label='Настройки', menu=rm)
    rm.add_command(label='Обновить график', command=graph.print_graph)
    rm.add_command(label='Сброс', command=graph.sbros)
    rm.add_command(label='Легенда', command=graph.legend_set)
    rm.add_command(label='Сетка', command=graph.grid_set)
    m.add_command(label='Справка', command=about)
    showinfo('Внимание!!!', ('Спецформат меток grace не поддерживается\n'
                             'для нормального отображения меток удалите символы форматирования в исходном файле!'))
    root.mainloop()


if __name__ == '__main__':
    win()
