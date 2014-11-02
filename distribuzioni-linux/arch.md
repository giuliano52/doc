---
title: Arch Linux
author: Giuliano Dedda 
date: 10/07/2014
---

#Installazione
– c’è anche https://wiki.archlinux.org/index.php/Installation_Template

```bash
loadkeys it
cfdisk    (Partizionamento dischi)
mkfs.ext4 /dev/sda1
mkswap /dev/sda2

cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.orig
vi /etc/pacman.d/mirrorlist

#<PROXY>
export http_proxy=http://user:password@proxy:8080
export https_proxy=http://user:password@proxy:8080
export ftp_proxy=http://user:password@proxy:8080
#</PROXY>

mount /dev/sda1 /mnt
pacstrap /mnt base 


genfstab -p -U /mnt >> /mnt/etc/fstab 
		# -U usa gli UUID

echo "/dev/sda2	swap	swap	defaults	0	0" >> /mnt/etc/fstab

# SCEGLIERE IL BOOTLOADER GRUB (meglio) O SYSLINUX
#<GRUB>
arch-chroot /mnt pacman -S grub-bios
#</GRUB>
#<SYSLINUX>
arch-chroot /mnt pacman -S syslinux
#</SYSLINUX>

arch-chroot /mnt

# imposto l’hostname
echo "Hostname" > /etc/hostname

ln -s /usr/share/zoneinfo/Europe/Rome /etc/localtime

echo "LANG=it_IT.UTF-8" > /etc/locale.conf	

echo "KEYMAP=it" > /etc/vconsole.conf

nano /etc/locale.gen
	it_IT.UTF-8 UTF-8  
	it_IT ISO-8859-1  
	it_IT@euro ISO-8859-15
locale-gen

mkinitcpio -p linux

#<GRUB>
modprobe dm-mod
grub-install --target=i386-pc --boot-directory=/boot --recheck /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
#</GRUB>
#<SYSLINUX>
syslinux-install_update -i -a -m
nano /boot/syslinux/syslinux.cfg
	mettendo la giusta partizione di /
</SYSLINUX>
passwd
exit
reboot
```

# Post configuration

```
#<proxy>
nano /etc/enviroment
	http_proxy=http://user:password@proxy:8080
	https_proxy=http://user:paissword@proxy:8080
	ftp_proxy=http://user:password@proxy:8080
#</proxy>

#<network>
Vedi sezione NETWORK
#</network>


pacman -S openssh
systemctl enable sshd.service

per SSD
in /etcfstab aggiungere noatime,discard


[per grub2 su ubuntu ]
	sudo mount /dev/sdx /mnt/tmp
	sudo update-grub2
impostare i mirror
```


#Pacchetti Aggiuntivi
```
pacman -S cinnamon lxdm xf86-video-ati gnome-terminal
pacman -S sudo firefox vlc libreoffice-writer libreoffice-calc evince ntfs-3g
```

##Virtualbox
```
pacman -S virtualbox visrtualbox-host-modules
vi /etc/modules-load.d/virtualbox.conf
	vboxdrv 
	vboxnetadp 
	vboxnetflt 
```

##Truecrypt
```
/etc/modules-load.d/truecrypt.conf 
	loop
```

##Audio 
non viene salvato il livello del volume
pacman -s alsa-util

##Yaourt
```
vi /etc/pacman.conf 
Per x86-64 
[archlinuxfr] 
Server = http://repo.archlinux.fr/x86_64 

pacman -Sy yaourt
```

#Network
Bisogna usare netctl
per sapere le schede di rete:
	dmesg | grep eth
oppure
	ls /sys/class/net

```
cp /etc/netctl/examples/profilo /etc/netctl/
nano profilo
per vedere se funziona: 
netctl start <profile>

poi attivarlo definitivamente al boot: 
netctl enable <profile>
```


##Abilitare X via ssh 
Serve aggiungere I seguenti pacchetti:
pacman -S xorg-xauth
pacman -S xorg-fonts-type1

#Mirror
cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup
rankmirrors -n 6 /etc/pacman.d/mirrorlist.backup > /etc/pacman.d/mirrorlist

#Gestione pacchetti 

##Pacman

Opzione 	| Descrizione 				| Esempio
------- 	| ------- 				| ------- 
-S <pacchetto>	| Installa un pacchetto 		|
 -Syu		| aggiorna database e pacchetti 	|
 -Q		| queri sui pacchetti installati	|
 -Qdt		| trova gli le dipendenze orfani	| pacman -Rsn $(pacman -Qdtq) # rimuove  gli orfani

Visualizza la lista dei pacchetti ordinati per dimensione

    pacsysclean	


