'''
BST - left < root < right
kth smallest - 
brute force - in order - arr - [k-1]
TC - O(N) - O(logN)
SC - O(N) - 

stack -
    - iterative 
        - most left
        - k-=1
'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        def dfs(node):
            nonlocal res, k
            if not node: return
            dfs(node.left)
            k -= 1
            if k == 0 and res == -1:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res
                
        
        
        
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             while node.left:
#                 node = node.left
#                 stack.append(node)
#             k -= 1
#             if k == 0:
#                 return node.val
            
#             if node.right:
#                 stack.append(node.right)
                
#         return -1
            
            
                
            
            
        