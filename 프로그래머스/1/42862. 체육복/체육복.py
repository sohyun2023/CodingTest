def solution(n, lost, reserve):
    common=set(lost) & set(reserve)
    
    lost=list(set(lost)-common)
    reserve=list(set(reserve)-common)
    
    lost.sort()
    reserve.sort()        
    ans=n-len(lost)  
    
    for i in lost:
        if i-1 in reserve:
            ans +=1
            reserve.remove(i-1)
            
        elif i+1 in reserve:
            ans +=1
            reserve.remove(i+1)
            
        else:
            pass
    return ans
            