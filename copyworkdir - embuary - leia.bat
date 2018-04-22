@echo off
set dev=..\skin.embuary-leia
set target=skin.embuary-leia
set htpc=\\NUCFRED\Kodi\portable_data\addons\skin.embuary-leia
echo. 
echo Copying files
echo. 
rd /S /Q %target%
XCOPY %dev% %target% /E /C /Q /I /Y
rd /S /Q %target%\media-working-dir
del /q /s %target%\*.pyo 
del /q /s %target%\*.pyc 
del /q /s %target%\*.psd 
del /q /s %target%\*.mo
rd /S /Q %target%\.git
TIMEOUT /T 4 /NOBREAK
repoupdate.bat