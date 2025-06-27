# Tahim Bhuiya 
# Elgamal Implementation
import random  
from sympy import primerange  

# Greatest Common Divisor (gcd) Function
def gcd(a, b):
    if a < b:
        return gcd(b, a)  
    elif a % b == 0:
        return b  
    else:
        return gcd(b, a % b)  

# Modular Exponentiation Function (Square-and-Multiply Algorithm)
def power(a, b, c):
    result = 1  
    base = a % c  

    while b > 0:
        if b % 2 == 1:
            result = (result * base) % c  
        base = (base * base) % c  
        b //= 2  

    return result  

# Generate Large Prime Number using Fermat Primality Test
def generate_prime_fermat(bits):
    while True:
        p = random.getrandbits(bits)
        if p % 2 != 0 and pow(2, p - 1, p) == 1:
            if p.bit_length() != bits:
                continue
            return p

# Generate Large Prime Number using Miller-Rabin Primality Test
def generate_prime_miller_rabin(bits):
    while True:
        p = random.getrandbits(bits)
        if p % 2 != 0 and all(pow(a, p - 1, p) == 1 for a in random.sample(range(2, min(p, 2048)), min(p - 2, 5))):
            return p

