class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        
        for idx in range(n):
            i, j = idx, idx        
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    break
                res+=1
                i -= 1
                j += 1
            
            i, j = idx, idx+1       
            while i >= 0 and j < n:
                if s[i] != s[j]:
                    break
                res+=1
                i -= 1
                j += 1
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
                
                
            
        
        