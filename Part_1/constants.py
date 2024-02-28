import numpy as np

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


