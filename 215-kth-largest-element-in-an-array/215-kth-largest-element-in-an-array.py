'''
TC - nlogk
SC - O(k)
- select rand pivotIndex between left and right
get pivot from pivotIndex
1. pivot to the last(right)
2. move all smaller item to the left
3. move pivot to its final index



Quick select - 

partition(left, right):
pivotIndex = random.randint(left, right)

pivot = nums[pivotIndex]
#1. move the pivot to the last
nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]

#2. move allt he smaller items to right of the pivot 
storeIndex = left
for i in range(left, right)
    if nums[i] < pivot:
        nums[storeIndex], nums[i] = nums[i],  nums[storeIndex]
        storeIndex += 1
        
#3. Move the pivot to its right index
nums[storeIndex], nums[right] = nums[right], nums[pivotIndex]

quick(left, right)
if left == right: return nums[left]
pivotIndex = partition(left, right)

if pivotIndex == kthSmallest:
    return nums[pivotIndex]
elif pivotIndex > kthSmallest:
    return select(left, pivotIndex-1, kthSmallest)
else:
    return select(pivotIndex+1, right, kthSmallest)

'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(left, right):
            
            #pick a random index
            pivotIndex = random.randint(left, right)
            pivot = nums[pivotIndex]
            
            #1. move the pivot to right
            nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
            
            #2. move all smaller items then pivot to the left side
            scoreIndex = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[scoreIndex] = nums[scoreIndex], nums[i]
                    scoreIndex += 1
                    
            #3. move the pivot to its right location
            nums[scoreIndex], nums[right] = nums[right], nums[scoreIndex]
            return scoreIndex
        
        def select(left, right, kth):
            if left == right: return nums[left]
            
            pivotIndex = partition(left, right)
            pivot = nums[pivotIndex]
            
            if kth == pivotIndex:
                return nums[pivotIndex]
            elif kth < pivotIndex:
                return select(left, pivotIndex-1, kth)
            else:
                return select(pivotIndex+1, right, kth)
                
        n = len(nums)
        return select(0, n-1, n-k)