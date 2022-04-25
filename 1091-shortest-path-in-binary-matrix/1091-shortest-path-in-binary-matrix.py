class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minSteps = float('inf')
        MOVES = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        queue = deque([(0, 0, 1)])
        seen = set()
        
        while queue:
            r, c, step = queue.popleft()
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and (r, c) not in seen:
                seen.add((r, c))
                if r == rows-1 and c == cols-1: minSteps = min(minSteps, step)    
                for move in MOVES:
                    rn = r + move[0]
                    cn = c + move[1]
                    queue.append((rn, cn, step+1))  
        return minSteps if minSteps != float('inf') else -1