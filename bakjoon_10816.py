n = int(input())
arr = input().split()
dic = {}
for i in arr:
  if i in dic:
    dic[i] +=1
  else:
    dic[i] = 1
m = int(input())
arr2 = input().split()
ans = []
for j in arr2:
  if j in dic:
    ans.append(dic[j])
  else:
    ans.append(0)

for k in ans:
  print(k,end=" ")