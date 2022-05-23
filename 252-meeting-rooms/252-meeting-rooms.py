'''

'''
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: (x[0], x[1]))
        endTime = 0
        
        for start, end in intervals:
            if start < endTime: return False
            endTime = max(endTime, end)
        return True
            
        