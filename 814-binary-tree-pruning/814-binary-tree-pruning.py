# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
left = 
right = 

val = node.val
val == 0 and left == 0 and right == 0:
    node.left = None
    node.right = None
    node = None
elif left == 0 and right == 0:
    node.left = None
    node.right = None
elif left == None:
    node.left = None
elif right == None:
    node.right = None
    
return node
 

'''
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        
        def dfs(node):
            if not node: return None
            node.left = dfs(node.left) 
            node.right = dfs(node.right)
            if node.val == 0 and not node.left and not node.right:
                node = None
            return node
        return dfs(root)