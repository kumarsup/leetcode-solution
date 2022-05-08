'''
nums = [1,-1,5,-2,3], k = 3
maxSize - subarray -  sum is equals to k

[1,-1,5,-2,3]
sorted ?
negative numbers?

size of the array- ?
range of numebrs- ?
range of k - ?


hashmap - {0, -1}
sumA-k in hashmap - get the index 
len = max(len, curr - i + 1)

return len
'''
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sumA, maxLen, n, idxMap = 0, 0, len(nums), {0:-1}
        for idx in range(n):
            sumA += nums[idx]
            if sumA-k in idxMap: maxLen = max(maxLen, idx - idxMap[sumA-k])
            if sumA not in idxMap: idxMap[sumA] = idx
        return maxLen
    