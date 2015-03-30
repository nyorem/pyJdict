<h1>how to install the dictionary:</h1>

this project uses python 2.7.x. you will also need python-romkan library.

first you need to download the dictionary file here:

http://ftp.monash.edu.au/pub/nihongo/edict.gz
be sure to have it in utf-8. if you can't you can download the database directly and skip the next three steps
https://www.dropbox.com/s/wm8xp5xvo5si463/jdict.sqlite

1. extract the file
2. run csvgen.py to convert the edict file into a csv.
3. then run sqlitegen.py to create the database.

you can now use dict.py

<h1>how to use dict.py:</h1>

$python dict.py word

the dictionary will first search japanese word (kanji + kana), then reading (only kana), then romaji and finaly english

for example all of these are valid :
```
$python dict.py 探す
$python dict.py さがす
$python dict.py sagasu
$python dict.py "to search"
```

note that results are sorted by alphabetical order.
if there are too many results you can run ```$python dict.py word | more``` instead to produce a more readable ouput

<h1>TODO list</h1>

- [ ] example sentences
- [ ] smart result search
- [ ] GUI mode

<h1>License</h1>

<a href="https://raw.github.com/soimort/python-romkan/master/LICENSE">python-romkan license</a>
