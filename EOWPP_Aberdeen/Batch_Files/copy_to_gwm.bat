@echo off
REM This batch file copies files from the python script to the GWM folder
REM Note that this program assumes the root is where this batch file was called from
COPY .\abr.decvar .\AberdeenModel\model\tr
COPY .\abr.hedcon .\AberdeenModel\model\tr
