import math
from primePy import primes
from classical.util import *


class RSA:
    fermat_primes = [3, 5, 17, 257, 65537]

    @staticmethod
    def gen_public_key(p, q):
        """
        :param p: prime number
        :param q: prime number
        :return: tuple (n, e) where n=p*q, e = public key
        """

        if not (primes.check(p) and primes.check(q)):
            raise ValueError("p & q must be prime.")

        phi = (p - 1) * (q - 1)

        e = 0
        for i in RSA.fermat_primes:
            if i < phi and math.gcd(phi, i) == 1:
                e = i
                break

        # In case 'e' not one of Fermat's primes
        if e == 0:
            for i in range(4, phi):
                if math.gcd(phi, i) == 1:
                    e = i
                    break

        return p * q, e

    @staticmethod
    def gen_private_key(p, q, e):
        """
        :param p:
        :param q:
        :param e: public key
         :return: tuple (n, d) where n=p*q, d = private key
        """
        phi = (p - 1) * (q - 1)
        if phi < e or math.gcd(phi, e) != 1:
            raise ValueError("Invalid public key")

        return p * q, mod_inverse(e, phi)

    @staticmethod
    def encrypt(n, e, message):

        m = int.from_bytes(message.encode('utf-8'), byteorder='big')
        if m > n:
            raise ValueError("Message too long: message length= " + str(m) + ", n=" + str(n))
        c = pow(m, e, n)
        return c

    @staticmethod
    def decrypt(n, d, cipher):

        m = pow(cipher, d, n)
        m = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
        return m.decode('utf-8')
