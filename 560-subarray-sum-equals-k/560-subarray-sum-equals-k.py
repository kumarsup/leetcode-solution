'''
prefix sum
sumMap = {}


'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, summap = 0, {0: 1}
        sumA = 0
        
        for num in nums:
            sumA += num
            if sumA - k in summap: 
                count += summap[sumA-k]
            if sumA not in summap:
                summap[sumA] = 0
            summap[sumA] += 1
        return count
            
                