text = input()
start = 0
arr = []
for i in range(len(text)):
  if text[i] == '+' or text[i] == '-':
    arr.append(int(text[start:i]))
    arr.append(text[i])
    start = i+1
arr.append(int(text[start:]))
lst = ''.join(map(str,arr))

chk = True
i=0
while i < len(lst):
  if lst[i] == '-':
    if chk == True:
      lst = lst[:i+1]+'('+lst[i+1:]

      chk = False
    elif chk == False:
      lst = lst[:i]+')'+lst[i:]
     
      chk = True
  i+=1
if chk == False:
  lst = lst+')'
print(int(eval(lst)))
  
