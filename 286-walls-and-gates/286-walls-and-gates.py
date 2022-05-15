'''
[[2147483647,-1,0,2147483647],
[2147483647,2147483647,2147483647,-1],
[2147483647,-1,2147483647,-1],
[0,-1,2147483647,2147483647]]

'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        MOVES = [(1, 0), (0, 1), (-1, 0),(0, -1)]
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    
        while queue:
            r, c = queue.popleft()        
            for move in MOVES:
                row = r + move[0]
                col = c + move[1]
                if 0 <= row < rows and 0 <= col < cols and rooms[row][col] != -1 and rooms[row][col] == 2147483647:
                    rooms[row][col] = rooms[r][c] + 1
                    queue.append((row, col))