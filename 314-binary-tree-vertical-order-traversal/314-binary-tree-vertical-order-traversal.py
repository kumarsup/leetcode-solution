# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        minCol, maxCol = float('inf'), float('-inf')
        
        def dfs(node, hashmap, col = 0, row = 0):
            nonlocal minCol, maxCol
            
            if not node: return
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            
            hashmap[col].append((node.val, row))
            
            dfs(node.left, hashmap, col-1, row+1)
            dfs(node.right, hashmap, col+1, row+1)
            
            
        hashmap = defaultdict(list)
        dfs(root, hashmap)
        res = []
        for col in range(minCol, maxCol+1):
            items = hashmap[col]
            vals = [val for val, row in sorted(items, key = lambda x: x[1])]
            res.append(vals)
        return res