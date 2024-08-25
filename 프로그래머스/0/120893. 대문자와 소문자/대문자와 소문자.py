def solution(my_string):
    result=[]
    for i in my_string:
        if i.islower():
            result.append(i.upper())
        else:
            result.append(i.lower())
            
    return ''.join(result)