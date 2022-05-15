class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        rows = len(nums)
        mapping = defaultdict(list)
        
        for r in range(rows):
            for c in range(len(nums[r])):
                mapping[r+c+1].append(nums[r][c])
        res = []
        
        for value in mapping.values():
            res.extend(value[::-1])
        return res