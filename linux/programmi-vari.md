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


#Systemd

Comando                         | Effetto
----------------------------    | ----------------------------
journalctl -b 			        | messagi dal boot
journalctl --no-pager		    | messaggi senza visualizzazione a pagine
systemctl -t service -a 	    | mostra i servizi al boot
systemctl list-unit-files       | mostra lo stato dei servizi

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
    
#OCR - tesseract

installare anche community/tesseract-data-ita

tesseract converte solo da tif pertanto bisogna convertire i file prima:
su : http://wiki.ubuntu-it.org/Grafica/Ocr c'è una buona guida e un programma per converitire un PDF con più pagine.





