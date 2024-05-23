def solution(arr):
    
    sorted_arr=sorted(arr,reverse=True) #내림차순
    max=sorted_arr[0]
    
    
    multiples=[]
    current=max
    
    while True:
        multiples.append(current)
        if all(current % x == 0 for x in arr):
            break
        else:
            current=current+max
    
    
    return current