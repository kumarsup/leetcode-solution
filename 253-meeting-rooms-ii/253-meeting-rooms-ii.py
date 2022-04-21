class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], x[1]))
        n = len(intervals)
        if n == 0: return 0
        
        maxSize, counter, heap = 0, 0, []     
        for i in range(n):
            start, end = intervals[i]
            
            while heap and heap[0][0] <= start:
                heapq.heappop(heap)
                
            if not heap or heap[0][0] > start:
                heapq.heappush(heap, (end, counter, start))
            
            counter+=1
            maxSize = max(maxSize, len(heap))
        return maxSize
            
'''
[[6,17],[8,9],[11,12],[6,9]]

[6,9], [6,17], [8,9], [11,12]
i = 2
heap - (9, 6), (9, 8)
'''      
            
            
        