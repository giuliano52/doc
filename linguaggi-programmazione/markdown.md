---
title: Markdownrkdown
author: Giuliano Dedda 
date: 10/07/2014
---
    

per mandare a capo terminare con due o più spazi una riga. 

#Tabelle
Intestazione 1                  | Intestazione 2
----------------------------    | ----------------------------
Campo 1							| Valore 1
`lshw` <br> `lshw -html` 		| Codice separato su due righe su github

 
#Metadati
all' inizio inserire :
```
---
title: Test
author: Author Name
header-includes:
    - \usepackage{fancyhdr}
    - \pagestyle{fancy}
    - \fancyhead[CO,CE]{This is fancy}
    - \fancyfoot[CO,CE]{So is this}
    - \fancyfoot[LE,RO]{\thepage}
abstract: This is a pandoc test . . . 
---
```

