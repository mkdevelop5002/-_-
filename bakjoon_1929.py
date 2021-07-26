import math

n,m= map(int,input().split())
def sosu(num):

    if num <= 1:
        return 0
    else:

        for i in range(2,int(math.sqrt(num)+1)):

            if num % i ==0:
                return 0
            return 1

arr = []
for i in range(n,m+1):

    if sosu(i) == 1:
        arr.append(i)

for i in arr:
    print(i)