def solution(n, computers):
    
    parent=[0] * (n+1)
    parent=[i for i in range(n+1)]
        
    # print(parent)
    def find_parent(parent,x):
        if parent[x] != x:
            return find_parent(parent, parent[x])
        return x
    
    def union(parent,a,b):
        a=find_parent(parent,a)
        b=find_parent(parent,b)
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
            
    
    link=[]
    for i in range(n):
        for j in range(n):
            if i != j:
                if computers[i][j] ==1:
                    link.append((i+1,j+1))
                
    for tuple in link:
        a,b= tuple
        union(parent,a,b)
    
        
    for i in range(1,n+1):
        parent[i] = find_parent(parent,i)
    
    print(parent)
    sets=set(parent)
    return len(sets)-1
        
        