def solution(k, dungeons):
    n=len(dungeons)
    visited=[False]*n
    answer=0
    def dfs(current_fatigue, count):
        nonlocal answer
        answer=max(count,answer)
        for i in range(n):
            req,cost=dungeons[i]
            if not visited[i] and current_fatigue >= req:
                visited[i]=True
                dfs(current_fatigue - cost,count+1)
                visited[i]=False
                
    
    dfs(k,0)
    return answer
    
    