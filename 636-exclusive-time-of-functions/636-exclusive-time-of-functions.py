'''
"{function_id}:{"start" | "end"}:{timestamp}"

res = [0, 0]
["0:start:0","1:start:2","1:end:5","0:end:6"]

start - 
 id = 0
 time = 6
 stack = [0]
 last = 6
 val = time - last + 1 = 1
 index = 0
 res = [3, 4]
 
 
 

 
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
                    
        