import numpy as np
import sys
sys.path.append('/Users/oleevjen-caspersen/Desktop/4.klasse/Programmering_i_geomatikk/Part_1/')
from Constants import constants


def jN(n):

    e = np.sqrt(constants.e2)

    if n % 2 == 1:
        return 0
    
    else:
        return (((-1)**(n/2)) * ((3*e**n*(1-n/2+(5/2)*(constants.j2n/(e**2))*n))/((n+1)*(n+3)*np.sqrt(2*n+1))))
    
