# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NodeValue:
    def __init__(self, min_node = float('inf'), max_node = float('-inf'), max_size = 0):
        self.min_node = min_node
        self.max_node = max_node
        self.max_size = max_size


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def getMaxBSTTree(node):
            if not node: return NodeValue()
            left = getMaxBSTTree(node.left)
            right = getMaxBSTTree(node.right)
            
            if left.max_node < node.val < right.min_node:
                return NodeValue(min(node.val, left.min_node), max(node.val, right.max_node), left.max_size + right.max_size +1)
            return NodeValue(float('-inf'), float('inf'), max(left.max_size, right.max_size))
        
        return getMaxBSTTree(root).max_size
        
    
                 
                 
          