'''
s = "lee(t(c ) o ) de )"
"lee(t(c)o)de"

validate stack - 
    - add index in stack on start brackets (
    - pop index in stack on start brackets )
    - if cant pop then keep the index in stack
    
arr = list(s)
stack = 

validate parentheses
    if c == '('
        - stack = add i
    elif c == ')'
        if stack: stack pop
        else
            arr[i] = ''
while stack:
    arr[stack.pop()] = ''
return ''.join(arr)

TC - O(N)
SC - O(N)

'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, arr = [], list(s)
        
        for index in range(len(arr)):
            if arr[index] == '(':
                stack.append(index)
            elif arr[index] == ')':
                if stack:
                    stack.pop()
                else:
                    arr[index] = ''
        while stack:
            arr[stack.pop()] = ''
        
        return ''.join(arr)
        