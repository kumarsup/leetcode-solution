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
        stack = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0: return root.val
            root = root.right
        
        