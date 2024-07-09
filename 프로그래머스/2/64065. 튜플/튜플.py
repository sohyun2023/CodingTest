from collections import Counter
def solution(s):
    s=s[1:-1]
    s=s.replace('{','')
    s=s.replace('}','')
    s=s.split(',')
    
    count = Counter(s)
    sorted_elements = sorted(count.items(), key=lambda x: (-x[1], int(x[0])))
    result = [int(num) for num, freq in sorted_elements]
    return result
    
    

    
    
        