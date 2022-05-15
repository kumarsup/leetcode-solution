'''
mat = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[None, 0, None],
]

start from 0 to 9
    - backtrack and find all possible path till len == n
'''
class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = { 0:(4,6), 1:(6,8), 2:(7,9), 3:(4,8), 4:(0,3,9), 5:(), 6:(0,1,7), 7:(2,6), 8:(1,3), 9:(2,4)}
        
        memo = {}
        def helper(i, n):
            if n == 1: return 1
            if (i, n) not in memo:
                memo[(i,n)] = 0
                for nei in neighbors[i]:
                    memo[(i,n)] += helper(nei, n-1)
            return memo[(i,n)]
        res = 0
        for i in range(10):
            res += helper(i, n)
        return res%(10**9+7)
            