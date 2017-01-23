#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Tue Oct 18 14:38:07 2016.

@author: lashkov

"""

import os.path
import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class Graph:
    def __init__(self, root):
        self.root = root
        self.root.protocol('WM_DELETE_WINDOW', self.close_win)
        self.fra = tk.Frame(root, width=660, height=515)
        self.fra.grid(row=0, column=0, padx=5, pady=5)
        self.legend = False
        self.grid = False
        self.fig = None
        self.lines = None
        self.nparrays = []
        self.files = []

    def cmd_open(self):
        for n in range(len(sys.argv)-1):
            xvg_file = sys.argv[n+1]
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
                self.lines = open(xvg_file, 'r').readlines()
                self.nparrays.append(nparray)
                self.files.append(xvg_file)
            except UnicodeDecodeError:
                continue
            except ValueError:
                continue
            try:
                self.print_graph()
            except AttributeError:
                pass

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
            self.lines = open(xvg_file, 'r').readlines()
            self.nparrays.append(nparray)
            self.files.append(xvg_file)
            showinfo('Информация', 'Столбцов данных: {0:d}\nCтрок данных: {1:d}\nНомер графика: {2:d}'.format(
                nparray.shape[1], nparray.shape[0], len(self.nparrays)))
        except UnicodeDecodeError:
            showerror('Ошибка!', 'Неверный формат файла!')
            return
        except ValueError:
            showerror('Ошибка!', 'Неверный формат файла!')
            return
        try:
            self.print_graph()
        except AttributeError:
            pass

    def labels(self):
        label, name_x, name_y = '', '', ''
        for line in self.lines:
            if line.find('title') != -1:
                i = line.index('"')
                j = line.rindex('"')
                label = line[i + 1:j]
            elif line.find('xaxis  label') != -1:
                i = line.index('"')
                j = line.rindex('"')
                name_x = line[i + 1:j]
            elif line.find('yaxis  label') != -1:
                i = line.index('"')
                j = line.rindex('"')
                name_y = line[i + 1:j]
        return label, name_x, name_y

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
        if self.lines is None:
            return
        try:
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
        except AttributeError:
            pass
        self.fig = Figure()
        ax = self.fig.add_subplot(111)
        ax.set_title(self.labels()[0])
        ax.set_xlabel(self.labels()[1])
        ax.set_ylabel(self.labels()[2])
        ax.grid(self.grid)
        legends = []
        for file in self.files:
            with open(file) as f:
                lines = f.readlines()
            for line in lines:
                if line.find('yaxis  label') != -1:
                    i = line.index('"')
                    j = line.rindex('"')
                    legend = line[i + 1:j]
                    legends.append(legend)
        i = 0
        for nparray in self.nparrays:
            x = nparray[:, 0]
            for j in range(1, nparray.shape[1]):
                y = nparray[:, j]
                if nparray.shape[1] == 2 and len(self.nparrays) == 1:
                    ax.plot(x, y, color='black', label=self.labels()[2])
                elif len(self.nparrays) == 1:
                    ax.plot(x, y, label=self.labels()[2] + '_' + str(j))
                elif nparray.shape[1] == 2:
                    ax.plot(x, y, label=os.path.splitext(os.path.basename(self.files[i]))[0] + ':' + legends[i])
                else:
                    ax.plot(x, y,
                            label=os.path.splitext(os.path.basename(self.files[i]))[0] + ':' + legends[i] + '_' + str(
                                j))
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
        self.fig = None
        self.lines = None

    def save_graph(self):
        if self.fig is None:
            showerror('Ошибка!', 'График недоступен!')
            return
        sa = asksaveasfilename()
        if sa:
            try:
                self.fig.savefig(sa, dpi=600)
            except FileNotFoundError:
                pass
            except AttributeError:
                showerror('Ошибка!', 'График недоступен!')
            except ValueError:
                showerror('Неподдерживаемый формат файла рисунка!',
                          'Поддреживаемые форматы: eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff.')

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.root.destroy()


def about():
    showinfo('Информация',
             'Отображение графиков по данным xvg-файлов')


def win():
    root = tk.Tk()
    root.title('Multigraph')
    root.resizable(False, False)
    graph = Graph(root)
    if len(sys.argv) > 1:
        graph.cmd_open()
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
    rm.add_command(label='Сброс', command=graph.sbros)
    rm.add_command(label='Легенда', command=graph.legend_set)
    rm.add_command(label='Сетка', command=graph.grid_set)
    m.add_command(label='Справка', command=about)
    showinfo('Внимание!!!', ('Спецформат меток grace не поддерживается\n'
                             'для нормального отображения меток удалите символы форматирования в исходном файле!'))
    root.mainloop()


if __name__ == '__main__':
    win()
