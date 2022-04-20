class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
        indexs = [0]*n
        maxVal, maxIdx = 0, -1
        
        for i in range(n-1, -1, -1):
            if int(nums[i]) > maxVal:
                maxIdx = i
                maxVal = int(nums[i])
            indexs[i] = maxIdx 
        
        for i in range(n):
            maxIdx = indexs[i]
            if int(nums[i]) <  int(nums[maxIdx]):
                nums[i], nums[maxIdx] = nums[maxIdx], nums[i]
                break
        return int(''.join(nums))
            