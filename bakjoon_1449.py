n,size = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
answer = 0
width = 0
for i in range(len(arr)):
  if arr[i] > width:
    answer+=1
    width = arr[i]+size-1
  else:
    pass
print(answer)

