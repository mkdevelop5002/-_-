from collections import deque
answer = []
number = int(input())
for i in range(number):
  n,m,k = map(int,input().split())
  arr = [[0]*n for i in range(m)]
  for i in range(k):
      x,y = map(int,input().split())
      arr[y][x] = 1

  x_arr = [0,0,1,-1]
  y_arr = [1,-1,0,0]

  def bfs(x,y):
    dq = deque()
    dq.append([x,y])
    visited = []
    while dq:
      top = dq.pop()
      arr[top[0]][top[1]] = 0
      for i in range(4):
        nx = x_arr[i]+top[0]
        ny = y_arr[i]+top[1]
        if 0<=nx<len(arr) and 0<=ny<len(arr[0]):
          if arr[nx][ny] == 1:
            dq.append([nx,ny])





  cnt = 0
  for a in range(len(arr)):
    for b in range(len(arr[0])):
      if arr[a][b] == 1:
        cnt+=1
        bfs(a,b)

  answer.append(cnt)

for i in answer:
  print(i)