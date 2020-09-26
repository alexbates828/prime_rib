from math import ceil, sqrt, gcd

def is_prime(n: int) -> bool:
    if type(n)==float:
        raise TypeError("Input parameter n should be of type 'int'.")
    if n<0:
        return is_prime(-n)
    if n in [0, 1]:
        return False
    sqrtn = ceil(sqrt(n))
    for i in range(3, sqrtn+1, 2):
        if n%i == 0:
            return False
    return True

def range_by_with_mod(n: int, b: int):
    if n==0:
        pass
    if n==1:
        yield 0
        pass
    if n < 0 or b <= 0:
        raise ValueError("Both arguments must be greater than zero!")
    if b > n:
        return range_by_with_mod(n, b%n)
    assert gcd(n,b)==1, f"The greatest common divisor of n and b must be 1."

    iters = 0
    r = 0
    while True:
        yield r
        r = (r + b)%n
        if r==0:
            break
        iters+=1
        if iters > n:
            raise RuntimeException(f"While loop should not execute more than input {n} number of times! Infinite loop prevented.")
    pass

def is_prime_with_range_by_with_mod(n: int, b: int = None) -> bool:
    # "good" choices of b are much larger than 1 and much smaller than n-1
    if type(n)==float:
        raise TypeError("Input parameter n should be of type 'int'.")
    if n<0:
        return is_prime_with_range_by_with_mod(-n)
    if n in [0, 1]:
        return False
    if n==2:
        return True
    sqrtn = ceil(sqrt(n))
    b = b or sqrtn
    try:
        for i in range_by_with_mod(n, b):
            if i>sqrtn or i<=1:
                continue
            if n%i == 0:
                return False
    except AssertionError:
        return False
    return True
