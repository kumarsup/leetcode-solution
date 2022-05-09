class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = set()
        
        for i, num in enumerate(nums):
            if num in hset: return True
            hset.add(num)
            if len(hset) > k:
                hset.remove(nums[i-k])
        return False
        