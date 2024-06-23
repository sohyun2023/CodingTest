def solution(n):
    count=1
    
    for k in range(1,n):
        if (2*n-k*2+k) <=0:
            break
        if (2*n-k*2+k) % (2*k) ==0:
            count+=1
    return count