#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Mon Nov 28 23:52:06 2016.

@author: lashkov

"""

import random
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showinfo


def dna_gen():
	AT_RATIO = var.get()/100
	try:
		dna_len = int(ent.get())
	except ValueError:
		showinfo("Error", "Lenght DNA field int value requerred")
		return
	dna_seq = []
	for n in range(dna_len):
		if n < int(AT_RATIO * dna_len):
			dna_seq.append(random.choice(('A', 'T')))
		else:
			dna_seq.append(random.choice(('G', 'C')))
	random.shuffle(dna_seq)
	txt_dna = ''.join(dna_seq)
	tx.delete(1.0,tk.END)
	tx.insert(tk.END,txt_dna)

def dna_gen_ev(event):
	dna_gen()
	
def save_txt():
	sa = asksaveasfilename()
	letter = tx.get(1.0,tk.END)
	with open(sa,"w") as f:
		f.write(letter)

def close_win():
     root.destroy()

def about():
     win = tk.Toplevel(root)
     lab = tk.Label(win,text="Генерация случайной последовательности ДНК")
     lab.pack()
     
def main():
	global ent
	global root
	global var
	global tx
	root = tk.Tk()
	dna_len = tk.StringVar()
	m = tk.Menu(root) #создается объект Меню на главном окне
	root.config(menu=m) #окно конфигурируется с указанием меню для него
	fm = tk.Menu(m) #создается пункт меню с размещением на основном меню (m)
	m.add_cascade(label="File",menu=fm) #пункту располагается на основном меню (m)
	fm.add_command(label="Save...",command=save_txt) #формируется список команд пункта меню
	fm.add_command(label="Exit", command=close_win)
	m.add_command(label="Run", command=dna_gen)
	m.add_command(label="About", command=about)
	fra1 = tk.Frame(root)
	fra1.grid(row=0,column=1)
	ent = tk.Entry(fra1,width=10,bd=3)
	ent.bind("<Return>", dna_gen_ev)
	var = tk.IntVar()
	sca = tk.Scale(fra1, orient="horizontal", length=300, from_=0, to=100, tickinterval=10, resolution=1, variable=var)
	ent.grid(row=1,column=1)
	sca.grid(row=1,column=2)
	lab1 = tk.Label(fra1, text="Lenght DNA")
	lab2 = tk.Label(fra1, text="AT/GC ratio")
	lab1.grid(row=0,column=1)
	lab2.grid(row=0,column=2)
	fra2 = tk.Frame(root)
	fra2.grid(row=1,column=1)
	tx = tk.Text(fra2,width=50,height=10)
	scr = tk.Scrollbar(fra2,command=tx.yview)
	tx.configure(yscrollcommand=scr.set)
	tx.pack(side=tk.LEFT)
	scr.pack(side=tk.RIGHT, fill=tk.Y)
	root.mainloop()
if __name__ == "__main__":
    main()
    

	