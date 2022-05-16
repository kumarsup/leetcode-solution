'''
k palndrome - 

recursion= (k)

if left != right:
    if k == 0: return False
    return recursion(left+1, right) or recursion(left, right+1)

'''
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        dp = {}
        
        def validatePalindrome(left, right):
            nonlocal dp
            
            if left == right: return 0
            if left == right-1:
                return 1 if s[left] != s[right] else 0
            
            if (left, right) in dp: 
                return dp[(left, right)]
            
            if s[left] == s[right]:
                dp[(left, right)] = validatePalindrome(left+1, right-1)
            else:
                dp[(left, right)] = 1 + min(validatePalindrome(left+1, right), validatePalindrome(left, right-1))
            return dp[(left, right)]
        
        n = len(s)
        return validatePalindrome(0, n-1) <= k
            