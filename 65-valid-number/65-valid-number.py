'''
    regex - 
    - write validate functions
        - digit, dot, e, sign
        - +/- only can be at 0th index or just after e
        - e should be after digit and before few digit
        - . can be only once and only before e        

digitSeen, expoSeen, dotSeen
for sign = can be the first char or first char after e or E
return digitSeen
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        digitSeen, expoSeen, dotSeen = False, False, False
        n = len(s)
        
        for i in range(n):
            if s[i].isdigit():
                digitSeen = True
            elif s[i] in '+-':
                if i > 0 and s[i-1] not in 'eE': return False
            elif s[i] == '.':
                if dotSeen or expoSeen: return False
                dotSeen = True
            elif s[i] in 'eE':
                if not digitSeen or expoSeen: return False
                expoSeen = True
                digitSeen = False
            else: 
                return False
        return digitSeen
        
        