def solution(arr, divisor):
    list=[]
    for i in arr:
        if i % divisor ==0:
            list.append(i)
    if len(list)!=0:
        return sorted(list)
    else:
        return [-1]
        