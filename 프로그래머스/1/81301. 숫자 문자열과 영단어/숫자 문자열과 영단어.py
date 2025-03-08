def solution(s):
    
    dict={}
    dict['zero']=0
    dict['one']=1
    dict['two']=2
    dict['three']=3
    dict['four']=4
    dict['five']=5
    dict['six']=6
    dict['seven']=7
    dict['eight']=8
    dict['nine']=9
    dict_keys=list(dict.keys())
    
    for i in dict_keys:
        if i in s:
            s=s.replace(i,str(dict[i]))
        
    return int(s)