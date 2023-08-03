from util.math import *
from sympy.ntheory.primetest import isprime


class RSA:
    fermat_primes = [3, 5, 17, 257, 65537]
    padding = b'\x00'

    @staticmethod
    def gen_public_key(p: int, q: int) -> (int, int):
        """
        - Generate public key

        :param p: prime number
        :param q: prime number
        :return: tuple (n, e) where n=p*q, e = public key (encryption exponent)
        """
        if not (isprime(p) and isprime(q)):
            raise ValueError("p & q must be prime.")

        phi = (p - 1) * (q - 1)

        e = 0
        for i in RSA.fermat_primes:
            if i < phi and gcd(phi, i) == 1:
                e = i
                break

        # In case 'e' not one of Fermat's primes
        if e == 0:
            for i in range(4, phi):
                if gcd(phi, i) == 1:
                    e = i
                    break

        return p * q, e

    @staticmethod
    def gen_private_key(p: int, q: int, e: int) -> (int, int):
        """
        - Generate private key

        :param p: prime number
        :param q: prime number
        :param e: public key (encryption exponent)
        :return: tuple (n, d) where n=p*q, d = private key (decryption exponent)
        """
        if not (isprime(p) and isprime(q)):
            raise ValueError("p & q must be prime.")

        phi = (p - 1) * (q - 1)
        if phi < e or gcd(phi, e) != 1:
            raise ValueError("Invalid public key")

        return p * q, mod_inverse(e, phi)

    @staticmethod
    def encrypt__(n: int, e: int, message: str, use_bytes=True) -> int:
        """
        - This is a basic implementation of RSA encryption.
        - The whole message is converted into an integer and encrypted.
        - The downside is that the integer 'm' that represents the message, must always be less than or equal to 'n'
        - ie. m <= n

        :param n: p*q
        :param e: public key (encryption exponent)
        :param message: string
        :param use_bytes: Set this to False, if you want work with only integers without converting to bytes
        :return: integer that represents the original encryption
        """
        if use_bytes:
            m = int.from_bytes(message.encode('utf-8'), byteorder='big')
        else:
            m = int(message)

        if m > n:
            raise ValueError("n is too small.")
        c = pow(m, e, n)
        return c

    @staticmethod
    def decrypt__(n: int, d: int, cipher: int, use_bytes=True) -> str:
        """
        - This is a basic implementation of RSA decryption
        - Used to decrypt output from encrypt__() function

        :param n: p*q
        :param d: private key (decryption exponent)
        :param cipher: integer that represents the original encryption
        :param use_bytes: Set this to False, if the message is an integer.
        :return: decrypted text
        """
        m = pow(cipher, d, n)

        if use_bytes:
            m = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
            return m.decode('utf-8')
        else:
            return str(m)

    @staticmethod
    def encrypt(n: int, e: int, block_size: int, message: str) -> bytes:
        """
        This is a more generic implementation that allows us to adjust the block size of the
        encryption to align with the size of n.

        :param n: p * q
        :param e: public key (encryption exponent)
        :param block_size: size in bytes per block
        :param message: string
        :return: bytes object of the encrypted message
        """
        min_n = 2 ** (block_size * 8)
        if n < min_n:
            raise ValueError("n must be greater than or equal to " + str(min_n))

        c_blocks = []
        msg_bytes = message.encode('utf-8')
        for i in range(0, len(msg_bytes), block_size):
            block = msg_bytes[i:i + block_size]

            # Last block is padded if less than block size
            while len(block) < block_size:
                block += RSA.padding

            m = int.from_bytes(block, byteorder='big')
            c = pow(m, e, n)

            # Encrypted block is converted into a bytes object of the size of n.
            # This enables us to separate the blocks of bytes in the decrypt function.
            c_bytes = c.to_bytes((n.bit_length() + 7) // 8, byteorder='big')
            c_blocks.append(c_bytes)

        return b''.join(c_blocks)

    @staticmethod
    def decrypt(n: int, d: int, block_size: int, cipher: bytes) -> str:
        """
        Generic decryption function

        :param n: p * q
        :param d: private key (decryption exponent)
        :param block_size: size in bytes per block
        :param cipher: bytes object
        :return: decrypted message string
        """
        min_n = 2 ** (block_size * 8)
        if n < min_n:
            raise ValueError("n must be greater than or equal to " + str(min_n))

        message_blocks = []  # list of byte arrays
        cipher_block_size = (n.bit_length() + 7) // 8

        for i in range(0, len(cipher), cipher_block_size):
            block = int.from_bytes(cipher[i:i + cipher_block_size], byteorder='big')
            m = pow(block, d, n)
            b = m.to_bytes(block_size, byteorder='big')
            message_blocks.append(b)

        # Removing padding
        last_block = message_blocks[-1]
        while last_block[-1:] == RSA.padding:
            last_block = last_block[:- 1]
        message_blocks[-1] = last_block

        return b''.join(message_blocks).decode('utf-8')

    @staticmethod
    def encrypt_32bit(n: int, e: int, message: str):
        """
        block size = 4 bytes
        """
        return RSA.encrypt(n, e, 4, message)

    @staticmethod
    def decrypt_32bit(n: int, d: int, cipher: bytes) -> str:
        """
        block size = 4 bytes
        """
        return RSA.decrypt(n, d, 4, cipher)
