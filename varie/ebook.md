
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

    pandoc libro.epub -o latex/global.tex

mettere a posto tutte le immagini


     mogrify -format png tmp/*.jpg
     mkdir tmp/img
     mv tmp/*.png tmp/img

    ~/public_html/pyhub/varie/from_epub_to_latex/correct_latex.py global.tex



in tmp si troveranno tutte le immagini


    
    


    pandoc input.epub -o outpout.tex

#Creazione da Latex

convertire con tex2ebook.py es: 

    latex/main.tex -o main.epub

poi con _Sigil_ rimettere a posto l'indice
    
