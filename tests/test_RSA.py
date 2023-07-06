from unittest import TestCase
from modern.RSA import *
from math import gcd
import time


class TestRSA(TestCase):
    def test_gen_public_key(self):
        # Not prime
        p, q = 12, 19
        with self.assertRaises(ValueError):
            e = RSA.gen_public_key(p, q)

        # Not prime
        p, q = 19, 22
        with self.assertRaises(ValueError):
            e = RSA.gen_public_key(p, q)

        p, q = 17, 19
        e = RSA.gen_public_key(p, q)
        self.assertTrue(gcd(e, p * q) == 1, "checking phi")

        p, q = 89, 97
        e = RSA.gen_public_key(p, q)
        self.assertTrue(gcd(e, p * q) == 1, "checking phi")

        # p, q = 45845791, 4940867
        # start = time.time()
        # e = RSA.gen_public_key(p, q)
        # end = time.time()
        # print("large prime pub key: "+str(e)+", time taken: " + str(end-start))

    def test_gen_private_key(self):
        p, q, e = 7, 29, 149
        d = RSA.gen_private_key(p, q, e)
        self.assertEqual(d, 53)



