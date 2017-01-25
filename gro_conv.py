#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:46:41 2017

@author: lashkov
"""

import sys

old_file = sys.argv[1]
new_file = sys.argv[2]
with open(old_file, 'r') as of:
    lines = of.readlines()
nf = open(new_file, 'a')
i=1
for line in lines:
    if i > 2 and i < len(lines):
        s = line[0:10] + '{0:>5s}'.format(line[10:13].strip()) + line[15:]
    else:
        s = line[:]
    nf.write(s)
    i+=1
nf.close()

    
    
 
