'''
operators = ['+', '-', '/', '*']
list of chars

backtrack(index = 0, expr, ) 
    if len expr  == n:
        eval(expr) == target:
            res.appand(''.join(path))
            return
            
    for idx in range(index, n):
        op in operators:
            ch + op 
'''
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        res = []
        n = len(num)
        
        def backtrack(index, prev, curr, val, path):
            nonlocal res
            if index == n:
                if val == target and curr == 0:
                    res.append(''.join(path[1:]))
                return
            
            curr = curr*10 + int(num[index])
            str_op = str(curr)
            
            if curr > 0:
                backtrack(index+1, prev, curr, val, path)
            
            #ADD
            path.append('+')
            path.append(str_op)
            backtrack(index+1, curr, 0, val+curr, path)
            path.pop()
            path.pop()
            
            if path:
                #SUBSTRACTION
                path.append('-')
                path.append(str_op)
                backtrack(index+1, -curr, 0, val-curr, path)
                path.pop()
                path.pop()
                
                 #MULTIPLICATION
                path.append('*')
                path.append(str_op)
                backtrack(index+1, curr*prev, 0, val-prev + (curr*prev), path)
                path.pop()
                path.pop()
                
        backtrack(0, 0, 0, 0, [])
        return res
