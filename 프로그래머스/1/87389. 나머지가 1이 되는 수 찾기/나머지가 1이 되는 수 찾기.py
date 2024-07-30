def solution(n):
    list=[]
    for i in range(1,n):
        if (n-1)%i==0:
            list.append(i)
    return list[1]