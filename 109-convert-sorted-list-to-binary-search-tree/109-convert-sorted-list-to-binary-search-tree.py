# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    - fill items in arr - inorder
    - start, end
        mid = (start+end)//2
        node = Node(nums[mid])
        node.left = dfs(start, mid-1)
        node.right = dfs(mid+1, end)
'''
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        def dfs(start, end):
            nonlocal nums
            if start > end: return None
            mid = (start+end)//2
            node = TreeNode(nums[mid])
            node.left = dfs(start, mid-1)
            node.right = dfs(mid+1, end)
            return node
        return dfs(0, len(nums)-1)