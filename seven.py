import heapq

max_heap = []

heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, 360)


max_value = -heapq.heappop(max_heap)  # Convert back to positive
print("Max Element:", max_value)


print("heap", [-x for x in max_heap])

