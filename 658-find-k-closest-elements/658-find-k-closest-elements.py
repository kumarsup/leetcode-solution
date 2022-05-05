'''
diff = abs(x - num)
heap - (dif, num)

'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        res = sorted(arr, key = lambda num: abs(x-num))
        return sorted(res[:k])
    