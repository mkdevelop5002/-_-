n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))
dq = [0 for i in range(len(arr))]
dq[0] = arr[0]
if n == 1:
  ans = arr[0]
elif n ==2:
  ans  = arr[0]+arr[1]
elif n ==3:
  ans = max(arr[0]+arr[1],arr[0]+arr[2],arr[1]+arr[2])
else:
  dq[1] = arr[0]+arr[1]
  dq[2] = max(arr[0]+arr[1],arr[0]+arr[2],arr[1]+arr[2])
  for i in range(3,n):
    dq[i] = max(dq[i-1],dq[i-2]+arr[i],dq[i-3]+arr[i-1]+arr[i])

  ans = max(dq)

print(ans)
