def solution(citations):
    citations.sort(reverse=True)  # 인용 횟수를 내림차순으로 정렬합니다.
    h_index = 0
    
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break
    
    return h_index
