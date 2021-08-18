n, m= map(int,input().split())
arr = list(map(int,input().split()))

import itertools
arr.sort()
ans = list(itertools.permutations(arr,m))
ans = set(ans)
ans = list(ans)
ans.sort()
for i in ans:
  for j in i:
    print(j,end=' ')
