def solution(array, commands):
    result=[]
    for i in commands:
        a=i[0]
        b=i[1]
        c=i[2]
        result.append(sorted(array[a-1:b])[c-1])
    return result