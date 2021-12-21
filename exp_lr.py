#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created by lashkov on 07.10.2019"""

import argparse
import sys
import numpy as np
import bigfloat
from scipy.constants import R

R = R * 0.001  # Gas constant in kJ/mol/K


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f1', '--file1', type=str,
                        help='First xvg-file')
    parser.add_argument('-f2', '--file2', type=str,
                        help='Second xvg-file')
    parser.add_argument('-t', '--temp', type=float,
                        default=298.15, help='Temperature (К)')
    parser.add_argument('-b', '--begin', type=int,
                        default=0, help='Begin count')
    return parser


def xvg_open(xvg_file: str) -> np.ndarray:
    if not xvg_file:
        print("File name is not defined!")
        sys.exit(-1)
    try:
        with open(xvg_file) as fname:
            n = 0
            for line in fname:
                if (line[0] == '@') or (line[0] == '#'):
                    n += 1
        nparray = np.loadtxt(xvg_file, skiprows=n)
        return nparray
    except UnicodeDecodeError as e:
        print('Error! {:s}'.format(str(e)))
        sys.exit(-1)
    except ValueError as e:
        print('Error! {:s}'.format(str(e)))
        sys.exit(-1)
    except FileNotFoundError:
        print('Error! File {:s} is not found!'.format(xvg_file))
        sys.exit(-1)


def exp_avr(pot1: np.ndarray, pot2: np.ndarray, T: float) -> float:
    if len(pot2) != len(pot1):
        print("Количество отсчётов потенциала не совпадает!")
        sys.exit(-1)
    deltapot = -(pot2-pot1)/(R*T)
    exp_np = np.array([bigfloat.exp(x) for x in deltapot])
    exp_avg = np.sum(exp_np)/len(exp_np)
    log_avg = float(bigfloat.log(exp_avg))
    return -1*R*T*log_avg


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    temp = namespace.temp
    begin = namespace.begin
    if temp <= 0:
        print("Temperature must be > 0!")
        sys.exit(-1)
    pot1 = xvg_open(namespace.file1)[begin:, 1]
    pot2 = xvg_open(namespace.file2)[begin:, 1]
    exp_lr = exp_avr(pot1, pot2, temp)
    print("deltaG = {:}".format(exp_lr))

