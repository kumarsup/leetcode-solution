# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        pFound = False
        qFound = False
        
        def dfs(node):
            nonlocal pFound, qFound
            
            if not node: return None
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node == p: pFound = True
            if node == q: qFound = True
            
            if (left and right) or (node == p or node == q):
                return node
            return left or right
        
        node = dfs(root)
        if not pFound or not qFound: return None
        return node
            