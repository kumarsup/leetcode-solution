"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
'''
head, curr, tail


'''
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        nodelist = []
        
        def dfs(node):
            nonlocal nodelist
            if not node: return 
            dfs(node.left)
            nodelist.append(node)
            dfs(node.right)
        dfs(root)
        
        head, curr = None, None
        last = TreeNode(-1)
        
        for node in nodelist:
            curr = TreeNode(node.val)
            
            if not head:
                head = TreeNode(-1)
                head.right = curr
                
            curr.left = last
            last.right = curr
            last = curr
            
        head.right.left = last
        last.right = head.right
        return head.right
            