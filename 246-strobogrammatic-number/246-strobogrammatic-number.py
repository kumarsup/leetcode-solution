'''
vals = {1: 1, 8: 8, 6: 9, 9: 6}

'''

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        vals = {'0':'0', '1': '1', '8': '8', '6': '9', '9': '6'}
        n = len(num)
        i, j = 0, n-1
        while i <= j:
            if num[i] not in vals or vals[num[i]] != num[j]:
                return False
            i, j = i+1, j-1
        return True
            
    