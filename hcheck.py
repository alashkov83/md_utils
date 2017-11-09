#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Wed Nov  1 17:31:15 2017.

@author: lashkov

"""

import sys


def rast(vector1, vector2):
    """
    Евклидово расстояние
    :param vector1:
    :param vector2:
    :return:
    """
    return (((vector1[0] - vector2[0]) ** 2) + ((vector1[1] -
                                                 vector2[1]) ** 2) + ((vector1[2] - vector2[2]) ** 2)) ** 0.5


def check_link(ocu_h, ocu_noh, alt_h, alt_noh):
    """
    Формальная проверка связности атомов.
    :param ocu_h:
    :param ocu_noh:
    :param alt_h:
    :param alt_noh:
    :return:
    """
    if ocu_h == 1.0 and ocu_noh == 1.0:
        return True
    elif (ocu_h < 1.0 and ocu_noh < 1.0) and (alt_h == alt_noh):
        return True
    elif (ocu_h < 1.0 and ocu_noh == 1.0) and alt_noh == ' ':
        return True
    else:
        return False


def check_res(atom, vector, element, occupancy, alter, resn_curent, chain_id_curent, res_name):
    """
    Проверка остатка на "проблемные" атомы водорода.
    :param atom:
    :param vector:
    :param element:
    :param occupancy:
    :param alter:
    :param resn_curent:
    :param chain_id_curent:
    :param res_name:
    """
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
            alt = alter[rast_e.index(r)]
            min_dist = dist_dict.get(el, (0.8, 1.5))[0]
            max_dist = dist_dict.get(el, (0.8, 1.5))[1]
            if r > max_dist and check_link(occupancy[ih], oc, alter[ih], alt):
                print("""Похоже, что водород {1:s}:{0:s} остатка {2:s}{8:s}{3:d} цепи {4:s} не связан с тяжёлыми атомами! 
Минимальное расстояние c {5:s}{9:s}{6:s} = {7:6.2f} \u212b!""".format(
                    atom[ih], alter[ih], res_name[ih], resn_curent, chain_id_curent, alt, at, r, '' if alter[ih] ==' ' else ':', '' if alt ==' ' else ':'))
            elif r < min_dist and check_link(occupancy[ih], oc, alter[ih], alt):
                print("""Похоже, что водород {1:s}:{0:s} остатка {2:s}{8:s}{3:d} цепи {4:s} конфликтует с {5:s}{9:s}{6:s}!
r = {7:6.2f} \u212b!""".format(atom[ih], alter[ih], res_name[ih], resn_curent, chain_id_curent, alt, at, r, '' if alter[ih] ==' ' else ':', '' if alt ==' ' else ':'))


if len(sys.argv) != 2:
    print('Использование: hcheck.py file.pdb')
    sys.exit()
try:
    fname = open(sys.argv[1])
    lines_pdb = fname.readlines()
except FileNotFoundError:
    print('Файл {:s} не найден!'.format(sys.argv[1]))
    sys.exit()
except ValueError:
    print('Неверный формат файла {:s}!'.format(sys.argv[1]))
    sys.exit()
atom = []
res_name = []
vector = []
element = []
occupancy = []
alter = []
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
                    check_res(atom, vector, element, occupancy, alter,
                              resn_curent, chain_id_curent, res_name)
                    n -= 1
                    atom.clear()
                    vector.clear()
                    res_name.clear()
                    element.clear()
                    occupancy.clear()
                    alter.clear()
                    break
                atom.append(s[12:16].strip())
                element.append(s[76:78])
                vector.append(
                    (float(s[30:38]), float(s[38:46]), float(s[46:54])))
                res_name.append(s[17:20].strip())
                occupancy.append(float(s[54:60]))
                alter.append(s[16])
            n += 1
            s = lines_pdb[n]
    n += 1
