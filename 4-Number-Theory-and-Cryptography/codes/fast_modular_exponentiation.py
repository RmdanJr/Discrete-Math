# Fast Modular Exponentiation: Code
"""function FastModularExponentiation(b, e, m) which computes b^2^k mod m using only around 2*k modular multiplications. """
def FastModularExponentiation(b, k, m):
    for i in range(1, k + 1):
        b = b % m
        b = b * b
    return b % m


def Modular_Exponentiation_Power(b, k, m):
    for i in range(1, k + 1):
        b = b % m
        b = b * b
    return b % m


"""function FastModularExponentiation(b, e, m) which computes b^e mod m using around 2*log2(e) modular multiplications. """
def FastModularExponentiation(b, e, m):
    a = 1
    n = bin(e)
    for i in range(len(n) - 1, 1, -1):
        if int(n[i]) != 0:
            a = a * Modular_Exponentiation_Power(b, len(n)-1-i, m)
    return a % m
