'''
use two pointer approach - 
if left != right - try left+1 or right-1
    - any of this true then return true else return false
TC- O(N)
SC- O(1)

'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n-1
        
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]: return False
                left, right = left+1, right-1
            return True
        
        while left < right:
            if s[left] != s[right]: 
                return isPalindrome(left+1, right) or isPalindrome(left, right-1)
            left, right = left+1, right-1
        return True
        
        