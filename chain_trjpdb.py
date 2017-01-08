#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Thu Oct 27 20:17:17 2016.

@author: lashkov

"""
OLD_FILENAME = str(input('Введите имя входного файла: '))
i = int(input('Введите номер первого а.о.: '))
j = int(input('Введите номер последнего а.о.: '))
CHAIN_NAME = str(input('Введите название цепи: '))
NEW_FILENAME = str(input('Введите имя выходного файла: '))
OLDFILE = open(OLD_FILENAME, 'r')
NEWFILE = open(NEW_FILENAME, 'a')
for line in OLDFILE:
    s = str(line)
    if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  ') or (s[0:6] == 'ANISOU'):
        if int(s[22:26]) in range(i, j + 1):
            s = s[0:21] + CHAIN_NAME + s[22:]
    NEWFILE.write(s)
OLDFILE.close()
NEWFILE.close()
