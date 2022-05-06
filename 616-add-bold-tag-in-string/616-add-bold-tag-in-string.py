'''
s = "abcxyz123", words = ["abc","123"]
"<b>abc</b>xyz<b>123</b>"


s = "aaabbcc", words = ["aaa","aab","bc"]
"<b>aaabbc</b>c"

1- As there is a word may overlap- solve this we need overlap intervals
    - find patterns in s and create interval = [start, end]
    - sort interval
    - merged interval
    - iterate from end and add bold tag on the interval    
'''
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        
        def findMatchIntervals(word):
            i, match, res = 0, s.find(word, 0), []
            while match != -1:
                res.append([match, match + len(word)])
                i = match + 1
                match = s.find(word, i)
            return res
        
        intervals = []
        
        for word in words:
            interval = findMatchIntervals(word)
            intervals.extend(interval)
        
        if not intervals: 
            return s
        
        intervals.sort()
        
        mergedIntervals = []
        
        last = intervals[0]
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= last[1]:
                last[1] = max(curr[1], last[1])
            else:
                mergedIntervals.append(last)
                last = curr
        mergedIntervals.append(last)
        
        res = list(s)
        
        for i in range(len(mergedIntervals)-1, -1, -1):
            start, end = mergedIntervals[i]
            res.insert(end, '</b>')
            res.insert(start, '<b>')
        return ''.join(res)
            
        
        