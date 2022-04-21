class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = [val[0] for val in intervals]
        ends = [val[1] for val in intervals]
        starts.sort()
        ends.sort()
        
        s, e, count = 0, 0, 0
        
        while s < len(intervals):
            if starts[s] < ends[e]:
                s+=1
                count+=1
            else:
                s+=1
                e+=1
        return count
            
        
        
        
        # intervals.sort(key = lambda x: (x[0], x[1]))
        # maxSize, counter, heap, n = 0, 0, [], len(intervals)
        # for i in range(n):
        #     start, end = intervals[i]
        #     while heap and heap[0] <= intervals[i][0]: heapq.heappop(heap)
        #     if not heap or heap[0] > intervals[i][0]: heapq.heappush(heap, intervals[i][1])
        #     maxSize = max(maxSize, len(heap))
        # return maxSize  
            
        
        