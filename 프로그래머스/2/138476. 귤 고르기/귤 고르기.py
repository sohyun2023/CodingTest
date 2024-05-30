from collections import Counter


def solution(k, tangerine):
    freq = Counter(tangerine).values()
    
    # 빈도 높은 순으로 정렬
    sorted_freq = sorted(freq, reverse=True)
    # 최소 종류의 수를 계산
    kinds = 0
    selected_count = 0
    
    for count in sorted_freq:
        selected_count += count
        kinds += 1
        if selected_count >= k:
            break
    
    return kinds
    
    