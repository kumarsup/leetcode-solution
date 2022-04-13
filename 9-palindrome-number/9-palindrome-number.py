class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse, sign = 0, -1 if x < 0 else 1
        if sign == -1: return False
        num = x*sign
        
        while num > 0:
            val = num%10
            num = num//10
            reverse = reverse * 10 + val
        return reverse*sign == x