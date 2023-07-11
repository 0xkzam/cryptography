from unittest import TestCase
from modern.DeffiHellman import *


class TestDeffiHellman(TestCase):
    def test_gen_shared_key(self):
        g = 3
        p = 541
        pk_a = 5
        pk_b = 12
        k = DeffiHellman.gen_shared_key(g, p, pk_a, pk_b)
        self.assertEqual(k, 352)

        g = 10
        p = 541
        pk_a = 7
        pk_b = 11
        k = DeffiHellman.gen_shared_key(g, p, pk_a, pk_b)
        self.assertEqual(k, 504)