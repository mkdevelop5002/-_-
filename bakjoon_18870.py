n = int(input())
arr = list(map(int,input().split()))
lst = sorted(arr)
dic = {}
cnt = 0
for i in lst:
  if i not in dic:
    dic[i] = cnt
    cnt+=1

for j in arr:
  print(dic[j],end=' ')