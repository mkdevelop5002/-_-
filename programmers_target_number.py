from collections import deque
def solution(numbers, target):
    answer = 0
    dq = deque()
    n = len(numbers)
    dq.append([numbers[0],0])
    dq.append([-numbers[0],0])
    while dq:
        num,idx = dq.popleft()
        idx+=1
        if idx<n:
            dq.append([num+numbers[idx],idx])
            dq.append([num-numbers[idx],idx])
        else:
            if num == target:
                answer+=1
            
    return answer