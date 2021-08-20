n = int(input())
arr = list(map(int,input().split()))
if n==1:
  print(0)
else:
  lst= [0 for i in range(n)]
  for i in range(len(arr)):
    if arr[i] == 0:
      continue
    else:
      num = arr[i]
      for j in range(1,num+1):
        if (i+j) < n :
          if i==0:
            lst[i+j] = lst[i]+1
          elif lst[i+j] == 0 and lst[i]!=0:
            lst[i+j] = lst[i]+1
          else:
            lst[i+j] = min(lst[i]+1,lst[i+j])

  if lst[-1]!=0:
    print(lst[-1])
  else:
    print(-1)