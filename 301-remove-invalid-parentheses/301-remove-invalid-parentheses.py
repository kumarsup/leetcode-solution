'''
"()())()"
 - "()()()"
 - "(())()"
'''
class Solution:
    
    def __init__(self):
            self.validExpresions = set()
            self.minRemoved = float('inf')
            
    def removeInvalidParentheses(self, s: str) -> List[str]:
            
        def remaining(index, leftCount, rightCount, expr, remCount):
            if index == len(s):
                if leftCount == rightCount:
                    if remCount <= self.minRemoved:
                        ans = ''.join(expr)
                        if remCount < self.minRemoved:
                            self.validExpresions = set()
                            self.minRemoved = remCount
                        self.validExpresions.add(ans)
            else:
                currChar = s[index]
                if currChar != '(' and currChar != ')':
                    expr.append(currChar)
                    remaining(index+1, leftCount, rightCount, expr, remCount)
                    expr.pop()
                else:
                    remaining(index+1, leftCount, rightCount, expr, remCount+1)
                    
                    expr.append(currChar)
                    if currChar == '(':
                        remaining(index+1, leftCount+1, rightCount, expr, remCount)
                    elif rightCount < leftCount:
                        remaining(index+1, leftCount, rightCount+1, expr, remCount)
                    expr.pop()
                    
        remaining(0, 0, 0, [], 0)
        return self.validExpresions
                
                            
                    