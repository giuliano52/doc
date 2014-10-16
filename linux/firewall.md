#Firewall

##UCF (uncomplicated firewall)

    sudo pacman -S ufw
    sudo ufw default deny
    sudo ufw allow from 192.168.1.0/24
    sudo ufw allow http
    sudo ufw allow from 10.20.30.40 port ssh
    
abilitare il firewall     
    
    sudo ufw enable
    sudo systemctl enable ufw
    
	
per vedere lo stato

    sudo ufw status
    
	
