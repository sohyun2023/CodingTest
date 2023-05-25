def solution(s):
    answer=''
    
    
    for i in range(len(s.split(' '))):
        target = s.split(' ')[i] 
        if target == '':
            answer += ' '
        else:
            answer += target.capitalize()
            answer += ' '
    
    if answer[-1] == ' ':
        return answer[:-1]
    else:
        return  answer
