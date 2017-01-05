#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Thu Oct 27 20:17:17 2016.

@author: lashkov

"""

import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno

def open_pdb():
	global oldfile
	pdb = askopenfilename()
	try:
		oldfile = open(pdb,"r")
	except FileNotFoundError:
		showinfo("Информация","Выберите файл формата PDB")
		return


def save_log():
	sa = asksaveasfilename()
	global newfile
	try:
		newfile = open(sa,"w")
	except FileNotFoundError:
		showinfo("Информация","Выберите файл формата PDB")
		return

def close_win():
	if askyesno("Выход", "Вы точно хотите выйти?"):
		root.destroy()

def about():
     showinfo("Информация","Проверка корректности суммы заселенностей атомов а.о.")

def rename_pdb():
	try:
		if len(oldfile.readlines()) < 80:
			showinfo("Ошибка","Некорректный PDB файл!")
			return
	except:
		showinfo("Ошибка","Некорректный PDB файл!")
		return
	i = int(v1.get())
	j = int(v2.get())
	ink = int(v3.get())
	chain_name_old = str(v4.get())
	chain_name = str(v5.get())
	for line in oldfile:
		s = str(line)
		if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  '):
			if (int(s[22:26]) in range(i, j + 1)) and (s[21] == chain_name_old):
				s = s[0:21] + chain_name + '{0:>4d}'.format(int(s[22:26])+ink) + s[26:]
		newfile.write(s)
	oldfile.close()
	newfile.close()

def main():
	global root
	global v1
	global v2	
	global v3	
	global v4
	global v5
	root = tk.Tk()
	m = tk.Menu(root) #создается объект Меню на главном окне
	root.config(menu=m) #окно конфигурируется с указанием меню для него
	fm = tk.Menu(m) #создается пункт меню с размещением на основном меню (m)
	m.add_cascade(label="Файл",menu=fm) #пункту располагается на основном меню (m)
	fm.add_command(label="Открыть PDB",command=open_pdb) #формируется список команд пункта меню
	fm.add_command(label="Сохранить PDB", command=save_log)
	fm.add_command(label="Выход", command=close_win)
	m.add_command(label="Запуск...", command=rename_pdb)
	m.add_command(label="Справка", command=about)
	v1 = tk.StringVar()
	ent1 = tk.Entry (root, textvariable = v1)
	ent1.grid(row=0,column=1)
	lab1 = tk.Label(root, text="Номер первого а.о.: ")
	lab1.grid(row=0,column=0)
	v2 = tk.StringVar()
	ent2 = tk.Entry (root, textvariable = v2)
	ent2.grid(row=1,column=1)
	lab2 = tk.Label(root, text="Номер последнего а.о.: ")
	lab2.grid(row=1,column=0)
	v3 = tk.StringVar()
	ent3 = tk.Entry (root, textvariable = v3)
	ent3.grid(row=2,column=1)
	lab3 = tk.Label(root, text="Инкремент: ")
	lab3.grid(row=2,column=0)
	v4 = tk.StringVar()
	ent4 = tk.Entry (root, textvariable = v4)
	ent4.grid(row=3,column=1)
	lab4 = tk.Label(root, text="Старое наименование цепи (Пробел при отсутствия наименования): ")
	lab4.grid(row=3,column=0)
	v5 = tk.StringVar()
	ent5 = tk.Entry (root, textvariable = v5)
	ent5.grid(row=4,column=1)
	lab5 = tk.Label(root, text="Новое наименование цепи (Пробел при отсутствия наименования): ")
	lab5.grid(row=4,column=0)
	root.mainloop()
if __name__ == "__main__":
    main()
