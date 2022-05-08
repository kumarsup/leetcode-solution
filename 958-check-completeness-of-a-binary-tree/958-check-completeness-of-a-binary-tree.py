# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
leftNull
if node.right and leftNull: return False
[       1
     2        3
  5  null   7   8

'''
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue, leftNull, nodeNull, foundNull = deque([root]), False, False, False
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node:
                    if foundNull: return False
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    foundNull = True
        return True
                
            