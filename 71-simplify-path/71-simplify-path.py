class Solution:
    def simplifyPath(self, path: str) -> str:
        pList, stack = path.split('/'), []
        for val in pList:
            if val == '..':
                if stack: stack.pop()
            elif val and val != '.':
                stack.append(val)
        return '/'+ '/'.join(stack)
