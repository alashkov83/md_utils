#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Mon Nov 28 23:52:06 2016.

@author: lashkov

"""

import random
import sys

if (len(sys.argv) < 2) or (len(sys.argv) > 3):
    print('Использование: dna_srg длина_сиквенса АТ:ГЦ_соотношение')
    sys.exit()
AT_RATIO = 0.5
if len(sys.argv) == 3:
    try:
        AT_RATIO = float(sys.argv[2])
    except ValueError:
        pass
dna_seq = []
for n in range(int(sys.argv[1])):
    if n < int(AT_RATIO * int(sys.argv[1])):
        dna_seq.append(random.choice(('A', 'T')))
    else:
        dna_seq.append(random.choice(('G', 'C')))
random.shuffle(dna_seq)
print(''.join(dna_seq))
