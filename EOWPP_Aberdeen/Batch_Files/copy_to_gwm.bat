@echo off
REM This batch file copies files from the python script to the GWM folder
REM Note that this program assumes the root is where this batch file was called from
COPY .\abr.wel .\AberdeenModel\model\tr
COPY .\abr.wel .\AberdeenModel\Runner1\tr
COPY .\abr.wel .\AberdeenModel\Runner2\tr
COPY .\abr.decvar .\AberdeenModel\model\tr
COPY .\abr.hedcon .\AberdeenModel\model\tr
