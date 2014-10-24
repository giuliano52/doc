---
Title: NFS
---

#SERVER

     aptitude install nfs-common, nfs-kernel-server
    
editare il file /etc/exports nel seguente modo:

    NomeDirDaEsportare host1(opt) host2(opt) 
es: 

    /home/test01/Software/Linux srv.domain.it(ro) 192,168,1,1(rw) 
    service nfs start 
    exportfs 			mostra i filesystem esportati

#CLIENT
su arch : 

    sudo pacman -S nfs-utils
    sudo systemctl start rpcbind.service
    sudo systemctl start nfs-client.target


su debain: installare anche nfs-common  (Verificare)

    mount nomehost://directory/ /mount/point 	per montare una directory via nfs

es

    sudo mount 192.168.1.51:///mnt/HD/HD_a2 ./nas/
    

su fstab
    
    # NAS (no auto)
    nfs_server:/mnt/HD/HD_a2 /mnt/nas nfs rw,hard,intr,nolock,noauto,user 0 0

    #NAS auto
    nfs_server:/mnt/HD/HD_a2 /mnt/nas nfs rw,hard,intr,nolock,user 0 0
 
#Permessi

devono essere messi sul server (non è possibile ad esempio modificare l'owner di una cartella da root del client)
