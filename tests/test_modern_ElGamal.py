from unittest import TestCase
from modern.ElGamal import *


class TestElGamal(TestCase):
    def test_gen_keys(self):

        # Not prime
        p, g = 12, 19
        with self.assertRaises(ValueError):
            ElGamal.gen_keys(p, g)

        p, g, sk = 29, 14, 23
        (_, _, h), _ = ElGamal.gen_keys(p, g, sk)
        self.assertEqual(h, 26)

    def test_encrypt_decrypt(self):
        # p, g = 45845791, 1000
        p, g = 3731292319, 14

        message = "1234"

        pub_key, private_key = ElGamal.gen_keys(p, g)
        c = ElGamal.encrypt__(pub_key, message)

        msg = ElGamal.decrypt__(pub_key, private_key, c)
        self.assertEqual(message, msg)

