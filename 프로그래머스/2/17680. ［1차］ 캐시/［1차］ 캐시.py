from collections import deque

def solution(cacheSize, cities):
    # 캐시가 0인 경우, 모든 접근이 miss이므로 바로 계산
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = deque(maxlen=cacheSize)
    total_time = 0
    
    for city in cities:
        city = city.lower()  # 대소문자 구분하지 않음
        if city in cache:
            # Cache hit
            cache.remove(city)
            cache.append(city)
            total_time += 1
        else:
            # Cache miss
            if len(cache) >= cacheSize:
                cache.popleft()  # LRU 방식을 위해 가장 오래된 항목 제거
            cache.append(city)
            total_time += 5
    
    return total_time