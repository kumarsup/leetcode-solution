class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        slist = s.split(' ')
        lastLen = 0
        
        for word in slist:
            word = word
            if len(word) > 0:
                lastLen = len(word)
        return lastLen
                