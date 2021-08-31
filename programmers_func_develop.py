def solution(pro, speed):
    answer = []
    lst = []
    idx = 1
    dic ={}
    for cnt in range(len(pro)):
        while pro[cnt] <100:
            for i in range(len(pro)):
                pro[i] += speed[i]
                idx+=1
        lst.append(idx)

    for i in lst:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1
    for j in dic:
        answer.append(dic[j])  
    return answer