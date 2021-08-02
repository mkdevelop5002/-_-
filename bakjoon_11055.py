n = int(input())
arr = list(map(int,input().split()))
lst = [0 for i in range(n)]
lst[0] = arr[0]
for i in range(1,len(arr)):
  for j in range(i):
    if arr[j] < arr[i]:
      if lst[i] == 0:
        lst[i] = arr[i]+arr[j]
      else:
        lst[i] = max(lst[i],arr[i]+lst[j])

print(max(lst))

