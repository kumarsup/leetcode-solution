class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashset = set()
        stack = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if k - root.val in hashset: return True
            hashset.add(root.val)
            root = root.right
        return False
            
#         def dfs(node):
#             nonlocal hashset
#             if not node: return False
#             if k - node.val in hashset:  return True
#             hashset.add(node.val)
#             return dfs(node.left) or dfs(node.right)
        
#         return dfs(root)