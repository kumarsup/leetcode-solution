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
        sumA, maxLen, n = 0, 0, len(nums)
        hashmap = {}
        
        for right in range(n):
            sumA += nums[right]
            
            if sumA == k:
                maxLen = right + 1
                
            if sumA-k in hashmap:
                index = hashmap[sumA-k]
                maxLen = max(maxLen, right - index)
                
            if sumA not in hashmap:
                hashmap[sumA] = right
        return maxLen
            