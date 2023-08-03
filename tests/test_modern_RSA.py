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

    def test_encrypt___decrypt__(self):
        p, q = 45845791, 3731292319
        n, e = RSA.gen_public_key(p, q)
        n, d = RSA.gen_private_key(p, q, e)
        message = "1234567"

        c = RSA.encrypt__(n, e, message)
        msg = RSA.decrypt__(n, d, c)
        self.assertEqual(message, msg)

        # when message is an integer===================
        # use_bytes = False
        p, q = 7, 5
        message = "17"
        e = 5
        n, d = RSA.gen_private_key(p, q, e)
        c = RSA.encrypt__(n, e, message, False)
        decrypted_message = RSA.decrypt__(n, d, c, False)
        self.assertEqual(message, decrypted_message)

    def test_encrypt_decrypt(self):
        p, q = 45845791, 3731292319
        n, e = RSA.gen_public_key(p, q)
        n, d = RSA.gen_private_key(p, q, e)
        block_size = 8

        # n is too small. n >= 2^(64)
        with self.assertRaises(ValueError):
            RSA.encrypt(n, e, block_size, "")

        block_size = 7

        # Empty
        self.assertEqual(RSA.encrypt(n, e, block_size, ""), b"")

        # Single character
        message = "A"
        c = RSA.encrypt(n, e, block_size, message)
        self.assertEqual(message, RSA.decrypt(n, d, block_size, c))

        # Alphanumeric + symbols
        message = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+"
        c = RSA.encrypt(n, e, block_size, message)
        self.assertEqual(message, RSA.decrypt(n, d, block_size, c))

        # Arbitrary string
        message = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKgRE+tUN2AVZJ5S/eHr/B/gdQreYX8OqVAeRJR0CgxIvDx3qFrMkjk2odflcV32ZuPv20fbW8MaBpUYEsoHSwECAwEAAQ=="
        c = RSA.encrypt(n, e, block_size, message)
        self.assertEqual(message, RSA.decrypt(n, d, block_size, c))

        # Q5 - relatively small primes
        n = 937513
        e = 638471
        p, q = 877, 1069
        message = "Hello World!"

        # n too small
        block_size = 3
        with self.assertRaises(ValueError):
            RSA.encrypt(n, e, block_size, message)

        # n too small
        block_size = 4
        with self.assertRaises(ValueError):
            RSA.encrypt(n, e, block_size, message)

        block_size = 2
        c = RSA.encrypt(n, e, block_size, message)
        n, d = RSA.gen_private_key(p, q, e)
        msg = RSA.decrypt(n, d, block_size, c)
        self.assertEqual(message, msg)

    def test_encrypt_decrypt_32bit(self):
        p, q = 45845791, 3731292319
        n, e = RSA.gen_public_key(p, q)
        n, d = RSA.gen_private_key(p, q, e)

        message = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
        c = RSA.encrypt_32bit(n, e, message)
        self.assertEqual(message, RSA.decrypt_32bit(n, d, c))

        message = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKgRE+tUN2AVZJ5S/eHr/B/gdQreYX8OqVAeRJR0CgxIvDx3qFrMkjk2odflcV32ZuPv20fbW8MaBpUYEsoHSwECAwEAAQ=="
        c = RSA.encrypt_32bit(n, e, message)
        self.assertEqual(message, RSA.decrypt_32bit(n, d, c))
