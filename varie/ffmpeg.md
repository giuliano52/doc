---
title: FFMPEG
author: Giuliano Dedda 
date: 19/09/2014
---

Il comando Base è:

    ffmpeg -y -i INPUT_FILE video_options audio_opt OUTPUT_FILE

Info mode

    ffprobe INPUT.MOV
	ffmpeg -i INPUT.MOV -vcodec copy -acodec copy -fs -1 -f null /dev/null 2>&1 | sed -n '/^Input /,/^Stream /p' | sed '$d' 
	

##Parametri


Parametri		| Descrizione
----------------|----------------
-f 				| Formato in uscita
-i 				| File in ingresso
-y 				| sovrascrivi i file in uscita 
-v 				| Livello di verbosità
-fs limit_size 	| Set the file size limit
-threads count	| Numero di thread (impostando il valore 0 si ottiene il numero ottiamle (massimo?) di threads)

###AUDIO

Parametri		| Descrizione
----------------|----------------
-acodec ACODEC 	| Audio Codec, usare copy per lasciare inalterato il formato
-ab bitrate		|audio bitrate in bit/s (default = 64k) 
-ac channels	| Numero di audio channels (default = 1)
-an 			| Disabilita l'audio 
-ar freq 		| audio frequenza di campionamento (default = 44100 Hz). 

###VIDEO

Parametri		| Descrizione
----------------|----------------
-vcodec VCODEC	| Video Codec, usare copy per lasciare inalterato il formato
-b bitrate		| video bitrate in bit/s (default = 200 kb/s). 
-bt tolerance	| Set video bitrate tolerance (in bits, default 4000k). Has a minimum value of: (target_bitrate/target_framerate). In 1-pass mode, bitrate tolerance specifies how far ratecontrol is willing to deviate from the target average bitrate value. This is not related to min/max bitrate. Lowering tolerance too much has an adverse effect on quality. 
-aspect aspect	| aspect ratio (4:3, 16:9 or 1.3333, 1.7777). 


#H265 

    ffmpeg -i input -c:v libx265 -c:a copy output.mp4
  
The above command will copy over the audio as is. If that doesn't work, convert the audio to AAC by replacing copy with libfdk_aac, libfaac or arc (ordered quality-wise)


