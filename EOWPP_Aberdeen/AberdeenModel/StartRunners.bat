@echo off

REM This is StartRunners.bat
REM StartRunners takes one argument, an integer, 
REM which is the number of runners to be started.

if "%1"=="" goto NoRunners
set N=%1

if %N%==0 goto NoRunners

cd Runner1\tr
Echo Starting Runner 1
Start "Runner 1" /min ..\..\bin\jrunnerm-x64

if %N%==1 goto GoHome

cd ..\..\Runner2\tr
Echo Starting Runner 2
Start "Runner 2" /min ..\..\bin\jrunnerm-x64

if %N%==2 goto GoHome

cd ..\..\Runner3\tr
Echo Starting Runner 3
Start "Runner 3" /min ..\..\bin\jrunnerm-x64

if %N%==3 goto GoHome

cd ..\..\Runner4\tr
Echo Starting Runner 4
Start "Runner 4" /min ..\..\bin\jrunnerm-x64

if %N%==4 goto GoHome

cd ..\..\Runner5\tr
Echo Starting Runner 5
Start "Runner 5" /min ..\..\bin\jrunnerm-x64

if %N%==5 goto GoHome

cd ..\..\Runner6\tr
Echo Starting Runner 6
Start "Runner 6" /min ..\..\bin\jrunnerm-x64

if %N%==6 goto GoHome

:GoHome
cd ..\..
goto End

:NoRunners
Echo No Runners started

:End
