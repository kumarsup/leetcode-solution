class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.count = size
        
    def find(self, x):
        while x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            self.count-=1

            
class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        unionFind = UnionFind(rows)
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 and r != c:
                    unionFind.union(r, c)
        return unionFind.count
                    
        