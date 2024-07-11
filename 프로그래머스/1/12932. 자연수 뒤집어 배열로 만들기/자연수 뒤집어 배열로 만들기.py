def solution(n):
    list=[]
    s=str(n)
    n=len(s)
    for i in range(1,n+1):
        list.append(int(s[-i]))
    return list
    