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
list- 
def dfs(list, index, depdth):
    res = 0
    if index >= llen(list): return 0
    
    node = list[index]
    if node.isInteger():
        res += node.getInteger() * depdth
    else:
        res += dfs(node.getList(), 0, depdth+1)
    res += dfs(nlist, index+1, depdth)
return res


'''
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        def dfs(nlist, index, depdth):
            res = 0
            if not nlist or index >= len(nlist): return res
            node = nlist[index]
            res += depdth * node.getInteger() if node.isInteger() else dfs(node.getList(), 0, depdth+1)
            res += dfs(nlist, index+1, depdth)
            return res
        return dfs(nestedList, 0, 1)