
🔐 ElGamal Encryption and Decryption in Python  
By Tahim Bhuiya  

This is a Python implementation of the **ElGamal public-key cryptosystem**, which encrypts and decrypts text using asymmetric cryptography based on modular arithmetic and discrete logarithms.

---

📜 Overview  
ElGamal is an asymmetric-key encryption algorithm used for secure data exchange. This project simulates ElGamal by:

- Generating a large prime number `q`  
- Finding a generator `g` for the finite field  
- Generating a private key and computing the corresponding public key  
- Performing asymmetric encryption using a random session key  
- Decrypting ciphertext using modular inverse and private key  

---

▶️ Usage  

Run the Python program:  
```bash
python elgamal.py
```

Then:  
- Enter the key size in bits (e.g., 16, 32, 64, 128, 256)  
- Enter the plaintext message to encrypt  

The program will output:  
- The generated prime number `q`  
- Public and private keys  
- Encrypted ciphertext as a list of integer pairs  
- Decrypted plaintext  

This program requires only Python and the `sympy` library. It runs in:  
- Any Python-compatible IDE  
- VS Code, PyCharm  
- Replit or Terminal with Python 3  

---

🧠 Code Description  

| Function              | Purpose                                                                 |
|-----------------------|-------------------------------------------------------------------------|
| `gcd(a, b)`           | Computes the greatest common divisor using Euclidean algorithm          |
| `power(a, b, c)`      | Efficient modular exponentiation (square-and-multiply)                  |
| `generate_prime_fermat(bits)` | Generates a prime number using Fermat primality test             |
| `generate_prime_miller_rabin(bits)` | Optional Miller-Rabin test-based prime generator          |
| `find_generator(p)`   | Finds a suitable generator `g` for prime `p`                            |
| `generate_keys(bits)` | Generates `(q, g, private_key, public_key)`                            |
| `encrypt(msg, q, g, public_key)` | Encrypts a plaintext message into a list of cipher tuples     |
| `decrypt(ciphertext, q, private_key)` | Decrypts ciphertext using modular inverse              |

---

🔐 Key Concepts  

| Concept       | Description                                                                      |
|----------------|----------------------------------------------------------------------------------|
| Prime `q`      | Large prime number used as the modulus                                          |
| Generator `g`  | Primitive root modulo `q`                                                       |
| Private Key    | Randomly chosen secret number                                                  |
| Public Key     | Computed from generator and private key                                        |
| Session Key    | Random key generated per encryption session                                    |
| Shared Secret  | Used to securely mask plaintext values                                         |

---

🧪 Example Output  
```
Enter the key size in bits (preferably 16,32,64,128,256): 32

Prime Number (q): 4294967311

Public Key: 998341234

Private Key: 34829281

Enter the plaintext: hello

Ciphertext: [(234151, 13251234), (634232, 7654321), ...]

Decrypted Plaintext: hello
```

---

📦 Requirements  
- Python 3.x  
- `sympy` library  
  Install with:  
  ```bash
  pip install sympy
  ```

---

✅ Notes  
- The plaintext can be any UTF-8 string.  
- Keys and ciphertexts are generated fresh on each run.  
- The implementation uses `ord()` and `chr()` to encode/decode individual characters.  
- Prime generation is randomized, so results vary every time.

---

📣 Credits  
Developed by **Tahim Bhuiya**  

🎉 Enjoy!
