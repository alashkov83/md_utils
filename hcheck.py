#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Wed Nov  1 17:31:15 2017.

@author: lashkov

"""

import sys


def rast(vector1, vector2):
    return (((vector1[0] - vector2[0]) ** 2) + ((vector1[1] -
                                                 vector2[1]) ** 2) + ((vector1[2] - vector2[2]) ** 2)) ** 0.5


def check_res(atom, vector, element, occupancy, resn_curent, chain_id_curent, res_name):
    dist_dict = {
        ' C': (0.82, 1.12),
        ' N': (0.80, 1.06),
        ' O': (0.80, 0.99),
        ' P': (1.3, 1.45),
        ' S': (1.15, 1.36)}
    for ih, ah in enumerate(atom):
        if element[ih] == ' H':
            rast_e = []
            atom_noh = []
            elements = []
            occu = []
            for inoh, anoh in enumerate(atom):
                if element[inoh] != ' H':
                    rast_e.append(rast(vector[ih], vector[inoh]))
                    atom_noh.append(anoh)
                    elements.append(element[inoh])
                    occu.append(occupancy[inoh])
            if not rast_e:
                break
            r = min(rast_e)
            at = atom_noh[rast_e.index(r)]
            el = elements[rast_e.index(r)]
            oc = occupancy[rast_e.index(r)]
            min_dist = dist_dict.get(el, (0.8, 1.5))[0]
            max_dist = dist_dict.get(el, (0.8, 1.5))[1]
            if r > max_dist:
                print(
                    """Похоже, что водород {0:s} остатка {1:s}:{2:d} цепи {3:s} не связан с тяжёлыми атомами! 
Минимальное расстояние c {4:s} = {5:6.2f} \u212b!""".format(
                        atom[ih], res_name[ih], resn_curent, chain_id_curent, at, r))
            elif r < min_dist and not (occupancy[ih] < 1.0 and oc < 1.0):
                print(
                    'Похоже, что водород {0:s} остатка {1:s}:{2:d} цепи {3:s} конфликтует с {4:s}, r = {5:6.2f} \u212b!'.format(
                        atom[ih], res_name[ih], resn_curent, chain_id_curent, at, r))


if len(sys.argv) != 2:
    print('Использование: hcheck.py file.pdb')
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
res_name = []
vector = []
element = []
occupancy = []
n = 0
while n < len(lines_pdb) - 1:
    s = lines_pdb[n]
    if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  '):
        resn_curent = int(s[22:26])
        chain_id_curent = s[21]
        while n < len(lines_pdb) - 1:
            if (s[0:6] == 'HETATM') or (s[0:6] == 'ATOM  '):
                resn = int(s[22:26])
                chain_id = s[21]
                if (chain_id != chain_id_curent) or (resn_curent != resn):
                    check_res(atom, vector, element, occupancy,
                              resn_curent, chain_id_curent, res_name)
                    n -= 1
                    atom.clear()
                    vector.clear()
                    res_name.clear()
                    element.clear()
                    occupancy.clear()
                    break
                atom.append(s[12:16])
                element.append(s[76:78])
                vector.append(
                    (float(s[30:38]), float(s[38:46]), float(s[46:54])))
                res_name.append(s[17:20])
                occupancy.append(float(s[54:60]))
            n += 1
            s = lines_pdb[n]
    n += 1
