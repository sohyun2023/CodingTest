import heapq
# def heapsort(iterable):
#         h=[]
#         result=[]
#         for k in range(len(iterable)):
#             heapq.heappush(h,iterable[k])
#         for i in range(len(iterable)):
#             result.append(heapq.heappop(h))
#         return result
def solution(scoville, K):
    count=0
    heapq.heapify(scoville)
    while not scoville[0]>=K:
        if len(scoville)<2:
            return -1
        
        a= heapq.heappop(scoville)
        b= heapq.heappop(scoville)
        heapq.heappush(scoville,a+2*b)
        count+=1
        
    return count
    