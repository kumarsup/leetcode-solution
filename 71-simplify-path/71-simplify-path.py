class Solution:
    def simplifyPath(self, path: str) -> str:
        pList = path.split('/')
        stack = []
        
        for val in pList:
            if val == '..' and stack:
                stack.pop()
            elif val and val != '.' and val != '..':
                stack.append(val)
        return '/'+'/'.join(stack)
            