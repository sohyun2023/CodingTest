def solution(arr, delete_list):
    new=[]
    for i in arr:
        if i not in delete_list:
            new.append(i)
    return new