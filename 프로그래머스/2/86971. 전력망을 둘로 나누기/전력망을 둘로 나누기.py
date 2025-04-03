from collections import Counter
def solution(n, wires):
    parent=[0]*(n+1)
    
        
    def find_parent(parent,x):
        if parent[x] != x:
            parent[x]=find_parent(parent,parent[x])
        return parent[x]
    
    def union_parent(parent,a,b):
        a=find_parent(parent,a)
        b=find_parent(parent,b)
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
    list=[]        
    for i in range(len(wires)):
        for h in range(1,n+1):
            parent[h]=h
        for j, wire in enumerate(wires):
            if i==j:
                continue
            a,b = wire
            union_parent(parent,a,b)
            
        for k in range(1, n+1):
            find_parent(parent,k)
        count=Counter(parent)
        
        count=sorted(count.items(),key=lambda x: x[0])
        print(count)
        list.append(abs(count[1][1]-count[2][1]))
    return min(list)
        
            
            
        
        
            
            
        
            
    
        
        