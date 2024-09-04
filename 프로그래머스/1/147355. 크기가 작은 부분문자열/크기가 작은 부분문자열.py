def solution(t, p):
    n=len(t)
    m=len(p)
    sum=0
    for i in range(0,n-m+1):
        if int(t[i:i+m]) <= int(p):
            sum=sum+1
    return sum