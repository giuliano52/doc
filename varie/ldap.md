---
title: LDAP
author: Giuliano Dedda 
date: 15/07/2014
---

#Ldapsearch
```
ldapsearch -x -b dc=zumba,dc=local
			-x : Simple authentication
			-b : base dn for search
			-D : Bind DN
			-h : server
```
			
Per ricercare l'untente *aaaaa* sul server *server-ldap* con facendo bind con l'utente *bbbbb* e *password_segreta*

    ldapsearch -x -h server-ldap -D "CN=bbbbb,OU=amministrativa,DC=corp,DC=zumba,DC=local" -o ldif-wrap=no -b "DC=corp,DC=zumba,DC=local" -w password_segreta -LLL "(&(objectClass=User)(sn=aaaaa))" cn sAMAccountName 


#Filtri LDAP

Windows Account = ciccio

    (&(objectClass=User)(sAMAccountName=ciccio))

Account Never Expire

    (&(objectClass=User)(userAccountControl:1.2.840.113556.1.4.803:=65536)) 

trova gli account con cognome uguale a Pluto

     (&(objectClass=User)(sn=Pluto))
	 
trova gli account con name uguale a papero	
	 (&(objectClass=User)(name=papero*))

Gruppi con membro il CN indicato

    (&(objectClass=group)(member=CN=S-1-5-21-194 ... 6961-546487652-86 ... 15-32915,CN=ForeignSecurityPrincipals,DC=corp,DC=zumba,DC=local))
	
Con un lastlogon maggiore di una data 

    (&(objectClass=User)(lastlogon >= 126769842140239368))
	
