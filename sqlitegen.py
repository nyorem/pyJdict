#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sqlite3

con = sqlite3.Connection('jdict.sqlite')
con.text_factory = str
cur = con.cursor()
cur.execute('CREATE TABLE "edict" ("word" text, "kana" text, "english" text);')

f = open('csvdict')
csv_reader = csv.reader(f, delimiter=';', quotechar='`')
cur.executemany(u'INSERT INTO edict VALUES (?, ?, ?)', csv_reader)
cur.close()
con.commit()
con.close()
f.close()