from functools import lru_cache
import numpy as np
import constants2
import pandas as pd
from tqdm import tqdm
import numba


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


'''
Function to calculate r and q for a n-m pair
'''


@lru_cache(None)
def calculateStokesCoefficients(n, m, dlat, dlon, dataset_values):
    """
    Memoized version of calculateStokesCoefficients.
    `dataset_values` is a list of tuples instead of a DataFrame for memoization.
    """
    rho_w = constants2.rho_water
    rho_avg = constants2.rho_avg
    k_n = constants2.k_n[n]
    a = constants2.a
    
    constant_term = (1/(4*np.pi)) * ((1 + k_n) / (2 * n + 1)) * ((3 * rho_w) / (a * rho_avg))
    sum_r = 0
    sum_q = 0
    
    for row in dataset_values:
        latitude = float(row[1])  # Assuming row[1] is latitude
        longitude = float(row[0])  # Assuming row[0] is longitude
        value = float(row[2])      # Assuming row[2] is the relevant value (e.g., mass)

        da = np.cos(np.deg2rad(latitude)) * dlat * dlon
        long_term_r = (value / rho_w) * np.cos(m * np.deg2rad(longitude)) * da   
        long_term_q = (value / rho_w) * np.sin(m * np.deg2rad(longitude)) * da
        
        sum_r += long_term_r
        sum_q += long_term_q

    r = constant_term * sum_r
    q = constant_term * sum_q
    
    return r, q

def createGravityModel(nmax, dlat, dlon, dataset):
    """
    Creates the gravity model. The dataset rows are converted to tuples for memoization.
    """
    # Convert dataset rows into a list of tuples for hashing
    dataset_values = [tuple(row) for _, row in dataset.iterrows()]
    
    df = pd.DataFrame(columns=['n', 'm', 'r', 'q'])
    
    for n in tqdm(range(nmax + 1), leave=True, colour='green'):
        for m in range(n + 1):
            # Memoized function call
            r, q = calculateStokesCoefficients(n, m, dlat, dlon, tuple(dataset_values))
            df_temp = pd.DataFrame({'n': [n], 'm': [m], 'r': [r], 'q': [q]})
            df = pd.concat([df, df_temp], ignore_index=True)
    
    # Saving the result based on dataset name
    if 'ECCO' in dataset.name:       
        df.to_csv(f'Part_2/Data/Results/ECCO/{dataset.name}.txt', index=False)
    elif 'GLDAS' in dataset.name:
        df.to_csv(f'Part_2/Data/Results/GLDAS/{dataset.name}.txt', index=False)


colspecs_ECCO = [(1, 6), (7, 12), (15, 20)]

ecco_2005 = pd.read_fwf('Part_2/Data/ECCO/2005.txt', skiprows = 14, colspecs = colspecs_ECCO, header = None)
ecco_2005.name = '2005_ECCO_r_q'

createGravityModel(constants2.n_max, 0.5, 0.5, ecco_2005)



