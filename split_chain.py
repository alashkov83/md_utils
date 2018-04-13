#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Wed Nov  1 17:31:15 2017.

@author: lashkov

"""

import os
import sys


def chainsave(chain, chain_id_curent, fn):
    chain_id_curent = chain_id_curent.strip().lower()
    nfn = str(os.path.basename(fn).split('.')[0]) + '_' + chain_id_curent + '.pdb'
    try:
        with open(nfn, 'a') as f:
            f.writelines(chain)
    except PermissionError:
        print('Ошибка! Недостаточно прав для записи файла!')
        sys.exit()


if len(sys.argv) != 2:
    print('Использование: split_chain.py file.pdb')
    sys.exit()
else:
    fn = sys.argv[1]
try:
    fname = open(fn)
    lines_pdb = fname.readlines()
except FileNotFoundError:
    print('Файл {:s} не найден!'.format(fn))
    sys.exit()
except ValueError:
    print('Неверный формат файла {:s}!'.format(fn))
    sys.exit()

chain = []
chain_id_curent = None
for s in lines_pdb:
    if (s[0:6] == 'HETATM' or s[0:6] == 'ATOM  ' or s[0:6] == 'ANISOU') and (chain_id_curent is None or chain_id_curent == s[21]):

        chain_id_curent = s[21]
        chain.append(s)
    elif (s[0:6] == 'HETATM' or s[0:6] == 'ATOM  ' or s[0:6] == 'ANISOU'):
        chainsave(chain, chain_id_curent, fn)
        chain.clear()
        chain_id_curent = s[21]
        chain.append(s)