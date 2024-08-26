def solution(n):
    s=''
    while n>0:
        n,q=divmod(n,3)
        s=s+str(q)
    return(int(s,3))