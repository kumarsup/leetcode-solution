# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, depth, queue = [], 0, deque([root])
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                if depth%2: level.insert(0, node.val)
                else: level.append(node.val)
                    
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            depth += 1
            res.append(level[:])
        return res
            