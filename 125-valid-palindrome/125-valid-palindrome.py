'''
two pointer approach - i, j
    - if val not a valid char then increament the index or decreament the indesx and continue
    if left char not equals to right then return False - to lower
    
TC - O(N)
SC - O(1)
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n-1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left, right = left+1, right-1
        return True