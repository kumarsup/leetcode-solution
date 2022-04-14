'''
result = 0
lastNum = 0
curNum = 0

if +:
    - result += lastNum
    - lastNum = curNum
if -:
    - result += lastNum
    - lastNum = -curSum
if *:
    - lastNum = lastNum*curNum
if /:
    - lastNum = lastNum/curNum
result += lastNum
return lastNum
 

'''
class Solution:
    def calculate(self, s: str) -> int:
#         if not s or len(s) == 0: return 0
#         n = len(s)
#         curNum = 0
#         lastNum = 0
#         result = 0
#         operation = '+'
        
#         for i in range(n):
            
#             char = s[i]
#             if char.isdigit():
#                 curNum = curNum * 10 + int(char)
                
#             if (not char.isdigit() and char != ' ') or i == n-1:
#                 if operation in '+-':
#                     result += lastNum
#                     lastNum = curNum if operation == '+' else -curNum
#                 elif operation == '*':
#                     lastNum = lastNum * curNum
#                 elif operation == '/':
#                     #remove the sign if number is negative
#                     sign = -1 if lastNum < 0 else 1
#                     lastNum = sign*lastNum // curNum
#                     lastNum = lastNum*sign
#                 operation = char
#                 curNum = 0
#         result += lastNum
            
#         return result
        
        
        
        stack, val, sign = [], 0, '+'
        n = len(s)
        
        for index in range(n):
            char = s[index]
            
            if char.isdigit():
                val = val * 10 + int(char)
            
            if not char.isdigit() and char != ' ' or index == n-1:
                if sign in '+-':
                    val = val if sign == '+' else -val
                    stack.append(val)
                elif sign == '*':
                    stack.append(stack.pop()*val)
                elif sign == '/':
                    top = stack.pop()
                    sign = -1 if top < 0 else 1
                    value = top*sign//val
                    stack.append(value*sign)
                sign = char
                val = 0
        return sum(stack)
            
                
            
                
            
            