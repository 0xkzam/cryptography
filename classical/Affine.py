from .Cipher import Cipher
from .util import *


class Affine(Cipher):

    def encrypt(self, text, key):
        """
        :param text:
        :param key: (a, b) tuple
        """

        a, b = key
        m = 26  # English alphabet

        if not is_coprime(a, m):
            raise ValueError(" 'a' must be coprime with " + str(m))

        cipher = ""

        for char in text:

            if char.isalpha():
                offset = ord('a') if char.islower() else ord('A')
                x = ord(char) - offset
                c = (a * x + b) % m
                cipher += chr(offset + c)
            else:
                cipher += char

        return cipher

    def decrypt(self, cipher, key):
        """
        :param cipher:
        :param key: (a, b) tuple
        """

        a, b = key
        m = 26  # English alphabet

        if not is_coprime(a, m):
            raise ValueError(" 'a' must be coprime with " + str(m))

        text = ""

        for char in cipher:

            if char.isalpha():
                offset = ord('a') if char.islower() else ord('A')
                x = ord(char) - offset

                a_inv = mod_inverse(a, m)
                c = (a_inv * (x - b)) % m

                text += chr(offset + c)
            else:
                text += char
        return text
