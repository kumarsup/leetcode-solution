'''
[1,5,9], k -3 = 8-3 = 5
[10,11,13] -3 = 5-3 = 2
[12,13,15] - find 2nd element from this row
row and cols are in assending orders
cols
k = 8
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])    
        heap = []
        
        for r in range(rows):
            heapq.heappush(heap, (matrix[r][0], r, 0))
            
        while k:
            item, r, c = heapq.heappop(heap)
            if c < cols-1:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
            k-=1
        return item