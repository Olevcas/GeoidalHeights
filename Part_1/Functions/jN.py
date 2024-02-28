import numpy as np
import constants

def jN(n):

    if n % 2 == 1:
        return 0
    
    else:
        return (-1**(n/2) * ((3*np.e**n*(1-n/2+(5/2)*(constants.j2n/np.e**2)*n))/((n+1)*(n+3)*np.sqrt(2*n+1))))
    
