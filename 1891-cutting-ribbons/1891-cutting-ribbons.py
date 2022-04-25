'''
[9,7,5], k = 3

9 - 5, 4
7 - 5, 2
5 - 5

l = 0, r = total//2
mid = (l+r)//2


'''
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        
        left, right = 1, sum(ribbons)//k
        
        while left < right:
            mid = (left + right+1)//2
            total = 0
            for rib in ribbons:
                total += rib//mid
            if total >= k:
                left = mid
            else:
                right = mid-1
        return right