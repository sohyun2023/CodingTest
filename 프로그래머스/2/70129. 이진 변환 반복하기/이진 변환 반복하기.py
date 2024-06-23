def solution(s):
    b=0
    a=0
    while s != '1':
        b1=s.count('0')
        b=b+b1
        s= s.replace('0','')
        s=bin(len(s))[2:]
        a=a+1
        
    
    return[a,b]
        