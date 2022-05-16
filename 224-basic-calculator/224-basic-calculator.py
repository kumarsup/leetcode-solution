class Solution:
    def calculate(self, s: str) -> int:
        
        def evalExpresion(stack):
            if not stack or type(stack[-1]) == str:
                stack.append(0)
            res = stack.pop()
            while stack and stack[-1] != ')':
                sign = stack.pop()
                
                if sign == '+':
                    res+=stack.pop()
                else:
                    res-=stack.pop()
            return res
        
        
        stack = []
        n, val = 0, 0
        
        for i in range(len(s)-1, -1, -1):
            ch = s[i]
            
            if ch.isdigit():
                val = 10**n*int(ch) + val
                n += 1
            elif ch != ' ':
                if n:
                    stack.append(val)
                    n, val = 0, 0
                    
                if ch == '(':
                    res = evalExpresion(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(ch)
        if n:
            stack.append(val)
        return evalExpresion(stack)
    
                    
                
                