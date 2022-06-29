import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)
    
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    
    return result

trying = [1, 4, 5, 3, 8, 7]
heap = []
for i in trying:
    heapq.heappush(heap, i)

print(heap)