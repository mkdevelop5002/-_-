
answer = []
while True:
  n,k = map(int,input().split())
  if n ==0 and k == 0:
    break
  arr = []
  for i in range(k):
    arr.append(list(map(int,input().split())))


  x_list = [0,0,1,-1,-1,1,-1,1]
  y_list = [1,-1,0,0,-1,-1,1,1]
  from collections import deque
  def bfs(i,j):
    dq = deque()
    dq.append([i,j])
    while dq:
      top = dq.pop()
      x = top[0]
      y = top[1]
      arr[x][y] = 0
      for idx in range(8):
        nx = x + x_list[idx]
        ny = y + y_list[idx]
        if 0<=nx<k and 0<=ny<n:
          if arr[nx][ny] == 1:
            dq.append([nx,ny])


  cnt = 0 
  for i in range(k):
    for j in range(n):
      if arr[i][j] == 1:
        cnt +=1
        bfs(i,j)

  answer.append(cnt)

for i in (answer):
  print(i)