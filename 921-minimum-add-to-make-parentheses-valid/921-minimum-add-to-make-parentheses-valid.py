'''

'''
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count, stack = 0, []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    count+=1
        return count + len(stack)