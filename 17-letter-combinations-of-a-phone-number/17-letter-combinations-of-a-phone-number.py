class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, n = [], len(digits)
        digitsMap = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if n < 1:
            return []
            
        def backtrack(comb = [], index = 0):
            nonlocal res
            
            #basecases - condition
            if len(comb) == n:
                res.append(''.join(comb))
                return
            
            if index == n:
                return
            
            digit = digits[index]
            
            for char in digitsMap[digit]:
                comb.append(char)
                backtrack(comb, index+1)
                comb.pop()
                
        backtrack()
        return res
                
                