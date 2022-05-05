'''
find i > i-1
j = i
find i > j
    swap
revese(i)

- 1258764 - 12 5 8764 -> 12 5 876 4 - > 12 6 875 4 -> 1264578
- 1264578
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(left):
            right = n-1
            while left < right:
                swap(left, right)
                left, right = left+1, right-1
        
        def swap(left, right):
            nums[left], nums[right] = nums[right], nums[left]
            
        n = len(nums)
        i = n-2
        
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
            
        if i >= 0:
            j = n-1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            swap(i, j)    
            
        reverse(i+1)
        
        return nums
        
            
            
            
            
        