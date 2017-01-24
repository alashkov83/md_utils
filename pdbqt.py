#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:46:41 2017

@author: lashkov
"""

import sys
import Bio.PDB as pdb

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
        print("Информация", "Файл прочитан!")
        return structure
    
io = pdb.PDBIO()
io.set_structure(open_pdb(sys.argv[1]))
io.save(sys.argv[2])