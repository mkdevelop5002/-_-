# 15
# push_back 1
# push_front 2
# front
# back
# size
# empty
# pop_front
# pop_back
# pop_front
# size
# empty
# pop_back
# push_front 3
# empty
# front

import sys
from collections import deque
n = int(input())
dq = deque()
for i in range(n):
  text = sys.stdin.readline().split()
  if text[0] == 'push_back':
    dq.append(int(text[1]))
  elif text[0] == 'push_front':
    dq.appendleft(int(text[1]))
  elif text[0] == 'pop_back':
    if len(dq) == 0:
      print(-1)
    else:
      pri = dq.pop()
      print(pri)
  elif text[0] == 'pop_front':
    if len(dq)==0:
      print(-1)
    else:
      pri= dq.popleft()
      print(pri)
  elif text[0] == 'size':
    print(len(dq))
  elif text[0] == 'empty':
    if len(dq)==0:
      print(1)
    else:
      print(0)
  elif text[0]=='front':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[0])
  elif text[0]=='back':
    if len(dq) == 0:
      print(-1)
    else:
      print(dq[-1])




