from unittest import TestCase
from classical.util import *


class Test(TestCase):
    def test_extended_gcd(self):
        p, q = 1, 1
        gcd, s, t = extended_gcd(p, q)
        self.assertEqual(gcd, 1)
        self.assertEqual(p * s + q * t, gcd)

        p, q = 1, 0
        gcd, s, t = extended_gcd(p, q)
        self.assertEqual(gcd, 1)
        self.assertEqual(p * s + q * t, gcd)

        p, q = 161, 28
        gcd, s, t = extended_gcd(p, q)
        self.assertEqual(gcd, 7)
        self.assertEqual(p * s + q * t, gcd)

        p, q = 28, 161
        gcd, s, t = extended_gcd(p, q)
        self.assertEqual(gcd, 7)
        self.assertEqual(p * s + q * t, gcd)

        p, q = -45122, 885
        gcd, s, t = extended_gcd(p, q)
        self.assertEqual(p * s + q * t, gcd)

    def test_mod_inverse(self):
        a_inv = mod_inverse(0, 1)
        self.assertEqual(0, a_inv)

        a_inv = mod_inverse(1, 1)
        self.assertEqual(0, a_inv)

        a_inv = mod_inverse(11, 26)
        self.assertEqual(19, a_inv)

        with self.assertRaises(ValueError):
            mod_inverse(464632, 26)


