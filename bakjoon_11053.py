n = int(input())
arr = list(map(int,input().split()))
dp_arr = [0 for i in range(len(arr))]
for i in range(1,len(arr)):
  for j in range(i):
    if arr[i] > arr[j]:
      dp_arr[i] = max(dp_arr[i],dp_arr[j]+1)

print(max(dp_arr)+ 1)