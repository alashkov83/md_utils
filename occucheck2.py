#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:14:47 2016

@author: lashkov
"""

import sys
import argparse
import Bio.PDB as pdb
from Bio.PDB.mmtf import MMTFParser

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pdb_f', type=str,
                        help='Имя PDB файла')
    parser.add_argument('-c', '--cif_f', type=str,
                        help='Имя CIF файла')
    parser.add_argument('-id', '--id_pdb', type=str,
                        help='ID PDB')
    parser.add_argument('-ocu', '--min_ocu', type=float,
                        default=0.1, help='Минимальное значение суммы заселенности')
    parser.add_argument('-o', '--logout', type=str, default='ocu.log',
                        help='Имя LOG файла')
    return parser

def open_pdb(pdb_f):
    parser = pdb.PDBParser()
    try:
        structure = parser.get_structure('X', pdb_f)
    except FileNotFoundError:
        print("Ошибка! PDB файл: {0:s} не найден!".format(pdb_f))
        sys.exit()
    except (KeyError, ValueError):
        print("Ошибка! Некорректный PDB файл: {0:s}!".format(pdb_f))
        sys.exit()
    else:
        print("Информация","Файл прочитан!")
        return structure

def open_url(url):
    try:
        structure = MMTFParser.get_structure_from_url(url)
    except Exception:
        print("Ошибка!", "ID PDB: {0:s} не найден или ссылается на некорректный файл!".format(url))
        sys.exit()
    else:
        print("Файл загружен!")
        return structure

def open_cif(cif_f):
    parser = pdb.MMCIFParser()
    try:
        structure = parser.get_structure('X', cif_f)
    except FileNotFoundError:
        print("Ошибка! CIF файл: {0:s} не найден!".format(pdb_f))
        sys.exit()
    except (KeyError, ValueError,  AssertionError):
        print("Ошибка! Некорректный CIF файл: {0:s}!".format(pdb_f))
        sys.exit()
    else:
        print("Файл прочитан!")
        return structure

def save_log(log, namespace):
    with open(namespace.logout,"w") as f:
        f.write("\n".join(log))


def check_pdb(structure, namespace):
    min_ocu = namespace.min_ocu
    try:
        atoms = structure.get_atoms()
    except Exception:
        print("Ошибка!", "Структура не загружена!")
        sys.exit()
    log = []
    for atom in atoms:
        sum_ocu = 0.0
        if atom.is_disordered() ==0:
            sum_ocu += atom.get_occupancy()
        else:
            for X in atom.disordered_get_id_list():
                atom.disordered_select(X)
                sum_ocu += atom.get_occupancy()
        if (sum_ocu > 1.00) or (sum_ocu < min_ocu):
            log.append("Для атома {0:s} а.о. {1:s}:{2:4d} цепи {3:s} cумма заселенностей равна {4:.2f}".format(atom.get_fullname(), (atom.get_parent()).get_resname(), int(atom.get_full_id()[3][1]), atom.get_full_id()[2], sum_ocu))
    return log

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.pdb_f is not None:
        structure = open_pdb(namespace.pdb_f)
    elif namespace.cif_f is not None:
        structure = open_cif(namespace.cif_f)
    elif namespace.id_pdb is not None:
        structure = open_url(namespace.id_pdb)
    else:
        print("Ошибка!", "Структура не загружена! -h - справка")
        sys.exit()
    log = check_pdb(structure, namespace)
    if len(log) > 0:
        print("\n".join(log))
        save_log(log, namespace)
    else:
        print("Ошибок не найдено!")

