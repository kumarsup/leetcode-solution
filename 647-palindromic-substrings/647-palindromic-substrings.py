class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        
        def countPalindrome(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left, right, count = left-1, right+1, count+1
            return count
        
        for idx in range(n):
            res += countPalindrome(idx, idx)
            res += countPalindrome(idx, idx+1)
        return res
        
        

        
        
        
#         n = len(s)
#         res = n
        
#         def isPalindrom(path):
#             print(path)
#             left, right = 0, len(path)-1
#             while left < right:
#                 if path[left] != path[right]:
#                     return False
#                 left, right = left + 1, right-1
#             return True
        
#         def backtrack(path = [], index = 0):
#             nonlocal res
            
#             if len(path) > 1 and isPalindrom(path):
#                 res += 1
            
#             for idx in range(index, n):
#                 path.append(s[idx])
#                 backtrack(path, idx+1)
#                 path.pop()
                
#         backtrack()
#         return res
                
                
            
        
        