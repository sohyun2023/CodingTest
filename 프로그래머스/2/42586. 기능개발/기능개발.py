from collections import deque

def solution(progresses, speeds):
    list=[]
    n=len(progresses)
    for i in range(0,n):
        a=(100-progresses[i]) % speeds[i]
        if a==0:
            list.append((100-progresses[i]) // speeds[i])
        else:
            list.append(((100-progresses[i]) // speeds[i])+1)
    queue=deque(list)
    answer=[]
    while queue:
        current=queue.popleft()
        count=1
        while queue and queue[0] <= current:
            queue.popleft()
            count=count+1
        answer.append(count)
    return answer
            