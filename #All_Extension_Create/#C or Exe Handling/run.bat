@echo off
cls
gcc Simple.c
echo  Enter agr1:
set /p a=
echo  Enter arg2:
set /p b=
set /a d = a.exe a b
echo %d%