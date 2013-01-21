"""
Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math
import re

isPrime = lambda n: re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None

def primes(x):
    for i in range(x+1):
        if isPrime(i):
            yield i

def lowest_prime_factor(n):
    rN = int(math.sqrt(n))
    for x in primes(rN):        
        if n % x == 0:
            return x
    return n
    
N = 600851475143
while N != 1:
    f = lowest_prime_factor(N)
    print f
    N = N/f
