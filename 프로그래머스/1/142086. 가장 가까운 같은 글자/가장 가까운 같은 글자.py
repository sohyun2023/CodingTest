def solution(s):
    result=[-1]
    for i in range(1,len(s)):
        if s[i] in s[:i]:
            result.append((list(s[:i])[::-1].index(s[i]))+1)
        else:
            result.append(-1)
    return result
        
        
        