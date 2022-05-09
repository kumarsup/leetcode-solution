'''
prefix sum
sumMap = {}


'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, n, sumMap, sumA = 0, len(nums), {0: 1}, 0
        
        for num in nums:
            sumA += num
            
            if sumA-k in sumMap:
                count += sumMap[sumA-k]
            if sumA not in sumMap:
                sumMap[sumA] = 0
            sumMap[sumA] += 1
        return count