
def solution(s1, s2):
    result=0
    set1=set(s1)
    set2=set(s2)
    diff=len(set2-set1)
    ans=len(s2)-diff
    return ans