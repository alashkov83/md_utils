#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Tue Dec 20 21:49:54 2016.

@author: lashkov

"""

import argparse
import os
import os.path
import sys
from shutil import copyfile

import matplotlib.pyplot as plt
import numpy as np
import progressbar


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g1', '--group1', type=int,
                        help='Номер первой группы')
    parser.add_argument('-g2', '--group2', type=int,
                        help='Номер второй группы')
    parser.add_argument('-d', '--dist', type=float,
                        default=0.1, help='Расстояние между окнами (нм)')
    parser.add_argument('-b', '--begin', type=int,
                        default=0, help='Номер первого фрейма')
    parser.add_argument('-e', '--end', type=int, default=0,
                        help='Номер последнего фрейма')
    return parser


def xvg_extract(s_xvg):
    for line in s_xvg:
        if ('@' in line) or ('#' in line):
            continue
        else:
            return float(line.split()[1])


def udistgen(namespace):
    if (namespace.group1 is None) or (namespace.group2 is None):
        print('Не заданы pull-группы для справки -h')
        sys.exit()
    com1 = namespace.group1
    com2 = namespace.group2
    if not os.path.isfile('md.tpr'):
        print('Файл md.tpr не найден в каталоге ' + os.getcwd())
        sys.exit()
    if os.path.isdir('FRAMES_ALL'):
        os.rename('FRAMES_ALL', 'FRAMES_ALL_OLD')
    os.mkdir('FRAMES_ALL')
    if os.path.isfile('md.xtc'):
        os.system('echo "0" | gmx trjconv -f md.xtc -s md.tpr -o ./FRAMES_ALL/conf.gro -sep')
    elif os.path.isfile('md.trr'):
        os.system('echo "0" | gmx trjconv -f md.trr -s md.tpr -o ./FRAMES_ALL/conf.gro -sep')
    else:
        print('Файл траектории не найден в каталоге ' + os.getcwd())
        sys.exit()
    list_file = os.listdir(path='./FRAMES_ALL')
    list_dir = list(filter(lambda x: ('conf' in x) and ('.gro' in x), list_file))
    number_list = sorted(list(
        (map(lambda x: int(''.join([i if i.isdigit() else '' for i in x])), list_dir))))
    print('Обрабатываю фреймы...')
    bar1 = progressbar.ProgressBar(maxval=max(number_list)).start()
    for i in number_list:
        bar1.update(i)
        os.system(
            "gmx distance -s md.tpr -f ./FRAMES_ALL/conf{0:d}.gro -oall ./FRAMES_ALL/dist{0:d}.xvg -select 'com of group {1:d} plus com of group {2:d}' > /dev/null 2>&1".format(
                i, com1, com2))
    bar1.finish()
    dist_file = open('summary_distances.dat', 'a')
    print('Собираю данные..')
    bar2 = progressbar.ProgressBar(maxval=max(number_list)).start()
    for i in number_list:
        bar2.update(i)
        with open('./FRAMES_ALL/dist{0:d}.xvg'.format(i), 'r') as xvg_file:
            s_xvg = xvg_file.readlines()
            dist_d = xvg_extract(s_xvg)
            dist_file.write('{0:d}\t{1:.3f}\n'.format(i, dist_d))
    dist_file.close()
    bar2.finish()
    for i in number_list:
        os.remove('./FRAMES_ALL/dist{0:d}.xvg'.format(i))
    return


def frame_prefilter(nparray, namespace):
    f_frame = namespace.begin
    if namespace.end == 0:
        l_frame = len(nparray[:, 0])
    else:
        l_frame = 1 + int(namespace.end)
    nparray2 = nparray[(l_frame >= nparray[:, 0]) & (nparray[:, 0] >= f_frame)]
    return nparray2


def frame_filter(nparray, d):
    f_array = nparray[:, 0]
    d_array = nparray[:, 1]
    ff_frame = []
    i = 0
    for n in range(int(f_array[0]), int(f_array[-1])):
        nd = d_array[0] + i * d
        i += 1
        df_array = list(map(lambda x: abs(x - nd), d_array))
        ff_frame.append(f_array[df_array.index(min(df_array))])
    l = list(map(lambda x: int(x), ff_frame))
    l2 = sorted(list(dict(zip(l, l)).values()))
    l2.pop()
    return l2


def umbr_frame(nparray, namespace):
    d = namespace.dist
    ff_frame = frame_filter(frame_prefilter(nparray, namespace), d)
    print('Отобранные фреймы: ' + ' '.join(map(lambda x: str(x), ff_frame)))
    newdir = './FRAMES'
    try:
        os.makedirs(newdir, exist_ok=True)
    except OSError:
        print('Невозможно создать каталог ' + newdir)
        sys.exit()
    for frame in ff_frame:
        filename = './FRAMES_ALL/conf' + str(frame) + '.gro'
        newfilename = newdir + '/conf' + str(frame) + '.gro'
        try:
            copyfile(filename, newfilename)
        except OSError:
            print('Невозможно скопировать ' + filename)


def picture(nparray):
    fig = plt.figure()
    plt.title('Distance vs. frame No.')
    plt.ylabel('D (nm)')
    plt.xlabel('Frame (No.)')
    plt.grid(True)
    ax = fig.add_subplot(111)
    x = nparray[:, 0]
    y = nparray[:, 1]
    ax.plot(x, y)
    plt.savefig('summary_distances.png')


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    if os.path.isfile('summary_distances.dat'):
        nparray = np.loadtxt('summary_distances.dat')
        picture(nparray)
        umbr_frame(nparray, namespace)
    else:
        udistgen(namespace)
        nparray = np.loadtxt('summary_distances.dat')
        if not os.path.isfile('summary_distances.png'):
            picture(nparray)
        umbr_frame(nparray, namespace)
