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


Per le immagini

    \usepackage{graphicx}					% per includere le grafiche esterne 

poi usare

    \includegraphics{nomeimmagine}			%include l'immagine (provato jpg funziona senza problemi)

per fare una funzione custum 

    \newcommand\abs[1]{\left|#1\right|}

##Nel document

Per includere un file esterno 

    \include{nomefile} 		 % Include il file esterno 


#Esempi Base

##Book
```
\documentclass[11pt]{book}            
\begin{document}
Prova
\end{document}
```
