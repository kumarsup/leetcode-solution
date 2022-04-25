# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res, to_delete = [], set(to_delete)
        
        def dfs(node, arr = []):
            nonlocal res, to_delete
            if not node: return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.val in to_delete:
                if node.left: res.append(node.left)
                if node.right: res.append(node.right)
                node = None
            
            return node
        
        node = dfs(root)
        if node: res.append(node)
        return res
                