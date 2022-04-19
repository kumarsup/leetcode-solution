class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hset = set(nums)
        res = []
        
        for num in range(1, n+1):
            if num not in hset:
                res.append(num)
        return res
        