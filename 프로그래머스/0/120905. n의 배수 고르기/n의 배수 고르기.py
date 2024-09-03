def solution(n, numlist):
    list1=[]
    for i in range(len(numlist)):
        if numlist[i] % n ==0:
            list1.append(numlist[i])
    return list1