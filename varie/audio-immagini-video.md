---
title: Audio Immagini Video
author: Giuliano Dedda 
date: 19/09/2014
---


#DVD 

per fare una copia di sucurezza di un DVD su HD
(vobcopy può dare un errore se usato direttamente dal device)

    sudo mount -n /dev/sr0 ~/mnt/tmp/
    vobcopy -m ~/mnt/tmp/

se vobcopy si blocca si può crere l'iso con ddrescue e poi lanciare vobcopy sull'iso 

    ddrescue /dev/sr0 out.iso
    vobcopy -l out.iso
 

#Mp3

Rimuovere il tag v1 (uso il programma _eye3D_)

    find ./ -iname "*.mp3" -exec eyeD3 --remove-v1  {} \;
