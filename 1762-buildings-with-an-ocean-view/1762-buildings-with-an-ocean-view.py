'''
heights = [4,2,3,1] -->
[0,2,3]
view - right - ?
result - order ?
return - ?
constraints -? negative values in the heights array?
val or index

start iterating from right and store max val traverse- if cur val > max val then add curr to the res
as we iterated the arr from right so we need to return the building res so can reverse or sort
'''
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res, n, maxHeight = [], len(heights), 0
        
        for idx in range(n-1, -1, -1):
            if heights[idx] > maxHeight:
                res.append(idx)
                maxHeight = heights[idx]
        
        def reverse(left, right):
            while left < right:
                res[left], res[right] = res[right], res[left]
                left, right = left+1, right-1
        reverse(0, len(res)-1)
        return res
            
        
        