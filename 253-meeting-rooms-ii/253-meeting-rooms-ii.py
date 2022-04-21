class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        
        maxSize, counter, heap, n = 0, 0, [], len(intervals)
        
        for i in range(n):
            start, end = intervals[i]
            while heap and heap[0][0] <= start: heapq.heappop(heap)
            if not heap or heap[0][0] > start: heapq.heappush(heap, (end, counter, start))
            maxSize = max(maxSize, len(heap))
            counter+=1
        
        return maxSize
            
'''
[[6,17],[8,9],[11,12],[6,9]]

[6,9], [6,17], [8,9], [11,12]
i = 2
heap - (9, 6), (9, 8)
'''      
            
            
        