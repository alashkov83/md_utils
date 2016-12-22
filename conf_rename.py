#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:29:22 2016

@author: lashkov
"""
import os
import sys

ink = int(sys.argv[1])
list_file = os.listdir(path='.')
list_dir = list(filter(lambda x: ('conf' in x) and ('.gro' in x), list_file))
number_list = sorted(list(
    (map(lambda x: int(''.join([i if i.isdigit() else '' for i in x])), list_dir))))
for i in number_list:
    os.rename('conf'+str(i)+'.gro', 'conf'+str(i+ink)+'.gro')
