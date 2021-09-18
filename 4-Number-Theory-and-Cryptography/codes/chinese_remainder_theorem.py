# Chinese Remainder Theorem: Code
def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def extended_gcd(a, b):
    assert a >= b and b >= 0 and a + b > 0
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)
    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)


def divide(a, b, n):
    assert n > 1 and a > 0 and gcd(a, n) == 1
    if a >= b:
        d, x, y = extended_gcd(a, b)
    else:
        d, y, x = extended_gcd(b, a)
    k = x % n
    return b * k % n


def ChineseRemainderTheorem(n1, r1, n2, r2):
    prod = n1 * n2
    in1 = divide(n2, 1, n1)
    in2 = divide(n1, 1, n2)
    x = (r1 * n2 * in1) % prod
    y = (r2 * n1 * in2) % prod
    return (x + y) % prod


ChineseRemainderTheorem(3, 2, 5, 3)
