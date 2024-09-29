def solution(my_string, n):
    answer = ''
    for index,i in enumerate (my_string):
        if index< n:
            answer=answer+i
    return answer