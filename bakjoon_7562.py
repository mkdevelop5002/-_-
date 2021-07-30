
from collections import deque
x_list = [-2,-1,1,2,-2,-1,2,1]
y_list = [-1,-2,-2,-1,1,2,1,2]
def bfs(x,y):
  dq = deque()
  dq.append([x,y])
  while dq:
    if arr[t_x][t_y] !=0:
      return (arr[t_x][t_y])
    top = dq.popleft()
    top_x = top[0]
    top_y = top[1]
    for i in range(8):
      nx = top_x+x_list[i]
      ny = top_y+y_list[i]
      if 0<=nx<l and 0<=ny<l:
        if arr[nx][ny] == 0 :
          arr[nx][ny] = arr[top_x][top_y] +1
          dq.append([nx,ny])
n = int(input())
answer = []
for _ in range(n):
  l = int(input())
  s_x , s_y = map(int,input().split())
  t_x , t_y = map(int,input().split())
  if s_x == t_x and s_y == t_y:
    answer.append(0)
  else:
    arr = [[0]*l for _ in range(l)]
    answer.append(bfs(s_x,s_y))
for j in answer:
  print(j)