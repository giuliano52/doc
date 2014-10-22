---
title: GIT
author: Giuliano Dedda 
date: 17/07/2014
---

#GIT

inizializzare un repository

    git init
    git add.
    git remote add origin  https://giuliano52:password@github.com/giuliano52/phphub.git
    git push
    
clonare un repository:
	
    git clone https://github.com/giuliano52/phphub.git

commit:

    git add *
    git commit -m "Commenti"
    git push https://github.com/giuliano52/pyhub.git

al posto di git add e git commit si puà usare git commit -a -m "commento"
    
##Remove history from github
Step 1: remove all history

    rm -rf .git

Step 2: reconstruct the Git repo with only the current content

    git init
    git add .
    git commit -m "Initial commit"

Step 3: push to GitHub.

    git remote add origin <github-uri>
    git push -u --force origin master


