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
        i, j = 0, n-1
        
        while i < j:
            if i < n and not s[i].isalnum():
                i+=1
                continue
                
            if j >= 0 and not s[j].isalnum():
                j-=1
                continue
                
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True