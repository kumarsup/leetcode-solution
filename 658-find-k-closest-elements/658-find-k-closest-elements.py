'''
diff = abs(x - num)
TC - O(n log n) + O(k log k)
SC - O(N)




'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = 0
        right = n - k
        
        while left < right:
            mid = (left+right)//2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid+1
            else:
                right = mid
        return arr[left: left+k]