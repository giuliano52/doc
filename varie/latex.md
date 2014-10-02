---
title: Latex
author: Giuliano Dedda 
date: 31/7/2014
---

per pdflatex il file deve essere in codifica UTF-senza BOM (ASCI-UTF)


#Comandi vari

##Negli Header

Per un documento in italiano -> vedi latex-examples/base.tex


per il check del documento senza generare (molto più veloce) , poi basta commentare la seconda riga

    \usepackage{syntonly}
    \syntaxonly

Per le immagini

    vedi latex-examples/immagini.tex

poi usare

    \includegraphics{nomeimmagine}			%include l'immagine (provato jpg funziona senza problemi)

per fare una funzione custum 

    \newcommand\abs[1]{\left|#1\right|}

##Nel documento

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

#Formattazione testo

se serve formattare in italico una grossa parte di 
testo (anche con paragrafi) usare: 

    \itshape  e \normalfont 

se non voglio che ci sia una separazione di riga devo usare la tilde ~ es:

    fig~\ref{fig:f001}
    
#Stili
per un diverso tipo di capitoli: 

    \usepackage[Sonny]{fncychap}

oppure

    \usepackage[Bjornstrup]{fncychap}
    
