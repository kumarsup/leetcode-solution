class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def binarySearchFind(start = True):
            left, right = 0, n-1
            res = -1
            
            while left <= right:
                mid = (left+right)//2
                if target > nums[mid]:
                    left = mid+1
                elif target < nums[mid]:
                    right = mid-1
                else:
                    res = mid
                    if start:
                        right = mid-1
                    else:
                        left = mid+1
            return res
        
        start = binarySearchFind(True)
        end = binarySearchFind(False)
        return [start, end]
        
        