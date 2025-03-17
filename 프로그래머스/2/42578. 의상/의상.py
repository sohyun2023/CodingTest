
from itertools import combinations
from collections import Counter
def solution(clothes):
    sum=0
    multi=1
    closet= {}
    for list in clothes:
        if list[1] not in closet:
            closet[list[1]]=[]
        closet[list[1]].append(list[0])
    
    for key in closet:
        closet[key]=len(closet[key])
    print(closet)
        
    for key in closet:
        multi=  multi * (closet[key] +1)
    
    return multi-1