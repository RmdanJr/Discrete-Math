def gcd(a, b): return gcd(b % a, a) if a else b
def lcm(a, b):
  assert a > 0 and b > 0
  
  # Write your code here
  return a*b // gcd(a, b)