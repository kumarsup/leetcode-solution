'''
    regex - 
    write validate method - 
        - + or - can be only 
            - in the start of the string 
            - after e
        - every digit should be in 0 to 9 and e/E and +- and .
        - +- can me multiple times in start of the string
        - 
        
        

'''
class Solution:
    def isNumber(self, s: str) -> bool:
        seenDigit, seenExponent, seenDot = False, False, False
        
        for i, c in enumerate(s):
            if c.isdigit():
                seenDigit = True
            elif c in ['+', '-']:
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E':
                    return False
            elif c in ['e', 'E']:
                if seenExponent or not seenDigit:
                    return False
                seenExponent = True
                seenDigit = False
            elif c == '.':
                if seenDot or seenExponent: return False
                seenDot = True
            else:
                return False
        return seenDigit
                