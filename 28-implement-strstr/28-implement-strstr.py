class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hn = len(haystack)
        nn = len(needle)
        
        if hn < nn: return -1
        
        def gethash(s):
            hashkey = 0
            for i, ch in enumerate(s):
                hashkey += hash(ch) * 10**i
            return hashkey
        
        nhash = gethash(needle)
        hhash = gethash(haystack[:nn])
        if nhash == hhash: return 0
        
        for i in range(hn):
            hashkey = gethash(haystack[i:i+nn])
            if hashkey == nhash: return i
        return -1
        