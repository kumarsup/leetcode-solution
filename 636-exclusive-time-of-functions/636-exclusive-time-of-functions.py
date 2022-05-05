'''
n = 2, logs = [
"0:start:0" - "0:end:6" - 0  0 to 6 - 6 - 4 + 1
"1:start:2" - "1:end:5" - 5  2 to 5 - 5 -2 + 1
]
-> [3,4]


res = [0]*n
res = [0, 0]

start - 
    - if stack:
        - res[stack[-1]] += start - res[stack[-1]]
    - stack.append(_id)
    - res[id] += 
    - lastVal = 0
end -
    lastVal = end - res[stack.pop()] + 1
    res[id] += lastVal
'''

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        prev, stack, res = 0, [], [0]*n
        
        for log in logs:
            fid, state, time = log.split(':')
            fid, time = int(fid), int(time)
            
            if state == 'start':
                if stack:
                    res[stack[-1]] += time - prev
                stack.append(fid) 
                prev = time
            else:
                res[stack.pop()] += time - prev + 1
                prev = time + 1
        return res
                                                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
        