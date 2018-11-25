import numpy as np

def get_r(K, L, alpha, Z, delta):
    '''
    This funciton generates the interest rates
    '''

    r = alpha * Z * (L / K) ** (1 - alpha) - delta
    return r
