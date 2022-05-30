class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        slist = list(s)
        
        for i in range(len(s)):
            char = s[i]
            
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    slist[i] = '' 
        while stack:
            slist[stack.pop()] = ''
            
        return ''.join(slist)