class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastLen, slist = 0, s.split(' ')
        for word in slist:
            if len(word) > 0:
                lastLen = len(word)
        return lastLen
                