from sympy.ntheory.primetest import isprime
from util.math import *


class ElGamal:
    padding = b'\x00'

    @staticmethod
    def gen_keys(p: int, g: int, private_key: int = -1) -> ((int, int, int), int):
        """
        - Generate public and private keys

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
    def encrypt__(pub_key: (int, int, int), message: str, k=0, use_bytes=True) -> (int, int):
        """
        - This is a basic implementation of ElGamal encryption.
        - The integer 'm' that represents the message, must always be less than to 'p'
        - i.e. m < p

        :param pub_key: (p ,g ,h) tuple
        :param message: string
        :param k: Optional [random number k such that 1 < k < p-1]
        :param use_bytes: Set this to False, if the message is an integer.
        :return: (c1, c2) tuple
        """
        (p, g, h) = pub_key

        if k == 0:
            k = random.randrange(2, p - 1)
        c1 = pow(g, k, p)

        if use_bytes:
            m = int.from_bytes(message.encode('utf-8'), byteorder='big')
        else:
            m = int(message)

        if not m < p:
            raise ValueError("m must must be less that p")

        hk = pow(h, k, p)
        c2 = pow(m * hk, 1, p)
        return c1, c2

    @staticmethod
    def decrypt__(pub_key: (int, int, int), private_key: int, cipher: (int, int), use_bytes=True) -> str:
        """
        - This is a basic implementation of ElGamal decryption.

        :param pub_key: (p ,g ,h) tuple
        :param private_key:
        :param cipher: (c1, c2) tuple
        :param use_bytes: Set this to False, if the message is an integer.
        :return: string
        """
        p, _, _ = pub_key
        c1, c2 = cipher

        s = pow(c1, private_key, p)
        m = pow(c2 * mod_inverse(s, p), 1, p)

        if use_bytes:
            m = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
            return m.decode('utf-8')
        else:
            return str(m)

    @staticmethod
    def encrypt(pub_key: (int, int, int), block_size: int, message: str, k=0) -> (int, bytes):
        """
        - This is a more generic implementation that allows us to adjust the block size of the
        - encryption to align with the size of public key.
        - Only c2 {C= (c1, c2)} is broken down to blocks.

        :param pub_key: (p, g, h)
        :param block_size: size in bytes per block
        :param message: string
        :param k:
        :return: (c1, c2)
        """
        (p, g, h) = pub_key
        if k == 0:
            k = random.randrange(2, p - 1)
        c1 = pow(g, k, p)

        min_n = 2 ** (block_size * 8)
        if p < min_n:
            raise ValueError("Block size and p don't match. p must be greater than or equal to " + str(min_n))

        c_blocks = []
        msg_bytes = message.encode('utf-8')
        cipher_block_size = (p.bit_length() + 7) // 8

        for i in range(0, len(msg_bytes), block_size):
            block = msg_bytes[i:i + block_size]

            # Last block is padded if less than block size
            while len(block) < block_size:
                block += ElGamal.padding

            m = int.from_bytes(block, byteorder='big')
            hk = pow(h, k, p)
            c2 = pow(m * hk, 1, p)

            # Encrypted block is converted into a bytes object of the size of p.
            # This enables us to separate the blocks of bytes in the decrypt function.
            c_bytes = c2.to_bytes(cipher_block_size, byteorder='big')
            c_blocks.append(c_bytes)

        return c1, b''.join(c_blocks)

    @staticmethod
    def decrypt(pub_key: (int, int, int), private_key: int, block_size: int, cipher: (int, bytes)) -> str:
        """
        Generic decryption function

        :param pub_key: (p, g, h)
        :param private_key:
        :param block_size: size in bytes per block
        :param cipher: (c1, c2)
        :return: decrypted message string
        """
        p, _, _ = pub_key
        c1, c2 = cipher
        s = pow(c1, private_key, p)

        min_n = 2 ** (block_size * 8)
        if p < min_n:
            raise ValueError("Block size and p don't match. p must be greater than or equal to " + str(min_n))

        message_blocks = []  # list of byte arrays
        cipher_block_size = (p.bit_length() + 7) // 8

        for i in range(0, len(c2), cipher_block_size):
            block = int.from_bytes(c2[i:i + cipher_block_size], byteorder='big')
            m = pow(block * mod_inverse(s, p), 1, p)
            b = m.to_bytes(block_size, byteorder='big')
            message_blocks.append(b)

        # Removing padding
        last_block = message_blocks[-1]
        while last_block[-1:] == ElGamal.padding:
            last_block = last_block[:- 1]
        message_blocks[-1] = last_block

        return b''.join(message_blocks).decode('utf-8')
