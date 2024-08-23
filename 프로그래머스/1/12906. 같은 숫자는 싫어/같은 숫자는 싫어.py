
def solution(arr):
    list=[arr[0]]
    n=len(arr)
    for i in range(0,n-1):
        if arr[i]!=arr[i+1]:
                list.append(arr[i+1])
    return list
        