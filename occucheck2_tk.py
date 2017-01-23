#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Wed Nov 30 22:14:47 2016.

@author: lashkov

"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring

import Bio.PDB as pdb
from Bio.PDB.mmtf import MMTFParser


def open_pdb():
    global structure
    parser = pdb.PDBParser()
    opt = {'filetypes': [
        ('Файлы PDB', ('.pdb', '.PDB', '.ent')), ('Все файлы', '.*')]}
    pdb_f = askopenfilename(**opt)
    if pdb_f:
        try:
            structure = parser.get_structure('X', pdb_f)
        except FileNotFoundError:
            return
        except (KeyError, ValueError):
            showerror('Ошибка!', 'Некорректный PDB файл: {0:s}!'.format(pdb_f))
            return
        else:
            showinfo('Информация', 'Файл прочитан!')


def open_url():
    global structure
    url = askstring('Загрузить', 'ID PDB:')
    if url is not None:
        try:
            structure = MMTFParser.get_structure_from_url(url)
        except Exception:
            showerror('Ошибка!', ('ID PDB: {0:s} не найден'
                                  ' или ссылается на некорректный файл!').format(url))
        else:
            showinfo('Информация', 'Файл загружен!')


def open_cif():
    global structure
    parser = pdb.MMCIFParser()
    opt = {'filetypes': [
        ('Файлы mmCIF', ('.cif', '.CIF')), ('Все файлы', '.*')]}
    cif_f = askopenfilename(**opt)
    if cif_f:
        try:
            structure = parser.get_structure('X', cif_f)
        except FileNotFoundError:
            return
        except (KeyError, ValueError, AssertionError):
            showerror('Ошибка!', 'Некорректный CIF файл: {0:s}!'.format(cif_f))
            return
        else:
            showinfo('Информация', 'Файл прочитан!')


def save_log():
    sa = asksaveasfilename()
    if sa:
        letter = tx.get(1.0, tk.END)
        try:
            with open(sa, 'w') as f:
                f.write(letter)
        except FileNotFoundError:
            return


def close_win():
    if askyesno('Выход', 'Вы точно хотите выйти?'):
        root.destroy()


def about():
    showinfo('Информация',
             'Проверка корректности суммы заселенностей атомов а.о.')


def check_pdb():
    min_ocu = (var1.get()) / 100
    try:
        atoms = structure.get_atoms()
    except NameError:
        showerror('Ошибка!', 'Структура не загружена!')
        return
    tx.delete(1.0, tk.END)
    for atom in atoms:
        sum_ocu = 0.0
        if atom.is_disordered() == 0:
            sum_ocu += atom.get_occupancy()
        else:
            for X in atom.disordered_get_id_list():
                atom.disordered_select(X)
                sum_ocu += atom.get_occupancy()
        if (sum_ocu > 1.00) or (sum_ocu < min_ocu):
            tx.insert(tk.INSERT, ('Для атома {0:s} а.о. {1:s}:{2:4d} цепи {3:s}'
                                  ' cумма заселенностей равна {4:.2f}\n').format(
                atom.get_fullname(), (atom.get_parent()).get_resname(), int(
                    atom.get_full_id()[3][1]), atom.get_full_id()[2], sum_ocu))


def main():
    global root
    global tx
    global var1
    root = tk.Tk()
    root.title('Occucheck 2')
    root.resizable(False, False)
    m = tk.Menu(root)  # создается объект Меню на главном окне
    root.config(menu=m)  # окно конфигурируется с указанием меню для него
    fm = tk.Menu(m)  # создается пункт меню с размещением на основном меню (m)
    # пункту располагается на основном меню (m)
    m.add_cascade(label='Файл', menu=fm)
    # формируется список команд пункта меню
    fm.add_command(label='Открыть PDB', command=open_pdb)
    fm.add_command(label='Открыть CIF', command=open_cif)
    fm.add_command(label='Открыть ID PDB', command=open_url)
    fm.add_command(label='Сохранить LOG', command=save_log)
    fm.add_command(label='Выход', command=close_win)
    m.add_command(label='Запуск...', command=check_pdb)
    m.add_command(label='Справка', command=about)
    fra1 = ttk.Frame(root)
    fra1.pack(fill=tk.X)
    var1 = tk.IntVar()
    sca1 = tk.Scale(fra1, orient='horizontal', length=560, from_=10,
                    to=100, tickinterval=5, resolution=1, variable=var1)
    sca1.grid(row=1, column=0, padx=5)
    lab1 = ttk.Label(fra1, text=' Минимальная сумма заселенности (%): ')
    lab1.grid(row=0, column=0, sticky='W', padx=5)
    tx = tk.Text(root, width=80, height=10)
    scr = ttk.Scrollbar(root, command=tx.yview)
    tx.configure(yscrollcommand=scr.set)
    tx.pack(side=tk.LEFT)
    scr.pack(side=tk.RIGHT, fill=tk.Y)
    root.mainloop()


if __name__ == '__main__':
    main()
