import numpy as np
import pandas as pd
import sys
sys.path.append('./Part_1_1/')
from Constants import constants
import numba
from functools import lru_cache



@numba.njit
def jN(n):
    e = np.sqrt(constants.e2)
    if n % 2 == 1:
        return 0
    else:
        return (((-1) ** (n // 2)) * ((3 * e ** n * (1 - n / 2 + (5 / 2) * (constants.j2n / (e ** 2)) * n)) / ((n + 1) * (n + 3) * np.sqrt(2 * n + 1))))

@numba.njit
def r_nm(c, n, m):
    if m == 0:
        return c - jN(n)
    else:
        return c

@lru_cache(None)
def pN1(t, n, pn1, pn2):
    return ((-(np.sqrt(2*n+1))/n)*((n-1)/(np.sqrt(2*n-3)))*pn2 + t * ((np.sqrt(2*n+1))/(n))*np.sqrt(2*n-1)*pn1)

@lru_cache(None)
def pN2(t, n, m, pn1, pn2):
    return (-np.sqrt(((2*n+1)*(n+m-1)*(n-m-1))/((2*n-3)*(n+m)*(n-m)))*pn2 + t*np.sqrt(((2*n+1)*(2*n-1))/((n+m)*(n-m)))*pn1)

@lru_cache(None)
def pN3(t, n, pn1):
    return t * np.sqrt(2*n+1) * pn1

@lru_cache(None)
def pN4(t, n, pn1):
    return np.sqrt((2*n+1)/(2*n)) * np.sqrt(1-t**2) * pn1

# Memoize the main function
@lru_cache(None)
def pN_main(n, m, latitude):
    t = np.sin(latitude)
    
    if (n == 0 and m == 0):
        return 1
    elif (n == 1 and m == 0):
        return t * np.sqrt(3)
    elif (n == 2 and m == 0):
        return np.sqrt(5) * ((1.5 * t**2) - (1/2))
    elif (n == 1 and m == 1):
        return np.sqrt(3) * np.sqrt(1 - t**2)
    elif (n == 2 and m == 1):
        return t * np.sqrt(15) * np.sqrt(1 - t**2)

    elif (n >= 2 and m == 0):
        return pN1(t, n, pN_main(n-1, 0, latitude), pN_main(n-2, 0, latitude))

    elif (n >= 3 and m >= 1 and m <= n-2):
        return pN2(t, n, m, pN_main(n-1, m, latitude), pN_main(n-2, m, latitude))

    elif (n >= 1 and m == (n-1)):
        return pN3(t, n, pN_main(n-1, n-1, latitude))

    elif (n >= 2 and m == n):
        return pN4(t, n, pN_main(n-1, n-1, latitude))

def compute_geoidal_height(lat_radians, long_radians, R, model_values):
    sum = 0
    constant_term = constants.gm / (R * constants.gamma)
    for index in range(len(model_values)):
        
        if (index % 1000 == 0):
            print("Entering row: ", index)
        
        n = model_values[index, 0]
        m = model_values[index, 1]
        Cnm = model_values[index, 2]
        Snm = model_values[index, 3]
        q = Snm
        aRn = (constants.a / R) ** n
        long_term = (r_nm(Cnm, n, m) * np.cos(m * long_radians) + q * np.sin(m * long_radians)) * pN_main(n, m, lat_radians)
        sum += long_term * aRn
    geoidUndulation = constant_term * sum
    return geoidUndulation

def geoidalHeight(latitude, longitude, R, model):
    latitude_radians = latitude * (np.pi / 180)
    longitude_radians = longitude * (np.pi / 180)
    model_values = model[['n', 'm', 'Cnm', 'Snm']].values.astype(float)
    geoidUndulation = compute_geoidal_height(latitude_radians, longitude_radians, R, model_values)
    print("The point with latitude:", latitude, "and longitude:", longitude, "has N =", geoidUndulation, "m")
    return geoidUndulation

# Call the function
geoidalHeight(61.9308563192723, 5.12764703841812, constants.r, constants.df_EGM2008)
#geoidalHeight(61.9308563192723, 5.12764703841812, constants.r, constants.df_EGM2008)
#geoidalHeight(61.6929259311394, 5.1957949286442, constants.r, constants.df_GGM03S)