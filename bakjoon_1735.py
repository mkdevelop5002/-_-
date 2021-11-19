a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())

c2 = a2*b2
c1 = a1*b2 + (b1*a2)
def gcd(n,m):
  if n<m:
    n,m = m,n
  while m:
    temp = n%m
    n = m
    m = temp
  return n

temp = gcd(c1,c2)
c1 /= temp
c2 /= temp
print(int(c1),end =" ")
print(int(c2))