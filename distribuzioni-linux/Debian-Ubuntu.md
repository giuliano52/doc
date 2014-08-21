---
title: Debian - Ubuntu
author: Giuliano Dedda 
date: 17/07/2014
---

#Network
In /etc/network/interfaces ci sono le configurazioni di rete.

    auto eth0
    iface eth0 inet dhcp

oppure

    auto eth0
    iface eth0 inet static
    address 172.27.0.10
    netmask 255.255.255.192
    gateway 172.27.0.1
    broadcast 172.27.0.63
    dns-search zucca.com
    dns-nameservers 8.8.8.8 4.2.2.2

se voglio inserire un comando dopo l'attivazione della rete posso inserire anche la riga ad esempio:

    post-up /usr/sbin/ntpdate 192.168.1.100

Per le rotte statiche aggiungere anche 

    up route add -net 10.0.0.0 netmask 255.0.0.0 gw 192.168.0.2 dev $IFACE
	
Nel qual caso bisogna anche configurare il dns: /etc/network

    search dominio.com
    nameserver 130.186.1.53  # dns.cineca.it