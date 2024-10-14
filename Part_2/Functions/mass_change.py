import sys
import numpy as np
import os
current_dir = os.path.dirname(__file__)
part_1_1_path = os.path.join(current_dir, '../../Part_1_1')
sys.path.append(part_1_1_path)
part_2_path = os.path.join(current_dir, '../')
sys.path.append(part_2_path)
#sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/Part_2/')
#sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/Part_1_1/')
from Functions import pN
from Constants import constants2


#This function will be used to test the values estimated values for the R_nm and q_nm

def mass_change(latitude, longitude, harmonics):
    
    constant_term = (constants2.a * constants2.rho_avg) / 3
    latitude_radians = latitude * (np.pi/180)
    longitude_radians = longitude * (np.pi/180)
    #Initialize the sum of all terms to be 0
    sum = 0

    for index, row in harmonics.iterrows():
        n = int(row['n'])
        m = int(row['m'])
        Rnm = float(row['Rnm'])
        qnm = float(row['qnm'])
        k_n = constants2.k_n[n]

        long_term = (2 * n + 1) / (1 + k_n) * (Rnm * np.cos(m * longitude_radians) + qnm * np.sin(m * longitude_radians)) * pN.pN_main(n, m, latitude_radians)

        sum = sum + long_term
    
    total_mass_change = sum * constant_term

    return total_mass_change