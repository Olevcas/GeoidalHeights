import numpy as np
import sys
sys.path.append('./Part_1_1/')
import jN

def r_nm(c,n,m):
    
    if(m == 0):
        return c - jN.jN(n)
    
    else:
        return c

