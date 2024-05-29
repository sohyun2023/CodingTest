def solution(n, arr1, arr2):
    one=[]
    two=[]
    answer = []
    
    for i in arr1 :
        one.append(bin(i)[2:].zfill(n))
    print(one)
                   
                             
    for j in arr2 :
        two.append(bin(j)[2:].zfill(n))
    print(two)
               
    for i in range(n):
        combined=( int(one[i],2)  |  int(two[i],2))
        answer.append(bin(combined)[2:].zfill(n).replace('1', '#').replace('0', ' '))
        
    
        
    return answer