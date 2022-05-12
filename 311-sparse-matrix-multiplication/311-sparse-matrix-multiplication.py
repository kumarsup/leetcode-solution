'''
mat1 - m * k
mat2 - k * n
ans - m*n

ans[r][c] = loop from 0 to r for c col- + mat[]

TC - O(m * )
'''
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat1), len(mat2[0])
        res = [[0] * cols for _ in range(rows)]
        
        for rid, row in enumerate(mat1):
            for id, rval in enumerate(row):
                if rval:
                    for cid, cval in enumerate(mat2[id]):
                        res[rid][cid] += rval*cval
        return res
        
                    