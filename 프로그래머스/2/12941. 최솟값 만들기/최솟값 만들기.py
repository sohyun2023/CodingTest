import heapq

def solution(A,B):
    sorta= sorted(A,reverse=True)
    sortb=sorted(B)
    
    c=0
    for i in range(0, len(A)):
        c+=sorta[i]*sortb[i]
    return c