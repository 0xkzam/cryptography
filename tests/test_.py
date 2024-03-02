from unittest import TestCase
from util.math import *
from modern.ElGamal import *
from modern.RSA import *
from modern.DeffiHellman import *
from modern.SSS import *


class Test(TestCase):

    # standard - no block size
    def test_RSA_1(self):
        p, q = 7, 5
        message = 17

        n, e = RSA.gen_public_key(p, q)

        e = 5

        n, d = RSA.gen_private_key(p, q, e)

        print("RSA1-n: " + str(n))
        print("RSA1-public key: " + str(e))
        print("RSA1-private key: " + str(d))

        c = RSA.encrypt__(n, e, message, False)
        print("RSA1-c: " + str(c))

        decrypted_message = RSA.decrypt__(n, d, c, False)
        # print("RSA1-decryption: " + str(decrypted_message))

    def test_RSA_public_key(self):
        p, q = 7, 29
        check_rsa_public_key(p, q, 8737)
        check_rsa_public_key(p, q, 6533)
        check_rsa_public_key(p, q, 2859)
        check_rsa_public_key(p, q, 4536)
        check_rsa_public_key(p, q, 169)

        inv = mod_inverse(17, 27)
        print("mod inverse: " + str(inv))

    # standard - no block size
    def test_ElGamal_1(self):
        # p, g = 47, 5
        # message = "11"
        # private_key = 42
        # r = 9
        #
        # pub_key, _ = ElGamal.gen_keys(p, g, private_key)
        #
        # _, _, h = pub_key
        # print("ElGamal1-private key: " + str(private_key))
        # print("ElGamal1-public key: " + str(h))
        #
        # c1, c2 = ElGamal.encrypt__(pub_key, message, r, False)
        #
        # print("ElGamal1-c1: " + str(c1))
        # print("ElGamal1-c2: " + str(c2))

        c1, c2 = 2, 40
        private_key = 9
        pub_key = 83, 5, 52
        decrypted_message = ElGamal.decrypt__(pub_key, private_key, (c1, c2), False)
        print("ElGamal1-decryption: " + str(decrypted_message))

    # with block size
    def test_ElGamal_2(self):
        p, g = 3731292319, 14
        k = 3
        message = "A"

        pub_key, private_key = ElGamal.gen_keys(p, g)

        print("ElGamal2-public key: " + str(pub_key))
        print("ElGamal2-private key: " + str(private_key))

        block_size = 2
        c1, c2 = ElGamal.encrypt(pub_key, block_size, message, k)
        print("ElGamal2-c1: " + str(c1))
        print("ElGamal2-c2: " + str(c2))

        decrypted_message = ElGamal.decrypt(pub_key, private_key, block_size, (c1, c2))
        print("ElGamal2-decryption: " + str(decrypted_message))


def check_rsa_public_key(p, q, x) -> bool:
    phi = (p - 1) * (q - 1)
    # check = x < phi and gcd(phi, x) == 1
    check = x < p*q and gcd(phi, x) == 1
    print("e:" + str(x) + ": " + str(check))
    return check

