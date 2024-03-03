import numpy as np
import pandas as pd

import sys
sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/Part_1/')
from Constants import constants
from Functions import pN
from Functions import r_nm


def geoidalHeight(latitude, longitude, R):

    latitude_radians = latitude * (np.pi/180)
    longitude_radians = longitude * (np.pi/180)

    #The final result is initially 0, but we add all the terms in the sums as they are calculated.
    sum = 0
    i = 0

    constant_term = constants.gm / (R * constants.gamma)
    #print("This is constant_term:", constant_term)

    for index, row in constants.df.iterrows():
    # Access the value of each column using the column name
        n = int(row['n'])
        m = int(row['m'])
        Cnm = float(row['Cnm'])
        Snm = float(row['Snm'])
        q = Snm
    #The numbers in the dataframe are strings and not numbers, and so these have to be converted into ints or floats.
    #But because of the "d's" in the first row, they couldn't be converted and so it had to be replaced with an "e".
        
        aRn = (constants.a/R)**n

        long_term = (r_nm.r_nm(Cnm, n, m) * np.cos(m * longitude_radians) + q * np.sin(m * longitude_radians)) * pN.pN_main(n, m, latitude_radians)
        #print("n=", n, "and m=", m, "give long term=", long_term)
        #sumsjekk += long_term
        #print("Long term: ", long_term)
        #print("P: ", pN.pN_main(n, m, latitude_radians))
        #print("This is RM:", r_nm.r_nm(Cnm, n, m), "when m =",m)
        total = long_term * aRn
        #print("This is total:", total)
        sum = sum + total    

    geoidUndulation = constant_term * sum
    #print("The point with latitude:", latitude, " and longitude:", longitude, " has N = ", geoidUndulation)
    return geoidUndulation                                 

#geoidalHeight(20,20, constants.r)