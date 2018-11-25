
def smallest_factor(n):
    """Return prime factor of the positive integer n"""
    
    if isinstance(n, int):
        if n > 0:
            if n == 1:
                return 1
            #original incorrect code:
            #for i in range(2, int(n ** .5)):
            #error is because the loop does not iterate over the value int(n ** .5)
            #because the upper bound given in the range function is not inclusive
            #corrected code:
            for i in range(2, int(n ** .5) + 1):
                if n % i == 0:
                    return i
            return n
    return None
