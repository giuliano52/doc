---
title: Backup e Restore
author: Giuliano Dedda 
date: 12/10/2014
---

#Duplicity

      yaourt -S duplicity
bisogna avere già  una chiave GPG (vedi doc opportuno)

##backup

      duplicity sorgente destinazione
      duplicity /home/me scp://uid@other.host//usr/backup

##Restore

      duplicity scp://uid@other.host//usr/backup /home/me
    
#S3QL
tool per utilizzare un fileserver remoto (anche locale con encryption deduplicazione e compressione).

*20140612 Non sono riuscito a farlo funzionare. probabilmente esistono problemi tra python2 e 3*

      yaourt -S s3ql

creazione del backend

      mkdir s3ql-loc
      mkfs.s3ql local://s3ql-loc
