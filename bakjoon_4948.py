import math
def sosu(num):
  if num< 2:
    return 0
  else:
    for i in range(2,int(math.sqrt(num))+1):
      if num % i == 0:
        return 0
    return 1
arr = []

while True:
  n = int(input())
  if n == 0:
    break
  cnt = 0
  for i in range(n+1,2*n+1):
    if sosu(i) == 1:
      cnt+=1
  arr.append(cnt)

for j in arr:
  print(j)

