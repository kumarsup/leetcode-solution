'''
avg
total sum
left
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        maxAvg, sumA, left = float('-inf'), 0, 0
        
        for right in range(n):
            sumA += nums[right]
            if right - left + 1 > k:
                sumA -= nums[left]
                left += 1
                
            if right - left + 1 == k:
                sign = 1
                totalSum = sumA
                if totalSum < 0:
                    sign = -1
                    totalSum *= sign
                maxAvg = max(maxAvg, (totalSum/k)*sign)
        return maxAvg