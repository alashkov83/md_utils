#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Fri Dec  9 13:07:18 2016.

@author: lashkov

"""

import sys
import os
import os.path
import numpy as np
import matplotlib.pyplot as plt


def xvg_extract(s_xvg):
    for line in s_xvg:
        if ('@' in line) or ('#' in line):
            continue
        else:
            return float(line.split()[1])
if len(sys.argv) == 3:
    try:
        com1 = int(sys.argv[1])
        com2 = int(sys.argv[2])
    except:
        print('Использование: udistgen.py номер_первой_групппы номер_второй_группы')
        sys.exit()
else:
    print('Использование: udistgen.py номер_первой_групппы номер_второй_группы')
    sys.exit()
list_file = os.listdir(path='.')
list_dir = list(filter(lambda x: 'conf' in x, list_file))
number_list = sorted(list(
    (map(lambda x: int(''.join([i if i.isdigit() else '' for i in x])), list_dir))))
print(number_list)
for i in number_list:
    print('Обрабатываю конфигурацию номер {0:d}'.format(i))
    os.system(
        "gmx distance -s ../md.tpr -f conf{0:d}.gro -oall dist{0:d}.xvg -select 'com of group {1:d} plus com of group {2:d}' &>/dev/null".format(i, com1, com2))
if os.path.isfile('summary_distances.dat'):
    os.rename('summary_distances.dat', 'summary_distances_old.dat')
dist_file = open('summary_distances.dat', 'a')
for i in number_list:
    print('Собираю данные для конфигурации номер {0:d}'.format(i))
    with open('dist{0:d}.xvg'.format(i), 'r') as xvg_file:
        s_xvg = xvg_file.readlines()
        dist_d = xvg_extract(s_xvg)
        dist_file.write('{0:d}\t{1:.3f}\n'.format(i, dist_d))
dist_file.close()
nparray = np.loadtxt('summary_distances.dat')
fig = plt.figure()
plt.title('Distancs vs. frame No.')
plt.ylabel('D (nm)')
plt.xlabel('Frame (No.)')
plt.grid(True)
ax = fig.add_subplot(111)
x = nparray[:, 0]
y = nparray[:, 1]
ax.plot(x, y)
plt.savefig('summary_distances.png')
print('Очищаю каталог...')
for i in number_list:
    os.remove('./dist{0:d}.xvg'.format(i))