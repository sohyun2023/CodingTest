def solution(a, b):
    x= str(a) + str(b)
    y= str(b) + str(a)
    return(int(max(x,y)))