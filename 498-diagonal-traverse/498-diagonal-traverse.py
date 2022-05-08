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
        rows, cols = len(mat), len(mat[0])
        r, c, res = 0, 0, []
        direction = 1
        
        while r < rows and c < cols:
            res.append(mat[r][c])
            if direction == 1:
                if r == 0 and c < cols-1:
                    c += 1
                    direction*=-1
                elif c == cols-1:
                    r+=1
                    direction*=-1
                else:
                    r-=1
                    c+=1
            else:
                if c == 0 and r < rows-1:
                    r+=1
                    direction *= -1
                elif r == rows-1:
                    c+=1
                    direction *= -1
                else:
                    r+=1
                    c-=1
        return res
                    
                    
        