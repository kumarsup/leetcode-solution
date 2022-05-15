class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1 > n2: return self.isOneEditDistance(t, s)
        if n2 - n1 > 1: return False
        for i in range(n1):
            if s[i] != t[i]:        
                if n1 == n2: return s[i+1:] == t[i+1:]
                else: return s[i:] == t[i+1:]
        return n1 + 1 == n2  
            