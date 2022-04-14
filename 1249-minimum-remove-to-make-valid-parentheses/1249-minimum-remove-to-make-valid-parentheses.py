class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        stack = []
        
        for i in range(n):
            char = s[i]
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        slist = list(s)
        for idx in stack:
            slist[idx] = ''
        return ''.join(slist)
                
            