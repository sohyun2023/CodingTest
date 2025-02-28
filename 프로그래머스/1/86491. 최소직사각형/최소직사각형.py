def solution(sizes):
    a=[]
    b=[]
    for i in sizes:
        i=sorted(i)
        a.append(i[1])
        b.append(i[0])
    w=max(a)
    h=max(b)
    return w*h
        
        