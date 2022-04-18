'''
[4,3,2,-1],
[3,2,1,-1],
[1,1,-1,-2],
[-1,-1,-2,-3]

rows, cols
0, cols-1
count
'''
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count, r, c = 0, 0, cols-1
        
        while r < rows:
            while c >= 0 and grid[r][c] < 0:
                c -= 1
            r += 1 
            count += cols - c - 1
        return count
            
            
                