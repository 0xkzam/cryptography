import math
from primePy import primes
from classical.util import *


class RSA:
    fermat_primes = [3, 5, 17, 257, 65537]
    int_32bit_max = 4294967296  # 2^32

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
        """
        - This is the simplest implementation of RSA encryption.
        - The whole message is converted into an integer and encrypted.
        - The downside is that the integer 'm' that represents the message, must always be less than or equal to 'n'
        - ie. m <= n

        :param n: p*q
        :param e: public key (encryption exponent)
        :param message: string
        :return: integer that represents the original encryption
        """
        m = int.from_bytes(message.encode('utf-8'), byteorder='big')
        if m > n:
            raise ValueError("Message too long: message length= " + str(m) + ", n=" + str(n))
        c = pow(m, e, n)
        return c

    @staticmethod
    def decrypt(n, d, cipher):
        """
        This is used to decrypt the output from encrypt(n, e, message) function.

        :param n: p*q
        :param d: private key (decryption exponent)
        :param cipher: integer that represents the original encryption
        :return: decrypted text
        """
        m = pow(cipher, d, n)
        m = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
        return m.decode('utf-8')

    @staticmethod
    def encrypt_32bit(n, e, message):
        """

        :param n:
        :param e:
        :param message: string
        :return:
        """
        if n < RSA.int_32bit_max:
            raise ValueError("n must be greater than or equal to 2**32")

        c_blocks = []
        msg_bytes = message.encode('utf-8')
        for i in range(0, len(msg_bytes), 4):
            block = msg_bytes[i:i + 4]
            m = int.from_bytes(block, byteorder='big')
            c = pow(m, e, n)
            c_bytes = c.to_bytes((n.bit_length() + 7) // 8, byteorder='big')
            c_blocks.append(c_bytes)

        return b''.join(c_blocks)

    @staticmethod
    def decrypt_32bit(n, d, cipher):
        """

        :param n:
        :param d:
        :param cipher:
        :return:
        """
        message = ""
        for i in range(0, len(cipher), 8):
            block = int.from_bytes(cipher[i:i + 8], byteorder='big')
            m = pow(block, d, n)
            b = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
            message += b.decode('utf-8')

        return message
