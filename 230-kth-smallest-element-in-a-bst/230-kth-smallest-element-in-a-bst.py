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
        # res = -1
        # def dfs(node):
        #     nonlocal res, k
        #     if not node: return
        #     dfs(node.left)
        #     k -= 1
        #     if k == 0 and res == -1:
        #         res = node.val
        #         return
        #     dfs(node.right)
        # dfs(root)
        # return res
        
        
        def insertLeft(node):
            nonlocal stack
            while node:
                stack.append(node)
                node = node.left
        
        stack = []
        insertLeft(root)
        
        while stack:           
            node = stack.pop()
            k -= 1
            if k == 0: 
                return node.val
            if node.right: 
                insertLeft(node.right)
        return -1
            
            
                
            
            
        