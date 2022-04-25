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
        nums = [lower-1] + nums + [upper+1]
        n, res = len(nums), []
        
        def formatValue(low, high):
            if low + 2 == high:
                return str(low+1)
            return str(low+1) + '->' + str(high-1)
        
        for i in range(1, n):
            prev, curr = nums[i-1], nums[i]
            if curr - prev > 1:
                val = formatValue(prev, curr)
                res.append(val)
        return res
                
       