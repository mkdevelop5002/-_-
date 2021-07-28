n = int(input())
def move(n,start,end):
  mid = 6-start-end
  if n == 1:
    return print(start,end)  
  elif n>=2:
    move(n-1,start,mid)
    move(1,start,end)
    move(n-1,mid,end)

print((2**n) -1)
move(n,1,3)