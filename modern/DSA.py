import random
from util.math import mod_inverse


class DSA:

    @staticmethod
    def gen_public_key(p: int, q: int, g: int, private_key: int) -> (int, int, int, int):
        """
        - Basic implementation for generating public key

        :param p: prime s.t. (p - 1) % q == 0
        :param q: prime
        :param g:
        :param private_key: secret key
        :return:
        """
        if not ((p - 1) % q) == 0:
            raise ValueError("(p-1) must be divisable by q")

        alpha = pow(g, int((p - 1) / q), p)
        beta = pow(alpha, private_key, p)

        return p, q, alpha, beta

    @staticmethod
    def gen_signature(public_key, private_key, msg_hash: int, k=0) -> (int, int):
        """
        - Basic signature generation

        :param public_key:
        :param private_key:
        :param msg_hash: integer representation of the hashed message
        :param k: if not set a random number will be set
        :return:
        """
        p, q, alpha, beta = public_key

        if k == 0:
            k = random.randrange(2, q)

        r = pow(alpha, k, p) % q
        s = (mod_inverse(k, q) * (msg_hash + private_key * r)) % q

        return r, s

    @staticmethod
    def verify(public_key, signature, msg_hash: int) -> bool:
        """
        - Basic verification protocol

        :param public_key:
        :param signature:
        :param msg_hash: integer representation of the hashed message
        :return:
        """
        p, q, alpha, beta = public_key
        r, s = signature

        s_inv = mod_inverse(s, q)
        u1 = (s_inv * msg_hash) % q
        u2 = (s_inv * r) % q
        v = (((alpha ** u1)*(beta ** u2)) % p) % q

        return v == r
