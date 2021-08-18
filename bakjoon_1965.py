n = int(input())
lst = list(map(int,input().split()))
arr = [1 for i in range(n)]
for i in range(n):
  start = lst[i]
  for j in range(i+1,n):
    if lst[j]>lst[i]:
      arr[j]=max(arr[i]+1,arr[j])
print(max(arr))
