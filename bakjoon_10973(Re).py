n = int(input())
arr = list(map(int,input().split()))
# n =4
# arr = [4,1,2,3]
chk = True
for i in range(len(arr)-1,0,-1):
  if arr[i-1] > arr[i] :
    chk = False
    x= i-1
    idx = i
    while True:
      i+=1
      if i>n-1:
        break
      if arr[x]>arr[i]:
        idx= i
      else:
        break
    arr[x],arr[idx] = arr[idx],arr[x]
    ans = sorted(arr[x+1:],reverse=True)
    ans = arr[:x+1] + ans
    break
  

if chk == True:
  print(-1)
else:
  for i in ans:
    print(i,end=' ')