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
        self.diagonal = 0
        self.antidiagonal = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        curPlayer = 1 if player == 1 else -1
        
        n = len(self.rows)
        
        self.rows[row] += curPlayer
        self.cols[col] += curPlayer
        
        if row == col: 
            self.diagonal += curPlayer
            
        if row+col == n-1: 
            self.antidiagonal += curPlayer
            
        if (abs(self.rows[row]) == n) or (abs(self.cols[col]) == n) or  (abs(self.diagonal) == n) or (abs(self.antidiagonal) == n):
            return player
        
        return 0
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)