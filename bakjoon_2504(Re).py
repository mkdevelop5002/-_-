arr = list(input())
lst = []

def sol(arr):
  
  for i in arr:
    if i == '(' or i == '[':
      lst.append(i)
    elif i == ')':
      temp = []
      if len(lst) == 0:
        return 0
      else:
        while lst[-1]!='(' :
          if lst[-1] == '[':
            return 0
          temp.append(lst.pop())
          if len(lst) == 0:
            return 0
        else:
          lst.pop()
          if len(temp)!=0:
            lst.append(sum(temp)*2)
          else:
            lst.append(2)
    elif i == ']':
      temp = []
      if len(lst) == 0:
        return 0
      else:
        while lst[-1]!='[' :
          if lst[-1] == '(':
            return 0
          temp.append(lst.pop())
          if len(lst) == 0:
            return 0
        else:
          lst.pop()
          if len(temp)!=0:
            lst.append(sum(temp)*3)
          else:
            lst.append(3)
    
  ex_lst = ['(',')','[',']']
  for i in lst:
    if i in ex_lst:
      return 0
  return sum(lst)

print(sol(arr))
