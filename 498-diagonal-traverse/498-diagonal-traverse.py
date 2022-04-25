'''
[1,2,3]
[4,5,6]
[7,8,9]

m = len(mat)
n = len(mat[0])
res = []
rn, cn = -1, 1
r, c
    - while len(res) < m*n and 0 <= r < rows and 0 <= c < cols  
        -val = mat[r][c]
        res.append(val)
        - r = r + rn
        - c = c + cn
        if r < 0: r = 0
        if r >= rows: r = row-1
        
        if c < 0: c = 0
        if c >= cols: c = cols-1
        
        rn = rn*-1
        cn = cn*-1


'''

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        rows = len(mat)
        cols = len(mat[0])
        maps = defaultdict(list)
        
        for r in range(rows):
            for c in range(cols):
                maps[r+c].append(mat[r][c])

        res = []
        xx = -1
        
        def reverse(nums):
            left, right = 0, len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
            return nums
            
        for vals in maps.values():
            if xx < 0:
                vals = reverse(vals)
            res+=vals
            xx*=-1
        return res