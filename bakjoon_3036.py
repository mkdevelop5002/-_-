n = int(input())
arr = list(map(int,input().split()))
# n=4
# arr = [12,3,8,4]
def gcd(a,b):
  if b>a:
    a,b = b,a
  while b:
    temp = a%b
    a =b
    b =temp
  return a
ans = []
cen = arr[0]
for i in range(1,len(arr)):
  temp = gcd(cen,arr[i])
  ans.append([arr[i]//temp,cen//temp])

for idx in ans:
  print(str(idx[1])+"/"+str(idx[0]))
