from unittest import TestCase
from modern.DSA import *


class TestDSA(TestCase):

    def test_gen_public_key(self):
        p, q, g, private_key = 131, 13, 2, 6

        public_key = DSA.gen_public_key(p, q, g, private_key)
        self.assertEqual(public_key, (131, 13, 107, 45))

        message_hash = 27
        signature = DSA.gen_signature(public_key, private_key, message_hash, 4)
        self.assertEqual(signature, (6, 6))

        check = DSA.verify(public_key, signature, message_hash)
        self.assertTrue(check)
