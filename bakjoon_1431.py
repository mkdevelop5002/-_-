n = int(input())
arr = []
for i in range(n):
  arr.append(list(input()))

# arr =[['a', 'b', 'c', 'd'],
#       ['1', '4', '5', 'c'],
#       ['a'],
#       ['a', '9', '1', '0'],
#       ['z', '3', '2', '1']]

num = [str(i) for i in range(1,10)]
for i in range(len(arr)):
  cnt = 0
  for j in arr[i]:
    if j in num:
      cnt+=int(j)
  arr[i].append(cnt)

arr


new = sorted(arr,key=lambda x: (len(x),x[-1],x))
for i in new:
  answer = ''.join(i[:-1])
  print(answer)