def solution(array, height):
    
    sum=0
    for i in range(0,len(array)):
        if array[i]>height:
            sum=sum+1
            
    return sum