head, curr,
tail
​
1. store the tree nodes in list
2. iterate on the list and create new nodes and points to head
3. return the head
​
curr = TreeNode(node.val)
curr.left =  last
tail.right = head.next
​
Approach 2:
1. initialise the first and last node as null
2. call the standard in order traversal
3. if not is not null
4. call the recursion from the left subtree
5. if the last node is not null, link the last and curr node nodes
6. else inititate first node
7. mark the curr node as the last one
8. call the recursion for the right sub tree
9. link the first and the last nodes to close the DLL ring and return first node
​
3. if not is not null