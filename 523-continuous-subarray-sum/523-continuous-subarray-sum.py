class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0:-1}
        total = 0
        for i,num in enumerate(nums):
            total += num
            remainder = total%k
            
            if remainder not in hash_map:
                hash_map[remainder] = i
            elif i - hash_map[remainder] > 1:
                return True
        
        return False
                