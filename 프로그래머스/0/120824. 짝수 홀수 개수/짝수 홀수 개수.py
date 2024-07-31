def solution(num_list):
    list=[]
    for i in num_list:
        if i%2==0:
            list.append(0)
        else:
            list.append(1)
    a=list.count(0)
    b=list.count(1)
    return [a,b]
    