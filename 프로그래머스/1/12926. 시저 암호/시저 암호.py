def solution(s, n):
    result=""
    low=list('abcdefghijklmnopqrstuvwxyz') * 2
    for i in s:
        if i in low:
            i=low[low.index(i)+n]
        elif i ==" ":
            i=i
        else:
            i=low[low.index(i.lower())+n].upper()
            
        result+=i
    return result
        
            
            
        
            
    