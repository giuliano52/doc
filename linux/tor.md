---
title: Tor e Polipo
author: Giuliano Dedda 
date: 17/07/2014
---

#TOR

    pacman -S tor

##proxy 

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

	
#Polipo 
Proxy locale

    aptitude install polipo
    pacman -S polipo

	cd /etc/polipo; cp config.sample config
	
modificare  /etc/polipo/config modificando
# Uncomment this if you want to use a parent SOCKS proxy:
 socksParentProxy = "localhost:9050"
 socksProxyType = socks5
e aggiungendo
############## AGGIUNTE ###############
proxyAddress = "0.0.0.0"    # IPv4 only
# If you are enabling 'proxyAddress' above, then you want to enable the
# 'allowedClients' variable to the address of your network, e.g.
# allowedClients = 127.0.0.1, 192.168.42.0/24
                                          
allowedClients = 127.0.0.1, 10.20.20.30

/etc/init.d/polipo restart
 systemctl enable polipo.service