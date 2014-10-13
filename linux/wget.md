#Wget

Opzione | Descrizione 		  				  | Esempio
------- | ------- 					    	  	| ------- 
-m		  | Fa il mirror di un sito			|
-p		  | Scarica anche gli oggetti collegati (immagini, css ..) | 
-U 		  | Imposta  l'user agent 			| wget -U "Mozilla" http://my.url
. 		  | .						 			          | wget -U "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3" http://my.url
-c		  | Ripristina un download interrotto | whet -c 	http://my.url
-i 		  | Scarica da un lista le url 	| wget -i list.txt
-e 		  | esegue un comando come se fosse parte di .wgetrc | wget -e robots=off http://my.url
--wait n | aspetta n secondi tra uno scarico e l'altro | 
-k 	  	| converte i link in modo da fare il browsing locale dei file scaricati |
-np (oppure --no-parent) | non caricano le directory sopra quella specificata |
-nH 	  | non salva la struttura della directory con il nomehost |
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
