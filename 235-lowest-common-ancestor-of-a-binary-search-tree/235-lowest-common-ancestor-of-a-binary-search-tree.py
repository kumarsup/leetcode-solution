'''

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        def dfs(node):
            if not node: return None
            left = dfs(node.left)
            right = dfs(node.right)
            if (left and right) or node == p or node == q:
                return node
            return left or right
        return dfs(root)
            