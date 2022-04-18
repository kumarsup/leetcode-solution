class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smallCount = 0
        targetCount = 0
        
        for num in nums:
            if num < target: smallCount += 1
            if num == target: targetCount += 1
        return range(smallCount, smallCount+targetCount)
        
        
#         nums.sort()
#         res = []

#         for i, num in enumerate(nums):
#             if num == target:
#                 res.append(i)
#         return res
                
            