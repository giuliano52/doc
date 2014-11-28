#da PDF a HTML
##pdftohtml
se si usa il comndao _pdftohtml_ inserire nell'header del file il campo:

    <meta charset="UTF-8">

per correggere le lettere accentate. 
Inoltre si possono sostituire i _&#160;_ con spazio vuoti

    sed -i "s/&#160;/ /g" nomefile.html

##pdf2htmlEX
ripropone il pdf sul browser con la stessa impaginazione (in pratica rimane la divisione a pagine), 
ma il risultato è praticamente identico all'originale. Fa molto uso di javascript e css

#Creazione Latex da PDF

- per prima cosa convertire in epub con calibre il libro
- creare una directory di lavoro _orig_ in cui inserire sia il pdf originale che l'epub creato da calibre
- eseguire i seguenti comandi:


creare le directory base 

    mkdir latex
    mkdir latex/Images
    mkdir tmp

scompattare il dile epub per estrarre le immagini

    unzip orig/libro.epub -d tmp/

copiare il tempalte latex di base 

    cp ~/public_html/dochub/varie/latex-examples/epub/main.tex latex/   

creare il latex con pandoc

    pandoc orig/libro.epub -o latex/global.tex

mettere a posto tutte le immagini trasformandole tutte in png e poi unendole se sono separate verticalmente


     mogrify -format png tmp/*.jpg
     mkdir tmp/img
     mv tmp/*.png tmp/img
     rm tmp/*.jpg

     ~/public_html/pyhub/varie/from_epub_to_latex/join-images.py tmp/img/

correggo all'interno del latex gli includegraphics

    cd latex
    ~/public_html/pyhub/varie/from_epub_to_latex/correct_latex.py global.tex

Ora si può iniziare a correggere manualemnte:

- Eliminare i doppi \n 
- eliminare le immagini doppie

##versioning con git

si può creare un file .gitignore in questo modo:
```
*.aux
*.out
*.log
*.toc
latex/*.pdf
bk/*

```

#Creazione da Latex

convertire con tex2ebook.py es: 

    latex/main.tex -o main.epub

poi con _Sigil_ rimettere a posto l'indice
    
