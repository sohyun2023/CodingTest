def solution(genres, plays):
    genre_sum={}
    for i in range(len(genres)):
        if genres[i] not in genre_sum:
            genre_sum[genres[i]]=0
            genre_sum[genres[i]]=genre_sum[genres[i]] + plays[i]
        else:
            genre_sum[genres[i]]=genre_sum[genres[i]] + plays[i]
    
    genre_sum= sorted(genre_sum.items(), key=lambda x: x[1], reverse=True)
    
    
    music={}
    new_plays=[]
    for items in enumerate(plays):
        new_plays.append(items)
    
    for i in range(len(genres)):
        if genres[i] not in music:
            music[genres[i]]=[]
            music[genres[i]].append(new_plays[i])
        else:
            music[genres[i]].append(new_plays[i])
    
    
    for key in music:
        music[key]=sorted(music[key], key=lambda x: x[1],reverse=True)
    print(music)
    
    result=[]
    for key,_ in genre_sum:
        for i in range(min(2,len(music[key]))):
            result.append(music[key][i][0])
            
    return result