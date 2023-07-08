import random


def gcd(a: int, b: int) -> int:
    """
    Euclidean Algorithm
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extended_gcd(a: int, b: int) -> int:
    """
    Extended Euclidean Algorithm

    :return: gcd, s, t
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def mod_inverse(a: int, m: int):
    """
    a^(-1) mod m

    :return: modular inverse of a
    """
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError('Modular inverse does not exist')
    else:
        return x % m


def is_coprime(a: int, m: int) -> bool:
    gcd, _, _ = extended_gcd(a, m)
    return gcd == 1


def q1_isprime(n: int) -> bool:
    """
    Trial and error method
    Only odd number are taken into account
    """
    if n == 2:
        return True

    if n < 2 or n % 2 == 0:
        return False

    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True


def q2_isprime(n: int) -> bool:
    """
    Square root method
    """
    if n == 2 or n == 3:
        return True

    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def miller_rabin_test(n: int, k=10) -> bool:
    """
    Miller Rabin test for prime numbers - probabilistic approach

    Reference
    - https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Miller%E2%80%93Rabin_test
    """
    if n == 2 or n == 3:
        return True

    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for i in range(0, k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
        for j in range(0, s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False

    return True
