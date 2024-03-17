## Cryptographic Systems Security Basics
This repo is created solely for the purpose of studying basic cryptography. The code is mostly implemented from scratch for the purpose of understanding the fundamentals of cryptographic primitives and does not follow any official cryptographic standards. If you spot anything off or incorrect in this repo, I'd really appreciate if you could open an issue or drop me a message.

## Contents
- [Cryptographic Systems Security Basics](#cryptographic-systems-security-basics)
- [Contents](#contents)
- [Fundamental Math used in Cryptography](#fundamental-math-used-in-cryptography)
  - [1. Prime numbers](#1-prime-numbers)
  - [2. Modular Arithmetic](#2-modular-arithmetic)
  - [3. Euclidean/Extended Euclidean Algorithm](#3-euclideanextended-euclidean-algorithm)
  - [4. Modular Inverse (aka Multiplicative inverse)](#4-modular-inverse-aka-multiplicative-inverse)
  - [5. Integer Factoring Problem](#5-integer-factoring-problem)
  - [6. Discrete Logarithm Problem (DLP)](#6-discrete-logarithm-problem-dlp)
- [Classical Cryptography](#classical-cryptography)
  - [1. Caesar Cipher](#1-caesar-cipher)
  - [2. Vigenere Cipher](#2-vigenere-cipher)
  - [3. Affine Cipher](#3-affine-cipher)
- [Modern Cryptography](#modern-cryptography)
  - [1. RSA](#1-rsa)
  - [2. Deffi-Hellman Key Exchange protocol](#2-deffi-hellman-key-exchange-protocol)
  - [3. ElGamal](#3-elgamal)
  - [4. SHA256](#4-sha256)
  - [5. DSA](#5-dsa)
  - [6. Shamir's Secret Sharing](#6-shamirs-secret-sharing)
  - [7. Homomorphic Encryption](#7-homomorphic-encryption)
## Fundamental Math used in Cryptography


### 1. Prime numbers
- **Fundamental theorem of arithmetic** states that every integer greater than 1 is either a prime number itself or it can be factorized into prime numbers.
- Tests for primality
  - Deterministic tests: AKS Primality Test, Elliptic Curve Primality Proving (ECPP), Miller-Rabin Test-Deterministic, etc.
  - Probabalistic tests: Miller-Rabin Test-Probabilistic, Fermat Primality Test, etc
- Deterministic tests consume more computational power as the numbers get large, this is why probabilic tests are used to mitigate this issue. However in practical applications, both deterministic and probabilistic tests are used in conjunction. Typically, multiple rounds of probabilistic tests are done initially to filter out composite numbers and the final verification (in critical applications) is done with a deterministic test.
- The probabilistic version of the **Miller–Rabin** test for large prime numbers is implemented [here](https://github.com/0xkzam/cryptography/blob/876fc080ed0e2bfc0c8f9f7e3c7804b077684d64/util/math.py#L144).
  - Reference: [link](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Miller%E2%80%93Rabin_test)



### 2. Modular Arithmetic
- a, b and n are positive integers. If the remainders of a and b when divided by n are equal, then the integers a and b are congruent. It’s denoted as follows,
  - a ≡ b (mod n)
- Properties
  - Addition
    - If a ≡ b (mod n) and c ≡ d (mod n), then **a + c ≡ b + d (mod n)**	
    - If a ≡ b (mod n), then **a + k ≡ b + k (mod n)** for any integer k
    - If a + b = c, then **a (mod n) + b (mod n) ≡ c (mod n)**
  - Multiplication 
    - If a.b = c, then **a (mod n) . b (mod n) ≡ c (mod n)**
    - If a ≡ b (mod n), then **ka  ≡ kb (mod n)** any integer k
    - If a ≡ b (mod n) and c ≡ d (mod n), then **a * c ≡ b * d (mod n)**
  - Exponentiation
    - If a ≡ b (mod n), then **a<sup>k</sup> ≡ b<sup>k</sup> (mod n)** for any positive integer k


### 3. Euclidean/Extended Euclidean Algorithm 
- Euclidean algorithm is used to find the greatest common divisor of two integers **a** and **b**, typically denoted by **gcd(a,b)** 
  - Basic impl: [gcd](https://github.com/0xkzam/cryptography/blob/876fc080ed0e2bfc0c8f9f7e3c7804b077684d64/util/math.py#L5)
- Extended Euclidean algorithm is used find the **gcd(a, b)** and two integers **x** and **y** such that **ax + by = gcd(a,b)**
  - Basic impl: [extended_gcd](https://github.com/0xkzam/cryptography/blob/876fc080ed0e2bfc0c8f9f7e3c7804b077684d64/util/math.py#L43)


### 4. Modular Inverse (aka Multiplicative inverse)
  - Extended Euclidean algorithm is commonly used to find modular inverse.
  - Mod inverse of **a** is defined as an integer **x** such that **x ≡ a<sup>-1</sup> (mod n)**
    - For x to exist, **a** and **n** must be coprime i.e., **gcd(a, n) = 1**
    - Using Ext. Euclidean we can write **ax + ny = gcd(a, n)** and compute x, y when gcd(a,n) = 1 where x is the mod inverse of a.
  - Mod inverse is used in [RSA](#rsa) to calculate private key exponent.
  - Basic impl: [mod_inverse](https://github.com/0xkzam/cryptography/blob/876fc080ed0e2bfc0c8f9f7e3c7804b077684d64/util/math.py#L87)
  - Note: **Fermat's Little Theorem** can also be used to find mod inverse. The only catch is that, to use this theorem the **p** in **x ≡ a<sup>-1</sup> (mod p)** is required to be a prime.
    - The theorem: if **p** is a prime number and **a** is not divisible by **p**, then **x ≡ a<sup>−1</sup> ≡ a<sup>p−2</sup> (mod p)**



### 5. Integer Factoring Problem
- This is a fundamental problem in Number theory.
- The problem is, given the product of 2 or more prime numbers, find its prime factors.
- The problem is defined as follows:
  - Given a composite number N, find two prime numbers p, q such that N = p * q
- While factorization for small values of N can be done relatively easily, as the numbers p and q get larger, no efficient non-quantum integer factorization algorithm exists to solve this. If the primes are large enough, it is considered computationally infeasible to solve with the current technology.
- Integer Factoring is the basis for [RSA](#rsa), which is the first public key cryptography based system.  
  - Private key consists of prime factors p and q. (along with a decryption exponent e)
  - Public key consists of N which is the product of p and q. (along with an encryption exponent d)

### 6. Discrete Logarithm Problem (DLP)
- This is also an important fundamental problem in Number Theory which has significat implications in cryptography.
- Definitions:
  - **p** = a large prime number
  - **G** = finite cyclic group (multiplicative group)
  - **g** = generator for G and a primitive root prime **p**
    - A primitive root of a prime number **p** is a number **g** in the range **1 ≤ g < p** such that the set of numbers of **g<sup>k</sup> (mod p)** as k ranges from 1 to  p-1, must exactly be the set of numbers from 1 to p-1 .
    - E.g., g =2 and p =13
      - 2<sup>k</sup> (mod 13) = {2, 4, 8, 3, 6, 12, 11, 9, 5, 10, 7, 1} for k = 1, 2,…,12   
      - In this case, 2<sup>k</sup> (mod 13) generates all the integers from 1 to 12, hence g=2 is a primitive root of p=13
- The problem is defined as follows:
    - Find an integer **x** such that **g<sup>x</sup> ≡ h (mod p)** given **g**, **h** and **p** where **p** is a large prime and **g** is a primitive root of **p** (i.e. 1 <= g < p)
- DLP is the basis for [Deffi-Hellman Key Exchange](#deffi-hellman-key-exchange-protocol) and [ElGamal](#elgamal). 



## Classical Cryptography


### 1. Caesar Cipher
- The standard Caesar Cipher is only used to encrypt alpha characters and other characters are ignored.
- Each character in the plain text is shifted by a constant (Standard shift = 3).
- `m` = size of the alphabet (m = 26 for English letters)
- <code>Encrypt(p<sub>1</sub>, p<sub>2</sub>… p<sub>m</sub>) = (p<sub>1</sub>+3, p<sub>2</sub>+3… p<sub>m</sub>+3) (mod m)</code>
- <code>Decrypt(c<sub>1</sub>, c<sub>2</sub>… c<sub>m</sub>) = (c<sub>1</sub>-3, c<sub>2</sub>-3… c<sub>m</sub>-3) (mod m)</code>
- Implementation: [Caesar.py](https://github.com/0xkzam/cryptography/blob/main/classical/Caesar.py)


### 2. Vigenere Cipher
- The standard Vigenere Cipher is only used to encrypt alpha characters and other characters are ignored.
- Uses a series of different Caesar Ciphers according to the key.
- Has a key K = (k<sub>1</sub>, k<sub>2</sub>... k<sub>y</sub>) that contains only alpha characters.
- If the message length `y` > key length, the key is extended to match the length of the message.
    - Eg: if K = ‘KEY’ and the message = ‘HELLO’ then the extended key = ‘KEYKE’
- `m` = size of the alphabet (m = 26 for English letters)
- <code>Encrypt(p<sub>1</sub>, p<sub>2</sub>… p<sub>y</sub>) = (p<sub>1</sub>+k<sub>1</sub>, p<sub>2</sub>+k<sub>2</sub>… p<sub>m</sub>+k<sub>y</sub>) (mod m)</code>
- <code>Decrypt(c<sub>1</sub>, c<sub>2</sub>… c<sub>y</sub>) = (c<sub>1</sub>-k<sub>1</sub>, c<sub>2</sub>-k<sub>2</sub>… c<sub>m</sub>-k<sub>y</sub>) (mod m)</code>
- Implementation: [Vigenere.py](https://github.com/0xkzam/cryptography/blob/main/classical/Vigenere.py)


### 3. Affine Cipher
- `m` = size of the alphabet (m = 26 for English letters)
- Key = (a,b) 
    - Choose `a` such that `m` and `a` are coprime (ie. greatest common divisor = 1)
    - `b` = any postive integer
- For each character of the plain text, convert to its numeric equivalent `x` 
    - Create a mapping for each letter of the alphabet to a corresponding number
- `Encrypt(p) = ax+b mod m`
    - For each character, compute `(ax+b) mod m` and convert the result back to a letter
- <code>Decrypt(c) = a<sup>-1</sup>(c-b) mod m</code>
    - Find <code>a<sup>-1</sup> mod n</code> using Extended Euclidean Algorithm 
- Implementation: [Affine.py](https://github.com/0xkzam/cryptography/blob/main/classical/Affine.py)


## Modern Cryptography


### 1. RSA

- RSA (Ron Rivest, Adi Shamir, Leonard Adleman. 1978) is based on the Integer Factoring Problem using the product of 2 
large primes. In theory large scale quantum computing could potentially break RSA encryption using Shor’s algorithm.

- Key Generation
  - `n = p*q` (p and q are 2 large prime numbers)
  - Calculate the totient `φ(n) = (p-1)*(q-1) `
    - This is called Euler’s Totient function
  - Choose e such that it fulls the following 2 conditions 
    - `1 ≤ e < (p-1)(q-1)`
    - `gcd(e, φ(n)) = 1`
  - Compute d which is the multiplicative inverse of e mod φ(n)
    - Use extended Euclidean
    - <code>(d*e) mod φ(n) = 1</code>  thus <code>d = e<sup>-1</sup> mod φ(n)</code> 
  - Public key = `(n , e)`
  - Private key = `(n , d)`

- Encryption
  - Convert the message M into an integer `m`
    - In practice, messages are converted into byte representations and broken down to smaller blocks.
  - Then <code> c = m<sup>e</sup> (mod n)</code> 

- Decryption
  - <code> m = c<sup>d</sup> (mod n)</code> 
  - Then convert `m` back to M

- Basic implementation: [RSA.py](https://github.com/0xkzam/cryptography/blob/main/modern/RSA.py)


### 2. Deffi-Hellman Key Exchange protocol

- This protocol is a way of sharing a common secret key among 2 parties typically over an insecure channel.
- Key Generation
  - Choose 
    - `p` -> a prime number
    - `g` -> a primitive root (generator) 
    - `a` -> A's private key (a random number)
    - `b` -> B's private key (a random number)
  - Then A's public key, <code>A = g<sup>a</sup> mod p</code>
  - And B's public key, <code>B = g<sup>b</sup> mod p</code>
  - Compute shared secret key
    - A computes -> <code>k<sub>A</sub> = B<sup>a</sup> mod p</code>
    - B computes -> <code>k<sub>B</sub> = A<sup>b</sup> mod p</code>
    - Both <code>k<sub>A</sub> and k<sub>B</sub></code> should be equal.
- Basic implementation: [DeffiHellman.py](https://github.com/0xkzam/cryptography/blob/main/modern/DeffiHellman.py) 



### 3. ElGamal

- Taher Elgamal, 1985	
- Based on Diffie-Hellman key exchange (Discrete Logarithm Problem).
- DSA is a variant of ElGamal signature scheme
- Typically used to encrypt a symmetric key that is then used to encrypt the actual message.
- ElGamal is said to be resistant to quantum attacks

- Key Generation
  - Choose
    - `p` -> a large prime 
    - `g` -> a primitive root of p
    - `x` -> a secret key, such that `1 < x < p-1`
  - Calculate <code>h = g<sup>x</sup>(mod p)</code>
  - Public key = `(p, g, h)`
  - Private key = `x`
- Encryption
  - Choose a random number `k` such that `1 < k < p-1`
  - Calculate <code>c<sub>1</sub> = g<sup>k</sup> mod p</code>
  - Calculate <code>c<sub>2</sub> = (m * h<sup>k</sup>) mod p</code>
    - `m` = numerical representation of message M
  - `C = (c1, c2)`    
- Decryption
  - Calculate <code>s = c<sub>1</sub><sup>x</sup> mod p</code> where `x` is the private key
  - Then calculate <code>m = (c<sub>2</sub> * s<sup>-1</sup>) mod p</code>
- Basic implementation: [ElGamal.py](https://github.com/0xkzam/cryptography/blob/main/modern/ElGamal.py)



### 4. SHA256
- Follows the Merkel-Damgard paradigm, which is used in the MD5, SHA-1 and SHA-2 family.
- Takes an arbitrary length input, breaks it up into blocks of 512 bits, processes each block, and finally outputs a 256 bit value.

  - Message M is divided into blocks of 512 bits ( M<sub>1</sub>, M<sub>2</sub>,..., M<sub>n</sub>)
    - If the last block is less than 512 bits it’s padded by adding a ‘1’ bit followed by 0s. 
  - Generate the initial hash value, H<sub>0</sub>
    - Derived from the fractional parts of the square roots of the first 8 prime numbers (2, 3, 5, 7, 11, 13, 17, 19), which results in 8 x 32 bit words, ie. 256 bit value
  - Each message block is passed to the compression function, which takes 2 inputs
    - Hash of the previous message block, H<sub>k-1</sub>
    - Current message block, M<sub>k</sub>
  - For each M<sub>k</sub> the compression function runs 64 rounds, conducting a series of operations (ie. bitwise operations, addition of cube roots of the first 64 primes, addition modulo 2<sup>32</sup>, etc.) before producing the next state H<sub>k</sub>
    - H = H<sub>0</sub>
    - for each M<sub>k</sub> → H<sub>k</sub> = compress(H<sub>k-1</sub>, M<sub>k</sub>)



### 5. DSA
- Standard DSA is based on ElGamal.

- Key Generation
  - Choose 
    - A large prime `q`
    - A prime `p` such that (p-1) is divisible by q (i.e. p = kq + 1 for some integer k)
    - A primitive root `g` (mod p)
    - The secret (i.e. private key), `z` such that 1 < z < q
  - Calculate <code>⍺ = g<sup>(p-1)/q</sup> (mod p)</code>
  - Calculate <code>𝝱 = ⍺<sup>z</sup> (mod p)</code>
  - Thus, the public key = (p, q, ⍺, 𝝱)

- Signing Protocol
  - Choose a random number `k` such that 1 < k < q
  - Calculate <code>r =  (⍺<sup>k</sup> mod p) (mod q)</code>
  - Calculate <code>s = k<sup>-1</sup> (x + zr) (mod q) </code>
    - x = message hash
  - Thus, the signature = (r, s)

- Signature Verification
  - Calculate
    - <code>u1 = s<sup>-1</sup>x mod q</code>
    - <code>u2 = s<sup>-1</sup>r mod q</code>
    - <code>v = (⍺<sup>u1</sup>𝝱<sup>u2</sup> mod p) mod q</code>
- Then the signature is verified if v = r
- Basic implementation: [DSA.py](https://github.com/0xkzam/cryptography/blob/main/modern/DSA.py)



### 6. Shamir's Secret Sharing 
Sharmir's Secret Sharing (SSS) is a method of splitting a secret into multiple pieces such that the secret can only be reconstructed when a sufficient number of pieces are combined. 
The main principle behind SSS is the use of polynomial interpolation. We can find a polynomial with a degree `k-1` where `k` is the minimum number of pieces required to reconstruct the secret and `n` is the total number of pieces the secret is split into.

- Let the secret be `D`
- Let number of splits be `n`
- Choose k such that `n/2 < k ≤ n`
- The polynomial <code>f(x) = a<sub>0</sub> + a<sub>1</sub>x + a<sub>2</sub>x<sup>2</sup> +... + a<sub>k-1</sub> x<sup>k-1</sup></code>
  - Here, <code>a<sub>0</sub> = D</code>
  - Choose coefficients a<sub>1</sub>, a<sub>2</sub>, ...,a<sub>k-1</sub> randomly from a finite field
- Then generate `n` pairs of `(x, f(x))`
  - Calculate `f(x)` for `x = 1 , 2, …,n`

- The `n` pairs are distributed among the `n` parties. Since the polynomial is of degree `k-1`, we only need `k` pairs to reconstruct the polynomial using interpolation and compute `D`. 
- Basic implementation: [SSS.py](https://github.com/0xkzam/cryptography/blob/main/modern/SSS.py)

### 7. Homomorphic Encryption
- Homomorphic encryption allows operations to be performed on the encrypted data without the
need for decryption. When the encrypted data is eventually decrypted, the result of these
operations is identical to the result if the same operations were performed on the original data.
- There are three main HE schemes based on the mathematical operations they support and the number of times they can be performed.

  | | |  |
  |---|---|---|
  | Partially HE | only addition or only multiplication | infinite number of times
  | Somewhat HE | both addition and multiplication | limited number of times
  | Fully HE | both addition and multiplication | infinite number of times
  ||||

- see [Confidential ERC-20 Tokens Using HE](https://www.zama.ai/post/confidential-erc-20-tokens-using-homomorphic-encryption)