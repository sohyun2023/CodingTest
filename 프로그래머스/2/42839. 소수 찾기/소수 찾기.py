from itertools import permutations
import math
def is_prime(a):
    if a<=1:
        return False
    elif a==2:
        return True
    else:
        for i in range(2, int(math.sqrt(a)+1)):
            if a % i ==0:
                return False
        else:
            return True


def solution(numbers):
    list1=[]
    list2=[]
    for i in numbers:
        list1.append(int(i))
    for i in range(1, len(numbers)+1):
        list2+= list(permutations(list1,i))
        
    
    list3=[]
    for tuple in list2:
        strs=''
        for i in tuple:
            strs=strs+str(i)
            list3.append(strs)
        list3=list(set(list3))
    list3=list(set(list(map(int,list3))))
    print(list3)
    ans=0
    check=[]
    for k in list3:
        if is_prime(k):
            ans=ans+1
    return ans
    
            
            
    
    