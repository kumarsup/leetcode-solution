# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
'''
[[1,1],2,[1,1]]
1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.


 - nList, depth, index = 0
 res = 0
 if index >= len(nList): return res
 item = nList[index]
 if item.isInteger():
    res += item.getInteger()*depth
    res += dfs(nList, index+1, depth)
else:
    res += dfs(item, 0, depth+1)
    
return res
 


'''
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
        def dfs(nList, depth = 1, index = 0):
            res = 0
            if not nList or index >= len(nList): return  res
            node = nList[index]
            res += node.getInteger()*depth if node.isInteger() else dfs(node.getList(), depth+1, 0)
            res += dfs(nList, depth, index+1)
            return res
        return dfs(nestedList)
    
    
    
    