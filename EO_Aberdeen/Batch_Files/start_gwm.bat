@echo off
RMDIR /s /q .\GWMVI_1_0_2\Test\Runner1\
RMDIR /s /q .\GWMVI_1_0_2\Test\Runner2\
RMDIR /s /q .\GWMVI_1_0_2\Test\Supply2\
MKDIR .\GWMVI_1_0_2\Test\Runner1\
MKDIR .\GWMVI_1_0_2\Test\Runner2\
MKDIR .\GWMVI_1_0_2\Test\Supply2\
COPY .\Test_clean\Runner1 .\GWMVI_1_0_2\Test\Runner1
COPY .\Test_clean\Runner2 .\GWMVI_1_0_2\Test\Runner2
COPY .\Test_clean\Supply2 .\GWMVI_1_0_2\Test\Supply2
cd .\GWMVI_1_0_2\Test\Supply2
Supply2.bat