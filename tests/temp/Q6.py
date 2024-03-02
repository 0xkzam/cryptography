from util.math import miller_rabin_test, gcd, mod_inverse, factors


class RSA:
    padding = b'\x00'

    @staticmethod
    def gen_private_key(p: int, q: int, e: int) -> (int, int):
        """
        - Generate private key

        :param p: prime number
        :param q: prime number
        :param e: public key (encryption exponent)
        :return: tuple (n, d) where n=p*q, d = private key (decryption exponent)
        """
        if not (miller_rabin_test(p) and miller_rabin_test(q)):
            raise ValueError("p & q must be prime.")

        phi = (p - 1) * (q - 1)
        if phi < e or gcd(phi, e) != 1:
            raise ValueError("Invalid public key")

        return p * q, mod_inverse(e, phi)

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


def break_rsa(public_key: (int, int), encrypted_message: str):
    (n, e) = public_key
    pq_ = factors(n)
    p = pq_[0]
    q = pq_[1]
    phi = (p - 1) * (q - 1)
    private_key_exponent = 0
    if phi < e or gcd(phi, e) != 1:
        private_key_exponent = mod_inverse(e, phi)


if __name__ == "__main__":
    # public key (937513, 638471)
    n_, e_ = 937513, 638471

    # Finding p and q
    pq = factors(n_)

    # Generating private key
    _, d_ = RSA.gen_private_key(pq[0], pq[1], e_)

    message_ = "Hello World!"

    # Using 2 bytes (i.e. 16 bits) as block_size, since n is relatively small.
    block_size_ = 2

    # Encryption
    c_ = RSA.encrypt(n_, e_, block_size_, message_)

    # Decryption
    decrypted_text = RSA.decrypt(n_, d_, block_size_, c_)

    print("original message: " + message_)
    print("decrypted message: " + decrypted_text)
