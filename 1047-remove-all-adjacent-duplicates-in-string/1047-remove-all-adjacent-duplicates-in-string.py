'''
s = "abbaca"

stack - []
loop 0->n-1
while stack[-1] == s[i]: stack.pop()

else:
    stack.append(s[i])
return ''.join(stack)
'''
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack, n = [], len(s)
        
        for i in range(n):
            found = False
            while stack and stack[-1] == s[i]:
                stack.pop()
                found = True
            if not found:
                stack.append(s[i])
        return ''.join(stack)
        