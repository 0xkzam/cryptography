def extended_gcd(a, b):
    """
    :return: gcd, s, t
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def mod_inverse(a, m):
    """
    a^(-1) mod m

    :return: modular inverse of a
    """
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def is_coprime(a, m):
    gcd, _, _ = extended_gcd(a, m)
    return gcd == 1
