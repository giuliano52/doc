---
title: Samba 
author: Giuliano Dedda 
date: 21/07/2014
---

#Client
Per accedere alle share bisogna impostare il dominio. (Può essere impostato anche in /etc/samba/smb.conf)

    smbclient //host/share -U guest
    smbclient -L //host -U guest

se si vuole montare bisogna installare il pacchetto smbfs 

    smbmount //host/share /mnt/point/ -o username=guest

In fsab

    //mio_server_win2k/Cartella_condivisa
    /directory_in_cui_monto_la_condivisione smbfs uid=<num_uid>,fmask=<fmask>,dmask=<dmask>,username=USER,password=PASS,workgroup=WORK 0 0

#Server

     apt-get install samba 
     pacman -S samba

vi /etc/samba/smb.conf

Per fare la condivisione delle home aggiungere alla fine di /etc/samba/smb.conf:
    [homes]
    browseable = yes
	read only = no

    sudo  smbpasswd -a username

dalla versione 4 usare:
    
    pdbedit -a -u <user>

per abitilitare i servizi (con systemd) 
	
    systemctl enable smbd.service
    systemctl enable nmbd.service

accedere poi da Windows con  

    \\server-samba\username
 
se ci sono problemi di refresh (testato su windows 7)
Only had to add this registry key:

    DirectoryCacheLifetime[DWORD] = 0
    HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Lanmanworkstation\Parameters

#Winbind

    ntlm_auth –username=test01	| per verificare le credenziali dell'utente
    wbinfo -n test01			| per trovare il sid di un utente
    
 
