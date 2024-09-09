def solution(s):
    list=s.split(' ')
    sen=""
    for word in list:
        for i,l in enumerate(word):
            
            if (i==0 )or (i %2==0):
                sen=sen+ l.upper()
            else:
                sen= sen+ l.lower()
        sen= sen+ (' ')
    return sen[:-1]
    