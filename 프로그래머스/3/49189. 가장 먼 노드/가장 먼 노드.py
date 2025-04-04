import heapq
Inf=int(20000)
def solution(n, edge):
    
    distance=[Inf] * (n+1)
    
    graph=[[] for i in range(n+1)]
    
    for link in edge:
        a,b=link
        graph[a].append([b,1])
        graph[b].append([a,1])
    
    def dikstra(start):
        q=[]
        heapq.heappush(q,(0,start))
        distance[start]=0
        while q:
            dist, now =heapq.heappop(q)
            if distance[now]< dist: #꺼낸게 더 크면 뮤시
                continue
            for h in graph[now]:
                cost=dist + h[1]
                if cost < distance[h[0]]:
                    distance[h[0]]=cost
                    heapq.heappush(q,(cost,h[0]))
        
    dikstra(1)        
    
    m=max(distance[1:])
    return distance[1:].count(m)
    
            
    
            
        
        
        
    
    