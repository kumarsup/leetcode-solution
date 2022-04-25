'''

'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumA = 0
        n, hashmap = len(nums), {0: 1}
        count = 0
        
        for num in nums:
            sumA += num
            if sumA - k in hashmap:  count += hashmap[sumA-k]
            if sumA in hashmap: hashmap[sumA] += 1
            else: hashmap[sumA] = 1
        return count