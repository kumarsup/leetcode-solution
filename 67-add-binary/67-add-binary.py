class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)
        n2 = len(b)
        
        i, j = n1 -1, n2-1
        res, carry = '', 0
        
        while i >= 0 and j >= 0:
            val = int(a[i]) + int(b[j]) + carry
            if val == 3:
                carry = 1
                val = 1
            elif val == 2:
                carry = 1
                val = 0
            else:
                carry = 0
            i, j = i-1, j-1
            res = str(val) + res
            
        while i >= 0:
            val = int(a[i]) + carry
            if val == 2:
                carry = 1
                val = 0
            else:
                carry = 0
            i-=1
            res = str(val) + res
            
        while j >= 0:
            val = int(b[j]) + carry
            if val == 2:
                carry = 1
                val = 0
            else:
                carry = 0
            j-=1
            res = str(val) + res
            
        if carry > 0:
            res = str(carry) + res
            
        return res