# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newHead = curr = ListNode(-1)
        heap = []
        counter = 0
        
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, counter, head))
                counter+=1
        
        while heap:
            val, counter, node = heapq.heappop(heap)
            
            curr.next = ListNode(val)
            curr = curr.next
            
            node = node.next
            
            if node: 
                heapq.heappush(heap, (node.val, counter, node))
                counter+=1
        return newHead.next
            