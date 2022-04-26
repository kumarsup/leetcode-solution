class Solution:
    def trap(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0]*n
        lastMax = float('-inf')
        
        for i in range(n-1, -1, -1):
            lastMax = max(lastMax, nums[i])
            arr[i] = lastMax
            
        left, res = nums[0], 0
        for i in range(1, n):
            
            right = arr[i]
            waterH = min(left, right) - nums[i]
            if waterH > 0:
                res += waterH
            left = max(left, nums[i])
        return res
        
            