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