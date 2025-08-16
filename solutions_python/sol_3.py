import random
import math

def rho(n):    
    x = (random.randint(0, 2) % (n - 2))
    y = x
    c = (random.randint(0, 1) % (n - 1))
    d = 1
    while d == 1:
        x = (pow(x, 2, n) + c + n) % n
        y = (pow(y, 2, n) + c + n) % n
        y = (pow(y, 2, n) + c + n) % n
        d = math.gcd(abs(x-y), n)
        if d == n:
            return rho(n)
    return d

def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    r = int(num**0.5) + 1
    for i in range(3, r, 2):
        if num % i == 0:
            return False
    return True

def main(n):
    if is_prime(n):
        return n
    f = rho(n)
    return max(main(f), main( n // f))

print(main(600851475143))
