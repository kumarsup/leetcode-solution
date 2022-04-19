class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0: -1}
        total = 0
        
        for i, num in enumerate(nums):
            total += num
            key = total%k
            
            if key not in hash_map:
                hash_map[key] = i
            elif i - hash_map[key] > 1:
                return True
        return False