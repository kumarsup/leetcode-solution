class Solution:
    def romanToInt(self, s: str) -> int:
        hmap =  {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        
        n, idx, res = len(s), 0, 0
        
        while idx < n:
            val = 0
            if idx+2 <= n and s[idx: idx+2] in hmap:
                val = hmap[s[idx: idx+2]]
                idx += 2 
            else:
                val = hmap[s[idx: idx+1]]
                idx += 1
            res = res + val
        return res