'''
[1,2,3] - [1,3,2]
[1,2,5,3] - [1,3,2,5] - [1,3,5,2] - [1,3,{5,2}] reverse

right = n-1
start iterate from right and find small val at index i 
    - swap the item on ith and right index 
    - reverse the sub array i+1 to right
[1,2,6,5,4,3] - [1,3,6,5,4,2] - [1,3,2,4,5,6]
251 - 521 - 512

'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def swap(index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]
        
        def reverse(left):
            right = n-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        n = len(nums)
        index = n-2
        
        while index >= 0 and nums[index+1] <= nums[index]:
            index -= 1
            
        if index >= 0:
            jidx = n-1
            while nums[jidx] <= nums[index]:
                jidx -= 1
            swap(index, jidx)
            
        reverse(index+1)
        
            