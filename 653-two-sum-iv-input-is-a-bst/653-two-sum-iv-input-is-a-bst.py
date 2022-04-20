class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashset = set()
        
        def dfs(node):
            nonlocal hashset
            if not node: return False
            if k - node.val in hashset:  return True
            hashset.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
        
            
                
                