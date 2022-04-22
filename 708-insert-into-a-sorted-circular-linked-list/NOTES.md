Givin sorted circuler list
After insert the list sould be still sorted
a random node is given to start with -
​
1. first/last    -> head == curr
2. middle      -> curr < node and node < next
4.
​
​
​
​
if head is null then add the node and return
- curr, next and traverse
- if curr < node < next - insert between this and connect
- if next equals to head then insert the node in this possition
- if curr < node and node > next - insert at this position
​
[3,4,1], insertVal = 2
​
node = 2
curr = 1
next = 3
can add = yes
​
​
head = [], insertVal = 1
​
​
​
​
​
​
​