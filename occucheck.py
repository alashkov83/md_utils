#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:14:47 2016

@author: lashkov
"""

import sys


def min_ocu():
    if len(sys.argv) == 3:
        try:
            min_ocu = float(sys.argv[2])
        except ValueError:
            print("Введено неверное значение заселённости!\nИспользуется значение по умолчанию равное 0.1")
            min_ocu = 0.1
    else:
        min_ocu = 0.1
    return min_ocu


def check_occupancy(atom, occupancy, resn, chain_id, res_name, ocu):
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
        if (sum(occupancy2) > 1.00) or (sum(occupancy2) < ocu):
            print("Для атома {0:s} а.о. {1:s}:{2:4d} цепи {3:s} cумма заселенностей равна {4:.2f}".format(
                ''.join(set(atom3)), ' '.join(set(res_name2)), resn, chain_id, sum(occupancy2)))
        del occupancy2
        del atom3
        del res_name2
    return


if (len(sys.argv) < 2) or (len(sys.argv) > 3):
    print('Использование: occucheck.py file.pdb ocu')
    sys.exit()
try:
    fname = open(sys.argv[1])
    lines_pdb = fname.readlines()
except FileNotFoundError:
    print('Файл не найден!')
    sys.exit()
except ValueError:
    print('Неверный формат файла!')
    sys.exit()
atom = []
occupancy = []
res_name = []
n = 0
ocu = min_ocu()
while n < len(lines_pdb) - 1:
    s = lines_pdb[n]
    if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  '):
        resn_curent = int(s[22:26])
        chain_id_curent = str(s[21])
        while n < len(lines_pdb) - 1:
            if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  '):
                resn = int(s[22:26])
                chain_id = str(s[21])
                if (chain_id != chain_id_curent) or (resn_curent != resn):
                    check_occupancy(atom, occupancy, resn_curent, chain_id_curent, res_name, ocu)
                    n -= 1
                    atom.clear()
                    occupancy.clear()
                    res_name.clear()
                    break
                atom.append(str(s[12:16]))
                occupancy.append(float(s[54:60]))
                res_name.append(str(s[17:20]))
            n += 1
            s = lines_pdb[n]
    n += 1
