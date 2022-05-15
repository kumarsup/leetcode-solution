# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
tag each node with its depth
maxDepth = max
'''
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        depth = {}
        def dfs(node, d = 0):
            if not node: return
            depth[node] = d
            dfs(node.left, d+1)
            dfs(node.right, d+1)    
        dfs(root)
        maxDepth = max(depth.values())
        
        def helper(node):
            if not node or depth.get(node, None) == maxDepth:
                return node
            left = helper(node.left)
            right = helper(node.right)
            return node if left and right else left or right
        return helper(root)