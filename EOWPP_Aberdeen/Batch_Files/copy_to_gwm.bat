@echo off
REM This batch file copies files from the python script to the GWM folder
REM Note that this program assumes the root is where this batch file was called from
COPY .\abr.well .\AberdeenModel\model\tr
COPY .\abr.well .\AberdeenModel\Runner1\tr
COPY .\abr.well .\AberdeenModel\Runner2\tr
COPY .\abr.decvar .\AberdeenModel\model\tr
COPY .\abr.hedcon .\AberdeenModel\model\tr
