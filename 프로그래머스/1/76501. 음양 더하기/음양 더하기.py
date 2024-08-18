def solution(absolutes, signs):
    
    n=len(signs)
    for i in range(0,n):
        if signs[i]==True:
            absolutes[i]=absolutes[i]
        else:
            absolutes[i]=-absolutes[i]
    return sum(absolutes)
        