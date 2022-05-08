'''
weights = [1,2,3,4,5,6,7,8,9,10], 
days = 5
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        low = max(weights)
        high = sum(weights)
        res = -1
        
        def isFeasible(midWeight):
            day, currWeight = 1, 0
            for w in weights:
                currWeight += w
                if currWeight > midWeight:
                    currWeight = w
                    day += 1
            return day <= days 
        
        while low <= high:
            mid = (low + high)//2
            if isFeasible(mid):
                res = mid
                high = mid-1
            else:
                low = mid+1
        return res
        