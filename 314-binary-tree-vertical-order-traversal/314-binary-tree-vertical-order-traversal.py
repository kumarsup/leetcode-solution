# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        hashmap = defaultdict(list)
        minIndex, maxIndex = float('inf'), float('-inf')
        
        def dfs(node, row = 0, col = 0):
            nonlocal minIndex, maxIndex, hashmap
            if not node: return
            minIndex = min(minIndex, col)
            maxIndex = max(maxIndex, col)
            
            hashmap[col].append((node.val, row))
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1) 
            
        dfs(root)
        res = []
        #print(minIndex, maxIndex, hashmap)
        for col in range(minIndex, maxIndex+1):
            val = [val for val, row in sorted(hashmap[col], key = lambda x: x[1])]
            res.append(val)
        return res
            
        
        
        
            