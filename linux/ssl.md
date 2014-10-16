#SSL e Certificate Autority

Da: [http://www.flatmtn.com/computer/Linux-SSLCertificates.html]

    mkdir sslcert
    chmod 0700 sslcert
    cd sslcert
    mkdir certs private request
    echo '100001' >serial
    touch certindex.txt

creare il vile _openssl.cnf_ in questo modo 

```
#
# OpenSSL configuration file.
#

# Establish working directory.

dir						= .

[ ca ]
default_ca				= CA_default

[ CA_default ]
serial					= $dir/serial
database				= $dir/certindex.txt
new_certs_dir			= $dir/certs
certificate			= $dir/certs/cacert.pem
private_key			= $dir/private/cakey.pem
default_days			= 365
default_md				= sha1 # meglio di md5
preserve				= no
email_in_dn			= no
nameopt				= default_ca
certopt				= default_ca
policy					= policy_match

[ policy_match ]
countryName                     = supplied
stateOrProvinceName             = supplied
organizationName                = supplied
organizationalUnitName          = optional
commonName                      = supplied
emailAddress                    = optional


[ req ]
default_bits				= 2048			# Size of keys
default_keyfile			= key.pem		# name of generated keys
default_md					= md5				# message digest algorithm
string_mask				= nombstr		# permitted characters
distinguished_name		= req_distinguished_name
req_extensions			= v3_req

[ req_distinguished_name ]
# Variable name				Prompt string
#-------------------------	  ----------------------------------
0.organizationName			= Organization Name (company)
organizationalUnitName			= Organizational Unit Name (department, division)
emailAddress				= Email Address
emailAddress_max			= 40
localityName				= Locality Name (city, district)
stateOrProvinceName			= State or Province Name (full name)
countryName				= Country Name (2 letter code)
countryName_min				= 2
countryName_max				= 2
commonName				= Common Name (hostname, IP, or your name)
commonName_max				= 64


# Default values for the above, for consistency and less typing.
# Variable name				Value
#------------------------	  ------------------------------
0.organizationName_default	= Zuccabar
localityName_default			= Rome
stateOrProvinceName_default	= Lazio
countryName_default			= IT

[ v3_ca ]
basicConstraints				= CA:TRUE
subjectKeyIdentifier			= hash
authorityKeyIdentifier		= keyid:always,issuer:always

[ v3_req ]
basicConstraints				= CA:FALSE
subjectKeyIdentifier			= hash
```

-----

per il certificato di root:

    openssl req -new -x509 -extensions v3_ca -keyout private/cakey.pem -out certs/cacert.pem -days 1825 -config ./openssl.cnf

per fare la richiesta di certificato:

    openssl req -new -nodes -out request/name-req.pem -keyout private/name-key.pem -config ./openssl.cnf

per firmare la richiesta

    openssl ca -out certs/name-cert.pem -config ./openssl.cnf -infiles request/name-req.pem

per convertire un certificato in pkcs12 (Chiave pubblica e privata in un unico file)

    openssl pkcs12 -export -in certs/name-cert.pem -inkey private/name-key.pem -out name.p12


Script per i tre comandi assieme

```
#!/bin/sh

NOME=$1
if [ $# -ne 1 ]
    then
   echo "La sintassi e' genera-pks12.sh NOME "
   exit 1
fi
# per fare la richiesta di certificato:
openssl req -new -nodes -out request/$NOME-req.pem -keyout private/$NOME-key.pem -config ./openssl.cnf
# per firmare la richiesta
openssl ca -out certs/$NOME-cert.pem -config ./openssl.cnf -infiles request/$NOME-req.pem
# per convertire un certificato in pkcs12 (Chiave pubblica e privata in un unico file)
openssl pkcs12 -export -in certs/$NOME-cert.pem -inkey private/$NOME-key.pem -out pks12/$NOME.p12
```

il file di configurazione in policy_match ha la possibilità di impostare che certi campi debbano obbligatoriamente essere uguali:
es: 

    countryName                     = supplied

oppure

    countryName                     = match



#Apache:

    SSLEngine On
    SSLCertificateFile /etc/apache2/ssl/name-cert.pem
    SSLCertificateKeyFile /etc/apache2/ssl/name-key.pem




#IIS
Fare la richiesta su IIS

    openssl ca -out certs/hpsim-cer.pem -config ./openssl.cnf -infiles request/hpsim-req.pem


Per generare la certification autority completa: installare il certificato di root ( certs/cacert.pem ) nei trusted certificates. 
