class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
        
        for i in range(n):
            maxVal = 0
            maxIdx = -1
            j = n-1
            while j > i:
                if int(nums[j]) > maxVal:
                    maxIdx = j
                    maxVal = int(nums[j])
                j-=1

            if maxIdx != -1 and int(nums[i]) <  int(nums[maxIdx]):
                nums[i], nums[maxIdx] = nums[maxIdx], nums[i]
                break
                
        return int(''.join(nums))
            