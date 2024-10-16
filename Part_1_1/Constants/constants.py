import numpy as np
import pandas as pd


#The constants below are the ones given in the exercise text
a = 6378137.0000 #m
b= 6356752.3141 #m
f1 = 298.257222101
e2 = 0.006694380023
r = 6371000.7900 #m
gm = 3986005 * 10**8 #m^3/s^2
gamma = 9.81 #m/s^2
j2n = 0.108263 * 10**(-2)

#The columns containing the different parameters are specified
#Each number "x" in the arrays below symbolize the x number of signs from the left in the .txt file
colspecs_EGM2008 = [(5, 9), (12, 14), (17, 39), (42, 64)] 
colspecs_GGM03S = [(5, 9), (10, 14), (14, 33), (34, 53)]


#The two .txt files provided on Blackboard are then read and made into two pandas DataFrames, one for each gravimetric model
#Because the first couple of rows in the .txt files do not contain data, these are skipped
#In addition, the order of the hamonic series can be adjusted by specifying the number of rows that are to be read
df_EGM2008 = pd.read_fwf('Part_1_1/Data/EGM2008.txt', colspecs=colspecs_EGM2008, skiprows=19, nrows = 501499)
df_GGM03S = pd.read_fwf('Part_1_1/Data/GGM03S.txt', colspecs=colspecs_GGM03S, skiprows=38)


#print(df_EGM2008)











