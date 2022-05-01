class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        count, res, buf4 = 0, 0, ['']*4
        
        while res < n:
            count = min(read4(buf4), n-res)
            buf[res:] = buf4[:count]
            res += count
            if count < 4: break
        
      