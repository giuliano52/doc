---
title: Programmi Vari
author: Giuliano Dedda 
date: 17/07/2014
---

#GIT

inizializzare un repository

    git init
    git add.
    git remote add origin  https://giuliano52:password@github.com/giuliano52/phphub.git
    git push
    
clonare un repository:
	
    git clone https://github.com/giuliano52/phphub.git

commit:

    git add *
    git commit -m "Commenti"
    git push https://github.com/giuliano52/pyhub.git

al posto di git add e git commit si puà usare git commit -a -m "commento"
    
##Remove history from github
Step 1: remove all history

    rm -rf .git

Step 2: reconstruct the Git repo with only the current content

    git init
    git add .
    git commit -m "Initial commit"

Step 3: push to GitHub.

    git remote add origin <github-uri>
    git push -u --force origin master



#Pandoc
Serve per convertire formati di file (es da html a epub, ... )
20140709 per installartlo su ARCH meglio non usare AUR ma impostare il repository: come spiegato qui: http://gnuhacks.com/blog/how-to-install-pandoc-on-arch-linux/

Opzione | Descrizione 			| Esempio
------- | ------- 				| ------- 
-f		| From Format			|  pandoc -f html -t markdown hello.html
-t		| To Format 			| 
-o 		| Output filename		|
-s		| Standalone: produce un file HTML, RTF, ... completo con gli header | 
--toc	| Genera all'inizio una Table of Context (indice) |
-D		| Vede il default template relativi ad un formato | pandoc -D html ; pandoc -D latex

se non si usa utf-8 bisogna convertire con:
iconv -t utf-8 input.txt | pandoc | iconv -f utf-8

##Esempi
pandoc input.md -o output.html

imposta i margini per il pdf 
    
	pandoc  input.md -s -o output.pdf -V geometry:"top=2cm, bottom=2.5cm, left=2cm, right=2cm"

esempio impostando la pagina in a3 e facendo il passaggio con pdflatex
    
	pandoc  input.md -t latex -s  -o uno.tex  -V geometry:"a3paper"
	pdflatex uno.tex

esempio impostando i margini e facendo il passaggio con pdflatex	

    pandoc  input.md -t latex -s  -o uno.tex  -V geometry:"top=1cm, bottom=1.5cm, left=1cm, right=1cm"
    pdflatex uno.tex

per avere le tabelle tutte allineate a sinistra:

    pandoc  input.md -t latex -s  -o uno.tex  -V geometry:"top=1cm, bottom=1.5cm, left=1cm, right=1cm"

	sostituire \begin{longtable}[c]{@{}ll@{}} con \begin{longtable}[l]{@{}ll@{}}
e lanciare 

    pdflatex uno.tex
	
comando per la documentazione

    pandoc  input.md -s  -o output.pdf  -V geometry:"top=1cm, bottom=1.5cm, left=1cm, right=1cm"	

#Systemd

Comando                                               | Effetto
----------------------------                          | ----------------------------
journalctl -b 				 | messagi dal boot
systemctl -t service -a 	 | mostra i servizi al boot

#Webdav

##fstab

in /etc/davfs2/secrets inserire:
    
    https://dav.box.com/dav nome_utente_box_com@email.info password_box_com


per montare un disco remoto con l'utente_a inserire in /etc/fstab

    https://dav.box.com/dav /home/utente_a/mnt/box.com    davfs   defaults,uid=utente_a,gid=gruppo_a,noauto  0       0
#TOR

    pacman -S tor


modificare /etc/tor/torrc aggiungendo
```
############# AGGIUNTE ###########
HTTPProxy proxy.local.net:8080
HTTPProxyAuthenticator DOMINIO\user:password

HTTPSProxy proxy.local.net:8080
HTTPSProxyAuthenticator DOMINIO\user:password
```

Far ripartire il servizio

    /etc/init.d/tor restart
o 

    systemctl start tor.service
    systemctl enable tor.service

Installare POLIPO (vedi capitolo apposito)
far puntare i proxy su 127.0.0.1:8123

	
#Wget

Opzione | Descrizione 						| Esempio
------- | ------- 							| ------- 
-m		| Fa il mirror di un sito			|
-p		| Scarica anche gli oggetti collegati (immagini, css ..) | 
-U 		| Imposta  l'user agent 			| wget -U "Mozilla" http://my.url
. 		| .						 			| wget -U "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3" http://my.url
-c		| Ripristina un download interrotto | whet -c 	http://my.url
-i 		| Scarica da un lista le url 		| wget -i list.txt
-e 		| esegue un comando come se fosse parte di .wgetrc | wget -e robots=off http://my.url
--wait n | aspetta n secondi tra uno scarico e l'altro | 
-k 		| converte i link in modo da fare il browsing locale dei file scaricati |
-np (oppure --no-parent) | non caricano le directory sopra quella specificata |
-nH 	| non salva la struttura della directory con il nomehost |
--cut-dirs=4 | taglia 4 nomi di directory (es se il mirror ha molte directory annidiate) |

##wgetrc
per prelevare attraverso il proxy mettere in \$HOME/.wgetrc la linee:

    http_proxy=proxy.local:8080
    https_proxy=proxy.local:8080
    ftp_proxy=proxy.local:8080
    proxy_user=test01
    proxy_passwd=testpasswd
    robots=off			

in windows il file .wgetrc si chiama wgetrc e si mette nella directory di wget

##wget esempi
fare il mirror di un sito :

    wget -m -p -U "Mozilla" -e robots=off http://my.url
	
impostare il proxy 
	
    wget --proxy=on --proxy-user=test01 --proxy-passwd=ciccio http://www.yahoo.it 
    wget -e http_proxy=proxy.local:8080 http://www.yahoo.com
	
si possono sempre usare le variabili di ambiente:

    export http_proxy=http://user:pass@proxy.local:8080 
    export https_proxy=http://user:pass@proxy.local:8080 
    export ftp_proxy=http://user:pass@proxy.local:8080

ed eventualmente inserirle in /etc/environment
