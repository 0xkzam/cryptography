import random


def gcd(a: int, b: int) -> int:
    """
    Euclidean Algorithm - iterative
    - Iterative implementation is efficient compared to recursive version since there is no function overhead.
    - Absolute values of a and b are considered
    """
    if a == 0 and b == 0:
        raise ValueError("gcd is undefined when a=0 and b=0.")

    a, b = abs(a), abs(b)  # only absolute values are considered
    if a == 0:
        return b
    elif b == 0:
        return a

    while b != 0:
        a, b = b, a % b
    return a


def gcd_recursive(a: int, b: int) -> int:
    """
    Euclidean Algorithm - recursive
    - Recursive implementation could lead to stackoverflow because of the function overhead
    - Absolute values of a and b are considered
    """
    if a == 0 and b == 0:
        raise ValueError("gcd is undefined when a=0 and b=0.")

    a, b = abs(a), abs(b)  # only absolute values are considered
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


def extended_gcd(a: int, b: int) -> (int, int, int):
    """
    Extended Euclidean Algorithm - iterative
    - ax + by = gcd(a,b)
    - Iterative implementation is efficient compared to recursive version since there is no function overhead.

    :return: gcd, x, y
    """
    if a == 0 and b == 0:
        raise ValueError("gcd is undefined when a=0 and b=0.")

    if a == 0:
        return b, 0, 1
    elif b == 0:
        return a, 1, 0

    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return b, x, y


def extended_gcd_recursive(a: int, b: int) -> (int, int, int):
    """
    Extended Euclidean Algorithm - recursive
    - ax + by = gcd(a,b)
    - Recursive implementation could lead to stackoverflow because of the function overhead

    :return: gcd, x, y
    """
    if a == 0 and b == 0:
        raise ValueError("gcd is undefined when a=0 and b=0.")

    if a == 0:
        return b, 0, 1
    elif b == 0:
        return a, 1, 0
    else:
        gcd_, x, y = extended_gcd_recursive(b % a, a)
        return gcd_, y - (b // a) * x, x


def mod_inverse(a: int, m: int) -> int:
    """
    a^(-1) mod m

    :return: modular inverse of a
    """
    if not (0 <= a < m and m > 0):
        raise ValueError('m and n must be such that 0 <= a < m and m > 1')

    gcd_, x, y = extended_gcd(a, m)
    if gcd_ != 1:
        raise ValueError('Modular inverse does not exist')
    else:
        return x % m


def is_coprime(a: int, m: int) -> bool:
    return gcd(a, m) == 1


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
    Only odd numbers are taken into account
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

    :param n:
    :param k: Number of time to run the main algorithm. A higher k value means greater accuracy and cost.
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

        y = -1
        for j in range(0, s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False

    return True


def factors(n: int) -> list:
    """
    Based on the square root method
    Only odd numbers are taken into account
    """
    ls_factors = []

    while n % 2 == 0:
        ls_factors.append(2)
        n = n / 2

    i = 3
    while i * i < n:
        while n % i == 0:
            ls_factors.append(i)
            n = n // i
        i += 2

    if n > 1:
        ls_factors.append(n)

    return ls_factors
