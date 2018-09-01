#!venv/bin/python
# -*- coding: utf-8 -*-

import sqlite3
import sys
import romkan

con = sqlite3.connect('jdict.sqlite')
con.text_factory = str
cur = con.cursor()

if len(sys.argv) != 2:
    print "usage: python dict.py word"
    sys.exit("error: bad arguments")

word = sys.argv[1]

jpq = 'SELECT * FROM edict WHERE word LIKE "' + word + '"'
rq = 'SELECT * FROM edict WHERE kana LIKE "' + romkan.to_hiragana(unicode(word, 'utf-8')) + '"'
enq = 'SELECT * FROM edict WHERE english LIKE "%' + word + '%"'

cur.execute(jpq)
rows = cur.fetchall()
for row in rows:
    print row[0] + '【' + row[1] + '】' + row[2] +'\n'

cur.execute(rq)
rows = cur.fetchall()
for row in rows:
    print row[0] + '【' + row[1] + '】' + row[2] +'\n'

cur.execute(enq)
rows = cur.fetchall()
for row in rows:
    print row[0] + '【' + row[1] + '】' + row[2] +'\n'