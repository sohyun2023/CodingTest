import string
from collections import deque
def is_one(word1,word2):
        sum=0
        for a,b in zip(word1,word2):
            if a!=b: sum+=1
        if sum==1:
            return True
def solution(begin, target, words):
    lows=[i for i in string.ascii_lowercase]
    if target not in words:
        return 0
    
                
                
    visited=[begin]#이미 방문한애들만 적음
    
    queue=deque([(begin,0)])
    while queue:
        current,step= queue.popleft()
        if current==target:
            return step
        for word in words:
            if word not in visited and is_one(word,current):
                queue.append((word, step+1))
                visited.append(word)
            
    
    