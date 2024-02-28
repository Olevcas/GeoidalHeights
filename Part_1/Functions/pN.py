import numpy as np

def pN1(t, n, pn1, pn2):
    return ((-(np.sqrt(2*n+1))/n)*((n-1)/(np.sqrt(2*n-3)))*pn2 + t * ((np.sqrt(2*n+1))/(n))*np.sqrt(2*n-1)*pn1)

def pN2(t, n, m, pn1, pn2):
    return (-np.sqrt(((2*n+1)*(n+m-1)*(n-m-1))/((2*n-3)*(n+m)*(n-m)))*pn2 + t*np.sqrt(((2*n+1)*(2*n-1))/((n+m)*(n-m)))*pn1)

def pN3(t, n, pn1):
    return (t*np.sqrt(2*n+1)*pn1)

def pN4(t, n, pn1):
    return (np.sqrt((2*n+1)/(2*n))*np.sqrt(1-t**2)*pn1)


def pN_main(n, m, latitude):
   
    t = np.sin(latitude)

    if(n == 0 and m == 0):
        return (1)
    elif(n == 1 and m == 0):
        return (t * np.sqrt(3))
    elif(n == 2 and m == 0):
        return (np.sqrt(5)*((1.5*t**2)-(1/2)))
    elif(n == 1 and m == 1):
        return (np.sqrt(3) * np.sqrt(1-t**2))
    elif(n == 2 and m == 1):
        return (t * np.sqrt(15)*np.sqrt(1-t**2))
    
    elif(n >= 2 and m == 0):
        return pN1(t, n, pN_main(n-1, 0, latitude),pN_main(n-2, 0, latitude))
    
    elif(n >= 1 and m == (n-1)):
        return pN3(t, n, pN_main(n-1,n-1, latitude))
    
    elif(n >= 2 and m == n):
        return pN4(t, n, pN_main(n-1, n-1, latitude))
    else:
        return pN2(t, n, m, pN_main(n-1,m, latitude),pN_main(n-2, m, latitude))
    



