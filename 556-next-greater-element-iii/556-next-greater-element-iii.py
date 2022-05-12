'''
    - convert to arr and then check digits
        - sort and return
        
'''
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            
        MOD = 2 ** 31 - 1
        nums = list(str(n))
                    
        # find the head of the non-increasing subseq
        right = len(nums) - 1
        while 1 <= right < len(nums):
            if int(nums[right-1]) >= int(nums[right]):
                right -= 1
            else:
                break
        
        # now right is the head of the non-increasing seq
        # pivot is right-1
        # judge if right == 0, which means the whole seq is non-increasing
        # in this case, we return -1
        if right == 0:
            return -1
        
        pivot = right - 1
        
        # find the smallest element in the non-increasing subseq to replace with pivot from end
        for i in range(len(nums)-1, pivot, -1):
            if int(nums[i]) > int(nums[pivot]):
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break
        # reverse the previous subseq after substituting
        reverse(right, len(nums)-1)
        res = int("".join(nums))
        
        if res > MOD:
            return -1
        else:
            return res