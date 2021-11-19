n = int(input())
arr = [0 for i in range(70)]
arr[0]=1
arr[1]=1
arr[2]=2
arr[3]=4
lst = []
for i in range(n):
  lst.append(int(input()))
for i in range(len(arr)):
  if arr[i]!=0:
    pass
  else:
    arr[i] = arr[i-1]+arr[i-2]+arr[i-3]+arr[i-4]


for k in lst:
  print(arr[k])
