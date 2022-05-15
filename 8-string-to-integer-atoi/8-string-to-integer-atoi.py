'''
1. leading white space - ignore - not digitSeen
2. + or - can be before the digits - not degitSeen - keep sign
3. non digit char can be in the last-ignore it shold not have digit after this - nondigitSeen
4. if convert it to int
32 bit - -2^31 < num < 2^31-1

'''
class Solution:
    def myAtoi(self, s: str) -> int:
        degitSeen, signSeen, nonDigitSeen = False, False, False
        sign = 1
        res = 0
        index = 0
        n = len(s)
        
        #white space -ignore
        while index < n and s[index] == ' ':
            index+=1
            
        #sign = +1 or -1
        if index < n and s[index] == '+':
            sign = 1
            index+=1
        elif index < n and s[index] == '-':
            sign = -1
            index+= 1
            
        #traverse next digit of input and stop if not a digit
        while index < n and s[index].isdigit():
            digit = int(s[index])
            res = res*10 + digit
            index+=1
        res = sign*res
        if -2**31 < res < 2**31 - 1: return res
        
        return -2**31 if sign == -1 else 2**31-1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        