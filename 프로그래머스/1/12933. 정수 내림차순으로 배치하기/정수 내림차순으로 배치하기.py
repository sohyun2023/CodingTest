def solution(n):
    answer='k'
    s=str(n)
    s=sorted(s,reverse=True)
    for i in s:
        answer=answer+i
    return int(answer[1:])