#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 23:52:06 2016

@author: lashkov
"""

import sys
import random
if (len(sys.argv) < 2) or (len(sys.argv) > 3):
    print("Использование: dna_srg длина_сиквенса АТ:ГЦ_соотношение")
    sys.exit()
if len(sys.argv) == 2:
    at_ratio=0.5
if len(sys.argv) == 3:
    try:
        at_ratio = float(sys.argv[2])
    except:
        at_ratio = 0.5
dna_seq=[]
for n in range(int(sys.argv[1])):
    if n < int(at_ratio*int(sys.argv[1])):
         dna_seq.append(random.choice(('A', 'T')))
    else:
         dna_seq.append(random.choice(('G', 'C')))
random.shuffle(dna_seq)
print(''.join(dna_seq))
sys.exit()
