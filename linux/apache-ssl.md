---
title: Apache e SSL
author: Giuliano Dedda 
date: 20/08/2014
---

# Varie
per vedere i moduli attivi:

    apache2ctl -t -D DUMP_MODULES

#VirtualHost

Prima di fare alti virtualhost è meglio spostare  quello di default in /var/www/default 

    mkdir /var/www/nuovosito
    mkdir /var/www/nuovosito/httpdocs
    echo "funziona" > /var/www/nuovosito/httpdocs/index.html

vi /etc/apache2/sites-available/001-www.nuovosito.it.conf

    <VirtualHost *:80>
    ServerName www.nuovosito.it
    DocumentRoot /var/www/nuovosito/httpdocs
    </VirtualHost>

se serve si può inserire un blocco particolare per una directory all'interno del virtual host

    <Directory /var/www/www.mysite/httpdocs/administrator/ >
    Order Deny,Allow
    Deny from all
    Allow from 192.168.1.0/8
    </Directory>


#Userdir

    a2enmod userdir
abilita la directory nelle home public_html

per abilitare anche il php andare in /etc/apache2/mods-enabled/php5.conf
    
    <IfModule mod_userdir.c>
        <Directory /home/*/public_html>
           php_admin_value engine Off
        </Directory>
    </IfModule>
    
e commentarle con un #

#Modsecurity

     apt-get install libapache2-modsecurity 
     cp /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
     service apache2 reload

in  ls /var/log/apache2 ci dovrebbe essere il file: modsec_audit.log
ora bisogna 

1) attivare le regole di mod_security
2) passare dalla modalità simulation a quella blocco
3) modificare /etc/apache2/mods-available/Security2.conf

1) Attivare le regole:

    cd /usr/share/modsecurity-crs/base_rules
    for f in * ; do sudo ln -s /usr/share/modsecurity-crs/base_rules/$f /usr/share/modsecurity-crs/activated_rules/$f ; done

    cd /usr/share/modsecurity-crs/optional_rules
    for f in * ; do sudo ln -s /usr/share/modsecurity-crs/optional_rules/$f /usr/share/modsecurity-crs/activated_rules/$f ; done
    
    
Bisgona dire ad Apache dove trovare le regole:
  
     nano /etc/apache2/mods-available/security2.conf

Alla fine del file, subio prima di  </IfModule> inserire:

    Include "/usr/share/modsecurity-crs/*.conf"
    Include "/usr/share/modsecurity-crs/activated_rules/*.conf"

Abilitare il controllo degli header:

    a2enmod headers
    service apache2 restart
    
Ora Modsecurity è in Simulation Mode
per attivarlo: 

    vim /etc/modsecurity/modsecurity.conf

Modificando __SecRuleEngine DetectionOnly__ con __SecRuleEngine On__

oppure se si desidara attivarlo in un solo host mettere la direttiva __SecRuleEngine On__ all'interno del virtualhost
    
Testarlo 

    http://www.misito.com/index.php?abc=../../
    http://www.mio sito /faq.php?action=&type=view&s=&id=-1'%20union%20select%200,concat(char(85),char(115),char(101),char(114),char(110),char(97),char(109),char(101),char(58),name,char(32),char(124),char(124),char(32),char(80),char(97),char(115),char(115),char(119),char(111),char(114),char(100),char(58),pass),0,0,0,0,0%20from%20phpdesk_admin/* 

 
se si desidera abiliare una regola:

    SecRuleRemoveById 950006

può essere usato anche dentro il tag <Location /path> se di desidera abilitarla solo per un particola path

#GZIP

    a2enmod deflate
    
#Rev-Proxy

Abilitare il modulo 

    a2enmod proxy_http
    service apache2 restart

creo il file /etc/apache2/sites-available/revprx-www.mysite.local
 
     <VirtualHost 10.0.0.1:80>
     # dominio a cui risponde
     ServerName www.sito-esterno.local
     # Disabilita la possibilita' di usarlo come un Open Proxy
     ProxyRequests Off
     <Proxy *>
        Order deny,allow
        Allow from all
     </Proxy>
	 ProxyPassReverse / http://sito-esterno/
	 ProxyPass / http://sito-interno/ 
     </VirtualHost>

##Esempi
esempi: 
www.esterno.it → www.interno.it

    ProxyPassReverse / http://sito-esterno/
    ProxyPass / http://sito-interno/ 

www.esterno.it/ext → www.interno.it

    <Location /ext>
	ProxyPass http://sito-interno/ 
    </Location>
	ProxyPassReverse / http://sito-esterno/

www.esterno.it → www.interno.it/int

    ProxyPassReverse / http://sito-esterno/
    ProxyPass / http://sito-interno/int
    
attenzione che i link nell'applicazione devono essere corretti.  

altre opzioni 

Metto a posto i web server che non supportano correttamente http1.1

    SetEnv force-proxy-request-1.0 1
    SetEnv proxy-nokeepalive 1

##per pubblicare OWA

abilitare il mod_rewrite
    
    a2enmod rewrite
    service apache2 restart
    
inserire dentro /etc/hosts il record: mail.miosito.it
```
<VirtualHost *>
        ServerName mail.miosito.it

        ProxyRequests Off
        <Proxy *>
                Order deny,allow
                Allow from all
        </Proxy>

        #SecFilterEngine Off

#       AddDefaultCharset iso-8859-1
        AddDefaultCharset utf-8

        KeepAlive On

        RewriteEngine On
        RewriteRule     ^/$     /owa       [L,R]

        ProxyPassReverse /owa http://mail.miosito.it/owa
        ProxyPass /owa http://mail.miosito.it/owa

        ProxyPassReverse /emc http://mail.miosito.it/emc
        ProxyPass /emc http://mail.miosito.it/emc

        ProxyPassReverse /oab  http://mail.miosito.it/oab
        ProxyPass /oab  http://mail.miosito.it/oab

#       RewriteEngine On
#       RewriteCond %{SERVER_PORT} !^443$
#       RewriteRule ^/(.*) https://%{SERVER_NAME}/$1 [L,R]
#       RewriteRule ^/(.*) https://%{SERVER_NAME}/exchange$1 [L,R]

</VirtualHost>


<VirtualHost 192.168.1.1:443>
        ServerName mail.miosito.it

        # Attivo mod_secuirty
        # SecFilterEngine On
# Mi sapetto che non ci siano problemi di sicurezza su OWA
# (Inserito per permance / evitrare problemi)

        #SecFilterEngine Off

        # disabilito questo controllo per le mail con il % nel subject
        #SecFilterCheckURLEncoding Off

        AddDefaultCharset iso-8859-1

        KeepAlive On


        SSLEngine On
        SSLCertificateFile /etc/apache2/ssl/webmail-cert.pem
        SSLCertificateKeyFile /etc/apache2/ssl/webmail-key.pem

        ProxyRequests Off
        RequestHeader set Front-End-Https "On"

        RewriteEngine On
        RewriteRule     ^/$     /owa       [L,R]

        <Proxy *>
                Order deny,allow
                Allow from all
        </Proxy>
        SSLProxyEngine On

	# Elimino la verifica del certificato intenro
	SSLProxyVerify none 
	SSLProxyCheckPeerCN off
	SSLProxyCheckPeerName off
        ProxyPassReverse /owa https://mail.miosito.it/owa
        ProxyPass /owa https://mail.miosito.it/owa

        ProxyPassReverse /emc https://mail.miosito.it/emc
        ProxyPass /emc https://mail.miosito.it/emc

        ProxyPassReverse /oab  https://mail.miosito.it/oab
        ProxyPass /oab  https://mail.miosito.it/oab

</VirtualHost>







```
