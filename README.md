# Cryptography Basics
This repo is created solely for the purpose of learning. The code is mostly implemented from scratch for the purpose 
of understanding the fundamentals of cryptographic primitives and does not follow any official cryptographic standards.

#### Contents
  - [Caesar Cipher](#item-1)
  - [Vigenere Cipher](#item-2)
  - [Affine Cipher](#item-3)
  - [RSA](#item-4)
  - [Deffi-Hellman Key Exchange](#item-5)
  - [ElGamal](#item-6)
  - [Shamir's Secret Sharing](#item-7)

## Prime numbers
- The probabilistic version of the **Miller–Rabin** test for large prime numbers is implemented [here](https://github.com/0xkzam/cryptography/blob/main/util/math.py).
  - Reference [[link](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Miller%E2%80%93Rabin_test)]

## Classical Cryptography

<a id="item-1"></a>
#### Caesar Cipher
- The standard Caesar Cipher is only used to encrypt alpha characters and other characters are ignored.
- Each character in the plain text is shifted by a constant (Standard shift = 3).
- `m` = size of the alphabet (m = 26 for English letters)
- <code>Encrypt(p<sub>1</sub>, p<sub>2</sub>… p<sub>m</sub>) = (p<sub>1</sub>+3, p<sub>2</sub>+3… p<sub>m</sub>+3) (mod m)</code>
- <code>Decrypt(c<sub>1</sub>, c<sub>2</sub>… c<sub>m</sub>) = (c<sub>1</sub>-3, c<sub>2</sub>-3… c<sub>m</sub>-3) (mod m)</code>
- A basic implementation can be found [here](https://github.com/0xkzam/cryptography/blob/main/classical/Caesar.py).

<a id="item-2"></a>
#### Vigenere Cipher
- The standard Vigenere Cipher is only used to encrypt alpha characters and other characters are ignored.
- Uses a series of different Caesar Ciphers according to the key.
- Has a key K = (k<sub>1</sub>, k<sub>2</sub>... k<sub>y</sub>) that contains only alpha characters.
- If the message length `y` > key length, the key is extended to match the length of the message.
    - Eg: if K = ‘KEY’ and the message = ‘HELLO’ then the extended key = ‘KEYKE’
- `m` = size of the alphabet (m = 26 for English letters)
- <code>Encrypt(p<sub>1</sub>, p<sub>2</sub>… p<sub>y</sub>) = (p<sub>1</sub>+k<sub>1</sub>, p<sub>2</sub>+k<sub>2</sub>… p<sub>m</sub>+k<sub>y</sub>) (mod m)</code>
- <code>Decrypt(c<sub>1</sub>, c<sub>2</sub>… c<sub>y</sub>) = (c<sub>1</sub>-k<sub>1</sub>, c<sub>2</sub>-k<sub>2</sub>… c<sub>m</sub>-k<sub>y</sub>) (mod m)</code>
- A basic implementation can be found [here](https://github.com/0xkzam/cryptography/blob/main/classical/Vigenere.py).

<a id="item-3"></a>
#### Affine Cipher
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
- A basic implementation can be found [here](https://github.com/0xkzam/cryptography/blob/main/classical/Affine.py).


## Modern Cryptography

<a id="item-4"></a>
#### RSA

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

- A basic implementation can be found [here](https://github.com/0xkzam/cryptography/blob/main/modern/RSA.py). _(WIP)_
<br>

<a id="item-5"></a>
#### Deffi-Hellman Key Exchange protocol

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
- A basic implementation can be found [here](https://github.com/0xkzam/cryptography/blob/main/modern/DeffiHellman.py) 
<br>

<a id="item-6"></a>
#### ElGamal

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
- A basic implementation can be found [here](https://github.com/0xkzam/cryptography/blob/main/modern/ElGamal.py) _(WIP)_


<a id="item-7"></a>
#### Shamir's Secret Sharing 
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
- A basic implementation [here](https://github.com/0xkzam/cryptography/blob/main/modern/SSS.py) _(WIP)_