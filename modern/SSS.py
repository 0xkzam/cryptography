import random
from numpy.polynomial import Polynomial


class SSS:
    """
    Shamir's Secret Sharing
    """

    @staticmethod
    def gen_shards(n: int, k: int, secret: str) -> (list, list):
        """
        - Basic sharding method

        :param n: Total number of shards
        :param k: minimum number of keys needed to recover (degree of polynomial = k -1)
        :param secret:
        :return: n number of x, y coordinates as 2 separate lists
        """
        if not (n / 2 < k <= n):
            raise ValueError("n/2 < k <= n")

        s = int.from_bytes(secret.encode('utf-8'), byteorder='big')

        # secret + random coefficients
        coefficients = [random.randrange(0, 1000) for _ in range(k - 1)]
        coefficients.insert(0, s)

        p = Polynomial(coefficients)

        # random n number of points to calculate y
        x = [random.randrange(1, 1000) for _ in range(n)]
        # x = [i for i in range(1, n + 1)]
        y = [int(p(x[i])) for i in range(len(x))]

        return x, y

    @staticmethod
    def recover(x: list, y: list, k: int) -> str:
        """
        - Basic recovery method

        :param x:
        :param y:
        :param k: minimum number of keys needed to recover (degree of polynomial = k -1)
        :return:
        """
        p = Polynomial.fit(x, y, k - 1)
        s = round(p(0))
        s = s.to_bytes((s.bit_length() + 7) // 8, byteorder='big')
        return s.decode('utf-8')
