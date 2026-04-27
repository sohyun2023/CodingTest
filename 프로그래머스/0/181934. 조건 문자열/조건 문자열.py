def solution(ineq, eq, n, m):
    if eq =='=':
        if n>=m and ineq==">":
            return 1
        elif n<=m and ineq=="<":
            return 1
        else:
            return 0
        
    if eq =='!':
        if n>m and ineq==">":
            return 1
        elif n<m and ineq=="<":
            return 1
        else:
            return 0    
            