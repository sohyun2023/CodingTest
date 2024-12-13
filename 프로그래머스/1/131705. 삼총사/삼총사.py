from itertools import combinations

def solution(number):
    cnt=0
    for com in combinations(number,3):
        if sum(com)==0:
            cnt=cnt+1
    return cnt