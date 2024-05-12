#!/usr/bin/env python3

import re
file= "plaintext.xml"
with open("crawford" + file, "w") as g:
    line_number = 0
    rune_number = 0
    for line in open(file):
        if line.startswith('<div type="'):
            rune_number += 1 
            line_number = 0
            line= line
        elif line.startswith('<l>'):
            line_number += 1
            assert line_number < 1000
            line = line.replace('<l>', f'<l n="{rune_number:02d}.{line_number:03d}">')
        else:
            line = line
        print(line, file=g, end='')