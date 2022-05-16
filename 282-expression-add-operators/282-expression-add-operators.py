'''
operators = ['+', '-', '/', '*']
list of chars
index, prev, curr, val, path
0   0   0   0   []

curr = curr*10 + int(s[index])

NO OPP:
backtrack(index+1, prev, curr, val, path)
 
if path:

    #ADD
    
    
    #SUBSTRACTION
    
    
    #MULTIPLEICATION
 
 

'''
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res, n = [], len(num)
        
        def backtrack(index, prev, curr, val, path):
            if index == n:
                if val == target and curr == 0:
                    res.append(''.join(path[1:]))
                return
            
            curr = curr*10 + int(num[index])
            currOP = str(curr)
            
            if curr > 0:
                #NO OPP
                backtrack(index+1, prev, curr, val, path)
                
            #ADD
            path.append('+')
            path.append(currOP)
            backtrack(index+1, curr, 0, val+curr, path)
            path.pop()
            path.pop()
            
            if path:
                #SUBS
                path.append('-')
                path.append(currOP)
                backtrack(index+1, -curr, 0, val-curr, path)
                path.pop()
                path.pop()
                
                #MULTI
                path.append('*')
                path.append(currOP)
                backtrack(index+1, prev*curr, 0, val-prev + (prev*curr), path)
                path.pop()
                path.pop()
            
        backtrack(0, 0, 0, 0, [])
        return res

            
            
            
            
            