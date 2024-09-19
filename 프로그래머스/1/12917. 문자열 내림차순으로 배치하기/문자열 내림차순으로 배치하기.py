def solution(s):
    s=sorted(s,reverse=True)  #inverse와 구분
    return ''.join(s)
