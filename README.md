# Cryptography Basics


## Classical Cryptography

#### Caesar Cipher
- The standard Caesar Cipher is only used to encrypt alpha characters and other characters are ignored.
- Each character in the plain text is shifted by a constant (Standard shift = 3).
- `m` = size of the alphabet (m = 26 for English letters)
- <code>Encrypt(p<sub>1</sub>, p<sub>2</sub>… p<sub>m</sub>) = (p<sub>1</sub>+3, p<sub>2</sub>+3… p<sub>m</sub>+3) (mod m)</code>
- <code>Decrypt(c<sub>1</sub>, c<sub>2</sub>… c<sub>m</sub>) = (c<sub>1</sub>-3, c<sub>2</sub>-3… c<sub>m</sub>-3) (mod m)</code>
- A basic implementation can be found [here](https://github.com/0xkzam/cryptography/blob/main/classical/Caesar.py).


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

#### RSA

RSA (Ron Rivest, Adi Shamir, Leonard Adleman) is based on the Integer Factoring Problem using the product of 2 
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

#### ElGamal