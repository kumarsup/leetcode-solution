class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastPos = n-1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0
        
        
        
        
        
#         def backtrack(index):
#             nonlocal res
            
#             if index > n-1:
#                 return False
                
#             if index == n-1:
#                 res = True
#                 dp[index] = True
#                 return True
            
#             if dp[index] is not None: 
#                 return dp[index]
            
#             maxNum = nums[index]
#             maxJump = min(index+maxNum+1, n)
#             for idx in range(index+1, maxJump):
#                 dp[index] = backtrack(idx)
#             dp[index] = False
#             return False
#         backtrack(0)
#         return res
                
            