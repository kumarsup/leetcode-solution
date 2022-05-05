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
lowest common ancestor-  meanse? - lowset common node which is the parent of both the noth node or branch
    - what if node == p or node == q ?
    - what if p or q not exist in tree?
    
Approach - 
    - use set- 
    - start from p and add the node to hashmap
    - start from q and check if the node exist in hashmap
    
TC - O(N)
SC - O(N)

Approach 2:
    - traverse p parent or q parent and check until p != q
    - 
TC - O(n)
SC - O(1)
'''
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        origP, origQ = p, q
        while p != q:
            p = p.parent if p.parent else origQ
            q = q.parent if q.parent else origP
        return p
            