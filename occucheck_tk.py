#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:14:47 2016

@author: lashkov
"""

import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno


def open_pdb():
	global lines_pdb
	pdb = askopenfilename()
	try:
		with open(pdb,"r") as f:
			lines_pdb = f.readlines()
	except FileNotFoundError:
		showinfo("Информация","Выберите файл формата PDB")
		return


def save_log():
	sa = asksaveasfilename()
	letter = tx.get(1.0,tk.END)
	try:
		with open(sa,"w") as f:
			f.write(letter)
	except FileNotFoundError:
		showinfo("Информация","Выберите файл для записи лога")
		return

def close_win():
	if askyesno("Выход", "Вы точно хотите выйти?"):
		root.destroy()

def about():
     showinfo("Информация","Проверка корректности суммы заселенностей атомов а.о.")

def check_occupancy(atom, occupancy, resn, chain_id, res_name):
    min_ocu = (var1.get())/100
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
            tx.insert(tk.INSERT, "Для атома {0:s} а.о. {1:s}:{2:d} цепи {3:s} cумма заселенностей равна {4:.2f}\n".format(''.join(set(atom3)), ' '.join(set(res_name2)), resn, chain_id, sum(occupancy2)))
        del occupancy2
        del atom3
        del res_name2

def check_pdb():
	try:
		if len(lines_pdb) < 80:
			showinfo("Ошибка","Некорректный PDB файл!")
			return
	except:
		showinfo("Ошибка","Некорректный PDB файл!")
		return
	tx.delete(1.0,tk.END)
	atom = []
	occupancy = []
	res_name = []
	n = 0
	while n < len(lines_pdb)-1:
		s = lines_pdb[n]
		if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  '):
			resn_curent = int(s[22:26])
			chain_id_curent = str(s[21])
			while n < len(lines_pdb)-1:
				if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  '):
					resn = int(s[22:26])
					chain_id = str(s[21])
					if (chain_id != chain_id_curent) or (resn_curent != resn):
						check_occupancy(atom, occupancy, resn_curent, chain_id_curent, res_name)
						n = n-1
						atom.clear()
						occupancy.clear()
						res_name.clear()
						break
					atom.append(str(s[12:16]))
					occupancy.append(float(s[54:60]))
					res_name.append(str(s[17:20]))
				n = n+1
				s = lines_pdb[n]
		n = n+1
		
def main():
	global root
	global tx
	global var1
	root = tk.Tk()
	m = tk.Menu(root) #создается объект Меню на главном окне
	root.config(menu=m) #окно конфигурируется с указанием меню для него
	fm = tk.Menu(m) #создается пункт меню с размещением на основном меню (m)
	m.add_cascade(label="Файл",menu=fm) #пункту располагается на основном меню (m)
	fm.add_command(label="Открыть PDB",command=open_pdb) #формируется список команд пункта меню
	fm.add_command(label="Сохранить LOG", command=save_log)
	fm.add_command(label="Выход", command=close_win)
	m.add_command(label="Запуск...", command=check_pdb)
	m.add_command(label="Справка", command=about)
	fra1 = tk.Frame(root)
	fra1.pack(fill=tk.X)
	var1 = tk.IntVar()
	sca1 = tk.Scale(fra1, orient="horizontal", length=400, from_=10, to=100, tickinterval=10, resolution=1, variable=var1)
	sca1.grid(row=0,column=1)
	lab1 = tk.Label(fra1, text="Минимальная сумма заселенности (%):")
	lab1.grid(row=0,column=0)
	tx = tk.Text(root,width=80,height=10)
	scr = tk.Scrollbar(root,command=tx.yview)
	tx.configure(yscrollcommand=scr.set)
	tx.pack(side=tk.LEFT)
	scr.pack(side=tk.RIGHT, fill=tk.Y)
	root.mainloop()
if __name__ == "__main__":
    main()
	
