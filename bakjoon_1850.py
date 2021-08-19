n,m = map(int,input().split())

def gcd(i,j):
  mod = i%j
  while mod:
    i = j
    j = mod
    mod = i%j
  return j

k = gcd(n,m)
print('1'*k)