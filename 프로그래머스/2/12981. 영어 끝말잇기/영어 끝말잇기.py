def solution(n, words):
    used_words = {}
    
    for idx, word in enumerate(words):
        if word in used_words or (idx > 0 and words[idx-1][-1] != word[0]):
            player = (idx % n) + 1
            turn = (idx // n) + 1
            return [player, turn]
        
        used_words[word] = True
    
    return [0, 0]
