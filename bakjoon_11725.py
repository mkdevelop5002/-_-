n = int(input())
tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]


from collections import deque
def bfs(start,tree,parents):
  dq = deque()
  dq.append(start)
  while dq:
    top = dq.popleft()
    for i in tree[top]:
      if parents[i] == 0:
        parents[i] = top
        dq.append(i)

for _ in range(n-1):
  a,b = map(int,input().split())
  tree[a].append(b)
  tree[b].append(a)

bfs(1,tree,parents)
  
for j in range(2,n+1):
  print(parents[j])