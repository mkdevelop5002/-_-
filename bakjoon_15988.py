n = int(input())
arr = [0 for i in range(1000005)]
arr[0]=1
arr[1]=2
arr[2]=4

def sol(n):
  if n<=2:
    return arr[n]
  else:
    for i in range(3,n+1):
      if arr[i]!=0:
        continue
      else:
        arr[i] = arr[i-1]%1000000009+arr[i-2]%1000000009+arr[i-3]%1000000009
  return arr[n]

ans = []
for _ in range(n):
  ans.append(sol(int(input())-1))

for j in ans:
  print(j%1000000009)