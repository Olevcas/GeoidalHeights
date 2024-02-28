import numpy as np
import jN

def r_nm(c,n,m):
    
    if(m == 0):
        return c - jN(n)
    
    else:
        return c