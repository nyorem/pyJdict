#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
import sys

rexp = '^(.*)(\[.*\])? (\/.*\/)'
rexp2 = '^(.*) \[(.*)\]'

f = open("edict", "r")
fcsv = open("csvdict", "w")
# fcsv0 = open("csvdict0", "w")
# fcsv1 = open("csvdict1", "w")
# fcsv2 = open("csvdict2", "w")
# fcsv3 = open("csvdict3", "w")

fcsv.write('`kanji`;`reading`;`meaning`\n')
# fcsv0.write('`id`;`kanji`;`reading`;`meaning`\n')
# fcsv1.write('`id`;`kanji`;`reading`;`meaning`\n')
# fcsv2.write('`id`;`kanji`;`reading`;`meaning`\n')
# fcsv3.write('`id`;`kanji`;`reading`;`meaning`\n')

i = 0

for line in f:
    m = re.match(rexp, line)
    japanese = m.group(1)
    meaning = m.group(3)

    if re.match(rexp2, japanese):
        m2 = re.match(rexp2, japanese)
        kanji = m2.group(1)
        reading = m2.group(2)
    else:
        kanji = japanese
        reading = ""

    # if i < 3000:
    #     fcsv0.write('`' + str(i) +'`;`' + kanji + '`;`' + reading + '`;`' + meaning + '`\n')
    # elif i >= 3000 and i < 76000:
    #     fcsv1.write('`' + str(i) +'`;`' + kanji + '`;`' + reading + '`;`' + meaning + '`\n')
    # elif i >= 76000 and i < 152000:
    #     fcsv2.write('`' + str(i) +'`;`' + kanji + '`;`' + reading + '`;`' + meaning + '`\n')
    # elif i >= 152000:
    #     fcsv3.write('`' + str(i) +'`;`' + kanji + '`;`' + reading + '`;`' + meaning + '`\n')

    fcsv.write('`' + kanji + '`;`' + reading + '`;`' + meaning + '`\n')

    i += 1

f.close()
fcsv.close()
# fcsv0.close()
# fcsv1.close()
# fcsv2.close()
# fcsv3.close()