def solution(s):
    answer=''
    
    for i in range(len(s.split(' '))):
        target = s.split(' ')[i] 
        if target == '':
            answer += ' '
        else:
            answer += target.capitalize()
            answer += ' '
    
    
    return answer[:-1]

