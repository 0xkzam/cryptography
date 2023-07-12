import random
from sympy.ntheory.primetest import isprime
from util.math import *


class ElGamal:

    @staticmethod
    def gen_keys(p: int, g: int, private_key: int = -1) -> ((int, int, int), int):
        """
        Generate public and private keys

        :param p: large prime
        :param g: primitive root
        :param private_key: if empty, a random number is assigned
        :return: (public key (p, g, h), private key) tuple
        """
        if not isprime(p):
            raise ValueError("p must be prime.")

        if private_key == -1:
            private_key = random.randrange(2, p - 1)

        h = pow(g, private_key, p)

        return (p, g, h), private_key

    @staticmethod
    def encrypt__(pub_key: (int, int, int), message: str) -> (int, int):
        """
        - This is a basic implementation of ElGamal encryption.
        - The integer 'm' that represents the message, must always be less than to 'p'
        - i.e. m < p

        :param pub_key: (p ,g ,h) tuple
        :param message: string
        :return: (c1, c2) tuple
        """
        (p, g, h) = pub_key

        k = random.randrange(2, p - 1)
        c1 = pow(g, k, p)

        m = int.from_bytes(message.encode('utf-8'), byteorder='big')

        if not m < p:
            raise ValueError("m must must be less that p")

        c2 = m * pow(h, k, p)
        return c1, c2

    @staticmethod
    def decrypt__(pub_key: (int, int, int), private_key: int, cipher: (int, int)) -> str:
        """
        - This is a basic implementation of ElGamal decryption.

        :param pub_key: (p ,g ,h) tuple
        :param private_key:
        :param cipher: (c1, c2) tuple
        :return:
        """
        p, _, _ = pub_key
        c1, c2 = cipher

        s = pow(c1, private_key, p)
        m = pow(c2 * mod_inverse(s, p), 1, p)

        m = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
        return m.decode('utf-8')
