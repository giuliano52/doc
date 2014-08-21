#!/usr/bin/python
import os
# Autor: GD
# Data: 20140710
# Modifica: 20140714

# programma che prende i file markdown all'interno della directory e li converte in pdf tramite il comando pandoc
# se passa per il formato latex intermedio effettua alcune modifiche (es sposta le tabelle a sinistra )



def recusively_lanch_command(dir):
	for dirpath, dirnames, filenames in os.walk (dir):
		if '.git' in dirnames:
			dirnames.remove('.git')
		for subdir in dirnames:
			vuoto = ''
		for nomefile in filenames:
			nome_file_completo = os.path.join(dirpath,nomefile)
			(filebase,estensione) = os.path.splitext( nome_file_completo )
			if ((estensione.lower() == '.md') and (filebase != './README')): 	
				dir_name, file_name = os.path.split(nome_file_completo)
				
				comando_pdf = 'pandoc ' + nome_file_completo + ' -s -o ' + dir_name + '/pdf-rendered/'+ file_name +'.pdf  -V geometry:"top=1cm, bottom=1.5cm, left=1cm, right=1cm" ' 
				comando_tex = 'pandoc ' + nome_file_completo + ' -s -o ' + dir_name + '/pdf-rendered/'+ file_name +'.tex  -V geometry:"top=1cm, bottom=1.5cm, left=1cm, right=1cm" ' 
				comando_pdflatex = 'pdflatex -output-directory=' + dir_name + '/pdf-rendered/ '+ dir_name + '/pdf-rendered/'+ file_name +'.tex  > /dev/null '
			
			
				#sistema = 'direct_pdf'
				sistema = 'create_latex'
			
				if (sistema == 'direct_pdf') : 
					print (comando_pdf)
					os.system(comando_pdf)
				elif(sistema =='create_latex') :
					print (comando_tex)
					os.system(comando_tex)
					
					#rimpiazza \begin{longtable}[c] con \begin{longtable}[l] per avere le tabelle allineate a sinistra
					comando = "sed  -i 's/begin{longtable}\[c\]/begin{longtable}\[l\]/' " + dir_name + '/pdf-rendered/'+ file_name +'.tex'
					print (comando)
					os.system(comando)
					
					print (comando_pdflatex)
					os.system(comando_pdflatex)
					# due volte il comando pdflatex per generarare correttamente i capitoli all'interno del file pdf
					os.system(comando_pdflatex)
			
		
	
			
			
				# al posto di os.system si puo' usare subprocess
				
	



#------------------------------- MAIN --------------------------------

processing_directory = './'
recusively_lanch_command(processing_directory)

# un po' di pulizia
estensioni_da_rimuovere = ('*.toc','*.out','*.log','*.aux')
for estensione in estensioni_da_rimuovere:
	comando_remove = "find ./ -name '"+ estensione + "' -exec rm -f {} \;"
	print (comando_remove)
	os.system(comando_remove)

