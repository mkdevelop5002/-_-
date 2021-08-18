n = int(input())
arr = input().split()
chk = [False for i in range(10)]
mn,mx = '',''
def checkFunc(i,j,test):
  if test == '<':
    return i<j
  else:
    return i>j

def sol(cnt,text):
  global mn
  global mx
  if cnt == n+1:
    if len(mn) == 0:
      mn = text
    else:
      mx = text
    return
  for i in range(10):
    if chk[i] == False:
      if cnt == 0 or checkFunc(int(text[-1]),i,arr[cnt-1]):
        chk[i] =True
        sol(cnt+1,text+str(i))
        chk[i] = False

sol(0,"")
print(mx)
print(mn)

