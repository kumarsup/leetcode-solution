class Solution:
    def minInsertions(self, s: str) -> int:
        opening, closing = 0, 0
        i, n = 0, len(s)
        
        while i < n:
            if s[i] == '(':
                opening += 1
            elif s[i] == ')':
                if i == n-1 or s[i+1] != ')':
                    closing += 1
                else:
                    i+=1
                
                if opening:
                    opening -= 1
                else:
                    closing += 1
            i+=1
        return opening * 2 + closing