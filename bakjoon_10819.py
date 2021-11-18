n = int(input())
arr = list(map(int,input().split()))
import math
from collections import deque
# n = 6
# arr = [20,1,15,8,4,10]
arr.sort()
lst = []
lst2 = []

def make_lst(lst,flag):
  dq = deque(arr)
  if flag == 1:
    while dq:
      if len(dq)>=2:
        lst.append(dq.popleft())
        lst.append(dq.pop())
      else:
        lst.append(dq.popleft())
  else:
    while dq:
      if len(dq)>=2:
        lst.append(dq.pop())
        lst.append(dq.popleft())
      else:
        lst.append(dq.popleft())
  top = lst.pop()
  lst.insert(0,top)
  return lst
def cal(lst):
  chk1,chk2 = lst.copy() , lst.copy()
  chk1[0],chk1[-1] = chk1[-1],chk1[0]
  cnt,cnt2 = 0,0
  for i in range(0,n-1):
    cnt+=abs(chk1[i]-chk1[i+1])
    cnt2+=abs(chk2[i]-chk2[i+1])
  return max(cnt,cnt2)
lst = make_lst(lst,1)
lst2 = make_lst(lst2,2)


print(max(cal(lst),cal(lst2)))