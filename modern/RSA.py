import math
import random
from primePy import primes
from classical.util import *


class RSA:

    @staticmethod
    def gen_public_key(p, q):

        if not (primes.check(p) and primes.check(q)):
            raise ValueError("p & q must be prime.")

        phi = (p - 1) * (q - 1)

        # For simplicity, only prime numbers are considered
        candidates = set(primes.upto(phi))

        e = 0
        while len(candidates) != 0:
            e = candidates.pop()  # Assumption: pseudo randomness in set.pop()
            if math.gcd(phi, e) == 1:
                break

        # Even if only the set of prime numbers are considered there exists at least one prime that coprimes with
        # phi. Therefore, theoretically at this point p should be >= 0, but checked anyway.
        if e == 0:
            raise ValueError("Public key not found.")

        return e

    @staticmethod
    def gen_private_key(p, q, pub_key):
        phi = (p - 1) * (q - 1)
        if phi < pub_key:
            raise ValueError("pub_key=e such that 1 <= e < phi")
        return mod_inverse(pub_key, phi)
