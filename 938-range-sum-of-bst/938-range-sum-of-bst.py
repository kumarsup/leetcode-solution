# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        res = 0
        
        def dfs(node):
            nonlocal res
            if not node: return 
            if node.val >= low and node.val <= high:
                res += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        dfs(root)
        return res
            
            