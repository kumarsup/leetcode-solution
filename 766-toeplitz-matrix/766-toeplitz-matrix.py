'''



DS:
hashmap = {key, vslue}  
key = abs(r-c)

ALGO:
    - iterate on the matrix
    - check if key exist and value is not same then return False
    - return True

TC - O(r*c)
TC - O(r+c)

'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagset, rows, cols = defaultdict(set), len(matrix), len(matrix[0])
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r-1][c-1] != matrix[r][c]: return False
        return True
        
                
        