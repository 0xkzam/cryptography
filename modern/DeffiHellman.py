from sympy.ntheory.primetest import isprime


class DeffiHellman:

    @staticmethod
    def gen_shared_key(g: int, p: int, pk_a: int, pk_b: int) -> int:
        """

        :param g: generator/primitive root
        :param p: prime number
        :param pk_a: A's private key
        :param pk_b: B's private key
        :return: k shared key
        """
        if not isprime(p):
            raise ValueError("p must be prime.")

        pub_a = pow(g, pk_a, p)
        pub_b = pow(g, pk_b, p)

        k_a = pow(pub_b, pk_a, p)
        k_b = pow(pub_a, pk_b, p)

        if not k_a == k_b:
            raise ValueError("Shared key calculation error.")

        return k_a
