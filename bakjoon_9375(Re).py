n = int(input())
answer = []
for i in range(n):
  dic = {}
  k = int(input())
  for j in range(k):
    n,m = input().split()
    if m not in dic:
      dic[m] = [n]
    else:
      dic[m].append(n)
  ans = 1
  for i in dic:
    ans*=(len(dic[i])+1)
  ans -=1
  answer.append(ans)
for i in answer:
  print(i)