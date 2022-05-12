'''
grid = [[0]*n for _ in range(n)]
grid[row][col] = player

rows
cols
diags
'''
class TicTacToe:
    def __init__(self, n: int):
        self.rows = [0]*n
        self.cols = [0]*n
        self.posDiag = 0
        self.negDiag = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        currPlayer = 1 if player == 1 else -1
        n = len(self.rows)
        
        self.rows[row] += currPlayer
        self.cols[col] += currPlayer
        
        if row == col:
            self.posDiag += currPlayer
        
        if row + col == n-1:
            self.negDiag += currPlayer
            
        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.posDiag) == n or abs(self.negDiag) == n:
            return player
        return 0