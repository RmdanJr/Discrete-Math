# fix this code
def gcd(a, b): return gcd(b % a, a) if a else b
def squares(n, m): return n*m // (gcd(n,m)**2)