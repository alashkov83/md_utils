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


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Multigraph')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.close_win)
        self.fra = tk.Frame(self, width=660, height=515)
        self.fra.grid(row=0, column=0, padx=5, pady=5)
        fra2 = tk.Frame(self)
        fra2.grid(row=1, column=0, pady=10)
        self.tx = tk.Text(fra2, width=80, height=8)
        scr = tk.Scrollbar(fra2, command=self.tx.yview)
        self.tx.configure(yscrollcommand=scr.set, state='disabled')
        self.tx.pack(side=tk.LEFT)
        scr.pack(side=tk.RIGHT, fill=tk.Y)
        self.menu()

    def menu(self):
        m = tk.Menu(self)  # создается объект Меню на главном окне
        self.config(menu=m)  # окно конфигурируется с указанием меню для него
        fm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
        # пункту располагается на основном меню (m)
        m.add_cascade(label='Файл', menu=fm)
        # формируется список команд пункта меню
        fm.add_command(label='Открыть XVG', command=self.xvg_open)
        fm.add_command(label='Сохранить статистику', command=self.save_stat)
        fm.add_command(label='Сохранить график', command=self.save_graph)
        fm.add_command(label='Выход', command=self.close_win)
        rm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
        # пункту располагается на основном меню (m)
        m.add_cascade(label='Настройки', menu=rm)
        rm.add_command(label='Сброс', command=self.sbros)
        rm.add_command(label='Легенда', command=self.legend_set)
        rm.add_command(label='Сетка', command=self.grid_set)
        m.add_command(label='Справка', command=self.about)

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.destroy()

    @staticmethod
    def about():
        showinfo('Информация', 'Отображение графиков по данным xvg-файлов')


class Graph(Gui):
    def __init__(self):
        super().__init__()
        self.legend = False
        self.grid = False
        self.fig = None
        self.headers = []
        self.nparrays = []
        self.files = []

    def xvg_stat(self, x, y, lab):
        """Большая ложь т.е. статистика"""
        y_min = min(y)
        y_max = max(y)
        y_mean = y.mean()
        x_min = x[np.argmin(y)]
        x_max = x[np.argmax(y)]
        self.tx.configure(state='normal')
        self.tx.insert(tk.END, 'Статистика для {0:s}:'.format(
                lab) + '\nМинимальное значение y = {0:.3f} при x = {1:.2f}'.format(
                y_min, x_min) + '\nМаксимальное значение y = {0:.3f} при x = {1:.2f}'.format(
                y_max, x_max) + '\nСреднее значение y = {0:.3f}'.format(
                y_mean) + '\nСтандартное отклонение y = {0:.3f}'.format(
                np.std(y)) + '\nКвартили: y (25%) = {0:.3f}, y (50%) = {1:.3f}, y (75%) = {2:.3f}\n\n'.format(
                np.percentile(y, 25), np.percentile(y, 50), np.percentile(y, 75)))
        self.tx.configure(state='disabled')

    def save_stat(self):
        opt = {'filetypes': [('Текстовые файлы', ('.txt', '.TXT')), ('Все файлы', '.*')]}
        sa = asksaveasfilename(**opt)
        if sa:
            letter = self.tx.get(1.0, tk.END)
            try:
                with open(sa, 'w') as f:
                    f.write(letter)
            except FileNotFoundError:
                pass

    def cmd_open(self):
        for n in range(len(sys.argv) - 1):
            xvg_file = sys.argv[n + 1]
            if not xvg_file:
                return
            try:
                fname = open(xvg_file, 'r')
                n = 0
                header = []
                for line in fname:
                    if (line[0] == '@') or (line[0] == '#'):
                        header.append(line)
                        n += 1
                fname.close()
                with open(xvg_file, 'r') as fname:
                    nparray = np.loadtxt(fname, skiprows=n)
                if not header:
                    header = "Header not found"
                self.nparrays.append(nparray)
                self.files.append(xvg_file)
                self.headers.append(header)
                print(header)
                print('Информация:\nСтолбцов данных: {0:d}\nCтрок данных: {1:d}\nНомер графика: {2:d}'.format(
                    nparray.shape[1], nparray.shape[0], len(self.nparrays)))
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
            header = []
            for line in fname:
                if (line[0] == '@') or (line[0] == '#'):
                    header.append(line)
                    n += 1
            fname.close()
            with open(xvg_file, 'r') as fname:
                nparray = np.loadtxt(fname, skiprows=n)
            if not header:
                header = "Header not found"
            self.nparrays.append(nparray)
            self.files.append(xvg_file)
            self.headers.append(header)
            print(header)
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
        label, name_x, name_y = ' ', ' ', ' '
        for line in self.headers[0]:
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
        if self.headers is None:
            return
        try:
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
        except AttributeError:
            pass
        self.tx.configure(state='normal')
        self.tx.delete('1.0', tk.END)
        self.tx.configure(state='disabled')
        self.fig = Figure()
        ax = self.fig.add_subplot(111)
        ax.set_title(self.labels()[0])
        ax.set_xlabel(self.labels()[1])
        ax.set_ylabel(self.labels()[2])
        ax.grid(self.grid)
        i = 0
        for nparray in self.nparrays:
            legends = []
            name_fail = " "
            for line in self.headers[i]:
                if line.find('legend "') != -1:
                    k = line.index('"')
                    l = line.rindex('"')
                    legend = line[k + 1:l]
                    legends.append(legend)
                if line.find('yaxis  label') != -1:
                    o = line.index('"')
                    p = line.rindex('"')
                    name_fail = line[o + 1:p]
            num_f_leg = nparray.shape[1] - len(legends) - 1
            num_empty_leg = 1
            while nparray.shape[1] - len(legends) - 1:
                if num_f_leg == 1:
                    legends.append(name_fail)
                else:
                    legends.append(name_fail + '_' + str(num_empty_leg))
                    num_empty_leg += 1
            x = nparray[:, 0]
            for j in range(0, nparray.shape[1] - 1):
                y = nparray[:, j + 1]
                if len(self.nparrays) == 1:
                    lab = legends[j]
                else:
                    lab = os.path.splitext(os.path.basename(self.files[i]))[0] + ':' + legends[j]
                ax.plot(x, y, label=lab)
                self.xvg_stat(x, y, lab)
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
            pass
        self.legend = True
        self.grid = False
        self.nparrays = []
        self.files = []
        self.fig = None
        self.headers = []
        self.tx.configure(state='normal')
        self.tx.delete('1.0', tk.END)
        self.tx.configure(state='disabled')

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


def win():
    graph = Graph()
    if len(sys.argv) > 1:
        graph.cmd_open()
    showinfo('Внимание!!!', ('Спецформат меток grace не поддерживается\n'
                             'для нормального отображения меток удалите символы форматирования в исходном файле!'))
    graph.mainloop()


if __name__ == '__main__':
    win()
