#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Tue Oct 18 14:38:07 2016.

@author: lashkov

"""

import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

import matplotlib
from matplotlib.figure import Figure
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

import numpy as np


class Graph:
    def __init__(self, root):
        self.root = root
        self.root.protocol('WM_DELETE_WINDOW', self.close_win)
        self.fra = tk.Frame(root, width=660, height=515)
        self.fra.grid(row=0, column=0, padx=5, pady=5)
        self.legend = False
        self.grid = False
        self.xvg_file = None
        self.fig = None
        self.dpi = 600

    def xvg_open(self):
        opt = {'filetypes': [
            ('Файлы XVG', ('.xvg', '.XVG')), ('Все файлы', '.*')]}
        xvg_file = askopenfilename(**opt)
        if not xvg_file:
            return
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
            self.nparray = nparray
            self.xvg_file = xvg_file
            showinfo('Информация', 'Столбцов данных: {0:d}\nCтрок данных: {1:d}'.format(
                nparray.shape[1], nparray.shape[0]))
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
        x = self.nparray[:, 0]
        if self.nparray.shape[1] == 2:
            y = self.nparray[:, 1]
            ax.plot(x, y, color='black', label=self.name_y())
        else:
            for i in range(1, self.nparray.shape[1]):
                y = self.nparray[:, i]
                ax.plot(x, y, label=self.name_y() + str(i))
        if self.legend:
            ax.legend(loc='best', frameon=False)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fra)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.toolbar = NavigationToolbar2TkAgg(self.canvas, self.fra)
        self.toolbar.update()
        self.canvas._tkcanvas.pack(fill=tk.BOTH, side=tk.TOP, expand=1)

    def save_graph(self):
        if self.fig is None:
            showerror('Ошибка!', 'График недоступен!')
            return
        sa = asksaveasfilename()
        if sa:
            try:
                self.fig.savefig(sa, dpi=self.dpi)
            except FileNotFoundError:
                pass
            except AttributeError:
                showerror('Ошибка!', 'График недоступен!')
            except ValueError:
                showerror('Неподдерживаемый формат файла рисунка!', 'Поддреживаемые форматы: eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff.')

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.root.destroy()


def about():
    showinfo('Информация',
             'Отображение графика по данным одиночного xvg-файла')


def main():
    root = tk.Tk()
    root.title('Histo')
    root.resizable(False, False)
    graph = Graph(root)
    m = tk.Menu(root)  # создается объект Меню на главном окне
    root.config(menu=m)  # окно конфигурируется с указанием меню для него
    fm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
    # пункту располагается на основном меню (m)
    m.add_cascade(label='Файл', menu=fm)
    # формируется список команд пункта меню
    fm.add_command(label='Открыть XVG', command=graph.xvg_open)
    fm.add_command(label='Сохранить график', command=graph.save_graph)
    fm.add_command(label='Выход', command=graph.close_win)
    rm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
    # пункту располагается на основном меню (m)
    m.add_cascade(label='Настройки', menu=rm)
    rm.add_command(label='Обновить график', command=graph.print_graph)
    rm.add_command(label='Легенда', command=graph.legend_set)
    rm.add_command(label='Сетка', command=graph.grid_set)
    m.add_command(label='Справка', command=about)
    showinfo('Внимание!!!', ('Спецформат меток grace не поддерживается\n'
                             'для нормального отображения меток удалите символы форматирования в исходном файле!'))
    root.mainloop()


if __name__ == '__main__':
    main()
