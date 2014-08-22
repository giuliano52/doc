---
title: Python
author: Giuliano Dedda 
date: 28/07/2014
---

#Files

##Leggere e scrivere su files
```python
output = open('pippo.txt','w')	apertura di un file in scrittura
input = open('dati','r')	apertura di un file in lettura
s = input.read()	lettura dell'intero contenuto del file
s = input.read(N)	lettura di N bytes
s = input.readline()	lettura di una riga (per files di testo)
s = input.readlines()	restuisce l'intero file come lista di righe (per files di testo)
output.wre(s)	scrivo un intero file
output.wrelines(L)	scrive la lista L in righe nel file
output.close(L)	chiusura del file
```
è meglio usare  readlines rispetto a  readline perché è più veloce.

##Parsing di un file
```python
import sys

f = open(sys.argv[1], 'r')

for line in f.readlines():
	print line
```


##File in una directory
```python
dirname = './'
for dirpath, dirnames,files in os.walk(dirname):
	for filename in files:
		file_full_path = os.path.join(dirpath, filename)
		print(file_full_path)
```

##Movimentazione file

```python
(root,ext) = os.path.splitext(filename)	# divide il nomefile in basename e estensione

shutil.copyfile(src,dst) # copia file
shutil.move(src,dst) # sposta file
```

#Script che mostra gli argomenti e esegue un comando
```python
import sys
import subprocess

for x in sys.argv:
    print x

output = subprocess.check_output(['ls', '-l'])
print(output)

```

#Array, liste, dizionari
Una Lista (cioè un array) può essere definita così:
```python
xx = array([2, 4, -11])
yy = zeros(3, Int)        # Create empty array ready to receive result
for i in range(0, 3):
     yy[i] = xx[i] * 2
print yy
[  4   8 -22]

li = ["a", "b", "mpilgrim", "z", "example"]


Le tuple sono come le liste ma non hanno metodi e sono pià veloci
    t = ("a", "b", "mpilgrim", "z", "example")


Un dizionario invece ha una relazione uno a uno con le chiavi:
    d = {"server":"mpilgrim", "database":"master"} 
    print d['server']

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}

>>> params.keys()   
['server', 'uid', 'database', 'pwd']

>>> params.values() 
['mpilgrim', 'sa', 'master', 'secret']

>>> params.items()  
[('server', 'mpilgrim'), ('uid', 'sa'), ('database', 'master'), ('pwd', 'secret')]
```


#Stringhe
Per concatenare stringhe sui usa il '+'
per convertire da binarie a stringe usare:

    linea_str = str( linea_binaria, encoding='utf8' )

Comando                                             	| Effetto
--------------------------------------------------------|--------------------------------------------------------
print "Users connected: %d" % (userCount, )				| Inserire un intero in una stringa
stringa = format(int(data_video[1]), '02d')				| per formattare gli interi con gli zero davanti (leading zero)
testo = testo.replace('S', '6')							| sostituzione di caratteri all'interno di una stringa


#Espressioni regolari
```python
import sys
import re

NomeFile = sys.argv[1]

f = open(NomeFile, 'r')
for line in f.readlines():
	if re.search('espessione', line,re.I):
		print line
```

#Import
Per importare da librerie fatte da me
```python
sys.path.append("~/bin/")
import dvd_extract_vob_chapter
```
#Sqlite
```python
conn = sqlite3.connect('photos.db')
c = conn.cursor()
LineSQL = "SELECT base_uri,filename FROM photos, photo_tags WHERE photos.id=photo_id AND tag_id=1;"

c.execute(LineSQL)
for row in c:
	print row

```