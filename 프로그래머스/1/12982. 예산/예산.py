def solution(d, budget):
    d=sorted(d)
    n=len(d)
    count=0
    for i in range(0,n):
        if budget-d[i] >=0:
            budget= budget- d[i]
            count=count+1
    return count