n,target = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
import itertools
for i in range(1,len(arr)+1):
  lst = list(itertools.combinations(arr,i))
  for j in lst:
    if sum(j) == target:
      cnt+=1

print(cnt)
