# Generating Combinatorial Objects: Code

# Rule of sum
print(['Alice', 'Bob', 'Charlie']  + [0, 1, 2, 3, 4])

# Rule of product
from itertools import product
for p in product(['a', 'b', 'c'], ['x', 'y']):
  print("".join(p))

# Tuples
from itertools import product
for p in product("ab", repeat=3):
  print("".join(p))

# Permutations
from itertools import permutations
for p in permutations("abcd", 2):
  print("".join(p))

# Combinations
from itertools import combinations
for c in combinations( "abcdefgh", 2):
  print("".join(c))

# Pascal's Triangle
C =dict()   # C([n,k]) is equal to n choose k
for n in  range(8):
  C[n, 0] = 1
  C[n, n] = 1
  for k in  range(1 , n ):
    C[n, k] = C[n - 1, k - 1] + C[n - 1, k]
    print(C[7 , 4])

# Combinations with Replacement
from itertools import combinations_with_replacement
for c in combinations_with_replacement("TBLE", 7):
    print("".join(c))