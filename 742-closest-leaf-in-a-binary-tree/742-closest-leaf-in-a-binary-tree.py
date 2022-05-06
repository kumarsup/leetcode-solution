# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
target = 
leaf node =
update parent in each node- 
and then BFS - if we reach leaf node then return leaf node

TC- O(N)
SC- O(N)

root to leaf dist
root to target dist
    - if same subtree then dist = rootToLeaf - rootToTarget
    - if not same subtree- dist = rootToLeaf + rootToTarget
    - use min heap find min dist leaf and return
'''

class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        
        parents = defaultdict(TreeNode)
        target, minDist, res = None, float('inf'), None
        
        def updateParentDFS(node, parent = None):
            nonlocal parents, target
            if not node: return
            parents[node] = parent
            if node.val == k:
                target = node
            updateParentDFS(node.left, node)
            updateParentDFS(node.right, node)
        
        updateParentDFS(root)
        
        queue = deque([(target, 0)])
        visited = set()
        
        while queue:
            
            node, distance = queue.popleft()
            if not node.left and not node.right and minDist > distance:
                res = node
                minDist = distance
                
            if node in visited: continue
            visited.add(node)
            
            if node.left:
                queue.append((node.left, distance + 1))

            if node.right:
                queue.append((node.right, distance + 1))

            if parents[node] and parents[node] not in visited:
                queue.append((parents[node], distance + 1))
        
        return res.val
            
            
            
            
            
            
            
            
            
            
            
            
            