# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
"4  (2  (3) (1) )     (6(5) None)"

getValue - to generate value of each node
recursion - 
    - base consition - index == len(s) return
    - value, index = getValue
    node = TreeNode(value)
    
    if index < n and s[index] == '('
        node.left, index = recursive(index+1)
    
    if node.left and index < n and s[index] == '('
        node.right, index = recursive(index+1)
        
    return node, index+1 if index < n and s[index] == ')' else index
'''
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        n = len(s)
        
        def getValue(index):
            sign, val = 1, 0
            
            if s[index] == '-':
                sign = -1
                index+=1
                
            while index < n and s[index].isdigit():
                val = val*10 + int(s[index])
                index+=1
            return val*sign, index
        
        def constructTree(index):
            if index >= n: return None, index
            value, index = getValue(index)
            node = TreeNode(value)
            if index < n and s[index] == '(': node.left, index = constructTree(index+1)
            if node.left and index < n and s[index] == '(': node.right, index = constructTree(index+1)
            return node, index+1
        
        return constructTree(0)[0]
                