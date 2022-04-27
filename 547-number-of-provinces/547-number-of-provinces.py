class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            self.root[rootY] = rootX
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)
'''
[1,0,0,1],
[0,1,1,0],
[0,1,1,1],
[1,0,1,1]]
'''        
        
class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
#         graph = defaultdict(list)
#         for r in range(rows):
#             for c in range(cols):
#                 if mat[r][c] == 1:
#                     graph[r].append(c)
#                     graph[c].append(r) 
#         def dfs(node, seen):
#             if node not in seen:
#                 seen.add(node)
#                 for nei in graph[node]:
#                     dfs(nei, seen)               
#         count, seen = 0, set()
#         for r in range(rows):
#             if r not in seen:
#                 count += 1
#                 dfs(r, seen)              
#         for c in range(cols):
#             if c not in seen:
#                 count += 1
#                 dfs(c, seen)            
#         return count

    
        uFind = UnionFind(rows)
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 and r != c:
                    uFind.union(r, c)
        count = 0
        provinces = set()
        
        for r in range(rows):
            root = uFind.find(r)
            provinces.add(root)
            
        for c in range(cols):
            root = uFind.find(c)
            provinces.add(root)
      
        return len(provinces)