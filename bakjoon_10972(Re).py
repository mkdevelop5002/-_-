# 4
# 1 2 3 4
n = int(input())
arr = list(map(int,input().split()))
chk = False
for i in range(n-1,0,-1):
  if arr[i-1] < arr[i]:
    for j in range(n-1,0,-1):
      if arr[j] > arr[i-1]:
        arr[j],arr[i-1] = arr[i-1],arr[j]
        arr = arr[:i]+sorted(arr[i:])
        chk = True
        break
    if chk:
      print(*arr)
      break
if chk == False:
  print(-1)

