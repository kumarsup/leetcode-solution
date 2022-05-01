'''
    regex - 
    - write validate functions
        - digit, dot, e, sign
        - +/- only can be at 0th index or just after e
        - e should be after digit and before few digit
        - . can be only once and only before e
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        seenDigit, seenExpo, seenDot = False, False, False
        
        for i, c in enumerate(s):
            if c.isdigit():
                seenDigit = True
            elif c in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif c in 'eE':
                if seenExpo or not seenDigit: return False
                seenExpo = True
                seenDigit = False
            elif c == '.':
                if seenDot or seenExpo: return False
                seenDot = True
            else:
                return False
        return seenDigit
                
            