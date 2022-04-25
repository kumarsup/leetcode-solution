'''
"{function_id}:{"start" | "end"}:{timestamp}"

'''

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        last, stack, res = 0, [], [0]*n
        
        for i in range(len(logs)):
            fid, state, time = logs[i].split(':')
            fid, time = int(fid), int(time)
            
            if state == 'start':
                if stack: 
                    res[stack[-1]] += time - last
                stack.append(fid)
                last = time
            else:
                res[stack.pop()] += time - last + 1
                last = time + 1
        return res