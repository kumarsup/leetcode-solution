'''

'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        if n < 0:
            x = 1/x
            n = -n
            
        def fastPower(x, n):
            if n == 1: return x
            half = fastPower(x, n//2)
            if n%2: return half*half*x
            return half*half
        return fastPower(x, n)
            
            
        
        
        
        
                