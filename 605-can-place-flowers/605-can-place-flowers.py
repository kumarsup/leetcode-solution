class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length, count = len(flowerbed), 0
        for i in range(length):
            if flowerbed[i] == 0:
                leftEmpty = (i == 0 or flowerbed[i-1] == 0)
                rightEmpty = (i == length-1) or (flowerbed[i+1] == 0)
                
                if leftEmpty and rightEmpty:
                    flowerbed[i] = 1
                    count+=1
                    if count >= n: return True
        return count >= n