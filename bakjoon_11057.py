n = int(input())
arr = [[1 for i in range(10)] for j in range(n)]
for i in range(1,n):
  for j in range(10):
    num = 0
    for k in range(j,10):
      num+=arr[i-1][k]
    arr[i][j] = num

ans = sum(arr[n-1])
print(ans%10007)