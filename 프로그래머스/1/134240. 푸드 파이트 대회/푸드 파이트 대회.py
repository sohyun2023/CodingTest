def solution(food):
    result=[]
    
    for i in range(1, len(food)):
        j=1
        while 1<= j <=food[i]//2:
            result.append(i)
            j=j+1
        
    rev_result= sorted(result,reverse=True)
    result.append(0)
    ans= result+rev_result
    
    answer="".join(map(str,ans))
    return answer
    
    
    
    