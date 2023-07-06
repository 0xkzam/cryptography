from unittest import TestCase
from modern.RSA import *
from math import gcd
import time


class TestRSA(TestCase):
    def test_gen_public_key(self):
        # Not prime
        p, q = 12, 19
        with self.assertRaises(ValueError):
            n, e = RSA.gen_public_key(p, q)

        # Not prime
        p, q = 19, 22
        with self.assertRaises(ValueError):
            n, e = RSA.gen_public_key(p, q)

        p, q = 17, 19
        n, e = RSA.gen_public_key(p, q)
        self.assertTrue(gcd(e, p * q) == 1, "checking phi")

        p, q = 89, 97
        n, e = RSA.gen_public_key(p, q)
        self.assertTrue(gcd(e, p * q) == 1, "checking phi")

        # stress test
        p, q = 45845791, 3731292319
        start = time.time()
        n, e = RSA.gen_public_key(p, q)
        end = time.time()
        print("large prime pub key: " + str(e) + ", time taken: " + str(end - start))

    def test_gen_private_key(self):
        # phi < e
        p, q, e = 7, 29, 997
        with self.assertRaises(ValueError):
            RSA.gen_private_key(p, q, e)

        # e not coprime
        e = 100
        with self.assertRaises(ValueError):
            RSA.gen_private_key(p, q, e)

        p, q, e = 7, 29, 149
        n, d = RSA.gen_private_key(p, q, e)
        self.assertEqual(d, 53)

        # stress test
        p, q, e = 45845791, 3731292319, RSA.fermat_primes[4]
        start = time.time()
        n, d = RSA.gen_private_key(p, q, e)
        end = time.time()
        print("large prime private key: " + str(d) + ", time taken: " + str(end - start))

    def test_encrypt_decrypt(self):
        p, q = 45845791, 3731292319
        n, e = RSA.gen_public_key(p, q)
        n, d = RSA.gen_private_key(p, q, e)
        message = "1234567"

        c = RSA.encrypt(n, e, message)
        msg = RSA.decrypt(n, d, c)
        self.assertEqual(message, msg)

    # def test_decrypt(self):
    #     p, q = 17, 19
    #     n, e = RSA.gen_public_key(p, q)
    #
    #     print("public key: "+ str(e))
    #     n, d = RSA.gen_private_key(p, q, e)
    #     print("private key: " + str(d))
