def solution(num_list):
    n=len(num_list)
    result=[]
    for i in range(n-1,-1,-1):
        result.append(num_list[i])
    return result
        