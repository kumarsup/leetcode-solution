'''
nums length - n
fisrt, last from the nums
if first is smaller than k - return k
if n is equals to last:
    - if last is less than k: return k
    - while loop i < k-first for missing numser: return val


'''
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n, diff = len(nums), 0
        for i in range(1, n):
            diff = nums[i] - nums[i-1] - 1
            if diff >= k: return nums[i-1]+k
            k -= diff
        return nums[n-1] + k
        
        