class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def binarySearch(isLeft):
            left, right = 0, len(nums)-1
            index = -1
            
            while left <= right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid-1
                else:
                    index = mid
                    if isLeft:
                        right = mid-1
                    else:
                        left = mid+1
            return index
        
        
        left = binarySearch(True)
        right = binarySearch(False)
        return [left, right]
        
                