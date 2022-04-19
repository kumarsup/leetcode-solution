class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            newIndex = abs(nums[i]) -1
            
            if nums[newIndex] > 0:
                nums[newIndex] *=-1
        res = []
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                res.append(i)
        return res
        
        
        
        
#         n = len(nums)
#         hset = set(nums)
#         res = []
        
#         for num in range(1, n+1):
#             if num not in hset:
#                 res.append(num)
#         return res
        