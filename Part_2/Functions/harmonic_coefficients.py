import sys
import os
current_dir = os.path.dirname(__file__)
part_1_1_path = os.path.join(current_dir, '../../Part_1_1')
sys.path.append(part_1_1_path)
part_2_path = os.path.join(current_dir, '../')
sys.path.append(part_2_path)
import numpy as np
import pandas as pd
#sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/Part_2/')
#sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/Part_1_1/')
from Functions import pN
from Constants import constants2
import time

start_time = time.time()

df_harmonic_coefficients = pd.DataFrame(columns=['n', 'm', 'Rnm','qnm'])

#This calculates the harmonics R_nm and q_nm for one pair of n and m
def calculate_harmonics(n, m, dataset):

    constant_term = (1 / (4*np.pi)) * ((1 + constants2.k_n[n]) / (2*n + 1)) * ((3*constants2.rho_water) / (constants2.a * constants2.rho_avg))
    sum_Rnm = 0
    sum_qnm = 0

    for index, row in dataset.iterrows():
    # Access the value of each column using the column name
        longitude = float(row['longitude'])
        latitude = float(row['latitude'])
        latitude_radians = latitude * (np.pi/180)
        longitude_radians = longitude * (np.pi/180)
        total_water = float(row['total_water'])

        rnm_term = total_water * np.cos(m * longitude) * pN.pN_main(n, m, latitude_radians)
        qnm_term = total_water * np.sin(m * longitude) * pN.pN_main(n, m, latitude_radians)

        sum_Rnm = sum_Rnm + rnm_term
        sum_qnm = sum_qnm + qnm_term

    rnm = constant_term * rnm_term
    qnm = constant_term * qnm_term

    print("Her kommer Rnm: ", rnm)
    print("Her kommer qnm: ", qnm)

    return rnm, qnm 

calculate_harmonics(3,3,constants2.df_GLDAS_2005)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")







