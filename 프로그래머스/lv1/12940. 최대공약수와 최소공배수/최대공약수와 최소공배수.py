import math



def solution(n, m):
    answer=[]
    min1=0
    max1=0
    
    min1=min(n,m)
    for i in range(min1,0,-1):
        if (n%i==0)and(m%i==0):
            answer.append(i)
            break
    
    max1=max(n,m)
    for h in range(max1,n*m+1):
        if (h%m==0)and (h%n==0):
            answer.append(h)
            break
            
            
    return answer
