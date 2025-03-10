def solution(nums):
    n=len(nums)//2
    pokemon={}
    for i in list(map(str,nums)):
        pokemon[i]= nums.count(int(i))
    
    if n <= len(pokemon.keys()):
        return n
    
    small_poke=[]
    if n > len(pokemon.keys()):
        for _ in range (n):
            for key in pokemon.keys():
                small_poke.append(key)
                if len(small_poke)==n:
                    break
        return len(list(set(small_poke)))
            
            
            
            
        
        
    
        