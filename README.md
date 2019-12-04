Code and Documentation by Fleford Redoloza
04/28/2019

This project folder contains all the code and data for the masters thesis paper:
"A Novel Approach for Well Placement Design in Groundwater Management: Extremal Optimization"

For any questions, please email fleford@gmail.com

All code is written for Python 3.6
Necessary Libraries include:
matplotlib
numpy
math
copy

EO_Aberdeen\EO_PointTest\EO.py contains the class for the EO-WPP algorithm (so does EO_Aberdeen\EO_PointTest/EOWPP.py)
EO_Aberdeen\EO_PointTest contains the code for testing and benchmarking EOWPP
EO_Aberdeen\GWMVI_1_0_2 contains the code for GWM: Groundwater Management Process for MODFLOW Using Optimization
EO_Aberdeen\GWM_Manipulator.py contains code for Python to manipulate the GWM terminal program
EO_Aberdeen\Batch_Files contains batch files EO_Aberdeen\GWM_Manipulator.py uses to control GWM

EOWPP_Aberdeen contains all the code for applying EOWPP to the Aberdeen groundwater model
EOWPP_Aberdeen\AberdeenModel contains the Aberdeen model that Python works on
EOWPP_Aberdeen\AberdeenModel_Clean contains a clean copy of the Aberdeen model in case the working copy is corrupted
EOWPP_Aberdeen\EOWPP_FILES contains results from tests
EOWPP_Aberdeen\Solution_Reader.py contains code to convert files in EOWPP_FILES into numpy arrays
