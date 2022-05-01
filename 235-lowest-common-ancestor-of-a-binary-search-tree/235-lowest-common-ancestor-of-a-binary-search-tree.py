'''

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        def dfs(node):
            if not node: return None
            
            left, right = None, None
            
            if node.val > p.val or node.val > q.val:
                left = dfs(node.left)
                
            if node.val < p.val or node.val < q.val:    
                right = dfs(node.right)
                
            if (left and right) or node in [p, q]:
                return node
            
            return left or right
        
        return dfs(root)
            