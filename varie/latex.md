---
title: Latex
author: Giuliano Dedda 
date: 31/7/2014
---

#Comandi vari

##Negli Header

Per un documento in italiano 

    \usepackage[utf8]{inputenc}			% Consente l'uso caratteri accentati italiani
    \usepackage[utf8x]{inputenc}		% se ci sono problemi con file unicode, meglio usare utf8x
    \usepackage[italian]{babel}			% Adatta LaTeX alle convenzioni tipografiche italiane, e ridefinisce alcuni titoli in italiano, come "Capitolo" al posto di "Chapter"

per il check del documento senza generare (molto più veloce) , poi basta commentare la seconda riga

    \usepackage{syntonly}
    \syntaxonly

Per le immagini

    \usepackage{graphicx}					% per includere le grafiche esterne 

poi usare

    \includegraphics{nomeimmagine}			%include l'immagine (provato jpg funziona senza problemi)

per fare una funzione custum 

    \newcommand\abs[1]{\left|#1\right|}

##Nel document

Per includere un file esterno 

    \include{nomefile} 		 % Include il file esterno 


#Tabelle

per dividere la tabella su più pagine si può usare il pacchetto longtable

per ripetere la prima riga per ogni pagina alla fine della prima riga inserire:

    \endhead
    
#Libretti e fascicoli
```
% genera il libretto 
\usepackage{geometry}
\geometry {centering,nohead }
\geometry{width=108.5mm,height=170mm}

\usepackage[print,1to1]{booklet}
\nofiles
\pagespersignature{36}

\begin{document}
\setpdftargetpages
```

#Esempi Base

##Book
```
\documentclass[11pt]{book}            
\begin{document}
Prova
\end{document}
```
