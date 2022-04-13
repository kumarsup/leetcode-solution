class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(path, start, end):
            nonlocal res
            if len(path) == 2*n:
                res.append(path)
                return 
            
            if start < n:
                path = path + '('
                backtrack(path, start+1, end)
                path = path[:-1]
                
            if end < start:
                path = path + ')'
                backtrack(path, start, end+1)
                
        backtrack('', 0, 0)
        return res