from collections import Counter
def solution(participant, completion):
    
    book1= dict(Counter(participant))
    book2=dict(Counter(completion))

    if book1.keys() != book2.keys():
        return list(set(list(book1.keys()))-set(list(book2.keys())))[0]
    else:
        for k in book2.keys():
            if book1[k] != book2[k]:
                return k
            
    