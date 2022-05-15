class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        rows, cols = len(grid), len(grid[0])
        arr = []
        for r in range(rows):
            arr += grid[r]
        
        arr.sort()
        median = arr[len(arr)//2]
        operation = 0
        
        for val in arr:
            val = abs(val-median)
            if val%x != 0:
                return -1
            operation += val//x
        return operation
        