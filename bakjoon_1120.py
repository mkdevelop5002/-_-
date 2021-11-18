a,b = input().split()
diff = len(b)-len(a)
a_lst = list(a)
b_lst = list(b)
arr = []
if diff == 0:
  cnt = 0
  for i in range(len(a_lst)):
    if a_lst[i] != b_lst[i]:
      cnt+=1
  arr.append(cnt)
for i in range(diff+1):
  cnt = 0
  chk_lst = b_lst[i:]
  for k in range(len(a_lst)):
    if a_lst[k]!=chk_lst[k]:
      cnt+=1
  arr.append(cnt)
print(min(arr))
