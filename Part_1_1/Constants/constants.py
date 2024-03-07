import numpy as np
import pandas as pd

a = 6378137.0000 #m
b= 6356752.3141 #m
f1 = 298.257222101
e2 = 0.006694380023
r = 6371000.7900 #m
gm = 3986005 * 10**8 #m^3/s^2
gamma = 9.81 #m/s^2
j2n = 0.108263 * 10**(-2)

step_size = 0.5
latitudes = np.arange(-90, 90 + step_size, step_size)
longitudes = np.arange(-180, 180 + step_size, step_size)

# Specify the number of rows to skip

colspecs_EGM2008 = [(7, 9), (12, 14), (17, 39), (42, 64)]
colspecs_GGM03S = [(5, 9), (10, 14), (14, 33), (34, 53)]


# Read the text file into a pandas DataFrame, skipping the specified number of rows
df_EGM2008 = pd.read_fwf('Part_1_1/Data/EGM2008.txt', colspecs=colspecs_EGM2008, skiprows=19, nrows=229)
df_GGM03S = pd.read_fwf('Part_1_1/Data/GGM03S.txt', colspecs=colspecs_GGM03S, skiprows=38, nrows=231)

print(df_EGM2008)











