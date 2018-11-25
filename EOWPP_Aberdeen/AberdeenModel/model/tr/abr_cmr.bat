@echo off
REM  Aberdeen Model Composite Model Run
REM  Invoke MMProc to preprocess, run Aberdeen Model simulation,
REM  and postprocess 
echo abr_cmr.bat is deleting old Modflow output files...
if exist abr.lst del abr.lst
if exist abr_streamflow.cbc del abr_streamflow.cbc 
if exist abr.cbb del abr.cbb
if exist abr_heads.hds del abr_heads.hds
echo abr_cmr.bat is invoking MMProc-x64.exe...
..\..\bin\mmproc-x64.exe
echo abr_cmr.bat has finished.