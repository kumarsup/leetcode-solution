# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        queue, res = deque([root]), []
        while queue:
            size = len(queue)
            last = None
            
            for _ in range(size):
                node = queue.popleft()
                last = node
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            
            if last: res.append(node.val)
        return res