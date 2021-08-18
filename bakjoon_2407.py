import math
n,c = map(int,input().split())
print(math.factorial(n)//(math.factorial(c)*math.factorial(n-c)))