class Solution:
    def minInsertions(self, s: str) -> int:
        ret=0
        s = s.replace('))', ']')
        ret+=s.count(')')
        s = s.replace(')', ']')
        bal = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                bal += 1
            elif ch == ']':
                bal-=1
            if bal == -1:
                bal+=1
                ret+=1
        return ret + bal *2
        
        