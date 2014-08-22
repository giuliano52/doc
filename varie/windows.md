---
title: WINDOWS
author: Giuliano Dedda 
date: 15/07/2014
---

#Comandi vari
```
whoami /fqdn  |    Fornisce il FQDN
whoami /user  |    Fornisce il SID
```

#X per Windows
Scaricare Cygwin 

creare: C:\\cygwin\\bin\\startmyx.bat
```
REM @echo off
SET DISPLAY=:0.0

SET CYGWIN_ROOT=C:\\cygwin
if defined CYGWIN_ROOT goto :OK
SET CYGWIN_ROOT=%~dp0\\..
:OK

SET RUN=%CYGWIN_ROOT%\\bin\\run -p /usr/bin

SET PATH=%CYGWIN_ROOT%\\bin;%PATH%

SET XAPPLRESDIR=
SET XCMSDB=
SET XKEYSYMDB=
SET XNLSPATH=


REM
REM Cleanup after last run.
REM

if not exist %CYGWIN_ROOT%\\tmp\\.X11-unix\\X0 goto CLEANUP-FINISH
attrib -s %CYGWIN_ROOT%\\tmp\\.X11-unix\\X0
del %CYGWIN_ROOT%\\tmp\\.X11-unix\\X0

:CLEANUP-FINISH
if exist %CYGWIN_ROOT%\\tmp\\.X11-unix rmdir %CYGWIN_ROOT%\\tmp\\.X11-unix

%RUN% bash -l -c "XWin -multiwindow -clipboard -silent-dup-error"
sleep 5
REM %RUN% xhost +
```

in autorun eseguire mettere un link a:
C:\\cygwin\\bin\\run.exe /usr/bin/startmyx.bat