---
Titolo: X
---

#Login Manager

##LXDM

    systemctl enable lxdm
    
    
##LightDM
le configurazioni sono in: _/etc/lightdm/lightdm.conf_ 
e si sceglie il greeater con: 

    greeter-session=lightdm-gtk-greeter

abilitazione lightdm

    systemctl enable lightdm


