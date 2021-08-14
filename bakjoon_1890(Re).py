n = int(input())
arr = []
for _ in range(n):
  arr.append(list(map(int,input().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
  for j in range(n):
    if i == n-1 and j == n-1:
      print(dp[n-1][n-1])
      break
    start = arr[i][j]
    if i+start < n:
      dp[i+start][j]+=dp[i][j]
    if j+start < n:
      dp[i][j+start]+=dp[i][j]


