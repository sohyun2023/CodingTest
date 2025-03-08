def solution(numbers):
    result=[]
    numbers.sort()
    if len(numbers) >2:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                result.append(numbers[i] + numbers[j])
        result=list(set(result))
        result.sort()
    else:
        result.append(numbers[0]+numbers[1])
        
        
    
    return result
        