def solution(s):
    n=len(s)
    if n%2==0:
        a=n//2
        return s[a-1:a+1]
    else:
        return s[n//2]