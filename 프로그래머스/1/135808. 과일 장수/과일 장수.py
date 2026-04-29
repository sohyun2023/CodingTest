def solution(k, m, score):
    cnt= len(score)//m
    stk=sorted(score, reverse=False)
    
    total=0
    for i in range(len(stk)-m,-1,-m):
        total=total + stk[i] *m
    return total