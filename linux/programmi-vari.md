---
title: Programmi Vari
author: Giuliano Dedda 
date: 17/07/2014
---
#corkscrew

    pacman -S corkscrew
   
Configue corkscrew

    touch .corkscrew-auth
    nano .corkscrew-auth
    username:password
    
Configure ssh For Tunneling

    vim /home/yourusername/.ssh/config
    Host *
    ProxyCommand corkscrew proxyhostname proxyport %h %p /home/username/.corkscrew-auth

Test your SSH connection

    ssh serverip


#Pandoc
Serve per convertire formati di file (es da html a epub, ... )
20140709 per installartlo su ARCH meglio non usare AUR ma impostare il repository: come spiegato qui: http://gnuhacks.com/blog/how-to-install-pandoc-on-arch-linux/
in partica in _/etc/pacman.con_ inserire le seguenti righe:


    [haskell-core]
    Server = http://xsounds.org/~haskell/core/$arch


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

##errori 
se fornisce come errore: 
  
    Stack space overflow: current size
    
lanciare con le opzioni: +RTS -K64m -RTS  es:

    pandoc -t markdown d1.tex -o d1.txt +RTS -K64m -RTS


#Systemd

Comando                          | Effetto
----------------------------     | ----------------------------
journalctl -b 			 | messagi dal boot
journalctl --no-pager		 | messaggi senza visualizzazione a pagine
systemctl -t service -a 	 | mostra i servizi al boot

Il servizio per la risoluzione dei nomi si chiama _systemd-resolved.service_ e genera il file /run/systemd/resolve/resolv.conf che viene linkato a /etc/resolv.conf

##cose da verificare
in /usr/lib/systemd/system/ ci dovrebbero essere i servizi disponibili
in /etc/systemd/system quelli abilitati ?

#Webdav

##davfs2

installare davfs2 

###Proxy
in /etc/davfs2/davfs2.conf inserire

    proxy 127.0.0.1:28080

###montare le directory

in /etc/davfs2/secrets inserire:
    
    https://dav.box.com/dav nome_utente_box_com@email.info password_box_com

per montare un disco remoto con l'utente_a inserire in /etc/fstab

    https://dav.box.com/dav /home/utente_a/mnt/box.com    davfs   defaults,uid=utente_a,gid=gruppo_a,noauto  0       0
    
    


