---
title: Bash
author: Giuliano Dedda 
date: 10/07/2014
---

#Operazioni su files

##estrae l'estensione e il filename
```
filename=$(basename "$fullfile")
extension="${filename##*.}"
filename="${filename%.*}"
```

#Domanda are you sure?

```bash
read -p "Are you sure ? [Y/N] ? " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    # se non si preme Y il programma termina
    exit 1
fi
```

#Esempi


##Ciclo For

```bash
for i in `seq 1 10`;
do
        echo $i
done    
```

Esegui comando per ogni file
```bash
for f in dir_to_scan/* 
do 
   echo $f 
done
```

o in una sola riga
```bash   
for f in dir_to_scan/* ; do echo $f ; done
```

Elementi di un array: 
```bash
array=( one two three )
for i in "${array[@]}"
do
	echo $i
done
```

Elementi in un file
```bash
for i in $(cat host.txt) 
do
	echo $i
done
```

##WalkTree
Mostra ricorsivamente le directory
```bash
for i in `find $1 -iname '*.svg' -type f `
do
    echo "$i"
done
```

oppure 

```bash
function walk_tree {
      echo "Directory: $1"
      local directory="$1"
      local i
      for i in "$directory"/*; 
      do
      echo "File: $i"
        if [ "$i" = . -o "$i" = .. ]; then 
            continue
        elif [ -d "$i" ]; then  # Process directory and / or walk-down into directory
            # add command here to process all files in directory (i.e. ls -l "$i/"*)
            walk_tree "$i"      # DO NOT COMMENT OUT THIS LINE!!
        else
            continue    # replace continue to process individual file (i.e. echo "$i")
        fi
      done
}

walk_tree $HOME
```

