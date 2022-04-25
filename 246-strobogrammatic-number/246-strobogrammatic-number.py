'''
vals = {1: 1, 2: 5, 8: 8, 6: 9, 9: 6}

'''

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        vals = {'0':'0', '1': '1', '8': '8', '6': '9', '9': '6'}
        n = len(num)
        left, right = 0, n-1
        
        while left <= right:
            if num[left] not in vals: return False
            if num[right] not in vals: return False
            if num[left] != vals[num[right]]:
                return False
            left, right = left+1, right-1
        return True
            
        
       