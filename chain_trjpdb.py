#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Thu Oct 27 20:17:17 2016.

@author: lashkov

"""
old_filename = str(input('Введите имя входного файла: '))
chain_name_old = str(input('Введите старое название цепи: '))
i = int(input('Введите номер первого а.о.: '))
j = int(input('Введите номер последнего а.о.: '))
ink = int(input('Введите инкремент перенумерации: '))
chain_name = str(input('Введите новое название цепи: '))
new_filename = str(input('Введите имя выходного файла: '))
oldfile = open(old_filename)
newfile = open(new_filename, 'a')
for line in oldfile:
    s = str(line)
    if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  ') or (s[0:6] == 'ANISOU'):
        if (int(s[22:26]) in range(i, j + 1)) and (s[21] == chain_name_old):
            s = s[0:21] + chain_name + '{0:>4d}'.format(int(s[22:26])+ink) + s[26:]
    newfile.write(s)
oldfile.close()
newfile.close()
