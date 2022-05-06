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
        
        def findPatterns(word):
            patt = []
            i, matchIndex = 0, s.find(word, 0)
            while matchIndex != -1:
                patt.append([matchIndex, matchIndex + len(word)])
                i = matchIndex + 1
                matchIndex = s.find(word, i)
            return patt
        
        intervals = []
        
        for word in words:
            interval = findPatterns(word)
            intervals.extend(interval)
            
        if not intervals: 
            return s
        
        intervals.sort()
        
        
        mergeIntervals = []
        
        #merge interval
        last = intervals[0]
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                mergeIntervals.append(last)
                last = curr
        mergeIntervals.append(last)
        res = list(s)
        
        for i in range(len(mergeIntervals)-1, -1, -1):
            start, end = mergeIntervals[i]
            res.insert(end, '</b>')
            res.insert(start, '<b>')
        return ''.join(res)
            
        
        