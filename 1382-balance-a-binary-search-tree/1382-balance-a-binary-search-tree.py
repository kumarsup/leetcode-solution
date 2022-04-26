# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = []
        def dfs(node):
            nonlocal arr
            if not node: return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        def recursive(start, end):
            nonlocal arr
            if start > end: return None
            mid = (start+end)//2
            node = TreeNode(arr[mid])
            node.left = recursive(start, mid-1)
            node.right = recursive(mid+1, end)
            return node
    
        dfs(root)
        return recursive(0, len(arr)-1)
            