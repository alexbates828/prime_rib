from math import ceil, sqrt

def is_prime(n: int) -> bool:
    if type(n)==float:
        raise TypeError("Input parameter n should be of type 'int'.")
    if n<0:
        return is_prime(-n)
    if n in [0, 1]:
        return False
    sqrtn = ceil(sqrt(n))
    for i in range(2, sqrtn+1, 2):
        if n%i == 0:
            return False
    return True
