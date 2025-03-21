from collections import deque

def solution(priorities, location):
    prior=[]
    count=0
    for i in range(len(priorities)):
        prior.append((priorities[i],i))
    print(prior)
    
    prior=deque(prior)
    while prior:
        if any(prior[0][0] < item[0] for item in prior):
            prior.append(prior.popleft())
        else:
            count+=1
            if prior[0][1] == location:
                return count
            else:
                prior.popleft()
            
            