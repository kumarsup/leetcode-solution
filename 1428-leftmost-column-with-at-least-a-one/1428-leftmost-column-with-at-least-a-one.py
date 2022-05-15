# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

'''
rows, cols = api call
r, c get item - api call

binary search in each row, find most left 1 col in every row and then keep the result
'''
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        minCol = float('inf')
        
        for row in range(rows):
            found, left, right = False, 0, cols-1
            
            while left <= right:
                mid = (left + right)//2
                val = binaryMatrix.get(row, mid)
                if val == 1:
                    found = True
                    right = mid-1
                else:
                    left = mid+1
            
            if found:
                minCol = min(minCol, right+1)
                
        return minCol if minCol != float('inf') else -1
            
            
                    
                