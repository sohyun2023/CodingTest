def solution(num):
    a=0
    while num!=1:
        if num%2==0:
            num=num//2
            a=a+1
        elif num%2==1:
            num=num*3 +1
            a=a+1
    if a>500:
        return -1
    else:
        return a
        

            
        
            
            