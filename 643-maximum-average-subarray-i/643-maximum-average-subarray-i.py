'''
avg
total sum
left
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        best = now = sum(nums[:k])
        for i in range(k, n):
            now += nums[i] - nums[i-k]
            if now > best:
                best = now
        return best/k
            