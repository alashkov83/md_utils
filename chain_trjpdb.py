#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Thu Oct 27 20:17:17 2016.

@author: lashkov

"""
old_filename = str(input('Введите имя входного файла: '))
i = int(input('Введите номер первого а.о.: '))
j = int(input('Введите номер последнего а.о.: '))
chain_name = str(input('Введите название цепи: '))
new_filename = str(input('Введите имя выходного файла: '))
oldfile = open(old_filename, 'r')
newfile = open(new_filename, 'a')
for line in oldfile:
    s = str(line)
    if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  '):
        if int(s[22:26]) in range(i, j + 1):
            s = s[0:21] + chain_name + s[22:]
    newfile.write(s)
oldfile.close()
newfile.close()
