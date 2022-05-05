class SparseVector:
    
    def __init__(self, nums: List[int]):
        self.map = defaultdict(int)
        for i, num in enumerate(nums):
            if num != 0:
                self.map[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        
        for key, val in vec.map.items():
            if key in self.map:
                res += self.map[key] * val
        return res
                

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)