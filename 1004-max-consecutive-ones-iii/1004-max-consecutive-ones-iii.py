'''
nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2

left, sumA
r-l+1 > sumA + k:
    sumA -= nums[left]
    left += 1
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, sumA, n, maxLen = 0, 0, len(nums), 0
        
        for right in range(n):
            sumA += nums[right]
            if sumA + k < right - left + 1:
                sumA -= nums[left]
                left += 1
            maxLen = max(maxLen, right-left+1)
        
        return maxLen
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(nums)
        
#         left, sumA, res = 0, 0, 0
        
#         for right in range(n):
#             sumA += nums[right]
#             if right-left+1 > sumA+k:
#                 sumA -= nums[left]
#                 left += 1
#             res = max(res, right-left+1)
#         return res