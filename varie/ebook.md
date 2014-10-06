
#Creazione Latex da PDF

- per prima cosa convertire in epub con calibre il libro
- creare una directory di lavoro _orig_ in cui inserire sia il pdf originale che l'epub creato da calibre
- eseguire i seguenti comandi 

    mkdir latex
    mkdir tmp
    unzip orig/libro.epub -d tmp/

in tmp si troveranno tutte le immagini


    
    


    pandoc input.epub -o outpout.tex

#Creazione da Latex

convertire con tex2ebook.py es: 

    latex/main.tex -o main.epub

poi con _Sigil_ rimettere a posto l'indice
    
