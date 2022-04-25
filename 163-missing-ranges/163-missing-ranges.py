'''
nums = [0,1,3,50,75], lower = 0, upper = 99
nums = [0,0,1,3,50,75,99]
i = 2
prev = 1
curr = 3

curr - prev > 1 -> True
    - prev + 2 == curr:
        str(prev+1)
    - prev+1, -> , curr-1
'''

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        def formatRange(lower, upper):
            if lower + 2 == upper:
                return str(lower+1)
            return str(lower+1) + "->" + str(upper-1)
        
        nums = [lower-1] + nums + [upper+1]
        res, n = [], len(nums)
        
        for i in range(1, n):
            prev, curr = nums[i-1], nums[i]
            if curr - prev > 1:
                val = formatRange(prev, curr)
                res.append(val)
        return res
        
        