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

first and last = None, None

in order

dfs() - >
if last:
    last.right = node
    node.left = last
else:
    first = node
last = node
dfs(node.right)



'''
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        first, last = None, None
        
        def dfs(node):
            nonlocal first, last
            if not node: return
            dfs(node.left)
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            dfs(node.right)
        dfs(root)
        first.left = last
        last.right = first
        return first