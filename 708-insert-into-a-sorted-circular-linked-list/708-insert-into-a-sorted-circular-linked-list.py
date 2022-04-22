"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:  
            node.next = node
            return node
        
        curr = head
        next = curr.next
        
        while True:
            if next == head:
                print(1)
                curr.next = node
                node.next = next
                break
            elif curr.val <= node.val and node.val <= next.val:
                print(2)
                tmp = curr.next 
                curr.next = node
                node.next = tmp
                break
            elif curr.val > node.val and node.val <= next.val and curr.val > next.val:
                print(3)
                tmp = curr.next 
                curr.next = node
                node.next = tmp
                break
            elif curr.val < node.val and node.val > next.val and curr.val > next.val:
                print(4)
                tmp = curr.next 
                curr.next = node
                node.next = tmp
                break
            curr = next
            next = next.next
        return head