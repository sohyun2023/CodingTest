def solution(numbers):
    numbers= sorted(numbers,key=lambda x: str(x)*3,reverse=True)

    result=''.join(str(i) for i in numbers)
    return  str(int(result))
            
        
    