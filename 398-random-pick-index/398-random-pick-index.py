'''
target = 
index = 
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)
        for idx in range(len(nums)):
            self.map[nums[idx]].append(idx) 
        
    def pick(self, target: int) -> int:
        index = choice(self.map[target])
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)