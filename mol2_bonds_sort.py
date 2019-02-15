#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created by lashkov on 15.02.19"""

import argparse
import re
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str,
                        help='Input file name (mol2)')
    parser.add_argument('-o', '--output', type=str, default='output.mol2',
                        help='Input file name (mol2)')
    return parser


def read_in(file_name):
    try:
        with open(file_name) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File {:s} not found!".format(file_name))
        sys.exit(-1)
    except UnicodeDecodeError:
        print("Uncorrected file format!")
        sys.exit(-1)
    top_sections = []
    down_sections = []
    bonds = []
    pattern = re.compile(r'\s+(\d+)\s+(\d+)\s+(\d+)\s+(\w+)\s*')
    section_bond = False
    section_bond_end = False
    for s in lines:
        if s[0:13] != '@<TRIPOS>BOND' and not section_bond and not section_bond_end:
            top_sections.append(s)
        if s[0:13] != '@<TRIPOS>BOND' and not section_bond and section_bond_end:
            down_sections.append(s)
        elif s[0:13] == '@<TRIPOS>BOND' and not section_bond:
            top_sections.append(s)
            section_bond = True
        elif s[0:13] == '@<TRIPOS>BOND' and (section_bond or (not section_bond and section_bond_end)):
            print("Error! Bond section is duplicated!")
        elif section_bond and not section_bond_end and re.match(pattern, s):
            match_object = re.match(pattern, s)
            bond_tuple = (int(match_object.groups()[0]),
                          int(match_object.groups()[1]),
                          int(match_object.groups()[2]),
                          match_object.groups()[3])
            bonds.append(bond_tuple)
        elif section_bond and not section_bond_end and s[0] == '@':
            section_bond_end = True
            section_bond = False
            down_sections.append(s)
    return top_sections, bonds, down_sections


def sort_bonds(bonds):
    bonds_tmp = []
    for i, j, k, s in bonds:
        if j > k:
            bonds_tmp.append((i, k, j, s))
        else:
            bonds_tmp.append((i, j, k, s))
    bonds_tmp.sort(key=lambda t: (t[1], t[2]))
    bonds_tmp = [(i + 1, j, k, s) for i, (_, j, k, s) in enumerate(bonds_tmp)]
    return bonds_tmp


def write_out(file_out, top_sections, bonds, down_sections):
    s = ''.join(top_sections)
    s += ''.join(map(lambda bond: "{:5d}{:5d}{:5d} {:s}\n".format(*bond), bonds))
    s += ''.join(down_sections)
    with open(file_out, 'w') as f:
        f.write(s)


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.input is None:
        print("Input file is not defined!")
        sys.exit(-1)
    top_sections, bonds, down_sections = read_in(namespace.input)
    print(top_sections, bonds, down_sections)
    sorted_bonds = sort_bonds(bonds)
    write_out(namespace.output, top_sections, sorted_bonds, down_sections)


if __name__ == "__main__":
    main()
