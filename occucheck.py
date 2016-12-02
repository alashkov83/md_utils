#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:14:47 2016

@author: lashkov
"""

import sys
def check_occupancy(atom, occupancy, resn, chain_id, res_name):
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
        if (sum(occupancy2) > 1.00) or (sum(occupancy2) < 0.20):
            print("Для атома {0:s} а.о. {1:s}:{2:d} цепи {3:s} cумма заселенностей равна {4:.2f}".format(''.join(set(atom3)), ' '.join(set(res_name2)), resn, chain_id, sum(occupancy2)))
        del occupancy2
        del atom3
        del res_name2
    return

if len(sys.argv) != 2:
    print('Использование: occucheck.py file.pdb')
    sys.exit()
try:
    fname = open(sys.argv[1], 'r')
    lines_pdb = fname.readlines()
except FileNotFoundError:
    print('Файл не найден!')
    sys.exit()
except ValueError:
    print('Неверный формат файла!')
    fname.close()
    sys.exit()
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
sys.exit()
