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
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
            
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                
        n = len(nums)
        i = n-1-1
        
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        
        if i >= 0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            swap(i, j)
        reverse(i+1, n-1)
        