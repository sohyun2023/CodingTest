def solution(my_string):
    string=""
    n=len(my_string)
    stack=list(my_string)
    for i in range(0,n):
        top=stack.pop()
        string=string+top
    return string
        
    
        
        