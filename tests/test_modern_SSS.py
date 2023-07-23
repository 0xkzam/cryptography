from unittest import TestCase
from modern.SSS import SSS


class TestSSS(TestCase):
    def test_gen_shards(self):

        n = 5
        k = 3
        secret = "abc"

        x, y = SSS.gen_shards(n, k, secret)
        print(x)
        print(y)

        recovered = SSS.recover(x, y, k)
        self.assertEqual(secret, recovered)

        recovered = SSS.recover(x[1:], y[1:], k)
        self.assertEqual(secret, recovered)

        recovered = SSS.recover(x[:-1], y[:-1], k)
        self.assertEqual(secret, recovered)
