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

try:
    import Bio.PDB as pdb
    from Bio.PDB.mmtf import MMTFParser
except ImportError:
    imp_err = True
    pdb = None
    MMTFParser = None
else:
    imp_err = False


class Gui(tk.Tk):
    """ГУЙ"""

    def __init__(self):
        super().__init__()
        self.title('Occucheck')
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.close_win)
        fra1 = ttk.Frame(self)
        fra1.pack(fill=tk.X)
        self.var1 = tk.IntVar()
        sca1 = tk.Scale(fra1, orient='horizontal', length=560, from_=10,
                        to=100, tickinterval=5, resolution=1, variable=self.var1)
        sca1.grid(row=1, column=0, padx=5)
        lab1 = ttk.Label(fra1, text='Минимальная сумма заселенности (%):')
        lab1.grid(row=0, column=0, sticky='W', padx=5)
        self.tx = tk.Text(self, width=80, height=10)
        scr = ttk.Scrollbar(self, command=self.tx.yview)
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
        fm.add_command(label='Открыть PDB', command=self.open_pdb)
        fm.add_command(label='Открыть CIF', command=self.open_cif)
        fm.add_command(label='Открыть ID PDB', command=self.open_url)
        fm.add_command(label='Сохранить LOG', command=self.save_log)
        fm.add_command(label='Выход', command=self.close_win)
        m.add_command(label='Запуск...', command=self.check_pdb)
        om = tk.Menu(m)
        m.add_cascade(label='Режим', menu=om)
        om.add_command(label='Простой режим', command=self.simple_mod_set)
        om.add_command(label='Режим BioPython', command=self.bio_mod_set)
        m.add_command(label='Справка', command=self.about)

    def close_win(self):
        if askyesno('Выход', 'Вы точно хотите выйти?'):
            self.destroy()

    @staticmethod
    def about():
        showinfo('Информация',
                 'Проверка корректности суммы заселенностей атомов а.о.')


class App(Gui):
    """Класс логики работы программы"""

    def __init__(self):
        super().__init__()
        self.structure = None
        self.lines_pdb = None
        if imp_err:
            self.simple = True
            showerror('Ошибка импорта',
                      'Программа переключилась в простой режим!\nНекоторые функции недоступны!'
                      '\nДля исправления установите biopython и mmtf!')
        else:
            self.simple = False

    def simple_mod_set(self):
        self.simple = True
        self.structure = None

    def bio_mod_set(self):
        if imp_err:
            self.simple = True
            showerror('Ошибка импорта',
                      'Режим BioPython недоступен!\nДля исправления установите biopython и mmtf!')
        else:
            self.simple = False
            self.lines_pdb = None

    def open_pdb(self):
        opt = {'filetypes': [
            ('Файлы PDB', ('.pdb', '.PDB', '.ent')), ('Все файлы', '.*')]}
        pdb_f = askopenfilename(**opt)
        if pdb_f:
            try:
                if self.simple:
                    with open(pdb_f) as f:
                        self.lines_pdb = f.readlines()
                else:
                    parser = pdb.PDBParser()
                    self.structure = parser.get_structure('X', pdb_f)
            except FileNotFoundError:
                return
            except UnicodeDecodeError:
                showerror('Ошибка', 'Некорректный PDB файл!')
                return
            except (KeyError, ValueError):
                showerror('Ошибка!', 'Некорректный PDB файл: {0:s}!'.format(pdb_f))
                return
            else:
                showinfo('Информация', 'Файл прочитан!')

    def open_url(self):
        if self.simple:
            showerror('Ошибка!', 'Функция недоступна в простом режиме')
            return
        url = askstring('Загрузить', 'ID PDB:')
        if url is not None:
            try:
                self.structure = MMTFParser.get_structure_from_url(url)
            except Exception:
                showerror('Ошибка!', ('ID PDB: {0:s} не найден'
                                      ' или ссылается на некорректный файл!').format(url))
            else:
                showinfo('Информация', 'Файл загружен!')

    def open_cif(self):
        if self.simple:
            showerror('Ошибка!', 'Функция недоступна в простом режиме')
            return
        parser = pdb.MMCIFParser()
        opt = {'filetypes': [
            ('Файлы mmCIF', ('.cif', '.CIF')), ('Все файлы', '.*')]}
        cif_f = askopenfilename(**opt)
        if cif_f:
            try:
                self.structure = parser.get_structure('X', cif_f)
            except FileNotFoundError:
                return
            except (KeyError, ValueError, AssertionError):
                showerror('Ошибка!', 'Некорректный CIF файл: {0:s}!'.format(cif_f))
                return
            else:
                showinfo('Информация', 'Файл прочитан!')

    def save_log(self):
        sa = asksaveasfilename()
        if sa:
            letter = self.tx.get(1.0, tk.END)
            try:
                with open(sa, 'w') as f:
                    f.write(letter)
            except FileNotFoundError:
                return

    def check_pdb(self):
        if self.simple:
            self.check_pdb_simple()
        else:
            self.check_pdb_bio()

    def check_occupancy(self, atom, occupancy, resn, chain_id, res_name):
        min_ocu = (self.var1.get()) / 100
        atom_uniq = [e for i, e in enumerate(atom) if e not in atom[:i]]
        for x in atom_uniq:
            i = [index for index, val in enumerate(atom) if val == x]
            occupancy2 = []
            atom3 = []
            res_name2 = []
            for n in i:
                occupancy2.append(occupancy[n])
                atom3.append(atom[n])
                res_name2.append(res_name[n])
            if (sum(occupancy2) > 1.00) or (sum(occupancy2) < min_ocu):
                self.tx.configure(state='normal')
                self.tx.insert(tk.INSERT, ('Для атома {0:s} а.о. {1:s}:{2:4d} цепи {3:s} cумма'
                                           ' заселенностей равна {4:.2f}\n').format(
                    ''.join(set(atom3)), ' '.join(set(res_name2)), resn, chain_id, sum(occupancy2)))
                self.tx.configure(state='disabled')
                self.update()
            del occupancy2
            del atom3
            del res_name2

    def check_pdb_simple(self):
        if self.lines_pdb is None:
            showerror('Ошибка', 'Не загружен PDB файл!')
            return
        if len(self.lines_pdb) < 10:
            showerror('Ошибка', 'Некорректный PDB файл!')
            return
        self.tx.configure(state='normal')
        self.tx.delete('1.0', tk.END)
        self.tx.configure(state='disabled')
        atom = []
        occupancy = []
        res_name = []
        n = 0
        while n < len(self.lines_pdb) - 1:
            s = self.lines_pdb[n]
            if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  '):
                try:
                    resn_curent = int(s[22:26])
                except ValueError:
                    showerror('Ошибка', 'Некорректный PDB файл!')
                    return
                chain_id_curent = str(s[21])
                while n < len(self.lines_pdb) - 1:
                    if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  '):
                        resn = int(s[22:26])
                        chain_id = str(s[21])
                        if (chain_id != chain_id_curent) or (resn_curent != resn):
                            self.check_occupancy(atom, occupancy,
                                                 resn_curent, chain_id_curent, res_name)
                            n -= 1
                            atom.clear()
                            occupancy.clear()
                            res_name.clear()
                            break
                        atom.append(str(s[12:16]))
                        occupancy.append(float(s[54:60]))
                        res_name.append(str(s[17:20]))
                    n += 1
                    s = self.lines_pdb[n]
            n += 1

    def check_pdb_bio(self):
        min_ocu = (self.var1.get()) / 100
        try:
            atoms = self.structure.get_atoms()
        except AttributeError:
            showerror('Ошибка!', 'Структура не загружена!')
            return
        self.tx.configure(state='normal')
        self.tx.delete(1.0, tk.END)
        self.tx.configure(state='disabled')
        for atom in atoms:
            sum_ocu = 0.0
            if atom.is_disordered() == 0:
                sum_ocu += atom.get_occupancy()
            else:
                for X in atom.disordered_get_id_list():
                    atom.disordered_select(X)
                    sum_ocu += atom.get_occupancy()
            if (sum_ocu > 1.00) or (sum_ocu < min_ocu):
                self.tx.configure(state='normal')
                self.tx.insert(tk.INSERT, ('Для атома {0:s} а.о. {1:s}:{2:4d} цепи {3:s}'
                                           ' cумма заселенностей равна {4:.2f}\n').format(
                    atom.get_fullname(), (atom.get_parent()).get_resname(), int(
                        atom.get_full_id()[3][1]), atom.get_full_id()[2], sum_ocu))
                self.tx.configure(state='disabled')


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
