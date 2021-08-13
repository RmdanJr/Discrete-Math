# Even permutations
def is_permutation(p):
  return (set(p)==set(range(len(p))))

print (is_permutation([0]))
print (is_permutation([0,2,1]))
print (is_permutation([1,2,3]))