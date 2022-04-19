class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        MOVES = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        
        landSize = defaultdict(int)
        
        def colorLand(r, c, landId):
            grid[r][c] = landId
            landSize[landId] += 1
            
            for move in MOVES:
                rn = r + move[0]
                cn = c + move[1]
                if 0 <= rn < rows and 0 <= cn < cols and grid[rn][cn] == 1:
                    colorLand(rn, cn, landId)
        
        landId = 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    landId+=1
                    colorLand(r, c, landId)
                    
        def neighbors(r, c):
            res = []
            for move in MOVES:
                rn = r + move[0]
                cn = c + move[1]
                if 0 <= rn < rows and 0 <= cn < cols and grid[rn][cn] != 0:
                    res.append((rn, cn))
            return res
            
        res = max(landSize.values() or [0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    res = max(res, 1 + sum(landSize[i] for i in seen))
        return res
                    
        
        