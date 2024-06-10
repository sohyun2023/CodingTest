def solution(elements):
    n=len(elements)
    extended_elements= elements * 2
    unique_sums=set()
    
    
    for i in range(1, n+1):
        for j in range(0,n):
            pre_sum= sum(extended_elements[j: j+i])
            unique_sums.add(pre_sum)
        
        
    return len(unique_sums)