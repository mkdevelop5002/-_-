import heapq
## 힙큐는 최소 힙 지원해준다. 최대힙 사용하고 싶으면 -붙여서 사용하면 됨
n = int(input())
arr = []
for _ in range(n) :
  arr.append(-int(input()))
lst = []
answer= []
for i in range(len(arr)):
  if arr[i] == -0:
    if len(lst) !=0:
      answer.append(-heapq.heappop(lst))
    else:
      answer.append(0)
  else:
    heapq.heappush(lst,arr[i])

for j in answer:
  print(j)


