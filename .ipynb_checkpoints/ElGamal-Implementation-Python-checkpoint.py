# Tahim Bhuiya 
# Elgamal Implementation
import random  # For generating random numbers
from sympy import primerange  # For generating a range of prime numbers


# Greatest Common Divisor (GCD) using Euclidean algorithm
def gcd(a, b):
    if a < b:
        return gcd(b, a)  # Ensure the larger number is first
    elif a % b == 0:
        return b  # Base case: b is the GCD
    else:
        return gcd(b, a % b)  # Recursive case


# Modular Exponentiation Function (Square-and-Multiply Algorithm)
def power(a, b, c):
    result = 1  # Initialize result
    base = a % c  # Take modulo to simplify base

    while b > 0:
        if b % 2 == 1:
            result = (result * base) % c  # Multiply result by base if b is odd
        base = (base * base) % c  # Square the base
        b //= 2  # Divide exponent by 2

    return result  # Return the final result


# Generate a large prime number using the Fermat Primality Test
def generate_prime_fermat(bits):
    while True:
        p = random.getrandbits(bits)  # Generate a random number with the specified bit length
        if p % 2 != 0 and pow(2, p - 1, p) == 1:  # Check if p is odd and passes Fermat’s test
            if p.bit_length() != bits:  # Ensure p has the exact bit length
                continue
            return p  # Return the prime number


# Generate a large prime number using the Miller-Rabin Primality Test (basic form)
def generate_prime_miller_rabin(bits):
    while True:
        p = random.getrandbits(bits)  # Generate a random number with the specified bit length
        if p % 2 != 0 and all(pow(a, p - 1, p) == 1 for a in random.sample(range(2, min(p, 2048)), min(p - 2, 5))):
            # Check if p is odd and passes Fermat-based Miller-Rabin test with multiple random bases
            return p  # Return the probable prime number


# Generate Generator for Finite Field
def find_generator(p):
    for g in range(2, p):
        # Check that g is not a quadratic or cubic residue modulo p
        if pow(g, (p - 1) // 2, p) != 1 and pow(g, (p - 1) // 3, p) != 1:
            return g  # Return g as a generator


# Asymmetric Key Generation
def generate_keys(bits):
    q = generate_prime_fermat(bits)  # Generate a large prime number
    g = find_generator(q)  # Find a generator for the finite field
    min_private_key = 2 ** (bits // 2)  # Minimum value for the private key
    max_private_key = q - 1  # Maximum value for the private key
    private_key = random.randint(min_private_key, max_private_key)  # Generate the private key
    public_key = power(g, private_key, q)  # Compute the corresponding public key
    return q, g, private_key, public_key  # Return all key components



# Asymmetric Encryption
def encrypt(msg, q, g, public_key):
    k = random.randint(2, q - 1)
    s = power(public_key, k, q)
    ciphertext = [(power(g, k, q), (ord(char) * s) % q) for char in msg]
    return ciphertext

# Asymmetric Decryption
def decrypt(ciphertext, q, private_key):
    h = power(ciphertext[0][0], private_key, q)
    plaintext = ''.join([chr((char * pow(h, -1, q)) % q) for _, char in ciphertext])
    return plaintext


# Main Function
def main():
    while True:
        try:
            key_size = int(input("Enter the key size in bits (preferably 16,32,64,128,256): ")) 
            if key_size <= 0:
                print("Please enter a positive integer for the key size.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the key size.")

    # Generate Keys
    q, g, private_key, public_key = generate_keys(key_size)  
    print("\nPrime Number (q):", q) 
    print("\nPublic Key:", public_key) 
    print("\nPrivate Key:", private_key)  
   
    plaintext = input("\nEnter the plaintext: ") 
   
    ciphertext = encrypt(plaintext, q, g, public_key) 
    print("\nCiphertext:", ciphertext)  
   
    decrypted_plaintext = decrypt(ciphertext, q, private_key)  
    print("\nDecrypted Plaintext:", decrypted_plaintext)  

if __name__ == '__main__':
    main()  





