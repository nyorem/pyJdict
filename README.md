how to install the dictionary:

first you need to download the dictionary file here:

http://ftp.monash.edu.au/pub/nihongo/edict.gz
be sure to have it in utf-8. if you can't you can download the database directly and skip the next three steps
https://www.dropbox.com/s/wm8xp5xvo5si463/jdict.sqlite

1. extract the file
2. run csvgen.py to convert the edict file into a csv.
3. then run sqlitegen.py to create the database.

you can now use dict.py

how to use dict.py:

$python dict.py word

the dictionary will first search japanese word (kanji + kana), then reading (only kana), then romaji and finaly english

for example all these search are valid :

$python dict.py 探す
$python dict.py さがす
$python dict.py sagasu
$python dict.py "to search"

note that results are sorted by alphabetical order.
if there are too many results you can run "$python dict.py word | more" instead to produce a more readable ouput

