"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

'''
right
'''

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        origP, origQ = p, q
        while p!= q:
            p = p.parent if p.parent else origQ
            q = q.parent if q.parent else origP
        return p
        
#         hset = set()
#         node = p
        
#         while node:
#             hset.add(node)
#             node = node.parent
#         node = q
#         while node:
#             if node in hset: return node
#             node = node.parent
#         return None
            