# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
# 1 16 16
e,s,m = map(int,input().split())
cnt = 1
while True:
  e -=1
  s -=1
  m -=1
  if e == 0 and s ==0 and m ==0:
    print(cnt)
    break
  cnt +=1
  if e ==0 :
    e = 15
  if s == 0:
    s = 28
  if m == 0:
    m = 19
