def solution(a, d, included):
    num=[a]
    for _ in range(len(included)-1):
        num.append(num[-1]+d)
    sum=0
    for i in range(len(num)):
        if included[i]==1:
            sum=sum+num[i]
            
    return sum
    