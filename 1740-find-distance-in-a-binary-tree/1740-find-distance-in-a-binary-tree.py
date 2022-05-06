# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        parents = defaultdict(TreeNode)
        pNode = None
        def dfs(node, parent = None):
            nonlocal parents, pNode
            if not node: return
            dfs(node.left, node)
            dfs(node.right, node)
            parents[node] = parent
            if p == node.val: pNode = node
        
        dfs(root)
        queue = deque([(pNode, 0)])
        visited = set()
        
        while queue:
            node, dist = queue.popleft()
            if node.val == q:
                return dist
            
            if node in visited: 
                continue
            visited.add(node)
            
            if node.left and node.left not in visited:
                queue.append((node.left, dist+1))
                
            if node.right and node.right not in visited:
                queue.append((node.right, dist+1))
                
            if parents[node] and parents[node] not in visited:
                queue.append((parents[node], dist+1))
                
        return -1
            
            