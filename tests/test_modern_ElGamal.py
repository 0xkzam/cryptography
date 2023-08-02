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

    def test_encrypt__decrypt__(self):
        # p, g = 45845791, 1000
        p, g = 3731292319, 14

        message = "1234"

        pub_key, private_key = ElGamal.gen_keys(p, g)
        c = ElGamal.encrypt__(pub_key, message)

        msg = ElGamal.decrypt__(pub_key, private_key, c)
        self.assertEqual(message, msg)

        # when message is an integer===================
        # use_bytes = False
        p, g = 47, 5
        message = "11"
        private_key = 42
        r = 9

        pub_key, _ = ElGamal.gen_keys(p, g, private_key)
        _, _, h = pub_key
        c1, c2 = ElGamal.encrypt__(pub_key, message, r, False)
        decrypted_message = ElGamal.decrypt__(pub_key, private_key, (c1, c2), False)

        self.assertEqual(message, decrypted_message)

    def test_encrypt_decrypt_(self):
        p, g = 3731292319, 14
        pub_key, private_key = ElGamal.gen_keys(p, g)
        block_size = 8

        # n is too small. n >= 2^(64)
        with self.assertRaises(ValueError):
            ElGamal.encrypt(pub_key, block_size, "")

        block_size = 2

        # Empty
        _, c2 = ElGamal.encrypt(pub_key, block_size, "")
        self.assertEqual(c2, b"")

        # Single character
        block_size = 3
        message = "A"
        c = ElGamal.encrypt(pub_key, block_size, message)
        self.assertEqual(message, ElGamal.decrypt(pub_key, private_key, block_size, c))

        # Alphanumeric + symbols
        message = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"
        c = ElGamal.encrypt(pub_key, block_size, message)
        self.assertEqual(message, ElGamal.decrypt(pub_key, private_key, block_size, c))

        # Arbitrary string
        message = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKgRE+tUN2AVZJ5S/eHr/B/gdQreYX8OqVAeRJR0CgxIvDx3qFrMkjk2odflcV32ZuPv20fbW8MaBpUYEsoHSwECAwEAAQ=="
        c = ElGamal.encrypt(pub_key, block_size, message)
        self.assertEqual(message, ElGamal.decrypt(pub_key, private_key, block_size, c))

        # relatively small primes
        p, g = 877, 5
        pub_key, private_key = ElGamal.gen_keys(p, g)
        message = "Hello World!"

        # n too small
        block_size = 3
        with self.assertRaises(ValueError):
            ElGamal.encrypt(pub_key, block_size, message)

        # n too small
        block_size = 4
        with self.assertRaises(ValueError):
            ElGamal.encrypt(pub_key, block_size, message)

        block_size = 1
        c = ElGamal.encrypt(pub_key, block_size, message)
        msg = ElGamal.decrypt(pub_key, private_key, block_size, c)
        self.assertEqual(message, msg)
